import { useState, useEffect } from 'react'
import { useAuth } from '../AuthContext'
import './Navbar.css'

export default function Navbar({ title, backHref, showClock = false, showUpload = false }) {
  const { signOut, profile } = useAuth()
  const [time, setTime] = useState(new Date())

  const isDlhRole = profile?.role === 'dlh_manager' || profile?.role === 'dlh_operator'
  const shouldShowUpload = showUpload && !isDlhRole

  useEffect(() => {
    if (!showClock) return
    const timer = setInterval(() => setTime(new Date()), 1000)
    return () => clearInterval(timer)
  }, [showClock])

  const fmtTime = t => t.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' })

  return (
    <header className="navbar-vvip">
      {/* BRAND & NAVIGATION LEFT */}
      <div className="nav-left">
        {backHref && (
          <a href={backHref} className="btn-back">
            ←
          </a>
        )}
        <div className="nav-brand">
          <span className="logo-icon">💧</span>
          <span className="brand-title">{title || 'DRAIN-EYE'}</span>
        </div>
      </div>

      {/* USER & ACTIONS RIGHT */}
      <div className="nav-right">
        {showClock && (
          <span className="nav-clock">{fmtTime(time)} WIB</span>
        )}

        {shouldShowUpload && (
          <a href="/upload" className="btn-upload">
            📷 <span className="upload-text">Upload</span>
          </a>
        )}

        <div className="user-profile">
          <span className="user-name">{profile?.full_name || profile?.email}</span>
          <span className="user-role">
            {profile?.role === 'dlh_manager'  ? '🏛️ DLH Manager'  :
             profile?.role === 'dlh_operator' ? '🏛️ DLH Operator' :
                                                '👤 Warga'}
          </span>
        </div>

        <button onClick={signOut} className="btn-logout">
          Logout
        </button>
      </div>
    </header>
  )
}