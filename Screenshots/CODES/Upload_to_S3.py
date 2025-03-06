import boto3
import os
from datetime import datetime

# AWS S3 Configuration
AWS_ACCESS_KEY = "YOUR_ACCESS_KEY"
AWS_SECRET_KEY = "YOUR_SECRET_KEY"
BUCKET_NAME = "YOUR-weather-data-bucket"

# File path (update this to the actual file path)
FILE_PATH = "C:\\Users\\USERNAME\\Downloads\\weather_data.json"

# Generate a unique file name
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
s3_filename = f"weather_{timestamp}.json"

# Upload file to S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

try:
    s3.upload_file(FILE_PATH, BUCKET_NAME, s3_filename)
    print(f"Uploaded {FILE_PATH} to S3 as {s3_filename}")
except Exception as e:
    print(f"Failed to upload: {e}")
