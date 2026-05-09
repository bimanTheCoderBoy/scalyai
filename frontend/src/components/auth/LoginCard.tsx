import { useState } from "react"
import { useSignIn } from "@clerk/react/legacy"
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

interface LoginCardProps {
  onClickSignup: () => void
}

export function LoginCard({ onClickSignup }: LoginCardProps) {
  const { signIn, setActive, isLoaded } = useSignIn()
  const navigate = useNavigate()

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!isLoaded || !signIn) return

    setError("")
    setLoading(true)

    try {
      const result = await signIn.create({ identifier: email, password })

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

  const handleGoogleSignIn = async () => {
    if (!isLoaded || !signIn) return

    try {
      await signIn.authenticateWithRedirect({
        strategy: "oauth_google",
        redirectUrl: "/sso-callback",
        redirectUrlComplete: "/",
      })
    } catch (err: unknown) {
      setError(getClerkError(err))
    }
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
            Welcome back
          </CardTitle>
          <CardDescription>
            AI-powered sales engine login
          </CardDescription>
        </CardHeader>

        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-5">
            <div className="space-y-2">
              <Label htmlFor="email">Email</Label>
              <Input
                id="email"
                type="email"
                placeholder="you@company.com"
                className="bg-background/50 backdrop-blur-sm"
                value={email}
                onChange={(e) => { setEmail(e.target.value); setError("") }}
                required
                disabled={loading}
              />
            </div>

            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <Label htmlFor="password">Password</Label>
                <a
                  href="#"
                  className="text-xs text-muted-foreground hover:text-primary transition"
                >
                  Forgot?
                </a>
              </div>
              <Input
                id="password"
                type="password"
                className="bg-background/50 backdrop-blur-sm"
                value={password}
                onChange={(e) => { setPassword(e.target.value); setError("") }}
                required
                disabled={loading}
              />
            </div>

            {error && (
              <p className="text-sm text-destructive">{error}</p>
            )}

            <Button type="submit" className="w-full h-10 text-sm font-medium" disabled={loading}>
              {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : "Login →"}
            </Button>
          </form>
        </CardContent>

        <CardFooter className="flex flex-col gap-3">
          <Button
            variant="outline"
            className="w-full cursor-pointer h-10 bg-background/40 hover:bg-background/60 transition flex items-center justify-center gap-3 border border-border/60"
            onClick={handleGoogleSignIn}
            disabled={loading}
          >
            <FcGoogle className="w-5 h-5" />
            <span className="text-sm font-medium">
              Continue with Google
            </span>
          </Button>

          <p className="text-xs text-muted-foreground text-center">
            No account?{" "}
            <span className="text-primary cursor-pointer hover:underline" onClick={onClickSignup}>
              Create one
            </span>
          </p>
        </CardFooter>
      </Card>
    </div>
  )
}
