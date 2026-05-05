from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


# ----------------------------
# ENUMS
# ----------------------------

class CustomerType(str, Enum):
    B2B = "B2B"
    B2C = "B2C"
    BOTH = "Both"


class DeliveryModel(str, Enum):
    SAAS = "SaaS"
    SERVICE = "Service"
    HYBRID = "Hybrid"
    OTHER = "Other"


# ----------------------------
# BUSINESS IDENTITY
# ----------------------------

class BusinessIdentity(BaseModel):
    business_name: Optional[str] = Field(
        None, description="Official registered name of the business"
    )
    industry: Optional[str] = Field(
        None, description="Primary industry or niche (e.g., 'Third-party logistics (3PL)')"
    )
    products_services: Optional[List[str]] = Field(
        None, description="Distinct products or services offered, each as a separate item"
    )
    usp: Optional[str] = Field(
        None, description="The single core unique selling proposition"
    )
    differentiators: Optional[List[str]] = Field(
        None, description="Specific competitive advantages that set the business apart"
    )
    pricing_model: Optional[str] = Field(
        None, description="How the company charges customers (e.g., subscription, per-unit, contracts) — NOT the price itself"
    )
    business_size: Optional[str] = Field(
        None, description="Scale descriptor (e.g., 'Mid-sized', 'Enterprise', 'Startup')"
    )
    locations: Optional[List[str]] = Field(
        None, description="Cities or regions where the business operates"
    )
    avg_ticket_price: Optional[str] = Field(
        None, description="Average revenue per transaction or deal, if explicitly stated"
    )
    cac: Optional[str] = Field(
        None, description="Average customer acquisition cost, if explicitly stated"
    )


# ----------------------------
# OPERATIONS & TECHNOLOGY
# ----------------------------

class OperationalDetails(BaseModel):
    operational_model: Optional[str] = Field(
        None, description="How the business operates (e.g., 'hub-and-spoke model')"
    )
    operational_workflow: Optional[List[str]] = Field(
        None, description="Key stages in the operational workflow (e.g., 'order intake', 'shipment allocation')"
    )
    technology_stack: Optional[List[str]] = Field(
        None, description="Tools and systems used (e.g., 'logistics management systems', 'route optimization tools')"
    )
    internal_challenges: Optional[List[str]] = Field(
        None, description="The company's OWN operational pain points — NOT customer pain points"
    )


# ----------------------------
# ICP
# ----------------------------

class B2BICP(BaseModel):
    industry: Optional[List[str]] = Field(
        None, description="Target industries (e.g., 'E-commerce', 'Manufacturing')"
    )
    company_size: Optional[str] = Field(
        None, description="Size descriptor (e.g., 'SMBs')"
    )
    revenue_range: Optional[str] = Field(
        None, description="Annual revenue range of ideal customers (e.g., '2-80 Cr')"
    )
    geography: Optional[List[str]] = Field(
        None, description="Target geographies or city tiers"
    )
    monthly_volume: Optional[str] = Field(
        None, description="Operational volume indicator (e.g., '1,000-40,000 monthly shipments')"
    )
    growth_stage: Optional[str] = Field(
        None, description="Ideal customer's business stage (e.g., 'active growth stage')"
    )


class B2CDemographics(BaseModel):
    age_group: Optional[str] = Field(
        None, description="Target age range (e.g., '25-45')"
    )
    income_level: Optional[str] = Field(
        None, description="Income bracket of target consumers"
    )
    location: Optional[str] = Field(
        None, description="Geographic location of target consumers"
    )


class B2CICP(BaseModel):
    demographics: Optional[B2CDemographics] = Field(
        None, description="Demographic profile of target consumers"
    )
    behavioral_traits: Optional[List[str]] = Field(
        None, description="Behavioral characteristics of target consumers"
    )


# ----------------------------
# BUYER PERSONA
# ----------------------------

class BuyerPersona(BaseModel):
    role: Optional[str] = Field(
        None, description="Job title or role (e.g., 'D2C Founder', 'Operations Manager')"
    )
    focus_areas: Optional[List[str]] = Field(
        None, description="What this persona cares about professionally (e.g., 'growth', 'efficiency')"
    )
    pain_points: Optional[List[str]] = Field(
        None, description="Specific problems this persona faces *not the company itself*"
    )
    goals: Optional[List[str]] = Field(
        None, description="What this persona is trying to achieve"
    )
    communication_preference: Optional[str] = Field(
        None, description="Preferred communication style (e.g., 'simple and direct', 'structured and data-driven', 'formal')"
    )


# ----------------------------
# TARGET CUSTOMER PROFILE
# ----------------------------

class TargetCustomerProfile(BaseModel):
    customer_type: Optional[CustomerType] = Field(
        None, description="Whether the business targets B2B, B2C, or Both"
    )
    b2b_icp: Optional[B2BICP] = Field(
        None, description="Ideal Customer Profile for B2B targets"
    )
    b2c_icp: Optional[B2CICP] = Field(
        None, description="Ideal Customer Profile for B2C targets"
    )
    buyer_personas: Optional[List[BuyerPersona]] = Field(
        None, description="Each distinct decision-maker persona with their individual preferences"
    )
    customer_segments: Optional[List[str]] = Field(
        None, description="Distinct market segments targeted (e.g., 'E-commerce/D2C brands', 'Manufacturers')"
    )


