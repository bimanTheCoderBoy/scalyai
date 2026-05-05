"use client"

import * as React from "react"
import { FileText, UploadCloud, X } from "lucide-react"

import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

type StepUploadProps = {
  file: File | null
  onFileChange: (file: File | null) => void
  accept?: string
  maxSizeMb?: number
}

function formatBytes(bytes: number) {
  if (bytes < 1024) return `${bytes} B`
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
}

function StepUpload({
  file,
  onFileChange,
  accept,
  maxSizeMb = 25,
}: StepUploadProps) {
  const inputRef = React.useRef<HTMLInputElement>(null)
  const [dragOver, setDragOver] = React.useState(false)
  const [error, setError] = React.useState<string | null>(null)

  function validateAndSet(next: File | null) {
    setError(null)
    if (!next) {
      onFileChange(null)
      return
    }
    if (next.size > maxSizeMb * 1024 * 1024) {
      setError(`File is too large. Max ${maxSizeMb} MB.`)
      return
    }
    onFileChange(next)
  }

  function handleDrop(e: React.DragEvent<HTMLDivElement>) {
    e.preventDefault()
    setDragOver(false)
    const next = e.dataTransfer.files?.[0] ?? null
    validateAndSet(next)
  }

  function handleSelect(e: React.ChangeEvent<HTMLInputElement>) {
    const next = e.target.files?.[0] ?? null
    validateAndSet(next)
    e.target.value = ""
  }

  function clearFile(e: React.MouseEvent) {
    e.stopPropagation()
    validateAndSet(null)
  }

  return (
    <div className="space-y-3">
      <div
        role="button"
        tabIndex={0}
        onClick={() => inputRef.current?.click()}
        onKeyDown={(e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault()
            inputRef.current?.click()
          }
        }}
        onDragOver={(e) => {
          e.preventDefault()
          setDragOver(true)
        }}
        onDragLeave={() => setDragOver(false)}
        onDrop={handleDrop}
        className={cn(
          "group relative flex cursor-pointer flex-col items-center justify-center gap-2 rounded-xl border border-dashed border-input bg-muted/30 px-6 py-10 text-center transition-colors outline-none",
          "hover:border-ring/60 hover:bg-muted/50",
          "focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50",
          dragOver && "border-ring bg-muted/60",
          file && "border-solid border-input bg-background"
        )}
      >
        <input
          ref={inputRef}
          type="file"
          accept={accept}
          onChange={handleSelect}
          className="sr-only"
        />

        {file ? (
          <div className="flex w-full items-center gap-3 text-left">
            <div className="flex size-10 shrink-0 items-center justify-center rounded-lg bg-primary/10 text-primary">
              <FileText className="size-5" />
            </div>
            <div className="min-w-0 flex-1">
              <p className="truncate text-sm font-medium">{file.name}</p>
              <p className="text-xs text-muted-foreground">
                {formatBytes(file.size)}
              </p>
            </div>
            <Button
              variant="ghost"
              size="icon-sm"
              onClick={clearFile}
              aria-label="Remove file"
            >
              <X />
            </Button>
          </div>
        ) : (
          <>
            <div className="flex size-10 items-center justify-center rounded-full bg-background text-muted-foreground ring-1 ring-foreground/10 transition-colors group-hover:text-foreground">
              <UploadCloud className="size-5" />
            </div>
            <div className="space-y-0.5">
              <p className="text-sm font-medium">
                Drop a file here, or{" "}
                <span className="text-primary underline-offset-4 group-hover:underline">
                  browse
                </span>
              </p>
              <p className="text-xs text-muted-foreground">
                Up to {maxSizeMb} MB
              </p>
            </div>
          </>
        )}
      </div>

      {error && (
        <p className="text-xs text-destructive" role="alert">
          {error}
        </p>
      )}
    </div>
  )
}

export { StepUpload }
