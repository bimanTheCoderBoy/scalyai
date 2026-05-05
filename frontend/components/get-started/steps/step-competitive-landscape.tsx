"use client"

import { useGetStarted } from "../get-started-context"
import { FormField, TagField } from "../form-field"
import { AdvancedSection } from "../advanced-section"

function StepCompetitiveLandscape() {
  const { data, updateSection } = useGetStarted()
  const s = data.competitive_landscape

  function update(patch: Partial<NonNullable<typeof s>>) {
    updateSection("competitive_landscape", patch)
  }

  return (
    <div className="space-y-4">
      <TagField
        label="Competitor types"
        id="competitor_types"
        value={s?.competitor_types ?? null}
        onChange={(v) => update({ competitor_types: v })}
        placeholder="Large aggregators&#10;Regional players&#10;Tech-first startups"
      />
      <TagField
        label="Differentiation"
        id="differentiation"
        value={s?.differentiation ?? null}
        onChange={(v) => update({ differentiation: v })}
        placeholder="Better SLA&#10;Lower cost&#10;Dedicated account managers"
      />

      <AdvancedSection>
        <FormField
          label="Positioning statement"
          id="positioning_statement"
          value={s?.positioning_statement ?? null}
          onChange={(v) => update({ positioning_statement: v })}
          placeholder="How you position yourself in the market"
          multiline
        />
      </AdvancedSection>
    </div>
  )
}

export { StepCompetitiveLandscape }
