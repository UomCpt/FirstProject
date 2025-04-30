// src/components/Header.jsx
import React from 'react';
import ThemeToggle from '../Components/ThemeToggle';
import ProfileImage from '../assets/avatar.png'
import Logo from '../assets/logo.png'
import './Header.css';


function Header() {
  return (
    <header className="header">
      <div className="logo-section">
        <img src={Logo} alt="Logo" className="logo" />
        <span className="title">Cpt Competition</span>
      </div>

      <nav className="nav-links">
        <a href="#">ProblemSet</a>
        <a href="#">LeaderBoard</a>
      </nav>

      <div className="header-right">
        <div className="timer">00:28:08</div>
        <ThemeToggle />
        <img src={ProfileImage} alt="profile" className="profile-icon" />
      </div>
    </header>
  );
}

export default Header;