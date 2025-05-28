# Project Structure

```
moms/
├── backend/                     # Django backend
│   ├── moms_project/           # Main Django project
│   │   ├── settings/           # Settings (base, dev, prod)
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/                   # Django applications
│   │   ├── hr/                 # HR module
│   │   ├── analytics/          # Analytics module
│   │   ├── automation/         # Automation module
│   │   ├── collaboration/      # Collaboration module
│   │   ├── compliance/         # Compliance module
│   │   ├── crm/                # CRM module
│   │   ├── finance/            # Finance module
│   │   ├── project/            # Project management module
│   │   ├── strategy/           # Strategic planning module
│   │   └── supply_chain/       # Supply chain module
│   ├── static/                 # Static files
│   ├── media/                  # User-uploaded files
│   ├── templates/              # Django templates
│   ├── manage.py
│   └── requirements.txt        # Python dependencies
├── frontend/                   # Vue.js frontend
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── views/
│   │   │   ├── hr/
│   │   │   ├── analytics/
│   │   │   ├── automation/
│   │   │   ├── collaboration/
│   │   │   ├── compliance/
│   │   │   ├── crm/
│   │   │   ├── finance/
│   │   │   ├── project/
│   │   │   ├── strategy/
│   │   │   └── supply_chain/
│   │   ├── router/
│   │   ├── store/
│   │   ├── App.vue
│   │   └── main.js
│   ├── package.json
│   └── vue.config.js
├── deployment/                 # Deployment configurations
│   ├── docker/
│   │   ├── docker-compose.yml
│   │   ├── Dockerfile.backend
│   │   └── Dockerfile.frontend
│   └── aws/
│       ├── cloudformation/
│       └── scripts/
├── .github/                    # GitHub workflows
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── .gitignore
├── README.md
└── LICENSE
```