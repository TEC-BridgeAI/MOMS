// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import TecBridgeHome from '../views/TecBridgeHome.vue'
import store from '../store'
import ModuleHeader from '../components/ModuleHeader.vue'

// Create a placeholder component for modules that don't have views yet
const ModulePlaceholder = {
  components: { ModuleHeader },
  template: `
    <div class="module-placeholder">
      <module-header :title="$route.name + ' Module'" />
      <div class="module-content">
        <p>This module is under development.</p>
      </div>
    </div>
  `,
  style: `
    .module-content {
      padding: 20px;
    }
  `
}

const routes = [
  {
    path: '/',
    name: 'TecBridgeHome',
    component: TecBridgeHome
  },
  {
    path: '/moms',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/hr',
    name: 'HR',
    component: ModulePlaceholder,
    meta: { requiresAuth: true }
  },
  {
    path: '/analytics',
    name: 'Analytics',
    component: ModulePlaceholder,
    meta: { requiresAuth: true }
  },
  {
    path: '/automation',
    name: 'Automation',
    component: ModulePlaceholder,
    meta: { requiresAuth: true }
  },  
  {
    path: '/collaboration',
    name: 'Collaboration',
    component: ModulePlaceholder,
    meta: { requiresAuth: true }
  },  
  {
    path: '/compliance',
    name: 'Compliance',
    component: ModulePlaceholder,
    meta: { requiresAuth: true }
  },   
  {
    path: '/crm',
    name: 'CRM',
    component: ModulePlaceholder,
    meta: { requiresAuth: true }
  },
  {
    path: '/finance',
    name: 'Finance',
    component: ModulePlaceholder,
    meta: { requiresAuth: true }
  },   
  {
    path: '/project',
    name: 'Project',
    component: ModulePlaceholder,
    meta: { requiresAuth: true }
  },   
  {
    path: '/strategy',
    name: 'Strategy',
    component: ModulePlaceholder,
    meta: { requiresAuth: true }
  },   
  {
    path: '/supply_chain',
    name: 'Supply Chain',
    component: ModulePlaceholder,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // This route requires auth, check if logged in
    if (!store.getters.isAuthenticated) {
      // Not logged in, redirect to login page
      next({ 
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router