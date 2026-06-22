"use client"

import * as React from "react"
import { useGetStarted } from "../get-started-context"
import { Separator } from "@/components/ui/separator"
import type { BusinessContext } from "@/types/business-context"

const SECTION_LABELS: Record<keyof BusinessContext, string> = {
  business_identity: "Business Identity",
  operational_details: "Operations & Technology",
  target_customer_profile: "Target Customer Profile",
  customer_preferences: "Customer Preferences",
  product_service_details: "Product & Service",
  sales_funnel: "Sales Funnel",
  outreach_strategy: "Outreach Strategy",
  lead_scoring: "Lead Scoring",
  competitive_landscape: "Competitive Landscape",
}

function renderValue(val: unknown): React.ReactNode {
  if (val === null || val === undefined || val === "") return "—"
  if (Array.isArray(val)) {
    if (val.length === 0) return "—"
    if (typeof val[0] === "object") {
      return (
        <div className="space-y-2">
          {val.map((item, i) => (
            <div
              key={i}
              className="rounded-md border border-input/50 bg-muted/20 p-2"
            >
              {renderObject(item)}
            </div>
          ))}
        </div>
      )
    }
    return val.join(", ")
  }
  if (typeof val === "object") return renderObject(val as Record<string, unknown>)
  return String(val)
}

function renderObject(obj: Record<string, unknown>): React.ReactNode {
  return (
    <div className="space-y-1">
      {Object.entries(obj).map(([key, val]) => (
        <div key={key} className="flex gap-2 text-sm">
          <span className="shrink-0 text-muted-foreground">
            {formatKey(key)}:
          </span>
          <span>{renderValue(val)}</span>
        </div>
      ))}
    </div>
  )
}

function formatKey(key: string) {
  return key
    .replace(/_/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase())
}

function StepReview() {
  const { data } = useGetStarted()

  return (
    <div className="space-y-5">
      {(Object.keys(SECTION_LABELS) as (keyof BusinessContext)[]).map(
        (section) => {
          const sectionData = data[section]
          if (!sectionData) return null
          return (
            <div key={section}>
              <p className="mb-2 text-xs font-medium tracking-wide text-muted-foreground uppercase">
                {SECTION_LABELS[section]}
              </p>
              <div className="space-y-1.5">
                {Object.entries(sectionData).map(([key, val]) => (
                  <div
                    key={key}
                    className="flex flex-col gap-0.5 sm:flex-row sm:gap-3"
                  >
                    <span className="w-40 shrink-0 text-xs text-muted-foreground">
                      {formatKey(key)}
                    </span>
                    <span className="min-w-0 flex-1 text-sm">
                      {renderValue(val)}
                    </span>
                  </div>
                ))}
              </div>
              <Separator className="mt-4" />
            </div>
          )
        }
      )}
    </div>
  )
}

export { StepReview }
