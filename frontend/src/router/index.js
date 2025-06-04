// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

// Create a placeholder component for modules that don't have views yet
const ModulePlaceholder = {
  template: `
    <div class="module-placeholder">
      <h1>{{ $route.name }} Module</h1>
      <p>This module is under development.</p>
    </div>
  `
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/hr',
    name: 'HR',
    component: ModulePlaceholder
  },
  {
    path: '/analytics',
    name: 'Analytics',
    component: ModulePlaceholder
  },
  {
    path: '/automation',
    name: 'Automation',
    component: ModulePlaceholder
  },  
  {
    path: '/collaboration',
    name: 'Collaboration',
    component: ModulePlaceholder
  },  
  {
    path: '/compliance',
    name: 'Compliance',
    component: ModulePlaceholder
  },   
  {
    path: '/crm',
    name: 'CRM',
    component: ModulePlaceholder
  },
  {
    path: '/finance',
    name: 'Finance',
    component: ModulePlaceholder
  },   
  {
    path: '/project',
    name: 'Project',
    component: ModulePlaceholder
  },   
  {
    path: '/strategy',
    name: 'Strategy',
    component: ModulePlaceholder
  },   
  {
    path: '/supply_chain',
    name: 'Supply Chain',
    component: ModulePlaceholder
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router