import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNotification } from '../context/NotificationContext';
import { processAPI, FileSystemHelper } from '../services/api';

const FileProcessor = () => {
  const { user } = useAuth();
  const { showSuccess, showError, showWarning, showInfo } = useNotification();
  
  // File system state
  const [directoryHandle, setDirectoryHandle] = useState(null);
  const [files, setFiles] = useState([]);
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [browserSupport, setBrowserSupport] = useState(null);

  // Process state
  const [generalPrompt, setGeneralPrompt] = useState('');
  const [filePrompts, setFilePrompts] = useState({});
  const [outputFormat, setOutputFormat] = useState('html');
  const [templateId, setTemplateId] = useState('');
  const [templates, setTemplates] = useState({});
  
  // Result state
  const [result, setResult] = useState(null);
  const [processing, setProcessing] = useState(false);

  // Check browser support on mount
  useEffect(() => {
    checkBrowserSupport();
    loadTemplates();
  }, []);

  const checkBrowserSupport = async () => {
    const support = await FileSystemHelper.checkBrowserSupport();
    setBrowserSupport(support);
    
    if (!support.isSupported) {
      showWarning(
        `File System API bu tarayıcıda desteklenmiyor. Chrome, Edge veya Safari kullanın.`
      );
    }
  };

  const loadTemplates = async () => {
    try {
      const response = await processAPI.getTemplates();
      setTemplates(response.data.templates);
    } catch (error) {
      console.error('Template loading error:', error);
    }
  };

  const selectDirectory = async () => {
    try {
      setLoading(true);
      const handle = await FileSystemHelper.selectDirectory();
      setDirectoryHandle(handle);
      
      showInfo('Dizin seçildi. Dosyalar taranıyor...');
      
      // Read files from directory
      const extensions = getSelectedExtensions();
      const fileList = await FileSystemHelper.readFilesFromDirectory(handle, extensions);
      
      setFiles(fileList);
      setSelectedFiles(fileList.map(f => f.name)); // Select all by default
      
      showSuccess(`${fileList.length} dosya bulundu!`);
    } catch (error) {
      console.error('Directory selection error:', error);
      
      if (error.name === 'AbortError') {
        showInfo('Dizin seçimi iptal edildi.');
      } else {
        showError('Dizin seçilirken hata oluştu: ' + error.message);
      }
    } finally {
      setLoading(false);
    }
  };

  const getSelectedExtensions = () => {
    // Default extensions - user can customize this
    return ['py', 'js', 'jsx', 'ts', 'tsx', 'html', 'css', 'json', 'md', 'txt'];
  };

  const toggleFileSelection = (fileName) => {
    setSelectedFiles(prev => {
      if (prev.includes(fileName)) {
        return prev.filter(f => f !== fileName);
      } else {
        return [...prev, fileName];
      }
    });
  };

  const toggleAllFiles = () => {
    if (selectedFiles.length === files.length) {
      setSelectedFiles([]);
    } else {
      setSelectedFiles(files.map(f => f.name));
    }
  };

  const updateFilePrompt = (fileName, prompt) => {
    setFilePrompts(prev => ({
      ...prev,
      [fileName]: prompt
    }));
  };

  const processFiles = async () => {
    if (selectedFiles.length === 0) {
      showError('Lütfen en az bir dosya seçin.');
      return;
    }

    if (!generalPrompt.trim() && Object.keys(filePrompts).length === 0) {
      showError('Lütfen genel prompt girin veya dosyalara özel prompt ekleyin.');
      return;
    }

    try {
      setProcessing(true);
      
      // Prepare files data
      const selectedFilesData = files.filter(f => selectedFiles.includes(f.name));
      
      // Check user limits for file prompts
      const hasFilePrompts = Object.keys(filePrompts).some(key => filePrompts[key].trim());
      if (hasFilePrompts && user && !user.limits?.file_prompts_enabled) {
        showError('Dosyaya özel prompt özelliği Pro üyeler için geçerlidir.');
        return;
      }

      const requestData = {
        files: selectedFilesData,
        general_prompt: generalPrompt.trim(),
        file_prompts: filePrompts,
        output_format: outputFormat,
        template_id: templateId || null
      };

      // Choose endpoint based on authentication
      const response = user 
        ? await processAPI.processFiles(requestData)
        : await processAPI.processFilesGuest(requestData);

      setResult(response.data);
      showSuccess('Dosyalar başarıyla işlendi!');
      
    } catch (error) {
      console.error('Processing error:', error);
      
      if (error.response?.status === 429) {
        showError('Günlük sorgu limitiniz doldu. Yarın tekrar deneyin.');
      } else if (error.response?.status === 403) {
        showError(error.response.data.detail || 'Bu özellik için yetkiniz yok.');
      } else {
        showError('Dosyalar işlenirken hata oluştu: ' + (error.response?.data?.detail || error.message));
      }
    } finally {
      setProcessing(false);
    }
  };

  const downloadResult = () => {
    if (!result) return;
    
    const blob = new Blob([result.output], { 
      type: outputFormat === 'html' ? 'text/html' : 'text/plain' 
    });
    
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `codefuser-output.${outputFormat}`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    showSuccess('Dosya indirildi!');
  };

  const copyToClipboard = () => {
    if (!result) return;
    
    navigator.clipboard.writeText(result.output).then(() => {
      showSuccess('İçerik panoya kopyalandı!');
    }).catch(() => {
      showError('Panoya kopyalanamadı.');
    });
  };

  if (!browserSupport) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (!browserSupport.isSupported) {
    return (
      <div className="max-w-2xl mx-auto text-center py-12">
        <span className="text-6xl mb-4 block">⚠️</span>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">
          Tarayıcı Desteği Gerekli
        </h2>
        <p className="text-gray-600 mb-6">
          CodeFuser Web, dosyalarınıza erişmek için modern File System API kullanır. 
          Bu özellik şu anda sadece Chrome, Edge ve Safari tarayıcılarında desteklenmektedir.
        </p>
        <div className="bg-blue-50 p-4 rounded-lg">
          <p className="text-blue-800">
            <strong>Mevcut tarayıcınız:</strong> {browserSupport.browserName}
          </p>
          <p className="text-blue-600 mt-2">
            Lütfen Chrome, Edge veya Safari kullanarak tekrar deneyin.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      {/* Header */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h1 className="text-2xl font-bold text-gray-900 mb-2">
          🚀 Dosya İşleyici
        </h1>
        <p className="text-gray-600">
          Bilgisayarınızdaki dosyaları seçin ve AI prompt'larıyla birleştirin.
        </p>
        
        {/* User Limits Info */}
        {user?.limits && (
          <div className="mt-4 p-3 bg-blue-50 rounded-lg">
            <div className="flex items-center justify-between text-sm">
              <span className="text-blue-800">
                <strong>Günlük Kullanım:</strong> {user.limits.daily_queries_used}/{user.limits.daily_queries_limit === -1 ? '∞' : user.limits.daily_queries_limit}
              </span>
              <span className={`font-medium ${user.limits.file_prompts_enabled ? 'text-green-600' : 'text-yellow-600'}`}>
                {user.limits.file_prompts_enabled ? 'Dosya prompt\'ları aktif' : 'Sadece genel prompt'}
              </span>
            </div>
          </div>
        )}
      </div>

      {/* Directory Selection */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">1. Proje Klasörünü Seçin</h2>
        
        {!directoryHandle ? (
          <div className="text-center py-8">
            <span className="text-4xl mb-4 block">📁</span>
            <p className="text-gray-600 mb-6">
              İşlemek istediğiniz projenin bulunduğu klasörü seçin.
            </p>
            <button
              onClick={selectDirectory}
              disabled={loading}
              className="file-picker-button"
            >
              {loading ? (
                <div className="flex items-center">
                  <div className="spinner mr-2"></div>
                  Klasör Seçiliyor...
                </div>
              ) : (
                'Klasör Seç'
              )}
            </button>
          </div>
        ) : (
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <span className="text-green-600">✅</span>
                <span className="font-medium">Klasör seçildi</span>
                <span className="text-gray-500">({files.length} dosya bulundu)</span>
              </div>
              <button
                onClick={selectDirectory}
                className="text-blue-600 hover:text-blue-700 font-medium"
              >
                Başka klasör seç
              </button>
            </div>
            
            {/* File Selection */}
            <div className="file-list-container">
              <div className="p-3 border-b border-gray-200 bg-gray-100">
                <div className="flex items-center justify-between">
                  <label className="flex items-center">
                    <input
                      type="checkbox"
                      checked={selectedFiles.length === files.length && files.length > 0}
                      onChange={toggleAllFiles}
                      className="mr-2"
                    />
                    <span className="font-medium">Tümünü seç ({selectedFiles.length}/{files.length})</span>
                  </label>
                </div>
              </div>
              
              <div className="max-h-64 overflow-y-auto">
                {files.map((file) => (
                  <div key={file.name} className="file-item">
                    <label className="flex items-center flex-1 cursor-pointer">
                      <input
                        type="checkbox"
                        checked={selectedFiles.includes(file.name)}
                        onChange={() => toggleFileSelection(file.name)}
                        className="mr-3"
                      />
                      <div className="flex-1">
                        <div className="font-medium text-gray-900">{file.name}</div>
                        <div className="text-xs text-gray-500">
                          {(file.size / 1024).toFixed(1)} KB
                        </div>
                      </div>
                    </label>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Template Selection */}
      {Object.keys(templates).length > 0 && (
        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">2. Template Seçin (Opsiyonel)</h2>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            <div 
              className={`template-card ${!templateId ? 'selected' : ''}`}
              onClick={() => setTemplateId('')}
            >
              <h3 className="font-medium mb-1">Özel Prompt</h3>
              <p className="text-sm text-gray-600">Kendi prompt'ınızı yazın</p>
            </div>
            
            {Object.entries(templates).map(([id, template]) => (
              <div
                key={id}
                className={`template-card ${templateId === id ? 'selected' : ''}`}
                onClick={() => setTemplateId(id)}
              >
                <h3 className="font-medium mb-1">{template.name}</h3>
                <p className="text-sm text-gray-600">AI analizi için optimize edilmiş</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Prompts */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">3. Prompt'ları Girin</h2>
        
        {/* General Prompt */}
        <div className="space-y-4">
          <div>
            <label className="form-label">Genel Prompt</label>
            <textarea
              value={generalPrompt}
              onChange={(e) => setGeneralPrompt(e.target.value)}
              placeholder="Tüm dosyalar için geçerli olacak genel talimatlarınızı buraya yazın..."
              className="form-textarea h-32"
            />
          </div>

          {/* File Specific Prompts */}
          {user?.limits?.file_prompts_enabled && selectedFiles.length > 0 && (
            <div>
              <h3 className="font-medium text-gray-900 mb-3">Dosyaya Özel Prompt'lar (Pro Özelliği)</h3>
              <div className="space-y-3 max-h-64 overflow-y-auto">
                {selectedFiles.slice(0, 5).map((fileName) => (
                  <div key={fileName} className="border border-gray-200 rounded-lg p-3">
                    <label className="form-label text-sm">{fileName}</label>
                    <textarea
                      value={filePrompts[fileName] || ''}
                      onChange={(e) => updateFilePrompt(fileName, e.target.value)}
                      placeholder="Bu dosya için özel talimatlar..."
                      className="form-textarea h-20 text-sm"
                    />
                  </div>
                ))}
                {selectedFiles.length > 5 && (
                  <p className="text-sm text-gray-500">
                    İlk 5 dosya gösteriliyor. Daha fazla dosya için işleme geçin.
                  </p>
                )}
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Output Settings */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-lg font-semibold text-gray-900 mb-4">4. Çıktı Formatı</h2>
        
        <div className="flex space-x-4">
          <label className="flex items-center">
            <input
              type="radio"
              name="format"
              value="html"
              checked={outputFormat === 'html'}
              onChange={(e) => setOutputFormat(e.target.value)}
              className="mr-2"
            />
            <span>HTML (Önerilen)</span>
          </label>
          <label className="flex items-center">
            <input
              type="radio"
              name="format"
              value="txt"
              checked={outputFormat === 'txt'}
              onChange={(e) => setOutputFormat(e.target.value)}
              className="mr-2"
            />
            <span>Text</span>
          </label>
        </div>
      </div>

      {/* Process Button */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-lg font-semibold text-gray-900">5. İşleme Başla</h2>
            <p className="text-gray-600">
              {selectedFiles.length} dosya işlenecek
            </p>
          </div>
          
          <button
            onClick={processFiles}
            disabled={processing || selectedFiles.length === 0}
            className="btn-primary px-8 py-3 text-lg disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {processing ? (
              <div className="flex items-center">
                <div className="spinner mr-2"></div>
                İşleniyor...
              </div>
            ) : (
              'İşle'
            )}
          </button>
        </div>
      </div>

      {/* Results */}
      {result && (
        <div className="output-container">
          <div className="output-header">
            <h2 className="text-lg font-semibold text-gray-900">Sonuç</h2>
            <div className="flex space-x-2">
              <button onClick={copyToClipboard} className="copy-button">
                📋 Kopyala
              </button>
              <button onClick={downloadResult} className="copy-button">
                💾 İndir
              </button>
            </div>
          </div>
          
          <div className="output-content">
            {outputFormat === 'html' ? (
              <div 
                dangerouslySetInnerHTML={{ __html: result.output }}
                className="prose max-w-none"
              />
            ) : (
              <pre className="whitespace-pre-wrap text-sm bg-gray-50 p-4 rounded">
                {result.output}
              </pre>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default FileProcessor;