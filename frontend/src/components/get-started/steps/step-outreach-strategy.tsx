"use client"

import { useGetStarted } from "../get-started-context"
import { FormField, TagField } from "../form-field"
import { AdvancedSection } from "../advanced-section"

function StepOutreachStrategy() {
  const { data, updateSection } = useGetStarted()
  const s = data.outreach_strategy

  function update(patch: Partial<NonNullable<typeof s>>) {
    updateSection("outreach_strategy", patch)
  }

  return (
    <div className="space-y-4">
      <TagField
        label="Email structure"
        id="email_structure"
        value={s?.email_structure ?? null}
        onChange={(v) => update({ email_structure: v })}
        placeholder="Hook&#10;Problem&#10;Value&#10;CTA"
      />
      <TagField
        label="Messaging themes"
        id="messaging_themes"
        value={s?.messaging_themes ?? null}
        onChange={(v) => update({ messaging_themes: v })}
        placeholder="Cost savings&#10;Efficiency&#10;Scalability"
      />

      <AdvancedSection>
        <FormField
          label="Follow-up count"
          id="followup_count"
          value={s?.followup_count ?? null}
          onChange={(v) => update({ followup_count: v })}
          placeholder="e.g. 2-3"
        />
        <FormField
          label="Follow-up cadence"
          id="followup_cadence"
          value={s?.followup_cadence ?? null}
          onChange={(v) => update({ followup_cadence: v })}
          placeholder="e.g. Spaced over 1-2 weeks"
        />
      </AdvancedSection>
    </div>
  )
}

export { StepOutreachStrategy }
