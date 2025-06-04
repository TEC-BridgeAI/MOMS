<template>
  <div class="home">
    <header class="header">
      <div class="header-content">
        <img src="@/assets/logo.png" alt="TEC-Bridge AI Logo" class="logo">
        <div>
          <h1>TEC-Bridge AI Organizational Management System</h1>
          <p>The internal comprehensive business management platform</p>
        </div>
      </div>
      <div class="header-actions">
        <logout-button />
      </div>
    </header>

    <section class="intro">
      <h2>Welcome to TEC-Bridge AI!</h2>
      <p>
        The Modular Organizational Management System (MOMS) is an integrated platform 
        designed to streamline business operations across multiple departments.
      </p>
    </section>

    <section class="modules">
      <h2>Subsystems</h2>
      <div class="module-grid">
        <div class="module-card" v-for="module in modules" :key="module.id">
          <h3><router-link :to="module.path">{{ module.title }}</router-link></h3>
          <p>{{ module.description }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import LogoutButton from '@/components/LogoutButton.vue'

export default {
  name: 'HomePage',
  components: {
    LogoutButton
  },
  data() {
    return {
      modules: [
        {
          id: 'hr',
          title: 'HR Management',
          path: '/hr',
          description: 'Manage employee data, payroll, attendance, and performance evaluations.'
        },
        {
          id: 'analytics',
          title: 'Analytics',
          path: '/analytics',
          description: 'Gain insights through data visualization and business intelligence tools.'
        },
        {
          id: 'automation',
          title: 'Automation',
          path: '/automation',
          description: 'Automate routine tasks and workflows to improve efficiency.'
        },
        {
          id: 'collaboration',
          title: 'Collaboration',
          path: '/collaboration',
          description: 'Enable team communication and document sharing across departments.'
        },
        {
          id: 'compliance',
          title: 'Compliance',
          path: '/compliance',
          description: 'Ensure adherence to regulations and internal policies.'
        },
        {
          id: 'crm',
          title: 'CRM',
          path: '/crm',
          description: 'Track customer interactions, manage leads, and improve customer relationships.'
        },
        {
          id: 'finance',
          title: 'Finance',
          path: '/finance',
          description: 'Handle accounting, budgeting, invoicing, and financial reporting.'
        },
        {
          id: 'project',
          title: 'Project Management',
          path: '/project',
          description: 'Plan, execute, and monitor projects with task tracking and resource allocation.'
        },
        {
          id: 'strategy',
          title: 'Strategy',
          path: '/strategy',
          description: 'Develop and track strategic initiatives and business goals.'
        },
        {
          id: 'supply_chain',
          title: 'Supply Chain',
          path: '/supply_chain',
          description: 'Manage procurement, inventory, and supplier relationships.'
        }
      ]
    }
  }
}
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.header {
  margin-bottom: 40px;
  background-color: #0066cc;
  color: white;
  padding: 30px;
  border-radius: 5px;
  position: relative;
}

.header-content {
  display: flex;
  align-items: center;
}

.header-actions {
  position: absolute;
  top: 20px;
  right: 20px;
}

.logo {
  width: 80px;
  height: auto;
  margin-right: 20px;
}

.header h1 {
  margin: 0;
}

.module-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.module-card {
  background-color: #f5f5f5;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.module-card h3 a {
  color: #0066cc;
  text-decoration: none;
}

.module-card h3 a:hover {
  text-decoration: underline;
}
</style>