'use client'

import { Button } from "@/components/ui/button"
import { useRouter } from "next/navigation"

export default function Page() {
  const router = useRouter()

  return (
    <div className="flex min-h-svh items-center justify-center p-6">
        <Button
          onClick={() => {
            router.push("/get-started")
          }}
        >
          Get Started
        </Button>
    </div>
  )
}
