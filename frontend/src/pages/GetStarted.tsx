import { GetStartedProvider, useGetStarted } from "@/components/get-started/get-started-context"
import { GetStartedForm } from "@/components/get-started/get-started-form"
import { PhaseExtracting } from "@/components/get-started/phase-extracting"
import { PhaseForm } from "@/components/get-started/phase-form"

function PhaseRouter() {
  const { phase } = useGetStarted()
  return (
    <>
      {phase === "upload" && <GetStartedForm />}
      {phase === "extracting" && <PhaseExtracting />}
      {phase === "form" && <PhaseForm />}
    </>
  )
}

export default function GetStarted() {
  return (
    <main className="relative flex min-h-svh items-center justify-center px-4 py-10 sm:py-16">
      <div
        aria-hidden
        className="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_top,theme(colors.muted)_0%,transparent_55%)]"
      />
      <div className="w-full max-w-xl">
        <GetStartedProvider>
          <PhaseRouter />
        </GetStartedProvider>
      </div>
    </main>
  )
}
