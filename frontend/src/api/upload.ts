import { AxiosError } from "axios";
import { apiClient } from "@/api/client";
import type { FileUploadResponse } from "@/schemas";

export async function uploadFile(file: File){

    if(!file){
        throw new Error("File is required");
    }
    
    const formData = new FormData();
    formData.append("file", file);

    try {
        const res = await apiClient.post<FileUploadResponse>("/upload", formData);

        if(res.status !== 200){
            throw new Error("Failed to upload file");
        }

        return res.data;
    } catch (error) {
        if(error instanceof AxiosError){
            throw new Error(error.response?.data.errors?.[0] || "Failed to upload file");
        }
        throw new Error("Failed to upload file");
    }
}