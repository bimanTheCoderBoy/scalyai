"use client"

import * as React from "react"
import { ChevronDown } from "lucide-react"
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible"
import { cn } from "@/lib/utils"

function AdvancedSection({ children }: { children: React.ReactNode }) {
  const [open, setOpen] = React.useState(false)

  return (
    <Collapsible open={open} onOpenChange={setOpen} className="mt-4">
      <CollapsibleTrigger className="flex w-full items-center gap-2 rounded-lg px-1 py-1.5 text-xs font-medium text-muted-foreground transition-colors hover:text-foreground">
        <ChevronDown
          className={cn(
            "size-3.5 transition-transform",
            open && "rotate-180"
          )}
        />
        Advanced fields
      </CollapsibleTrigger>
      <CollapsibleContent className="mt-3 space-y-4">
        {children}
      </CollapsibleContent>
    </Collapsible>
  )
}

export { AdvancedSection }
