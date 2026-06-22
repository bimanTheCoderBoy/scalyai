import type { BusinessContext } from "@/types/business-context";

export interface ExtractorResponse {
    doc_link: string,
    business_context?: Partial<BusinessContext>,
    missing_fields?: string[],
}