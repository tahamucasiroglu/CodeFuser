import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useNotification } from '../context/NotificationContext';

const Header = () => {
  const { user, logout } = useAuth();
  const { showSuccess } = useNotification();
  const location = useLocation();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    showSuccess('Başarıyla çıkış yapıldı');
    navigate('/');
  };

  const getLimitColor = (limits) => {
    if (!limits) return 'text-gray-500';
    
    if (limits.subscription === 'pro') return 'text-purple-600';
    if (limits.subscription === 'starter') return 'text-blue-600';
    
    const usagePercent = limits.daily_queries_used / limits.daily_queries_limit;
    if (usagePercent >= 0.9) return 'text-red-600';
    if (usagePercent >= 0.7) return 'text-yellow-600';
    return 'text-green-600';
  };

  const formatLimits = (limits) => {
    if (!limits) return '';
    
    if (limits.subscription === 'pro') {
      return '∞ (Pro)';
    }
    
    return `${limits.daily_queries_used}/${limits.daily_queries_limit}`;
  };

  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo and Navigation */}
          <div className="flex items-center space-x-8">
            <Link to="/" className="flex items-center space-x-2">
              <span className="text-2xl">🚀</span>
              <h1 className="text-xl font-bold text-gray-900">CodeFuser Web</h1>
            </Link>
            
            <nav className="hidden md:flex space-x-6">
              <Link 
                to="/process" 
                className={`text-gray-600 hover:text-blue-600 transition-colors ${
                  location.pathname === '/process' ? 'text-blue-600 font-medium' : ''
                }`}
              >
                İşle
              </Link>
              
              {user && (
                <>
                  <Link 
                    to="/dashboard" 
                    className={`text-gray-600 hover:text-blue-600 transition-colors ${
                      location.pathname === '/dashboard' ? 'text-blue-600 font-medium' : ''
                    }`}
                  >
                    Dashboard
                  </Link>
                  <Link 
                    to="/history" 
                    className={`text-gray-600 hover:text-blue-600 transition-colors ${
                      location.pathname === '/history' ? 'text-blue-600 font-medium' : ''
                    }`}
                  >
                    Geçmiş
                  </Link>
                </>
              )}
            </nav>
          </div>

          {/* User Info and Actions */}
          <div className="flex items-center space-x-4">
            {user ? (
              <>
                {/* User Limits Display */}
                <div className="hidden sm:flex items-center space-x-3 text-sm">
                  <div className="text-gray-600">
                    <span className="font-medium">{user.name}</span>
                    <span className="mx-2">•</span>
                    <span className="capitalize font-medium text-blue-600">
                      {user.subscription}
                    </span>
                  </div>
                  
                  {user.limits && (
                    <div className={`font-medium ${getLimitColor(user.limits)}`}>
                      {formatLimits(user.limits)} sorgu
                    </div>
                  )}
                </div>

                {/* User Menu */}
                <div className="flex items-center space-x-2">
                  <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                    <span className="text-blue-600 font-medium text-sm">
                      {user.name.charAt(0).toUpperCase()}
                    </span>
                  </div>
                  
                  <button
                    onClick={handleLogout}
                    className="text-gray-600 hover:text-red-600 transition-colors text-sm font-medium"
                  >
                    Çıkış
                  </button>
                </div>
              </>
            ) : (
              <div className="flex items-center space-x-3">
                <Link
                  to="/login"
                  className="text-gray-600 hover:text-blue-600 transition-colors font-medium"
                >
                  Giriş Yap
                </Link>
                <Link
                  to="/login?mode=signup"
                  className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors font-medium"
                >
                  Kayıt Ol
                </Link>
              </div>
            )}
          </div>
        </div>

        {/* Mobile Navigation */}
        <div className="md:hidden border-t border-gray-200 py-3">
          <nav className="flex space-x-6">
            <Link 
              to="/process" 
              className={`text-gray-600 hover:text-blue-600 transition-colors text-sm ${
                location.pathname === '/process' ? 'text-blue-600 font-medium' : ''
              }`}
            >
              İşle
            </Link>
            
            {user && (
              <>
                <Link 
                  to="/dashboard" 
                  className={`text-gray-600 hover:text-blue-600 transition-colors text-sm ${
                    location.pathname === '/dashboard' ? 'text-blue-600 font-medium' : ''
                  }`}
                >
                  Dashboard
                </Link>
                <Link 
                  to="/history" 
                  className={`text-gray-600 hover:text-blue-600 transition-colors text-sm ${
                    location.pathname === '/history' ? 'text-blue-600 font-medium' : ''
                  }`}
                >
                  Geçmiş
                </Link>
              </>
            )}
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;