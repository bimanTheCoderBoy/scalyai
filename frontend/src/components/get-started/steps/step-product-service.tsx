"use client"

import { useGetStarted } from "../get-started-context"
import { FormField, TagField } from "../form-field"
import { AdvancedSection } from "../advanced-section"
import { Label } from "@/components/ui/label"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import type { DeliveryModel } from "@/types/business-context"

function StepProductService() {
  const { data, updateSection } = useGetStarted()
  const s = data.product_service_details

  function update(patch: Partial<NonNullable<typeof s>>) {
    updateSection("product_service_details", patch)
  }

  return (
    <div className="space-y-4">
      <TagField
        label="Features"
        id="features"
        value={s?.features ?? null}
        onChange={(v) => update({ features: v })}
        placeholder="Real-time tracking&#10;Automated dispatching&#10;Multi-carrier support"
      />
      <TagField
        label="Benefits"
        id="benefits"
        value={s?.benefits ?? null}
        onChange={(v) => update({ benefits: v })}
        placeholder="30% cost reduction&#10;2x faster delivery&#10;99.5% SLA"
      />
      <div className="space-y-1.5">
        <Label>Delivery model</Label>
        <Select
          value={s?.delivery_model ?? ""}
          onValueChange={(v) =>
            update({ delivery_model: v as DeliveryModel })
          }
        >
          <SelectTrigger className="w-full">
            <SelectValue placeholder="Select model" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="SaaS">SaaS</SelectItem>
            <SelectItem value="Service">Service</SelectItem>
            <SelectItem value="Hybrid">Hybrid</SelectItem>
            <SelectItem value="Other">Other</SelectItem>
          </SelectContent>
        </Select>
      </div>

      <AdvancedSection>
        <FormField
          label="Pricing tiers"
          id="pricing_tiers"
          value={s?.pricing_tiers ?? null}
          onChange={(v) => update({ pricing_tiers: v })}
          placeholder="Describe pricing structure if available"
          multiline
        />
      </AdvancedSection>
    </div>
  )
}

export { StepProductService }
