#!/bin/bash

# Exit on error
set -e

# Load environment variables
source .env

# Variables
STACK_NAME="moms-stack"
TEMPLATE_FILE="deployment/aws/cloudformation/moms-stack.yml"
REGION="us-east-1"  # Change to your preferred region

# Create S3 bucket for CloudFormation template if it doesn't exist
BUCKET_NAME="moms-cloudformation-templates"
aws s3api head-bucket --bucket $BUCKET_NAME 2>/dev/null || aws s3 mb s3://$BUCKET_NAME

# Upload CloudFormation template to S3
aws s3 cp $TEMPLATE_FILE s3://$BUCKET_NAME/

# Deploy CloudFormation stack
aws cloudformation deploy \
  --template-url https://s3.amazonaws.com/$BUCKET_NAME/$(basename $TEMPLATE_FILE) \
  --stack-name $STACK_NAME \
  --parameter-overrides \
    EnvironmentName=${ENVIRONMENT:-dev} \
    DBName=${DB_NAME:-moms_db} \
    DBUsername=${DB_USER:-postgres} \
    DBPassword=${DB_PASSWORD} \
  --capabilities CAPABILITY_IAM \
  --region $REGION

# Get stack outputs
echo "Deployment completed. Stack outputs:"
aws cloudformation describe-stacks \
  --stack-name $STACK_NAME \
  --query "Stacks[0].Outputs" \
  --region $REGION