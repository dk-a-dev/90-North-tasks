# Calculator AWS Lambda

This project demonstrates how to set up a simple calculator application using AWS Lambda, with the ability to perform basic arithmetic operations like addition, subtraction, multiplication, and division.

## Pre-requisites
- **Frontend**: None (CLI-based interaction for now)
- **Backend**: Python (AWS Lambda)
- **Hosting**: AWS Lambda
- **IAM Role**: AWS IAM for Lambda execution permissions

## Features
- Performs basic arithmetic operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`)
- Handles exceptions like division by zero
- Returns a JSON response with the result of the operation

## Prerequisites/tech stack
- AWS CLI configured on your local machine
- IAM role (`s3lambda`) with permissions to execute Lambda functions
- Python 3.9 (for Lambda runtime)

## Setup Instructions

### Step 1: AWS CLI Configuration

Ensure that the AWS CLI is properly configured with your credentials and region:
```bash
aws configure
```
This command will prompt you for your AWS Access Key, Secret Key, and region.

### Step 2: Create Lambda Function
1. Create the `calculator.py` file: This file contains the Python code to perform the arithmetic operations.


2. Zip the Python file:
```bash
zip calculator.zip calculator.py
```

3. Create the Lambda function:
This step assumes you have an IAM role with necessary permissions to run Lambda functions.
```bash
aws lambda create-function \
  --function-name calculator \
  --runtime python3.9 \
  --handler calculator.lambda_handler \
  --role <my_role_arn> \
  --zip-file fileb://calculator.zip
```
In this step:
- `--function-name calculator`: Name of the Lambda function
- `--runtime python3.9`: Python runtime version
- `--handler calculator.lambda_handler`: Handler for the Lambda function
- `--role <my_role_arn>`: IAM role with Lambda execution permissions
- `--zip-file fileb://calculator.zip`: Path to the zipped Python file

### Step 3: Testing the Lambda Function

To invoke the Lambda function and test it, use the following command with sample input:
```bash
aws lambda invoke \
    --function-name calculator \
    --payload '{"num1": 10, "num2": 5, "ope": "+"}' \
    response.json
```
- This command sends a JSON payload to the Lambda function to perform an addition operation (10 + 5).
- The response will be saved in `response.json`.

To view the result:
```bash
cat response.json
```

### Step 4: Update Lambda Function Code

If you make any changes to the `calculator.py` file, you’ll need to update the Lambda function code by zipping the updated file and using the `update-function-code` command:
```bash
zip calculator.zip calculator.py
aws lambda update-function-code \
    --function-name calculator \
    --zip-file fileb://calculator.zip
```

### Step 5: Additional Commands
- Invoke Lambda for other operations (multiplication example):
```bash
aws lambda invoke \
  --function-name calculator \
  --payload '{"num1": 10, "num2": 5, "ope": "*"}' \
  response.json
```

## Output
- [Creation proof of the Lambda function](https://github.com/dk-a-dev/90-North-tasks/blob/main/aws-task/output-calculator/create.png)
- [Testing the Lambda function](https://github.com/dk-a-dev/90-North-tasks/blob/main/aws-task/output-calculator/test.png)
- [Sample output](https://github.com/dk-a-dev/90-North-tasks/blob/main/aws-task/output-calculator/output.png)
- [Updating the Lambda function](https://github.com/dk-a-dev/90-North-tasks/blob/main/aws-task/output-calculator/proof.png)

---
---
# PDF Uploads to S3 with lambda functions
This section demonstrates how to upload PDF files to an S3 bucket using a Lambda function.


## Prerequisites
1. AWS CLI configured on your local machine
2. IAM role with permissions to execute Lambda functions and access S3
3. Python 3.9 (for Lambda runtime)

## Setup Instructions
1. Clone the repo

2. Run the Script
To upload a PDF file to an S3 bucket, run the following command:
```bash
python pdf_uploads.py <file_path> <bucket_name>
```
Replace <file_path> with the path to your PDF file and <bucket_name> with the name of your S3 bucket.

3. Check the S3 Bucket

## Output
- [Proof of PDF upload to S3](https://github.com/dk-a-dev/90-North-tasks/blob/main/aws-task/output-pdfupload/proof.png)
- [Sample PDF file uploaded](https://github.com/dk-a-dev/90-North-tasks/blob/main/aws-task/output-pdfupload/uploaded.png)
- [cmd aws creation](https://github.com/dk-a-dev/90-North-tasks/blob/main/aws-task/output-pdfupload/cmd.png)
