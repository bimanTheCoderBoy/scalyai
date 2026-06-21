"use client"

import { useGetStarted } from "../get-started-context"
import { FormField } from "../form-field"
import { AdvancedSection } from "../advanced-section"

function StepCustomerPreferences() {
  const { data, updateSection } = useGetStarted()
  const s = data.customer_preferences

  function update(patch: Partial<NonNullable<typeof s>>) {
    updateSection("customer_preferences", patch)
  }

  return (
    <div className="space-y-4">
      <FormField
        label="Preferred email length"
        id="preferred_email_length"
        value={s?.preferred_email_length ?? null}
        onChange={(v) => update({ preferred_email_length: v })}
        placeholder="e.g. 80-150 words"
      />
      <FormField
        label="Preferred structure"
        id="preferred_structure"
        value={s?.preferred_structure ?? null}
        onChange={(v) => update({ preferred_structure: v })}
        placeholder="e.g. Clear structure with relevant personalization"
      />

      <AdvancedSection>
        <FormField
          label="High-intent behavior"
          id="high_intent_behavior"
          value={s?.high_intent_behavior ?? null}
          onChange={(v) => update({ high_intent_behavior: v })}
          placeholder="e.g. Respond quickly, ask for pricing"
        />
        <FormField
          label="Low-intent behavior"
          id="low_intent_behavior"
          value={s?.low_intent_behavior ?? null}
          onChange={(v) => update({ low_intent_behavior: v })}
          placeholder="e.g. Delay or ignore messages"
        />
      </AdvancedSection>
    </div>
  )
}

export { StepCustomerPreferences }
