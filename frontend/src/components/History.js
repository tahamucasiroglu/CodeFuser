import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNotification } from '../context/NotificationContext';
import { processAPI } from '../services/api';

const History = () => {
  const { user } = useAuth();
  const { showError } = useNotification();
  const [queries, setQueries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState('all');
  const [sortBy, setSortBy] = useState('date');

  useEffect(() => {
    loadQueries();
  }, []);

  const loadQueries = async () => {
    try {
      setLoading(true);
      const response = await processAPI.getQueries();
      setQueries(response.data.queries);
    } catch (error) {
      console.error('Query loading error:', error);
      showError('Sorgu geçmişi yüklenemedi');
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleString('tr-TR', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getFilteredQueries = () => {
    let filtered = queries;

    // Apply filters
    if (filter === 'today') {
      const today = new Date().toDateString();
      filtered = queries.filter(q => 
        new Date(q.created_at).toDateString() === today
      );
    } else if (filter === 'week') {
      const weekAgo = new Date();
      weekAgo.setDate(weekAgo.getDate() - 7);
      filtered = queries.filter(q => 
        new Date(q.created_at) >= weekAgo
      );
    } else if (filter === 'template') {
      filtered = queries.filter(q => q.template_id);
    }

    // Apply sorting
    if (sortBy === 'date') {
      filtered.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    } else if (sortBy === 'files') {
      filtered.sort((a, b) => b.files_count - a.files_count);
    }

    return filtered;
  };

  const filteredQueries = getFilteredQueries();

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      {/* Header */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-gray-900">📋 Sorgu Geçmişi</h1>
            <p className="text-gray-600 mt-1">
              Geçmiş sorgularınızı görüntüleyin ve yönetin.
            </p>
          </div>
          
          <div className="text-right">
            <div className="text-2xl font-bold text-blue-600">{queries.length}</div>
            <div className="text-sm text-gray-600">Toplam sorgu</div>
          </div>
        </div>
      </div>

      {/* Filters and Sort */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between space-y-4 sm:space-y-0">
          {/* Filters */}
          <div className="flex items-center space-x-4">
            <label className="text-sm font-medium text-gray-700">Filtre:</label>
            <select
              value={filter}
              onChange={(e) => setFilter(e.target.value)}
              className="form-input text-sm"
            >
              <option value="all">Tüm sorgular</option>
              <option value="today">Bugün</option>
              <option value="week">Son 7 gün</option>
              <option value="template">Template kullananlar</option>
            </select>
          </div>

          {/* Sort */}
          <div className="flex items-center space-x-4">
            <label className="text-sm font-medium text-gray-700">Sırala:</label>
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
              className="form-input text-sm"
            >
              <option value="date">Tarihe göre</option>
              <option value="files">Dosya sayısına göre</option>
            </select>
          </div>
        </div>

        {/* Stats */}
        <div className="mt-4 pt-4 border-t border-gray-200">
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-center">
            <div>
              <div className="text-lg font-semibold text-gray-900">{filteredQueries.length}</div>
              <div className="text-sm text-gray-600">Görüntülenen</div>
            </div>
            <div>
              <div className="text-lg font-semibold text-gray-900">
                {filteredQueries.reduce((sum, q) => sum + q.files_count, 0)}
              </div>
              <div className="text-sm text-gray-600">Toplam dosya</div>
            </div>
            <div>
              <div className="text-lg font-semibold text-gray-900">
                {filteredQueries.filter(q => q.template_id).length}
              </div>
              <div className="text-sm text-gray-600">Template kullanan</div>
            </div>
            <div>
              <div className="text-lg font-semibold text-gray-900">
                {new Set(filteredQueries.map(q => q.output_format)).size}
              </div>
              <div className="text-sm text-gray-600">Farklı format</div>
            </div>
          </div>
        </div>
      </div>

      {/* Query List */}
      <div className="space-y-4">
        {filteredQueries.length > 0 ? (
          filteredQueries.map((query) => (
            <QueryCard key={query.id} query={query} />
          ))
        ) : (
          <div className="bg-white rounded-lg shadow-md p-12 text-center">
            <span className="text-4xl mb-4 block">🔍</span>
            <h3 className="text-lg font-medium text-gray-900 mb-2">
              {filter === 'all' ? 'Henüz sorgu yapılmamış' : 'Bu filtrede sorgu bulunamadı'}
            </h3>
            <p className="text-gray-600 mb-6">
              {filter === 'all' 
                ? 'İlk sorgunuzu oluşturmak için dosya işleyiciyi kullanın.'
                : 'Farklı bir filtre seçerek tekrar deneyin.'
              }
            </p>
            {filter === 'all' && (
              <a
                href="/process"
                className="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
              >
                İlk sorguyu oluştur
              </a>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

// Query Card Component
const QueryCard = ({ query }) => {
  const [expanded, setExpanded] = useState(false);

  const getFormatBadgeColor = (format) => {
    const colors = {
      html: 'bg-blue-100 text-blue-600',
      txt: 'bg-gray-100 text-gray-600',
      json: 'bg-green-100 text-green-600',
      pdf: 'bg-red-100 text-red-600'
    };
    return colors[format] || 'bg-gray-100 text-gray-600';
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleString('tr-TR', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <div className="p-6">
        {/* Header */}
        <div className="flex items-start justify-between mb-4">
          <div className="flex-1">
            <div className="flex items-center space-x-3 mb-2">
              <span className="text-lg font-semibold text-gray-900">
                {query.files_count} dosya işlendi
              </span>
              
              <span className={`px-2 py-1 text-xs font-medium rounded ${getFormatBadgeColor(query.output_format)}`}>
                {query.output_format.toUpperCase()}
              </span>
              
              {query.template_id && (
                <span className="px-2 py-1 text-xs font-medium rounded bg-purple-100 text-purple-600">
                  {query.template_id}
                </span>
              )}
            </div>
            
            <div className="text-sm text-gray-600">
              {formatDate(query.created_at)}
            </div>
          </div>

          <button
            onClick={() => setExpanded(!expanded)}
            className="text-gray-400 hover:text-gray-600 transition-colors"
          >
            <span className={`transform transition-transform ${expanded ? 'rotate-180' : ''}`}>
              ▼
            </span>
          </button>
        </div>

        {/* Preview */}
        <div className="mb-4">
          <h4 className="text-sm font-medium text-gray-700 mb-2">Genel Prompt:</h4>
          <p className="text-sm text-gray-600 line-clamp-2">
            {query.general_prompt || 'Prompt belirtilmemiş'}
          </p>
        </div>

        {/* Expanded Content */}
        {expanded && (
          <div className="pt-4 border-t border-gray-200 space-y-4">
            {/* Full Prompt */}
            {query.general_prompt && (
              <div>
                <h4 className="text-sm font-medium text-gray-700 mb-2">Tam Prompt:</h4>
                <div className="bg-gray-50 p-3 rounded text-sm text-gray-700 whitespace-pre-wrap">
                  {query.general_prompt}
                </div>
              </div>
            )}

            {/* File Prompts */}
            {query.file_prompts && Object.keys(query.file_prompts).length > 0 && (
              <div>
                <h4 className="text-sm font-medium text-gray-700 mb-2">Dosya Prompt'ları:</h4>
                <div className="space-y-2">
                  {Object.entries(query.file_prompts).map(([fileName, prompt]) => (
                    <div key={fileName} className="bg-gray-50 p-3 rounded">
                      <div className="text-sm font-medium text-gray-900 mb-1">{fileName}</div>
                      <div className="text-sm text-gray-600">{prompt}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Query Stats */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t border-gray-100">
              <div className="text-center">
                <div className="text-lg font-semibold text-gray-900">{query.files_count}</div>
                <div className="text-xs text-gray-600">Dosya</div>
              </div>
              <div className="text-center">
                <div className="text-lg font-semibold text-gray-900">{query.output_format}</div>
                <div className="text-xs text-gray-600">Format</div>
              </div>
              <div className="text-center">
                <div className="text-lg font-semibold text-gray-900">
                  {query.template_id ? 'Var' : 'Yok'}
                </div>
                <div className="text-xs text-gray-600">Template</div>
              </div>
              <div className="text-center">
                <div className="text-lg font-semibold text-gray-900">
                  {Object.keys(query.file_prompts || {}).length}
                </div>
                <div className="text-xs text-gray-600">Dosya Prompt</div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default History;