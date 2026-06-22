import { createBrowserRouter } from "react-router-dom"
import App from "@/App"
import { ProtectedRoute } from "@/components/auth/ProtectedRoute"
import Dashboard from "@/pages/Dashboard"
import Leads from "@/pages/Leads"
import Conversations from "@/pages/Conversations"
import Activity from "@/pages/Activity"
import Settings from "@/pages/Settings"
import Login from "@/pages/Login"
import Signup from "@/pages/Signup"
import SSOCallback from "@/pages/SSOCallback"
import GetStarted from "@/pages/GetStarted"

export const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      { path: "login", element: <Login /> },
      { path: "signup", element: <Signup /> },
      { path: "sso-callback", element: <SSOCallback /> },
      {
        element: <ProtectedRoute />,
        children: [
          { index: true, element: <Dashboard /> },
          { path: "leads", element: <Leads /> },
          { path: "conversations", element: <Conversations /> },
          { path: "activity", element: <Activity /> },
          { path: "settings", element: <Settings /> },
          { path: "get-started", element: <GetStarted /> },
        ],
      },
    ],
  },
])
