import { HandleSSOCallback } from "@clerk/react"
import {   useNavigate } from "react-router-dom"
import { Loader2 } from "lucide-react"

export default function SSOCallback() {
  const navigate = useNavigate()

  
   
  return (
    <div className="min-h-screen flex items-center justify-center bg-background">
      <HandleSSOCallback
        navigateToApp={async ({ decorateUrl }) => {
          console.log("navigateToApp")
          const url = decorateUrl("/")
          if (url.startsWith("http")) {
            window.location.href = url
            return
          }
          navigate(url)
        }}
        navigateToSignIn={() => {console.log("navigateToSignIn"); navigate("/login")}}
        navigateToSignUp={() => {console.log("navigateToSignUp"); navigate("/signup")}}
      />
      <Loader2 className="h-8 w-8 animate-spin text-muted-foreground" />
    </div>
       
  )
}
