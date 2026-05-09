import { useAuth } from "@clerk/react"
import { Navigate, useNavigate } from "react-router-dom"
import { SignupCard } from "@/components/auth/SignupCard"

export default function Signup() {
  const { isSignedIn, isLoaded } = useAuth()
  const navigate = useNavigate()

  if (isLoaded && isSignedIn) {
    return <Navigate to="/" replace />
  }

  return <SignupCard onClickLogin={() => navigate("/login")} />
}
