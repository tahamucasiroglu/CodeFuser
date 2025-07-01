import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import './App.css';

// Components
import Header from './components/Header';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import FileProcessor from './components/FileProcessor';
import History from './components/History';

// Context
import { AuthProvider, useAuth } from './context/AuthContext';
import { NotificationProvider } from './context/NotificationContext';

// API Services
import api from './services/api';

function App() {
  return (
    <NotificationProvider>
      <AuthProvider>
        <Router>
          <div className="min-h-screen bg-gray-50">
            <Header />
            <main className="container mx-auto px-4 py-8">
              <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/login" element={<Login />} />
                <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
                <Route path="/process" element={<FileProcessor />} />
                <Route path="/history" element={<ProtectedRoute><History /></ProtectedRoute>} />
              </Routes>
            </main>
          </div>
        </Router>
      </AuthProvider>
    </NotificationProvider>
  );
}

// Landing Page Component
function LandingPage() {
  const { user } = useAuth();

  if (user) {
    return <Navigate to="/dashboard" replace />;
  }

  return (
    <div className="text-center">
      {/* Hero Section */}
      <div className="max-w-4xl mx-auto mb-16">
        <div className="flex justify-center mb-8">
          <img 
            src="/api/logo" 
            alt="CodeFuser Logo" 
            className="w-24 h-24"
            onError={(e) => {
              e.target.style.display = 'none';
            }}
          />
        </div>
        
        <h1 className="text-5xl font-bold text-gray-900 mb-6">
          🚀 CodeFuser Web
        </h1>
        
        <p className="text-xl text-gray-600 mb-8 leading-relaxed">
          Projelerinizi AI prompt'larıyla birleştirin. Kurulum gerektirmez, 
          tarayıcınızdan doğrudan bilgisayarınızdaki dosyalara erişin.
        </p>
        
        <div className="flex justify-center space-x-4 mb-12">
          <a 
            href="/process" 
            className="bg-blue-600 text-white px-8 py-3 rounded-lg text-lg font-semibold hover:bg-blue-700 transition-colors"
          >
            Hemen Deneyin (3 Ücretsiz Hak)
          </a>
          <a 
            href="/login" 
            className="bg-gray-200 text-gray-800 px-8 py-3 rounded-lg text-lg font-semibold hover:bg-gray-300 transition-colors"
          >
            Giriş Yap / Kayıt Ol
          </a>
        </div>
      </div>

      {/* Features */}
      <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto mb-16">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <div className="text-3xl mb-4">📁</div>
          <h3 className="text-xl font-bold mb-2">Local Dosya Erişimi</h3>
          <p className="text-gray-600">
            Modern File System API ile bilgisayarınızdaki projelere doğrudan erişim. 
            Upload gerektirmez.
          </p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow-md">
          <div className="text-3xl mb-4">🎯</div>
          <h3 className="text-xl font-bold mb-2">Dual Prompt Sistemi</h3>
          <p className="text-gray-600">
            Genel prompt + dosyaya özel prompt özelliği. 
            Her dosya için farklı talimatlar verebilirsiniz.
          </p>
        </div>
        
        <div className="bg-white p-6 rounded-lg shadow-md">
          <div className="text-3xl mb-4">⚡</div>
          <h3 className="text-xl font-bold mb-2">Hızlı İşleme</h3>
          <p className="text-gray-600">
            Template sistemi ve akıllı filtreler ile hızlı sonuç alın. 
            Çoklu format desteği.
          </p>
        </div>
      </div>

      {/* Pricing */}
      <div className="max-w-4xl mx-auto">
        <h2 className="text-3xl font-bold text-center mb-8">Üyelik Paketleri</h2>
        
        <div className="grid md:grid-cols-3 gap-6">
          <div className="bg-white p-6 rounded-lg shadow-md border-2 border-gray-200">
            <h3 className="text-xl font-bold mb-2">👤 Misafir</h3>
            <div className="text-2xl font-bold text-blue-600 mb-4">Ücretsiz</div>
            <ul className="text-left space-y-2 text-gray-600">
              <li>✅ 3 sorgu hakkı</li>
              <li>✅ Sadece genel prompt</li>
              <li>✅ HTML/TXT output</li>
              <li>❌ Kayıt gerekmez</li>
            </ul>
            <a href="/process" className="block w-full bg-gray-200 text-center py-2 rounded-lg mt-4 hover:bg-gray-300 transition-colors">
              Hemen Dene
            </a>
          </div>
          
          <div className="bg-white p-6 rounded-lg shadow-md border-2 border-blue-500">
            <h3 className="text-xl font-bold mb-2">⭐ Starter</h3>
            <div className="text-2xl font-bold text-blue-600 mb-4">Manuel Yetki</div>
            <ul className="text-left space-y-2 text-gray-600">
              <li>✅ Günde 100 sorgu</li>
              <li>✅ Genel prompt desteği</li>
              <li>✅ Tüm output formatları</li>
              <li>✅ Sorgu geçmişi</li>
            </ul>
            <a href="/login" className="block w-full bg-blue-600 text-white text-center py-2 rounded-lg mt-4 hover:bg-blue-700 transition-colors">
              Kayıt Ol
            </a>
          </div>
          
          <div className="bg-white p-6 rounded-lg shadow-md border-2 border-purple-500">
            <h3 className="text-xl font-bold mb-2">🚀 Pro</h3>
            <div className="text-2xl font-bold text-purple-600 mb-4">Manuel Yetki</div>
            <ul className="text-left space-y-2 text-gray-600">
              <li>✅ Sınırsız sorgu</li>
              <li>✅ Dosyaya özel prompt</li>
              <li>✅ Tüm template'ler</li>
              <li>✅ Gelişmiş filtreler</li>
            </ul>
            <a href="/login" className="block w-full bg-purple-600 text-white text-center py-2 rounded-lg mt-4 hover:bg-purple-700 transition-colors">
              İletişime Geç
            </a>
          </div>
        </div>
      </div>
      
      {/* Footer */}
      <div className="mt-16 pt-8 border-t border-gray-200 text-gray-500">
        <p>&copy; 2024 CodeFuser Web. Tüm hakları saklıdır.</p>
      </div>
    </div>
  );
}

// Protected Route Component
function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return children;
}

export default App;