from fastapi import UploadFile
from api.schema.response import ResponseSchema, ResponseStatus
from service.upload import save_upload
import os
import asyncio

async def upload_file(file: UploadFile) -> ResponseSchema:
    storage_dir = os.getenv("FILE_STORAGE_PATH", "static/tmp")
    file_location = os.path.join(storage_dir, file.filename)

    await asyncio.to_thread(save_upload, file.file, file_location)

    data = {"file_url": file_location}
        
    return ResponseSchema(status=ResponseStatus.OK, data=data, message="File uploaded successfully.")