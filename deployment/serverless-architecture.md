# MOMS Serverless Architecture

## Overview

The MOMS application has been refactored to use a serverless architecture on AWS, eliminating the need for EC2 instances. This document outlines the architecture and components.

## Architecture Components

### API Layer
- **AWS API Gateway**: Routes HTTP requests to appropriate Lambda functions
- **AWS Lambda**: Executes application code in response to API requests
  - **Standard Functions**: Handle lightweight operations
  - **Containerized Functions**: Handle resource-intensive operations

### Database
- **Amazon Aurora Serverless v2**: PostgreSQL-compatible database
- **Auto-pause**: Automatically pauses after period of inactivity (dev/staging)
- **Auto-scaling**: Scales capacity based on demand

### Storage
- **Amazon S3**: Hosts static files (CSS, JS, images)
- **CloudFront** (optional): CDN for static file distribution

### Authentication & Security
- **API Gateway Authorizers**: Handle authentication
- **AWS Secrets Manager**: Store sensitive credentials
- **IAM Roles**: Control access between services

## Function Organization

```
Lambda Functions
├── standardApi           # Main API handler for most endpoints
│   └── layers            # Shared dependencies
├── containerizedApi      # Container-based handler for resource-intensive modules
├── migrations            # Database migration handler
└── collectstatic         # Static file collection handler
```

## Data Flow

1. Client makes HTTP request to API Gateway
2. API Gateway routes request to appropriate Lambda function
3. Lambda function processes request:
   - Connects to RDS for data operations
   - Accesses S3 for static files if needed
4. Lambda returns response to API Gateway
5. API Gateway returns response to client

## Module Distribution

### Standard Lambda Functions
- Authentication
- HR module
- CRM module
- Finance module
- Project module
- Strategy module
- Supply Chain module

### Containerized Lambda Functions
- Analytics module (with data processing libraries)
- Automation module (with workflow engines)
- Compliance module (with reporting engines)

## Advantages

1. **Cost Efficiency**: Pay only for actual usage
2. **Scalability**: Automatic scaling based on demand
3. **Reduced Maintenance**: No server management required
4. **High Availability**: Built-in redundancy across availability zones

## Limitations and Mitigations

1. **Cold Start Latency**
   - Mitigation: Provisioned concurrency for critical functions

2. **Function Timeout (15 min max)**
   - Mitigation: Design for asynchronous processing of long-running tasks

3. **Function Size Limits**
   - Mitigation: Hybrid approach with containerized functions for larger modules