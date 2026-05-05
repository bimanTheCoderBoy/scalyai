"use client"

import { useGetStarted } from "../get-started-context"
import { FormField, TagField } from "../form-field"
import { AdvancedSection } from "../advanced-section"

function StepBusinessIdentity() {
  const { data, updateSection } = useGetStarted()

  console.log("DATA", JSON.stringify(data, null, 2))

  const s = data.business_identity

  function update(patch: Partial<NonNullable<typeof s>>) {
    updateSection("business_identity", patch)
  }

  return (
    <div className="space-y-4">
      <FormField
        label="Business name"
        id="business_name"
        value={s?.business_name ?? null}
        onChange={(v) => update({ business_name: v })}
        placeholder="Acme Corp"
      />
      <FormField
        label="Industry"
        id="industry"
        value={s?.industry ?? null}
        onChange={(v) => update({ industry: v })}
        placeholder="e.g. Third-party logistics (3PL)"
      />
      <TagField
        label="Products / Services"
        id="products_services"
        value={s?.products_services ?? null}
        onChange={(v) => update({ products_services: v })}
        placeholder="Warehousing&#10;Last-mile delivery&#10;Freight forwarding"
      />
      <FormField
        label="Unique selling proposition"
        id="usp"
        value={s?.usp ?? null}
        onChange={(v) => update({ usp: v })}
        placeholder="What makes you different in one sentence"
        multiline
      />
      <TagField
        label="Differentiators"
        id="differentiators"
        value={s?.differentiators ?? null}
        onChange={(v) => update({ differentiators: v })}
        placeholder="AI-powered routing&#10;Real-time tracking&#10;99.5% SLA compliance"
      />
      <FormField
        label="Pricing model"
        id="pricing_model"
        value={s?.pricing_model ?? null}
        onChange={(v) => update({ pricing_model: v })}
        placeholder="e.g. subscription, per-unit, contracts"
      />

      <AdvancedSection>
        <FormField
          label="Business size"
          id="business_size"
          value={s?.business_size ?? null}
          onChange={(v) => update({ business_size: v })}
          placeholder="e.g. Startup, Mid-sized, Enterprise"
        />
        <TagField
          label="Locations"
          id="locations"
          value={s?.locations ?? null}
          onChange={(v) => update({ locations: v })}
          placeholder="Delhi&#10;Mumbai&#10;Bangalore"
        />
        <FormField
          label="Average ticket price"
          id="avg_ticket_price"
          value={s?.avg_ticket_price ?? null}
          onChange={(v) => update({ avg_ticket_price: v })}
          placeholder="e.g. ₹5,000 per shipment"
        />
        <FormField
          label="Customer acquisition cost"
          id="cac"
          value={s?.cac ?? null}
          onChange={(v) => update({ cac: v })}
          placeholder="e.g. ₹2,000"
        />
      </AdvancedSection>
    </div>
  )
}

export { StepBusinessIdentity }
