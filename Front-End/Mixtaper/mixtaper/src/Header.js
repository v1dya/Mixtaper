import React from 'react'
import './css/Header.css'
import logo from './img/mixtaper logo.png';

function Header() {
  return (
    <div className='header'>
        <img src={logo} alt='logo' className='header__logo'/>
    </div>
  )
}

export default Header