"use client"

import { useGetStarted } from "../get-started-context"
import { FormField, TagField } from "../form-field"
import { AdvancedSection } from "../advanced-section"

function StepOperationalDetails() {
  const { data, updateSection } = useGetStarted()
  const s = data.operational_details

  function update(patch: Partial<NonNullable<typeof s>>) {
    updateSection("operational_details", patch)
  }

  return (
    <div className="space-y-4">
      <FormField
        label="Operational model"
        id="operational_model"
        value={s?.operational_model ?? null}
        onChange={(v) => update({ operational_model: v })}
        placeholder="e.g. Hub-and-spoke model"
      />
      <TagField
        label="Operational workflow"
        id="operational_workflow"
        value={s?.operational_workflow ?? null}
        onChange={(v) => update({ operational_workflow: v })}
        placeholder="Order intake&#10;Shipment allocation&#10;Last-mile delivery"
      />
      <TagField
        label="Technology stack"
        id="technology_stack"
        value={s?.technology_stack ?? null}
        onChange={(v) => update({ technology_stack: v })}
        placeholder="Logistics management system&#10;Route optimization tool&#10;CRM"
      />

      <AdvancedSection>
        <TagField
          label="Internal challenges"
          id="internal_challenges"
          value={s?.internal_challenges ?? null}
          onChange={(v) => update({ internal_challenges: v })}
          placeholder="Driver attrition&#10;Manual dispatching&#10;Fragmented data"
        />
      </AdvancedSection>
    </div>
  )
}

export { StepOperationalDetails }