# ----------------------------
# CUSTOMER PREFERENCES
# ----------------------------

class CustomerPreferences(BaseModel):
    preferred_email_length: Optional[str] = Field(
        None, description="Preferred word count range for outreach emails (e.g., '80-150 words')"
    )
    preferred_structure: Optional[str] = Field(
        None, description="Preferred email format (e.g., 'clear structure with relevant personalization')"
    )
    high_intent_behavior: Optional[str] = Field(
        None, description="How high-intent leads typically behave (e.g., 'respond quickly')"
    )
    low_intent_behavior: Optional[str] = Field(
        None, description="How low-intent leads typically behave (e.g., 'delay or ignore messages')"
    )


# ----------------------------
# PRODUCT & SERVICE
# ----------------------------

class ProductServiceDetails(BaseModel):
    features: Optional[List[str]] = Field(
        None, description="What the product/service does — functional capabilities"
    )
    benefits: Optional[List[str]] = Field(
        None, description="Real-world outcomes and value delivered to customers"
    )
    pricing_tiers: Optional[str] = Field(
        None, description="Structured pricing details if available"
    )
    delivery_model: Optional[DeliveryModel] = Field(
        None, description="How the product/service is delivered: SaaS, Service, Hybrid, or Other"
    )


# ----------------------------
# SALES FUNNEL
# ----------------------------

class SalesFunnel(BaseModel):
    stages: Optional[List[str]] = Field(
        None, description="Ordered list of funnel stages (e.g., ['Awareness', 'Interest', 'Consideration', 'Decision', 'Conversion'])"
    )
    typical_cycle_duration: Optional[str] = Field(
        None, description="How long the sales cycle typically takes (e.g., '2-6 weeks')"
    )
    common_dropoff_reasons: Optional[List[str]] = Field(
        None, description="Reasons leads drop out of the funnel"
    )


# ----------------------------
# OUTREACH STRATEGY
# ----------------------------

class OutreachStrategy(BaseModel):
    email_structure: Optional[List[str]] = Field(
        None, description="Recommended email sequence components (e.g., ['Hook', 'Problem', 'Value', 'CTA'])"
    )
    followup_count: Optional[str] = Field(
        None, description="Number of follow-up emails recommended (e.g., '2-3')"
    )
    followup_cadence: Optional[str] = Field(
        None, description="Timing between follow-ups (e.g., 'spaced over 1-2 weeks')"
    )
    messaging_themes: Optional[List[str]] = Field(
        None, description="Core themes for messaging (e.g., 'cost savings', 'efficiency', 'scalability')"
    )


# ----------------------------
# LEAD SCORING
# ----------------------------

class LeadScoring(BaseModel):
    scoring_factors: Optional[List[str]] = Field(
        None, description="Criteria used to score leads (e.g., 'ICP fit', 'engagement', 'intent')"
    )
    lead_categories: Optional[List[str]] = Field(
        None, description="Classification tiers from lowest to highest (e.g., ['Cold', 'Warm', 'Qualified', 'High-Intent'])"
    )
    behavioral_signals: Optional[List[str]] = Field(
        None, description="External signals indicating purchase intent (e.g., 'hiring activity', 'expansion')"
    )
    automation_rules: Optional[str] = Field(
        None, description="How different lead tiers are handled (e.g., 'High-intent leads receive priority handling')"
    )


# ----------------------------
# COMPETITIVE LANDSCAPE
# ----------------------------

class CompetitiveLandscape(BaseModel):
    competitor_types: Optional[List[str]] = Field(
        None, description="Categories of competitors (e.g., 'Large aggregators', 'Regional players')"
    )
    differentiation: Optional[List[str]] = Field(
        None, description="What sets the business apart from competitors"
    )
    positioning_statement: Optional[str] = Field(
        None, description="How the company positions itself in the market"
    )


# ----------------------------
# MAIN MODEL
# ----------------------------

class BusinessContext(BaseModel):
    business_identity: Optional[BusinessIdentity] = Field(
        None, description="Core company identity: name, industry, offerings, USP, size, locations"
    )
    operational_details: Optional[OperationalDetails] = Field(
        None, description="How the business operates: model, workflow, tech stack, internal challenges"
    )
    target_customer_profile: Optional[TargetCustomerProfile] = Field(
        None, description="Who the business sells to: ICP, segments, personas"
    )
    customer_preferences: Optional[CustomerPreferences] = Field(
        None, description="How target customers prefer to be communicated with"
    )
    product_service_details: Optional[ProductServiceDetails] = Field(
        None, description="Features, benefits, pricing, and delivery model"
    )
    sales_funnel: Optional[SalesFunnel] = Field(
        None, description="Sales process: stages, cycle duration, drop-off points"
    )
    outreach_strategy: Optional[OutreachStrategy] = Field(
        None, description="Email outreach approach: structure, follow-ups, messaging"
    )
    lead_scoring: Optional[LeadScoring] = Field(
        None, description="How leads are scored, categorized, and prioritized"
    )
    competitive_landscape: Optional[CompetitiveLandscape] = Field(
        None, description="Competitors, differentiation, and market positioning"
    )
