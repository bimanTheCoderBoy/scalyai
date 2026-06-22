import * as React from "react"
import type { BusinessContext } from "@/types/business-context"
import { createEmptyBusinessContext } from "@/types/business-context"

export type Phase = "upload" | "extracting" | "form"

type GetStartedState = {
  phase: Phase
  setPhase: (phase: Phase) => void
  data: BusinessContext
  setData: React.Dispatch<React.SetStateAction<BusinessContext>>
  updateSection: <K extends keyof BusinessContext>(
    section: K,
    patch: Partial<NonNullable<BusinessContext[K]>>
  ) => void
}

const GetStartedContext = React.createContext<GetStartedState | null>(null)

function GetStartedProvider({ children }: { children: React.ReactNode }) {
  const [phase, setPhase] = React.useState<Phase>("upload")
  const [data, setData] = React.useState<BusinessContext>(
    createEmptyBusinessContext()
  )

  const updateSection = React.useCallback(
    <K extends keyof BusinessContext>(
      section: K,
      patch: Partial<NonNullable<BusinessContext[K]>>
    ) => {
      setData((prev) => ({
        ...prev,
        [section]: { ...prev[section], ...patch },
      }))
    },
    []
  )

  const value = React.useMemo(
    () => ({ phase, setPhase, data, setData, updateSection }),
    [phase, data, updateSection]
  )

  return (
    <GetStartedContext.Provider value={value}>
      {children}
    </GetStartedContext.Provider>
  )
}

function useGetStarted() {
  const ctx = React.useContext(GetStartedContext)
  if (!ctx) throw new Error("useGetStarted must be used within GetStartedProvider")
  return ctx
}

export { GetStartedProvider, useGetStarted }
