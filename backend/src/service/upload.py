import os
import shutil

def save_upload(sync_file, file_location: str) -> None:
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    
    try:
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(sync_file, buffer)

    except Exception as e:
        raise e