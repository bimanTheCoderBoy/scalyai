import { StepBusinessIdentity } from "@/components/get-started/steps/step-business-identity"
import { StepOperationalDetails } from "@/components/get-started/steps/step-operational-details"
import { StepTargetCustomer } from "@/components/get-started/steps/step-target-customer"
import { StepCustomerPreferences } from "@/components/get-started/steps/step-customer-preferences"
import { StepProductService } from "@/components/get-started/steps/step-product-service"
import { StepSalesFunnel } from "@/components/get-started/steps/step-sales-funnel"
import { StepOutreachStrategy } from "@/components/get-started/steps/step-outreach-strategy"
import { StepLeadScoring } from "@/components/get-started/steps/step-lead-scoring"
import { StepCompetitiveLandscape } from "@/components/get-started/steps/step-competitive-landscape"
import { StepReview } from "@/components/get-started/steps/step-review"


type StepDef = {
    id: string
    title: string
    description: string
    component: React.FC
}
  
export const STEPS: StepDef[] = [
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