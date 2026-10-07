import boto3
from botocore.exceptions import ClientError
from fastapi import UploadFile

from app.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, S3_BUCKET_NAME


def get_s3_client():
    """Create and return an S3 client using boto3."""
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION,
    )


async def upload_file_to_s3(file: UploadFile, folder: str = "uploads") -> str:
    """
    Upload a file to S3 bucket.

    Args:
        file: The uploaded file from FastAPI
        folder: The folder/prefix in S3 bucket

    Returns:
        The URL of the uploaded file
    """
    s3_client = get_s3_client()

    # Generate the S3 key (path)
    s3_key = f"{folder}/{file.filename}"

    try:
        # Read file content
        file_content = await file.read()

        # Upload to S3
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=s3_key,
            Body=file_content,
            ContentType=file.content_type,
        )

        # Generate the file URL
        file_url = f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{s3_key}"

        return file_url

    except ClientError as e:
        raise Exception(f"Failed to upload file to S3: {str(e)}")


async def delete_file_from_s3(file_url: str) -> bool:
    """
    Delete a file from S3 bucket.

    Args:
        file_url: The URL of the file to delete

    Returns:
        True if successful
    """
    s3_client = get_s3_client()

    # Extract key from URL
    key = file_url.split(f"{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/")[-1]

    try:
        s3_client.delete_object(Bucket=S3_BUCKET_NAME, Key=key)
        return True
    except ClientError as e:
        raise Exception(f"Failed to delete file from S3: {str(e)}")
