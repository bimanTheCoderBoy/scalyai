import { Outlet } from "react-router-dom"

function App() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <Outlet />
    </div>
  )
}

export default App
