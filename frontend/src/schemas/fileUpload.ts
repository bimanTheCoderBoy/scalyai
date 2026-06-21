export interface FileUploadRequest {
  file: File
}

export interface FileUploadResponse {
  status: number
  data: {
    file_url: string
  },
  message?: string,
  errors?: string[]
}