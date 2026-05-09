import { useAuth } from "@clerk/react"
import { Navigate, Outlet } from "react-router-dom"
import { Loader2 } from "lucide-react"

export function ProtectedRoute() {
  const { isLoaded, isSignedIn } = useAuth()

  if (!isLoaded) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-background">
        <Loader2 className="h-8 w-8 animate-spin text-muted-foreground" />
      </div>
    )
  }

  if (!isSignedIn && location.pathname !== "/sso-callback") {
    return <Navigate to="/login" />
  }

  return <Outlet />
}
