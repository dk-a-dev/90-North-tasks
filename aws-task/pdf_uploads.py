import base64
import boto3
import mimetypes
import os
import sys

s3_client = boto3.client('s3')

def verify_pdf(file_path: str) -> bool:
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type != 'application/pdf':
        return False

    with open(file_path, 'rb') as file:
        header = file.read(4)
        return header == b'%PDF'

def convert_to_base64(file_path: str) -> str:
    with open(file_path, 'rb') as file:
        encoded = base64.b64encode(file.read()).decode('utf-8')
    return encoded

def upload_to_s3(base64_content: str, bucket_name: str, object_name: str) -> None:
    s3_client.put_object(
        Bucket=bucket_name,
        Key=object_name,
        Body=base64_content,
        ContentType='text/plain'
    )

def main(file_path: str, bucket_name: str):
    object_name = os.path.basename(file_path).replace('.pdf', '_base64.txt')

    if not verify_pdf(file_path):
        print('Invalid file type. Only PDF files are allowed.')
        return

    base64_content = convert_to_base64(file_path)
    upload_to_s3(base64_content, bucket_name, object_name)
    print(f'File uploaded successfully as {object_name} in bucket {bucket_name}.')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_uploads.py <file_path> <bucket_name>")
    else:
        file_path = sys.argv[1]
        bucket_name = sys.argv[2]
        main(file_path, bucket_name)