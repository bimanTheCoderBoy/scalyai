import { NextRequest, NextResponse } from "next/server"
import type { BusinessContext } from "@/types/business-context"
import axios from "axios"

const LANGGRAPH_URL = process.env.LANGGRAPH_SERVER_URL

export async function POST(req: NextRequest) {
  const body = await req.json().catch(() => null)

  if (!LANGGRAPH_URL) {
    return NextResponse.json(
      { error: "Backend unavailable" },
      { status: 502 }
    )
  }

  console.log("REQUEST BODY", body)

  const initialState = {
    "doc_link": body?.data?.file_url,
    "business_context": {},
    "missing_fields": []
  }

  try {

    const res = await axios.post("http://localhost:2024/runs/wait", {
      "assistant_id": "extractor",
      "input": initialState
    });

    console.log("RESPONSE", res?.data)
    
    return NextResponse.json(res?.data, { status: 200 })
  } catch(error) {
    console.log("EXTRACTION ERROR", error)

    return NextResponse.json({ error: "Failed to extract information" }, { status: 500 })
  }

}
