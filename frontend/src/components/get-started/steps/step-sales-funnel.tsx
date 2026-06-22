"use client"

import { useGetStarted } from "../get-started-context"
import { FormField, TagField } from "../form-field"
import { AdvancedSection } from "../advanced-section"

function StepSalesFunnel() {
  const { data, updateSection } = useGetStarted()
  const s = data.sales_funnel

  function update(patch: Partial<NonNullable<typeof s>>) {
    updateSection("sales_funnel", patch)
  }

  return (
    <div className="space-y-4">
      <TagField
        label="Funnel stages"
        id="stages"
        value={s?.stages ?? null}
        onChange={(v) => update({ stages: v })}
        placeholder="Awareness&#10;Interest&#10;Consideration&#10;Decision&#10;Conversion"
      />
      <FormField
        label="Typical cycle duration"
        id="typical_cycle_duration"
        value={s?.typical_cycle_duration ?? null}
        onChange={(v) => update({ typical_cycle_duration: v })}
        placeholder="e.g. 2-6 weeks"
      />

      <AdvancedSection>
        <TagField
          label="Common drop-off reasons"
          id="common_dropoff_reasons"
          value={s?.common_dropoff_reasons ?? null}
          onChange={(v) => update({ common_dropoff_reasons: v })}
          placeholder="Budget constraints&#10;Competitor chosen&#10;Timing not right"
        />
      </AdvancedSection>
    </div>
  )
}

export { StepSalesFunnel }
