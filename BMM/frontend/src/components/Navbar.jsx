import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { UserButton, useUser } from '@clerk/clerk-react';

export default function Navbar() {
  const { isSignedIn } = useUser();
  const location = useLocation();

  return (
    <nav className="navbar">
      <div className="logo">
        <Link to="/">Social Scheduler</Link>
      </div>
      
      <div className="nav-links">
        {isSignedIn && (
          <>
            <Link 
              to="/dashboard" 
              className={location.pathname === '/dashboard' ? 'active' : ''}
            >
              Dashboard
            </Link>
            <div className="vertical-divider">
            <Link 
              to="/content-history" 
              className={location.pathname === '/content-history' ? 'active' : ''}
            >
              History
            </Link>
            </div>
          </>
        )}
      </div>
      
      <div className="user-section">
        {isSignedIn ? (
          <UserButton afterSignOutUrl="/" />
        ) : (
          <Link to="/login" className="login-btn">Sign In</Link>
        )}
      </div>
    </nav>
  );
}