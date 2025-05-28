# Serverless Deployment Guide for MOMS

This guide explains how to deploy the MOMS application using a serverless architecture on AWS.

## Architecture Overview

- **API Layer**: AWS Lambda + API Gateway
- **Database**: RDS Aurora PostgreSQL with auto-pause
- **Static Files**: S3
- **Lambda Functions**: Hybrid approach (standard + containerized)

## Prerequisites

1. AWS CLI configured with appropriate permissions
2. Node.js 14+ and npm
3. Serverless Framework CLI: `npm install -g serverless`
4. Docker (for containerized functions)

## Deployment Steps

### 1. Set up environment variables

Create a `.env` file for each environment (dev, staging, prod):

```
# .env.dev
STAGE=dev
AWS_REGION=us-east-1
DB_NAME=moms_db
DB_USERNAME=admin
# Other environment-specific variables
```

### 2. Deploy the database

```bash
# Create SSM parameters for database credentials (one-time setup)
aws ssm put-parameter --name "/moms/dev/db/username" --value "admin" --type "SecureString"
aws ssm put-parameter --name "/moms/dev/db/password" --value "your-secure-password" --type "SecureString"

# Deploy RDS with CloudFormation
aws cloudformation deploy \
  --template-file cloudformation/rds-template.yml \
  --stack-name moms-dev-db \
  --parameter-overrides \
    Stage=dev \
    DBUsername=admin \
    DBPassword=your-secure-password \
    DBName=moms_db
```

### 3. Build and push the container image (for containerized functions)

```bash
# Log in to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $(aws sts get-caller-identity --query Account --output text).dkr.ecr.us-east-1.amazonaws.com

# Create ECR repository (if it doesn't exist)
aws ecr create-repository --repository-name moms-serverless-dev

# Build and push the image
docker build -t moms-serverless-dev .
docker tag moms-serverless-dev:latest $(aws sts get-caller-identity --query Account --output text).dkr.ecr.us-east-1.amazonaws.com/moms-serverless-dev:latest
docker push $(aws sts get-caller-identity --query Account --output text).dkr.ecr.us-east-1.amazonaws.com/moms-serverless-dev:latest
```

### 4. Deploy the serverless application

```bash
# Install dependencies
npm install

# Deploy with Serverless Framework
npx serverless deploy --stage dev

# Run migrations
npx serverless invoke -f migrations --stage dev

# Collect static files
npx serverless invoke -f collectstatic --stage dev
```

## Function Organization

- **Standard Lambda Functions**: Handle lightweight API endpoints (most CRUD operations)
- **Containerized Lambda Functions**: Handle resource-intensive modules (analytics, reporting)

## Monitoring and Logs

Access logs through CloudWatch:

```bash
# View logs for standard API function
npx serverless logs -f standardApi -t

# View logs for containerized API function
npx serverless logs -f containerizedApi -t
```

## Cost Optimization

- RDS auto-pauses after 5 minutes of inactivity (dev/staging)
- Lambda functions scale to zero when not in use
- S3 lifecycle policies can be configured for static assets

## Troubleshooting

1. **Cold Start Issues**: Implement provisioned concurrency for critical functions
2. **Database Connection Errors**: Check security group settings and network configuration
3. **Container Size Limits**: Optimize Docker image size by removing unnecessary dependencies