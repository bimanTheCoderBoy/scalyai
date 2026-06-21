import { apiClient } from "@/api/client";

export async function extract(doc_link: string){

    if(!doc_link){
        throw new Error("Doc link is required");
    }

    const initialState = {
        "doc_link": doc_link,
        "business_context": {},
        "missing_fields": []
    }

    try {
        const res = await apiClient.post("/runs/wait", {
            "assistant_id": "extractor",
            "input": initialState
        });

        if(res.status !== 200){
            throw new Error("Failed to extract information");
        }

        return res.data;
        
    } catch (error) {
        console.error("Error invoking agent:", error);
        throw error;
    }
}