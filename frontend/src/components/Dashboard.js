import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useNotification } from '../context/NotificationContext';
import { processAPI, statsAPI } from '../services/api';

const Dashboard = () => {
  const { user, fetchUserInfo } = useAuth();
  const { showError } = useNotification();
  const [stats, setStats] = useState(null);
  const [recentQueries, setRecentQueries] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    try {
      setLoading(true);
      
      // Fetch user info to get updated limits
      await fetchUserInfo();
      
      // Fetch stats and recent queries
      const [statsResponse, queriesResponse] = await Promise.all([
        statsAPI.getStats(),
        processAPI.getQueries()
      ]);
      
      setStats(statsResponse.data);
      setRecentQueries(queriesResponse.data.queries.slice(0, 5)); // Last 5 queries
    } catch (error) {
      console.error('Dashboard data loading error:', error);
      showError('Dashboard verileri yüklenemedi');
    } finally {
      setLoading(false);
    }
  };

  const getLimitStatus = () => {
    if (!user?.limits) return null;
    
    const { daily_queries_used, daily_queries_limit, subscription } = user.limits;
    
    if (subscription === 'pro') {
      return {
        text: 'Sınırsız kullanım',
        color: 'text-purple-600',
        bgColor: 'bg-purple-100',
        progress: 100
      };
    }
    
    const usagePercent = (daily_queries_used / daily_queries_limit) * 100;
    
    if (usagePercent >= 90) {
      return {
        text: `${daily_queries_used}/${daily_queries_limit} (Limite yakın!)`,
        color: 'text-red-600',
        bgColor: 'bg-red-100',
        progress: usagePercent
      };
    } else if (usagePercent >= 70) {
      return {
        text: `${daily_queries_used}/${daily_queries_limit}`,
        color: 'text-yellow-600',
        bgColor: 'bg-yellow-100',
        progress: usagePercent
      };
    } else {
      return {
        text: `${daily_queries_used}/${daily_queries_limit}`,
        color: 'text-green-600',
        bgColor: 'bg-green-100',
        progress: usagePercent
      };
    }
  };

  const getSubscriptionBadge = (subscription) => {
    const badges = {
      free: { text: 'Free', color: 'bg-gray-100 text-gray-600' },
      starter: { text: 'Starter', color: 'bg-blue-100 text-blue-600' },
      pro: { text: 'Pro', color: 'bg-purple-100 text-purple-600' }
    };
    
    return badges[subscription] || badges.free;
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

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  const limitStatus = getLimitStatus();
  const subscriptionBadge = getSubscriptionBadge(user?.subscription);

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      {/* Welcome Header */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-gray-900">
              Hoş geldiniz, {user?.name}! 👋
            </h1>
            <p className="text-gray-600 mt-1">
              CodeFuser hesabınızı yönetin ve sorgu geçmişinizi görüntüleyin.
            </p>
          </div>
          <div className="flex items-center space-x-3">
            <span className={`px-3 py-1 rounded-full text-sm font-medium ${subscriptionBadge.color}`}>
              {subscriptionBadge.text}
            </span>
          </div>
        </div>
      </div>

      {/* Stats Cards */}
      <div className="grid md:grid-cols-3 gap-6">
        {/* Daily Usage */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-semibold text-gray-900">Günlük Kullanım</h3>
            <span className="text-2xl">📊</span>
          </div>
          
          {limitStatus && (
            <>
              <div className={`text-2xl font-bold mb-2 ${limitStatus.color}`}>
                {limitStatus.text}
              </div>
              
              {user?.limits?.subscription !== 'pro' && (
                <div className="w-full bg-gray-200 rounded-full h-2 mb-3">
                  <div 
                    className={`h-2 rounded-full transition-all duration-300 ${
                      limitStatus.progress >= 90 ? 'bg-red-500' : 
                      limitStatus.progress >= 70 ? 'bg-yellow-500' : 'bg-green-500'
                    }`}
                    style={{ width: `${limitStatus.progress}%` }}
                  ></div>
                </div>
              )}
              
              <p className="text-sm text-gray-600">
                {user?.limits?.file_prompts_enabled ? 
                  'Dosyaya özel prompt özelliği aktif' : 
                  'Sadece genel prompt kullanabilirsiniz'
                }
              </p>
            </>
          )}
        </div>

        {/* Total Queries */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-semibold text-gray-900">Toplam Sorgu</h3>
            <span className="text-2xl">🔍</span>
          </div>
          <div className="text-2xl font-bold text-blue-600 mb-2">
            {recentQueries.length}
          </div>
          <p className="text-sm text-gray-600">
            Bu hesapta yapılan toplam sorgu sayısı
          </p>
        </div>

        {/* System Stats */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-semibold text-gray-900">Sistem</h3>
            <span className="text-2xl">⚡</span>
          </div>
          <div className="space-y-2">
            <div className="flex justify-between text-sm">
              <span className="text-gray-600">Toplam Kullanıcı:</span>
              <span className="font-medium">{stats?.total_users || 0}</span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-gray-600">Template Sayısı:</span>
              <span className="font-medium">{stats?.templates_available || 0}</span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-gray-600">Toplam Sorgu:</span>
              <span className="font-medium">{stats?.total_queries || 0}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">Hızlı İşlemler</h2>
        <div className="grid md:grid-cols-3 gap-4">
          <Link
            to="/process"
            className="flex items-center p-4 border border-gray-200 rounded-lg hover:border-blue-500 hover:bg-blue-50 transition-colors"
          >
            <span className="text-2xl mr-3">🚀</span>
            <div>
              <h3 className="font-medium text-gray-900">Yeni İşlem</h3>
              <p className="text-sm text-gray-600">Dosyalarınızı işleyin</p>
            </div>
          </Link>
          
          <Link
            to="/history"
            className="flex items-center p-4 border border-gray-200 rounded-lg hover:border-blue-500 hover:bg-blue-50 transition-colors"
          >
            <span className="text-2xl mr-3">📋</span>
            <div>
              <h3 className="font-medium text-gray-900">Sorgu Geçmişi</h3>
              <p className="text-sm text-gray-600">Geçmiş sorgularınızı görün</p>
            </div>
          </Link>
          
          <div className="flex items-center p-4 border border-gray-200 rounded-lg bg-gray-50">
            <span className="text-2xl mr-3">📞</span>
            <div>
              <h3 className="font-medium text-gray-900">Destek</h3>
              <p className="text-sm text-gray-600">Yardım için iletişim</p>
            </div>
          </div>
        </div>
      </div>

      {/* Recent Queries */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-semibold text-gray-900">Son Sorgular</h2>
          <Link
            to="/history"
            className="text-blue-600 hover:text-blue-700 text-sm font-medium"
          >
            Tümünü gör →
          </Link>
        </div>
        
        {recentQueries.length > 0 ? (
          <div className="space-y-3">
            {recentQueries.map((query) => (
              <div
                key={query.id}
                className="flex items-center justify-between p-3 border border-gray-200 rounded-lg hover:bg-gray-50"
              >
                <div className="flex-1">
                  <div className="flex items-center space-x-3">
                    <span className="text-sm font-medium text-gray-900">
                      {query.files_count} dosya
                    </span>
                    <span className="text-xs text-gray-500">
                      {query.output_format.toUpperCase()}
                    </span>
                    {query.template_id && (
                      <span className="text-xs bg-blue-100 text-blue-600 px-2 py-1 rounded">
                        {query.template_id}
                      </span>
                    )}
                  </div>
                  <p className="text-sm text-gray-600 mt-1 truncate">
                    {query.general_prompt || 'Prompt belirtilmemiş'}
                  </p>
                </div>
                <div className="text-xs text-gray-500 ml-4">
                  {formatDate(query.created_at)}
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-8 text-gray-500">
            <span className="text-4xl mb-2 block">📝</span>
            <p>Henüz sorgu yapmamışsınız.</p>
            <Link
              to="/process"
              className="text-blue-600 hover:text-blue-700 font-medium"
            >
              İlk sorgunuzu oluşturun
            </Link>
          </div>
        )}
      </div>

      {/* Upgrade Notice */}
      {user?.subscription === 'free' && (
        <div className="bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg shadow-md p-6 text-white">
          <h2 className="text-xl font-semibold mb-2">Hesabınızı Yükseltin</h2>
          <p className="mb-4 opacity-90">
            Starter veya Pro paketine geçerek daha fazla özellik ve sorgu hakkı kazanın.
          </p>
          <div className="flex space-x-3">
            <span className="bg-white text-blue-600 px-4 py-2 rounded-lg font-medium">
              Starter: 100 sorgu/gün
            </span>
            <span className="bg-white text-purple-600 px-4 py-2 rounded-lg font-medium">
              Pro: Sınırsız + özel prompt
            </span>
          </div>
        </div>
      )}
    </div>
  );
};

export default Dashboard;