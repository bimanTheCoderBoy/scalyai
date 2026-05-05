"use client"

import * as React from "react"
import { ArrowRight, Loader2 } from "lucide-react"
import { toast } from "sonner"
import axios from "axios"

import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

import { StepUpload } from "./step-upload"
import { useGetStarted } from "./get-started-context"

function GetStartedForm() {
  const { setPhase, setData } = useGetStarted()
  const [file, setFile] = React.useState<File | null>(null)
  const [uploading, setUploading] = React.useState(false)

  async function handleUpload() {
    if (!file) {
      toast.warning("Please upload a file")
      return
    }

    setUploading(true)

    try {
      const formData = new FormData()
      formData.append("file", file)

      const uploadRes = await axios.post("/api/upload", formData)

      if (uploadRes.status !== 200) {
        toast.error("Failed to upload file")
        return
      }

      toast.success("File uploaded successfully")
      setPhase("extracting")

      const extractRes = await axios.post("/api/extract", uploadRes.data)

      console.log("EXTRACT RES", extractRes?.data)

      if (extractRes.status === 200) {
        setData(extractRes?.data?.business_context)
        toast.success("Information extracted successfully")
        setPhase("form")
      }
    } catch {
      toast.error("Failed to process file. Please try again.")
      setPhase("upload")
    } finally {
      setUploading(false)
    }
  }

  return (
    <Card className="overflow-hidden">
      <CardHeader>
        <CardTitle>Upload your file</CardTitle>
        <CardDescription>
          Drop your business document and we&apos;ll extract the details for
          you.
        </CardDescription>
      </CardHeader>

      <CardContent className="pt-1 pb-2">
        <StepUpload file={file} onFileChange={setFile} />
      </CardContent>

      <div className="flex items-center justify-end border-t px-4 py-3">
        <Button onClick={handleUpload} disabled={!file || uploading}>
          {uploading ? (
            <>
              <Loader2 data-icon="inline-start" className="animate-spin" />
              Uploading
            </>
          ) : (
            <>
              Continue
              <ArrowRight data-icon="inline-end" />
            </>
          )}
        </Button>
      </div>
    </Card>
  )
}

export { GetStartedForm }
