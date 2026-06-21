import * as React from "react"
import { ArrowLeft, ArrowRight, Check, Loader2 } from "lucide-react"
import { toast } from "sonner"

import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import { cn } from "@/lib/utils"

import { StepBusinessIdentity } from "./steps/step-business-identity"
import { StepOperationalDetails } from "./steps/step-operational-details"
import { StepTargetCustomer } from "./steps/step-target-customer"
import { StepCustomerPreferences } from "./steps/step-customer-preferences"
import { StepProductService } from "./steps/step-product-service"
import { StepSalesFunnel } from "./steps/step-sales-funnel"
import { StepOutreachStrategy } from "./steps/step-outreach-strategy"
import { StepLeadScoring } from "./steps/step-lead-scoring"
import { StepCompetitiveLandscape } from "./steps/step-competitive-landscape"
import { StepReview } from "./steps/step-review"

type StepDef = {
  id: string
  title: string
  description: string
  component: React.FC
}

const STEPS: StepDef[] = [
  {
    id: "business-identity",
    title: "Business Identity",
    description: "Core info about your company.",
    component: StepBusinessIdentity,
  },
  {
    id: "operations",
    title: "Operations & Technology",
    description: "How your business runs day-to-day.",
    component: StepOperationalDetails,
  },
  {
    id: "target-customer",
    title: "Target Customer",
    description: "Who you sell to — ICP, segments, personas.",
    component: StepTargetCustomer,
  },
  {
    id: "customer-preferences",
    title: "Customer Preferences",
    description: "How your customers prefer to be reached.",
    component: StepCustomerPreferences,
  },
  {
    id: "product-service",
    title: "Product & Service",
    description: "What you offer and how it's delivered.",
    component: StepProductService,
  },
  {
    id: "sales-funnel",
    title: "Sales Funnel",
    description: "Your sales process from lead to close.",
    component: StepSalesFunnel,
  },
  {
    id: "outreach-strategy",
    title: "Outreach Strategy",
    description: "Email structure and messaging approach.",
    component: StepOutreachStrategy,
  },
  {
    id: "lead-scoring",
    title: "Lead Scoring",
    description: "How you prioritize and categorize leads.",
    component: StepLeadScoring,
  },
  {
    id: "competitive-landscape",
    title: "Competitive Landscape",
    description: "Competitors and your market positioning.",
    component: StepCompetitiveLandscape,
  },
  {
    id: "review",
    title: "Review & Submit",
    description: "Confirm everything looks right.",
    component: StepReview,
  },
]

function PhaseForm() {
  const [stepIndex, setStepIndex] = React.useState(0)
  const [submitting, setSubmitting] = React.useState(false)
  const [submitted, setSubmitted] = React.useState(false)

  const current = STEPS[stepIndex]
  const isLast = stepIndex === STEPS.length - 1
  const progress = ((stepIndex + 1) / STEPS.length) * 100
  const StepComponent = current.component

  function handleBack() {
    setStepIndex((i) => Math.max(0, i - 1))
  }

  async function handleNext() {
    if (!isLast) {
      setStepIndex((i) => i + 1)
      return
    }
    setSubmitting(true)
    // TODO: POST final data to backend
    await new Promise((r) => setTimeout(r, 1000))
    setSubmitting(false)
    setSubmitted(true)
    toast.success("Submitted successfully")
  }

  if (submitted) {
    return (
      <Card className="overflow-hidden">
        <CardContent className="flex flex-col items-center gap-3 py-10 text-center">
          <div className="flex size-12 items-center justify-center rounded-full bg-primary/10 text-primary">
            <Check className="size-6" />
          </div>
          <div className="space-y-1">
            <h2 className="font-heading text-base font-medium">
              You&apos;re all set
            </h2>
            <p className="text-sm text-muted-foreground">
              Your business context has been saved. We&apos;ll take it from
              here.
            </p>
          </div>
        </CardContent>
      </Card>
    )
  }

  return (
    <Card className="overflow-hidden">
      <CardHeader>
        <div className="flex items-center justify-between gap-4">
          <span className="text-xs font-medium tracking-wide text-muted-foreground uppercase">
            Step {stepIndex + 1} of {STEPS.length}
          </span>
          <StepDots count={STEPS.length} active={stepIndex} />
        </div>
        <CardTitle className="mt-2">{current.title}</CardTitle>
        <CardDescription>{current.description}</CardDescription>
        <Progress value={progress} className="mt-3" />
      </CardHeader>

      <CardContent className="max-h-[60vh] overflow-y-auto pt-1 pb-2">
        <StepComponent />
      </CardContent>

      <div className="flex items-center justify-between gap-2 border-t px-4 py-3">
        <Button
          variant="ghost"
          onClick={handleBack}
          disabled={stepIndex === 0 || submitting}
        >
          <ArrowLeft data-icon="inline-start" />
          Back
        </Button>
        <Button onClick={handleNext} disabled={submitting}>
          {submitting ? (
            <>
              <Loader2 data-icon="inline-start" className="animate-spin" />
              Submitting
            </>
          ) : isLast ? (
            <>
              Submit
              <Check data-icon="inline-end" />
            </>
          ) : (
            <>
              Continue
              <ArrowRight data-icon="inline-end" />
            </>
          )}
        </Button>
      </div>
    </Card>
  )
}

function StepDots({ count, active }: { count: number; active: number }) {
  return (
    <div className="flex items-center gap-1.5">
      {Array.from({ length: count }).map((_, i) => (
        <span
          key={i}
          className={cn(
            "h-1.5 rounded-full transition-all",
            i === active
              ? "w-4 bg-primary"
              : i < active
                ? "w-1.5 bg-primary/60"
                : "w-1.5 bg-muted-foreground/25"
          )}
        />
      ))}
    </div>
  )
}

export { PhaseForm }
