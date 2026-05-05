"use client"

import * as React from "react"
import { Plus, Trash2 } from "lucide-react"
import { useGetStarted } from "../get-started-context"
import { FormField, TagField } from "../form-field"
import { AdvancedSection } from "../advanced-section"
import { Label } from "@/components/ui/label"
import { Button } from "@/components/ui/button"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Separator } from "@/components/ui/separator"
import type { BuyerPersona, CustomerType } from "@/types/business-context"

function StepTargetCustomer() {
  const { data, updateSection } = useGetStarted()
  const s = data.target_customer_profile
  const icp = s?.b2b_icp

  function update(patch: Partial<NonNullable<typeof s>>) {
    updateSection("target_customer_profile", patch)
  }

  function updateIcp(patch: Partial<NonNullable<typeof icp>>) {
    update({ b2b_icp: { ...icp!, ...patch } })
  }

  function addPersona() {
    const blank: BuyerPersona = {
      role: null,
      focus_areas: null,
      pain_points: null,
      goals: null,
      communication_preference: null,
    }
    update({ buyer_personas: [...(s?.buyer_personas ?? []), blank] })
  }

  function updatePersona(idx: number, patch: Partial<BuyerPersona>) {
    const list = [...(s?.buyer_personas ?? [])]
    list[idx] = { ...list[idx], ...patch }
    update({ buyer_personas: list })
  }

  function removePersona(idx: number) {
    update({
      buyer_personas: (s?.buyer_personas ?? []).filter((_, i) => i !== idx),
    })
  }

  return (
    <div className="space-y-4">
      <div className="space-y-1.5">
        <Label>Customer type</Label>
        <Select
          value={s?.customer_type ?? ""}
          onValueChange={(v) => update({ customer_type: v as CustomerType })}
        >
          <SelectTrigger className="w-full">
            <SelectValue placeholder="Select type" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="B2B">B2B</SelectItem>
            <SelectItem value="B2C">B2C</SelectItem>
            <SelectItem value="Both">Both</SelectItem>
          </SelectContent>
        </Select>
      </div>

      <TagField
        label="Customer segments"
        id="customer_segments"
        value={s?.customer_segments ?? null}
        onChange={(v) => update({ customer_segments: v })}
        placeholder="E-commerce / D2C brands&#10;Manufacturers&#10;Retailers"
      />

      <Separator />
      <p className="text-xs font-medium tracking-wide text-muted-foreground uppercase">
        B2B Ideal Customer Profile
      </p>

      <TagField
        label="Target industries"
        id="b2b_industry"
        value={icp?.industry ?? null}
        onChange={(v) => updateIcp({ industry: v })}
        placeholder="E-commerce&#10;Manufacturing"
      />
      <FormField
        label="Company size"
        id="b2b_company_size"
        value={icp?.company_size ?? null}
        onChange={(v) => updateIcp({ company_size: v })}
        placeholder="e.g. SMBs"
      />
      <FormField
        label="Revenue range"
        id="b2b_revenue_range"
        value={icp?.revenue_range ?? null}
        onChange={(v) => updateIcp({ revenue_range: v })}
        placeholder="e.g. 2-80 Cr"
      />
      <TagField
        label="Geography"
        id="b2b_geography"
        value={icp?.geography ?? null}
        onChange={(v) => updateIcp({ geography: v })}
        placeholder="Tier 1 cities&#10;Pan-India"
      />
      <FormField
        label="Monthly volume"
        id="b2b_monthly_volume"
        value={icp?.monthly_volume ?? null}
        onChange={(v) => updateIcp({ monthly_volume: v })}
        placeholder="e.g. 1,000-40,000 shipments"
      />
      <FormField
        label="Growth stage"
        id="b2b_growth_stage"
        value={icp?.growth_stage ?? null}
        onChange={(v) => updateIcp({ growth_stage: v })}
        placeholder="e.g. Active growth stage"
      />

      <Separator />
      <div className="flex items-center justify-between">
        <p className="text-xs font-medium tracking-wide text-muted-foreground uppercase">
          Buyer personas
        </p>
        <Button variant="ghost" size="sm" onClick={addPersona}>
          <Plus data-icon="inline-start" />
          Add persona
        </Button>
      </div>

      {(s?.buyer_personas ?? []).map((p, i) => (
        <div
          key={i}
          className="space-y-3 rounded-lg border border-input/60 bg-muted/20 p-3"
        >
          <div className="flex items-center justify-between">
            <span className="text-xs font-medium text-muted-foreground">
              Persona {i + 1}
            </span>
            <Button
              variant="ghost"
              size="icon-xs"
              onClick={() => removePersona(i)}
              aria-label="Remove persona"
            >
              <Trash2 />
            </Button>
          </div>
          <FormField
            label="Role"
            id={`persona_role_${i}`}
            value={p.role}
            onChange={(v) => updatePersona(i, { role: v })}
            placeholder="e.g. D2C Founder"
          />
          <TagField
            label="Focus areas"
            id={`persona_focus_${i}`}
            value={p.focus_areas}
            onChange={(v) => updatePersona(i, { focus_areas: v })}
          />
          <TagField
            label="Pain points"
            id={`persona_pain_${i}`}
            value={p.pain_points}
            onChange={(v) => updatePersona(i, { pain_points: v })}
          />
          <TagField
            label="Goals"
            id={`persona_goals_${i}`}
            value={p.goals}
            onChange={(v) => updatePersona(i, { goals: v })}
          />
          <FormField
            label="Communication preference"
            id={`persona_comm_${i}`}
            value={p.communication_preference}
            onChange={(v) =>
              updatePersona(i, { communication_preference: v })
            }
            placeholder="e.g. Simple and direct"
          />
        </div>
      ))}

      <AdvancedSection>
        <p className="text-xs font-medium tracking-wide text-muted-foreground uppercase">
          B2C Ideal Customer Profile
        </p>
        <FormField
          label="Age group"
          id="b2c_age"
          value={s?.b2c_icp?.demographics?.age_group ?? null}
          onChange={(v) =>
            update({
              b2c_icp: {
                ...s?.b2c_icp,
                demographics: {
                  ...s?.b2c_icp?.demographics,
                  age_group: v,
                  income_level: s?.b2c_icp?.demographics?.income_level ?? null,
                  location: s?.b2c_icp?.demographics?.location ?? null,
                },
                behavioral_traits: s?.b2c_icp?.behavioral_traits ?? null,
              },
            })
          }
          placeholder="e.g. 25-45"
        />
        <FormField
          label="Income level"
          id="b2c_income"
          value={s?.b2c_icp?.demographics?.income_level ?? null}
          onChange={(v) =>
            update({
              b2c_icp: {
                ...s?.b2c_icp,
                demographics: {
                  ...s?.b2c_icp?.demographics,
                  income_level: v,
                  age_group: s?.b2c_icp?.demographics?.age_group ?? null,
                  location: s?.b2c_icp?.demographics?.location ?? null,
                },
                behavioral_traits: s?.b2c_icp?.behavioral_traits ?? null,
              },
            })
          }
          placeholder="e.g. Upper-middle"
        />
        <FormField
          label="Location"
          id="b2c_location"
          value={s?.b2c_icp?.demographics?.location ?? null}
          onChange={(v) =>
            update({
              b2c_icp: {
                ...s?.b2c_icp,
                demographics: {
                  ...s?.b2c_icp?.demographics,
                  location: v,
                  age_group: s?.b2c_icp?.demographics?.age_group ?? null,
                  income_level: s?.b2c_icp?.demographics?.income_level ?? null,
                },
                behavioral_traits: s?.b2c_icp?.behavioral_traits ?? null,
              },
            })
          }
          placeholder="e.g. Metro cities"
        />
        <TagField
          label="Behavioral traits"
          id="b2c_behavioral"
          value={s?.b2c_icp?.behavioral_traits ?? null}
          onChange={(v) =>
            update({
              b2c_icp: {
                ...s?.b2c_icp,
                demographics: s?.b2c_icp?.demographics ?? null,
                behavioral_traits: v,
              },
            })
          }
        />
      </AdvancedSection>
    </div>
  )
}

export { StepTargetCustomer }
