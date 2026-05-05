export type CustomerType = "B2B" | "B2C" | "Both"

export type DeliveryModel = "SaaS" | "Service" | "Hybrid" | "Other"

export type BusinessIdentity = {
  business_name: string | null
  industry: string | null
  products_services: string[] | null
  usp: string | null
  differentiators: string[] | null
  pricing_model: string | null
  business_size: string | null
  locations: string[] | null
  avg_ticket_price: string | null
  cac: string | null
}

export type OperationalDetails = {
  operational_model: string | null
  operational_workflow: string[] | null
  technology_stack: string[] | null
  internal_challenges: string[] | null
}

export type B2BICP = {
  industry: string[] | null
  company_size: string | null
  revenue_range: string | null
  geography: string[] | null
  monthly_volume: string | null
  growth_stage: string | null
}

export type B2CDemographics = {
  age_group: string | null
  income_level: string | null
  location: string | null
}

export type B2CICP = {
  demographics: B2CDemographics | null
  behavioral_traits: string[] | null
}

export type BuyerPersona = {
  role: string | null
  focus_areas: string[] | null
  pain_points: string[] | null
  goals: string[] | null
  communication_preference: string | null
}

export type TargetCustomerProfile = {
  customer_type: CustomerType | null
  b2b_icp: B2BICP | null
  b2c_icp: B2CICP | null
  buyer_personas: BuyerPersona[] | null
  customer_segments: string[] | null
}

export type CustomerPreferences = {
  preferred_email_length: string | null
  preferred_structure: string | null
  high_intent_behavior: string | null
  low_intent_behavior: string | null
}

export type ProductServiceDetails = {
  features: string[] | null
  benefits: string[] | null
  pricing_tiers: string | null
  delivery_model: DeliveryModel | null
}

export type SalesFunnel = {
  stages: string[] | null
  typical_cycle_duration: string | null
  common_dropoff_reasons: string[] | null
}

export type OutreachStrategy = {
  email_structure: string[] | null
  followup_count: string | null
  followup_cadence: string | null
  messaging_themes: string[] | null
}

export type LeadScoring = {
  scoring_factors: string[] | null
  lead_categories: string[] | null
  behavioral_signals: string[] | null
  automation_rules: string | null
}

export type CompetitiveLandscape = {
  competitor_types: string[] | null
  differentiation: string[] | null
  positioning_statement: string | null
}

export type BusinessContext = {
  business_identity: BusinessIdentity | null
  operational_details: OperationalDetails | null
  target_customer_profile: TargetCustomerProfile | null
  customer_preferences: CustomerPreferences | null
  product_service_details: ProductServiceDetails | null
  sales_funnel: SalesFunnel | null
  outreach_strategy: OutreachStrategy | null
  lead_scoring: LeadScoring | null
  competitive_landscape: CompetitiveLandscape | null
}

export function createEmptyBusinessContext(): BusinessContext {
  return {
    business_identity: {
      business_name: null,
      industry: null,
      products_services: null,
      usp: null,
      differentiators: null,
      pricing_model: null,
      business_size: null,
      locations: null,
      avg_ticket_price: null,
      cac: null,
    },
    operational_details: {
      operational_model: null,
      operational_workflow: null,
      technology_stack: null,
      internal_challenges: null,
    },
    target_customer_profile: {
      customer_type: null,
      b2b_icp: {
        industry: null,
        company_size: null,
        revenue_range: null,
        geography: null,
        monthly_volume: null,
        growth_stage: null,
      },
      b2c_icp: {
        demographics: { age_group: null, income_level: null, location: null },
        behavioral_traits: null,
      },
      buyer_personas: null,
      customer_segments: null,
    },
    customer_preferences: {
      preferred_email_length: null,
      preferred_structure: null,
      high_intent_behavior: null,
      low_intent_behavior: null,
    },
    product_service_details: {
      features: null,
      benefits: null,
      pricing_tiers: null,
      delivery_model: null,
    },
    sales_funnel: {
      stages: null,
      typical_cycle_duration: null,
      common_dropoff_reasons: null,
    },
    outreach_strategy: {
      email_structure: null,
      followup_count: null,
      followup_cadence: null,
      messaging_themes: null,
    },
    lead_scoring: {
      scoring_factors: null,
      lead_categories: null,
      behavioral_signals: null,
      automation_rules: null,
    },
    competitive_landscape: {
      competitor_types: null,
      differentiation: null,
      positioning_statement: null,
    },
  }
}
