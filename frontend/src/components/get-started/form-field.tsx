"use client"

import * as React from "react"
import { X } from "lucide-react"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Label } from "@/components/ui/label"
import { Badge } from "@/components/ui/badge"
import { cn } from "@/lib/utils"

type FieldProps = {
  label: string
  id: string
  value: string | null
  onChange: (value: string) => void
  placeholder?: string
  multiline?: boolean
  extracted?: boolean
}

function FormField({
  label,
  id,
  value,
  onChange,
  placeholder,
  multiline = false,
  extracted,
}: FieldProps) {
  const isEmpty = value === null || value === ""
  const Comp = multiline ? Textarea : Input

  return (
    <div className="space-y-1.5">
      <Label htmlFor={id} className="flex items-center gap-2">
        {label}
        {extracted === false && isEmpty && (
          <span className="rounded-sm bg-amber-500/10 px-1.5 py-0.5 text-[10px] font-medium text-amber-600 dark:text-amber-400">
            Needs input
          </span>
        )}
      </Label>
      <Comp
        id={id}
        value={value ?? ""}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        className={cn(multiline && "min-h-20")}
      />
    </div>
  )
}

type TagFieldProps = {
  label: string
  id: string
  value: string[] | null
  onChange: (value: string[]) => void
  placeholder?: string
  extracted?: boolean
}

function TagField({
  label,
  id,
  value,
  onChange,
  placeholder,
  extracted,
}: TagFieldProps) {
  const [input, setInput] = React.useState("")
  const inputRef = React.useRef<HTMLInputElement>(null)
  const items = value ?? []
  const isEmpty = items.length === 0

  function addItem(raw: string) {
    const trimmed = raw.trim()
    if (trimmed && !items.includes(trimmed)) {
      onChange([...items, trimmed])
    }
    setInput("")
  }

  function removeItem(idx: number) {
    onChange(items.filter((_, i) => i !== idx))
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLInputElement>) {
    if (e.key === "Enter" || e.key === ",") {
      e.preventDefault()
      addItem(input)
    }
    if (e.key === "Backspace" && input === "" && items.length > 0) {
      removeItem(items.length - 1)
    }
  }

  function handlePaste(e: React.ClipboardEvent<HTMLInputElement>) {
    const text = e.clipboardData.getData("text")
    if (text.includes(",") || text.includes("\n")) {
      e.preventDefault()
      const newItems = text
        .split(/[,\n]/)
        .map((s) => s.trim())
        .filter(Boolean)
        .filter((s) => !items.includes(s))
      if (newItems.length > 0) {
        onChange([...items, ...newItems])
      }
    }
  }

  return (
    <div className="space-y-1.5">
      <Label htmlFor={id} className="flex items-center gap-2">
        {label}
        {extracted === false && isEmpty && (
          <span className="rounded-sm bg-amber-500/10 px-1.5 py-0.5 text-[10px] font-medium text-amber-600 dark:text-amber-400">
            Needs input
          </span>
        )}
      </Label>
      <div
        className={cn(
          "flex flex-wrap items-center gap-1.5 rounded-lg border border-input bg-transparent px-2.5 py-1.5 transition-colors",
          "focus-within:border-ring focus-within:ring-3 focus-within:ring-ring/50",
          "dark:bg-input/30"
        )}
        onClick={() => inputRef.current?.focus()}
      >
        {items.map((item, i) => (
          <Badge
            key={`${item}-${i}`}
            variant="secondary"
            className="gap-1 pr-1"
          >
            {item}
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation()
                removeItem(i)
              }}
              className="ml-0.5 rounded-full p-0.5 transition-colors hover:bg-foreground/10"
              aria-label={`Remove ${item}`}
            >
              <X className="size-2.5" />
            </button>
          </Badge>
        ))}
        <input
          ref={inputRef}
          id={id}
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          onBlur={() => addItem(input)}
          onPaste={handlePaste}
          placeholder={isEmpty ? (placeholder ?? "Type and press Enter") : "Add more..."}
          className="min-w-20 flex-1 bg-transparent py-0.5 text-sm outline-none placeholder:text-muted-foreground"
        />
      </div>
      <p className="text-xs text-muted-foreground">
        Press Enter or comma to add
      </p>
    </div>
  )
}

export { FormField, TagField }
