// app/api/upload/route.ts
import { NextRequest, NextResponse } from "next/server"

const LANGGRAPH_URL = process.env.LANGGRAPH_SERVER_URL

export async function POST(req: NextRequest) {
  const formData = await req.formData()
  const file = formData.get("file") as File | null

  if (!file) {
    return NextResponse.json({ error: "No file provided" }, { status: 400 })
  }

  // Forward to LangGraph server
  const lgFormData = new FormData()
  lgFormData.append("file", file)

  const response = await fetch(`${LANGGRAPH_URL}/upload`, {
    method: "POST",
    body: lgFormData,
  })

  if (!response.ok) {
    return NextResponse.json(
      { error: "Failed to process file" },
      { status: response.status }
    )
  }

  const data = await response.json()
  return NextResponse.json(data)
}