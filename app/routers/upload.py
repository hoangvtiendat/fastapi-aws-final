from fastapi import APIRouter, UploadFile, File, HTTPException

from app.s3_service import upload_file_to_s3
from app.schemas import FileUploadResponse

router = APIRouter(
    prefix="/upload",
    tags=["File Upload"],
)


@router.post("/", response_model=FileUploadResponse)
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a file to Amazon S3.

    Accepts any file type and uploads it to the configured S3 bucket.
    Returns the file URL after successful upload.
    """
    # Validate file
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    # Max file size: 10MB
    MAX_SIZE = 10 * 1024 * 1024
    content = await file.read()
    if len(content) > MAX_SIZE:
        raise HTTPException(status_code=400, detail="File too large. Max size is 10MB")

    # Reset file position after reading
    await file.seek(0)

    try:
        file_url = await upload_file_to_s3(file, folder="uploads")
        return FileUploadResponse(
            filename=file.filename,
            url=file_url,
            message="File uploaded successfully",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
