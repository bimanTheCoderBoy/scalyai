import { useState } from "react"
import { useSignUp } from "@clerk/react/legacy"
import { useNavigate } from "react-router-dom"
import { Loader2 } from "lucide-react"
import { FcGoogle } from "react-icons/fc"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { getClerkError } from "@/lib/clerk-error"

interface SignupCardProps {
  onClickLogin: () => void
}

export function SignupCard({ onClickLogin }: SignupCardProps) {
  const { signUp, setActive, isLoaded } = useSignUp()
  const navigate = useNavigate()

//   const [username, setUsername] = useState("")
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [confirmPassword, setConfirmPassword] = useState("")
  const [code, setCode] = useState("")
  const [error, setError] = useState("")
  const [loading, setLoading] = useState(false)
  const [pendingVerification, setPendingVerification] = useState(false)

  const clearError = () => setError("")

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!isLoaded || !signUp) return

    if (password !== confirmPassword) {
      setError("Passwords do not match.")
      return
    }

    setError("")
    setLoading(true)

    try {
      await signUp.create({
        // username,
        emailAddress: email,
        password,
      })

      await signUp.prepareEmailAddressVerification({ strategy: "email_code" })
      setPendingVerification(true)
    } catch (err: unknown) {
      setError(getClerkError(err))
    } finally {
      setLoading(false)
    }
  }

  const handleVerify = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!isLoaded || !signUp) return

    setError("")
    setLoading(true)

    try {
      const result = await signUp.attemptEmailAddressVerification({ code })

      if (result.status === "complete") {
        await setActive({ session: result.createdSessionId })
        navigate("/")
      }
    } catch (err: unknown) {
      setError(getClerkError(err))
    } finally {
      setLoading(false)
    }
  }

  const handleGoogleSignUp = async () => {
    if (!isLoaded || !signUp) return
    
    try {
      await signUp.authenticateWithRedirect({
        strategy: "oauth_google",
        redirectUrl: "/sso-callback",
        redirectUrlComplete: "/",
      })
    } catch (err: unknown) {
      setError(getClerkError(err))
    }
  }

  if (pendingVerification) {
    return (
      <div className="min-h-screen min-w-screen flex items-center justify-center bg-background relative">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(120,119,198,0.15),transparent_60%)]" />

        <Card className="w-full max-w-md relative backdrop-blur-xl bg-card/80 border border-border/50 shadow-2xl">
          <CardHeader className="space-y-2 text-center">
            <div className="text-sm text-muted-foreground tracking-widest">
              SCALYAI
            </div>
            <CardTitle className="text-2xl font-semibold">
              Verify your email
            </CardTitle>
            <CardDescription>
              We sent a verification code to {email}
            </CardDescription>
          </CardHeader>

          <CardContent>
            <form onSubmit={handleVerify} className="space-y-5">
              <div className="space-y-2">
                <Label htmlFor="code">Verification Code</Label>
                <Input
                  id="code"
                  placeholder="Enter 6-digit code"
                  className="bg-background/50 backdrop-blur-sm text-center tracking-widest text-lg"
                  value={code}
                  onChange={(e) => { setCode(e.target.value); clearError() }}
                  maxLength={6}
                  required
                  disabled={loading}
                  autoFocus
                />
              </div>

              {error && (
                <p className="text-sm text-destructive">{error}</p>
              )}

              <Button type="submit" className="w-full h-10 text-sm font-medium" disabled={loading}>
                {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : "Verify →"}
              </Button>
            </form>
          </CardContent>
        </Card>
      </div>
    )
  }

  return (
    <div className="min-h-screen min-w-screen flex items-center justify-center bg-background relative">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(120,119,198,0.15),transparent_60%)]" />

      <Card className="w-full max-w-md relative backdrop-blur-xl bg-card/80 border border-border/50 shadow-2xl">
        <CardHeader className="space-y-2 text-center">
          <div className="text-sm text-muted-foreground tracking-widest">
            SCALYAI
          </div>
          <CardTitle className="text-2xl font-semibold">
            Create your account
          </CardTitle>
          <CardDescription>
            Launch your AI sales engine
          </CardDescription>
        </CardHeader>

        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-5">
            {/* <div className="space-y-2">
              <Label htmlFor="username">Username</Label>
              <Input
                id="username"
                placeholder="yourname"
                className="bg-background/50 backdrop-blur-sm"
                value={username}
                onChange={(e) => { setUsername(e.target.value); clearError() }}
                required
                disabled={loading}
              />
            </div> */}

            <div className="space-y-2">
              <Label htmlFor="email">Email</Label>
              <Input
                id="email"
                type="email"
                placeholder="you@company.com"
                className="bg-background/50 backdrop-blur-sm"
                value={email}
                onChange={(e) => { setEmail(e.target.value); clearError() }}
                required
                disabled={loading}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input
                id="password"
                type="password"
                className="bg-background/50 backdrop-blur-sm"
                value={password}
                onChange={(e) => { setPassword(e.target.value); clearError() }}
                required
                disabled={loading}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="confirm">Confirm Password</Label>
              <Input
                id="confirm"
                type="password"
                className="bg-background/50 backdrop-blur-sm"
                value={confirmPassword}
                onChange={(e) => { setConfirmPassword(e.target.value); clearError() }}
                required
                disabled={loading}
              />
            </div>

            {error && (
              <p className="text-sm text-destructive">{error}</p>
            )}

            <Button type="submit" className="w-full h-10 text-sm font-medium" disabled={loading}>
              {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : "Create Account →"}
            </Button>
          </form>
        </CardContent>

        <CardFooter className="flex flex-col gap-3">
          <Button
            variant="outline"
            className="w-full h-10 bg-background/40 hover:bg-background/60 transition flex items-center justify-center gap-3 border border-border/60"
            onClick={handleGoogleSignUp}
            disabled={loading}
          >
            <FcGoogle className="w-5 h-5" />
            <span className="text-sm font-medium">
              Continue with Google
            </span>
          </Button>

          <p className="text-xs text-muted-foreground text-center">
            Already have an account?{" "}
            <span className="text-primary cursor-pointer hover:underline" onClick={onClickLogin}>
              Login
            </span>
          </p>
        </CardFooter>
      </Card>
    </div>
  )
}
