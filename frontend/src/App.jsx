import { useEffect, useState } from 'react'

export default function App() {
  const [status, setStatus] = useState('checking...')

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/health/')
      .then((res) => res.json())
      .then((data) => setStatus(`${data.app} backend says: ${data.status}`))
      .catch(() => setStatus('backend not reachable'))
  }, [])

  return (
    <div className="min-h-screen bg-slate-900 flex flex-col items-center justify-center gap-4">
      <h1 className="text-5xl font-bold text-emerald-400">MindOS</h1>
      <p className="text-lg text-slate-300">{status}</p>
    </div>
  )
}