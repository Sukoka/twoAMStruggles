import React from 'react'
import { Link } from 'react-router-dom'

function Navbar() {
    return (
        <>
            <nav className='navbar'>
                <div className='navbar-container'>
                    <Link to="/" className="navbar-logo">
                    DREY <i className='fas fa-hippo'></i>
                    </Link>
                </div>
            </nav>
        </>
    )
}

export default Navbar

