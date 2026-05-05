"use client"

import { useGetStarted } from "../get-started-context"
import { FormField, TagField } from "../form-field"
import { AdvancedSection } from "../advanced-section"

function StepLeadScoring() {
  const { data, updateSection } = useGetStarted()
  const s = data.lead_scoring

  function update(patch: Partial<NonNullable<typeof s>>) {
    updateSection("lead_scoring", patch)
  }

  return (
    <div className="space-y-4">
      <TagField
        label="Scoring factors"
        id="scoring_factors"
        value={s?.scoring_factors ?? null}
        onChange={(v) => update({ scoring_factors: v })}
        placeholder="ICP fit&#10;Engagement&#10;Intent signals"
      />
      <TagField
        label="Lead categories"
        id="lead_categories"
        value={s?.lead_categories ?? null}
        onChange={(v) => update({ lead_categories: v })}
        placeholder="Cold&#10;Warm&#10;Qualified&#10;High-Intent"
      />

      <AdvancedSection>
        <TagField
          label="Behavioral signals"
          id="behavioral_signals"
          value={s?.behavioral_signals ?? null}
          onChange={(v) => update({ behavioral_signals: v })}
          placeholder="Hiring activity&#10;Expansion plans&#10;Tech adoption"
        />
        <FormField
          label="Automation rules"
          id="automation_rules"
          value={s?.automation_rules ?? null}
          onChange={(v) => update({ automation_rules: v })}
          placeholder="e.g. High-intent leads receive priority handling"
          multiline
        />
      </AdvancedSection>
    </div>
  )
}

export { StepLeadScoring }
