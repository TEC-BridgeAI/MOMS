# MOMS - Modular Organizational Management System

A comprehensive web application built with Django, PostgreSQL, and Vue.js for enterprise management operations developed by TEC-Bridge AI.

## Overview

MOMS is an open-source enterprise management system that integrates multiple organizational modules into a single, cohesive platform. The system is designed to streamline business operations across departments and provide a unified interface for managing various aspects of an organization.

## Modules

- **HR**: Human Resources Management
  - Employee records
  - Recruitment
  - Performance management
  - Training and development

- **Analytics**: Data Analytics and Reporting
  - Business intelligence
  - Custom reports
  - Data visualization
  - Metrics and KPIs

- **Automation**: Workflow Optimization
  - Process automation
  - Task scheduling
  - Notifications and alerts
  - Integration with external systems

- **Collaboration**: Communication Tools
  - Team messaging
  - Document sharing
  - Meeting management
  - Knowledge base

- **Compliance**: Risk Management
  - Regulatory compliance
  - Policy management
  - Audit trails
  - Risk assessment

- **CRM**: Customer Relationship Management
  - Contact management
  - Sales pipeline
  - Customer service
  - Marketing campaigns

- **Finance**: Accounting Management
  - Budgeting
  - Expense tracking
  - Financial reporting
  - Invoicing and payments

- **Project**: Task Management
  - Project planning
  - Task assignment
  - Progress tracking
  - Resource allocation

- **Strategy**: Strategic Planning
  - Goal setting
  - Performance tracking
  - Scenario planning
  - Decision support

- **Supply Chain**: Inventory Control
  - Inventory management
  - Procurement
  - Supplier management
  - Logistics tracking

## Tech Stack

- **Backend**: Django + PostgreSQL
- **Frontend**: Vue.js
- **Deployment**: AWS

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL 13+
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/moms.git
   cd moms
   ```

2. Set up the backend:
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   # source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt

   # Set up environment variables
   cp .env.example .env
   # Edit .env with your configuration

   # Run migrations
   cd backend
   python manage.py migrate

   # Create superuser
   python manage.py createsuperuser

   # Run server
   python manage.py runserver
   ```

3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   npm run serve
   ```

4. Access the application:
   - Backend API: http://localhost:8000/api/
   - Admin interface: http://localhost:8000/admin/
   - Frontend: http://localhost:8080/

## Development

See [development_procedure.md](development_procedure.md) for detailed development guidelines.

## Deployment

This project is configured for serverless deployment on AWS using:
- AWS Lambda with API Gateway for application logic
- RDS Aurora PostgreSQL with auto-pause for database
- S3 for static file hosting
- Serverless Framework for infrastructure management

The deployment uses a hybrid approach with both standard Lambda functions and containerized Lambda functions for modules exceeding size limits.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Acknowledgments

- Django community
- Vue.js community
- All contributors to this project