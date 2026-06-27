import { useUser,useAuth } from "@clerk/react"
import { useEffect } from "react"
export default function Dashboard() {

  const { user } = useUser()
  const {getToken} = useAuth()
  useEffect(() => {
    const fetchData = async () => {
      const token = await getToken()
      console.log(token)
    }
    fetchData()
  }, [getToken])
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
