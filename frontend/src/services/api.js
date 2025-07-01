import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8001';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response?.status === 401) {
      // Token expired or invalid
      localStorage.removeItem('token');
      delete api.defaults.headers.common['Authorization'];
      
      // Redirect to login if not already there
      if (window.location.pathname !== '/login' && window.location.pathname !== '/') {
        window.location.href = '/login';
      }
    }
    
    return Promise.reject(error);
  }
);

// File System API Helper
export class FileSystemHelper {
  static async selectDirectory() {
    try {
      if (!window.showDirectoryPicker) {
        throw new Error('File System Access API is not supported in this browser');
      }
      
      const directoryHandle = await window.showDirectoryPicker();
      return directoryHandle;
    } catch (error) {
      console.error('Error selecting directory:', error);
      throw error;
    }
  }

  static async readFilesFromDirectory(directoryHandle, extensions = []) {
    const files = [];
    
    try {
      for await (const [name, handle] of directoryHandle) {
        if (handle.kind === 'file') {
          // Extension filter
          if (extensions.length > 0) {
            const extension = name.split('.').pop()?.toLowerCase();
            if (!extensions.includes(extension)) {
              continue;
            }
          }
          
          try {
            const file = await handle.getFile();
            const content = await file.text();
            
            files.push({
              name: name,
              path: name,
              content: content,
              size: file.size,
              lastModified: file.lastModified,
              type: file.type
            });
          } catch (readError) {
            console.warn(`Could not read file ${name}:`, readError);
          }
        } else if (handle.kind === 'directory') {
          // Recursive directory reading (optional)
          try {
            const subFiles = await this.readFilesFromDirectory(handle, extensions);
            files.push(...subFiles.map(f => ({
              ...f,
              name: `${name}/${f.name}`,
              path: `${name}/${f.path}`
            })));
          } catch (subDirError) {
            console.warn(`Could not read subdirectory ${name}:`, subDirError);
          }
        }
      }
    } catch (error) {
      console.error('Error reading directory:', error);
      throw error;
    }
    
    return files;
  }

  static getCommonExtensions() {
    return {
      'Python': ['py', 'pyx', 'pyi'],
      'JavaScript': ['js', 'jsx', 'ts', 'tsx'],
      'Web': ['html', 'htm', 'css', 'scss', 'sass'],
      'Data': ['json', 'xml', 'yaml', 'yml', 'csv'],
      'Documentation': ['md', 'txt', 'rst'],
      'Config': ['conf', 'ini', 'config', 'env'],
      'All': [] // Empty array means no filter
    };
  }

  static async checkBrowserSupport() {
    return {
      fileSystemAPI: 'showDirectoryPicker' in window,
      browserName: this.getBrowserName(),
      isSupported: 'showDirectoryPicker' in window
    };
  }

  static getBrowserName() {
    const userAgent = navigator.userAgent;
    if (userAgent.includes('Chrome')) return 'Chrome';
    if (userAgent.includes('Firefox')) return 'Firefox';
    if (userAgent.includes('Safari')) return 'Safari';
    if (userAgent.includes('Edge')) return 'Edge';
    return 'Unknown';
  }
}

// API Methods
export const authAPI = {
  login: (email, password) => api.post('/api/auth/login', { email, password }),
  signup: (name, email, password) => api.post('/api/auth/signup', { name, email, password }),
  getMe: () => api.get('/api/auth/me'),
};

export const processAPI = {
  processFiles: (data) => api.post('/api/process', data),
  processFilesGuest: (data) => api.post('/api/process/guest', data),
  getTemplates: () => api.get('/api/templates'),
  getQueries: () => api.get('/api/queries'),
};

export const statsAPI = {
  getStats: () => api.get('/api/stats'),
};

export default api;