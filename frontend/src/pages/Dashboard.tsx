import { useUser } from "@clerk/react"
export default function Dashboard() {

  const { user } = useUser()
  console.log("user", user)
  return (
    <div>
      <h1 className="text-xl font-semibold">Dashboard</h1>
      <p className="text-sm text-muted-foreground mt-1">
        Overview of your sales pipeline
        {
          user && <p className="text-sm text-muted-foreground mt-1">Welcome, {user.emailAddresses[0].emailAddress} {user.username || "not added"}</p>
        }
      </p>
    </div>
  )
}
