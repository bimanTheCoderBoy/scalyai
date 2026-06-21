import { Loader2 } from "lucide-react"
import {
  Card,
  CardContent,
} from "@/components/ui/card"

function PhaseExtracting() {
  return (
    <Card className="overflow-hidden">
      <CardContent className="flex flex-col items-center gap-4 py-16 text-center">
        <Loader2 className="size-8 animate-spin text-primary" />
        <div className="space-y-1">
          <h2 className="font-heading text-base font-medium">
            Extracting information&hellip;
          </h2>
          <p className="text-sm text-muted-foreground">
            We&apos;re analyzing your document. This may take a moment.
          </p>
        </div>
      </CardContent>
    </Card>
  )
}

export { PhaseExtracting }
