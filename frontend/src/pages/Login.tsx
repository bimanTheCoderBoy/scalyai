import { useAuth } from "@clerk/react"
import { Navigate, useNavigate } from "react-router-dom"
import { LoginCard } from "@/components/auth/LoginCard"

export default function Login() {
  const { isSignedIn, isLoaded } = useAuth()
  const navigate = useNavigate()

  if (isLoaded && isSignedIn) {
    return <Navigate to="/" replace />
  }

  return <LoginCard onClickSignup={() => navigate("/signup")} />
}
