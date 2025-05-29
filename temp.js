# Let's develop the core Vue components and views for the MOMS application. I'll focus on creating the essential structure and a few key components.

#1. Main App Component:

<!-- frontend/src/App.vue -->
<template>
  <div id="app">
    <app-header v-if="isAuthenticated" />
    <div class="container-fluid">
      <div class="row">
        <app-sidebar v-if="isAuthenticated" class="col-md-3 col-lg-2" />
        <main class="col-md-9 col-lg-10 px-4">
          <router-view />
        </main>
      </div>
    </div>
  </div>
</template>

<script>
import AppHeader from '@/components/layout/AppHeader.vue'
import AppSidebar from '@/components/layout/AppSidebar.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppSidebar
  },
  computed: {
    ...mapGetters('auth', ['isAuthenticated'])
  }
}
</script>


# 2. Header Component:

<!-- frontend/src/components/layout/AppHeader.vue -->
<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">MOMS</router-link>
      <div class="d-flex">
        <span class="navbar-text me-3">{{ user.username }}</span>
        <button class="btn btn-outline-light" @click="logout">Logout</button>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'AppHeader',
  computed: {
    ...mapGetters('auth', ['user'])
  },
  methods: {
    ...mapActions('auth', ['logout']),
    async logout() {
      await this.logout()
      this.$router.push('/login')
    }
  }
}
</script>


# 3. Sidebar Component:

<!-- frontend/src/components/layout/AppSidebar.vue -->
<template>
  <div class="sidebar bg-light">
    <ul class="nav flex-column">
      <li class="nav-item" v-for="(item, index) in menuItems" :key="index">
        <router-link :to="item.path" class="nav-link">
          <i :class="item.icon"></i> {{ item.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'AppSidebar',
  data() {
    return {
      menuItems: [
        { title: 'Dashboard', path: '/', icon: 'bi bi-speedometer2' },
        { title: 'HR', path: '/hr', icon: 'bi bi-people' },
        { title: 'Analytics', path: '/analytics', icon: 'bi bi-graph-up' },
        { title: 'Automation', path: '/automation', icon: 'bi bi-gear' },
        { title: 'Collaboration', path: '/collaboration', icon: 'bi bi-chat' },
        { title: 'Compliance', path: '/compliance', icon: 'bi bi-shield-check' },
        { title: 'CRM', path: '/crm', icon: 'bi bi-person-lines-fill' },
        { title: 'Finance', path: '/finance', icon: 'bi bi-cash' },
        { title: 'Projects', path: '/projects', icon: 'bi bi-kanban' },
        { title: 'Strategy', path: '/strategy', icon: 'bi bi-bullseye' },
        { title: 'Supply Chain', path: '/supply-chain', icon: 'bi bi-truck' }
      ]
    }
  }
}
</script>

<style scoped>
.sidebar {
  min-height: calc(100vh - 56px);
  padding-top: 1rem;
}
</style>


# 4. Login View:

<!-- frontend/src/views/auth/Login.vue -->
<template>
  <div class="login-container">
    <div class="card login-card">
      <div class="card-header bg-primary text-white">
        <h3 class="mb-0">Login to MOMS</h3>
      </div>
      <div class="card-body">
        <form @submit.prevent="handleLogin">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" class="form-control" id="username" v-model="username" required>
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" id="password" v-model="password" required>
          </div>
          <div v-if="error" class="alert alert-danger">{{ error }}</div>
          <button type="submit" class="btn btn-primary w-100" :disabled="loading">
            {{ loading ? 'Logging in...' : 'Login' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      error: null
    }
  },
  methods: {
    ...mapActions('auth', ['login']),
    async handleLogin() {
      this.loading = true
      this.error = null
      try {
        await this.login({ username: this.username, password: this.password })
        this.$router.push('/')
      } catch (err) {
        this.error = err.response?.data?.detail || 'Login failed'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.login-card {
  width: 100%;
  max-width: 400px;
}
</style>


# 5. Dashboard View:

<!-- frontend/src/views/Dashboard.vue -->
<template>
  <div class="dashboard">
    <h1 class="mb-4">Dashboard</h1>
    <div class="row">
      <div v-for="(module, index) in modules" :key="index" class="col-md-4 mb-4">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">{{ module.title }}</h5>
            <p class="card-text">{{ module.description }}</p>
            <router-link :to="module.path" class="btn btn-primary">View</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      modules: [
        {
          title: 'HR',
          description: 'Manage employees, departments, and HR processes',
          path: '/hr'
        },
        {
          title: 'CRM',
          description: 'Manage customers, opportunities, and sales activities',
          path: '/crm'
        },
        {
          title: 'Projects',
          description: 'Track projects, tasks, and milestones',
          path: '/projects'
        },
        {
          title: 'Finance',
          description: 'Manage invoices, transactions, and financial reports',
          path: '/finance'
        },
        {
          title: 'Supply Chain',
          description: 'Track inventory, suppliers, and purchase orders',
          path: '/supply-chain'
        },
        {
          title: 'Analytics',
          description: 'View reports and data visualizations',
          path: '/analytics'
        }
      ]
    }
  }
}
</script>


# 6. Router Configuration:

// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'

// Views
import Dashboard from '@/views/Dashboard.vue'
import Login from '@/views/auth/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { guest: true }
  },
  // Lazy-loaded module routes
  {
    path: '/hr',
    name: 'HR',
    component: () => import('@/views/hr/HRDashboard.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/crm',
    name: 'CRM',
    component: () => import('@/views/crm/CRMDashboard.vue'),
    meta: { requiresAuth: true }
  }
  // Add other module routes similarly
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Navigation guard
router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters['auth/isAuthenticated']
  
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next({ name: 'Login' })
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.guest)) {
    if (isAuthenticated) {
      next({ name: 'Dashboard' })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router


Copy
Vuex Store Configuration:

// frontend/src/store/index.js
import { createStore } from 'vuex'
import auth from './modules/auth'
import hr from './modules/hr'
import crm from './modules/crm'
// Import other modules as needed

export default createStore({
  modules: {
    auth,
    hr,
    crm
    // Add other modules
  }
})

Copy
Auth Store Module:

// frontend/src/store/modules/auth.js
import api from '@/services/api'

export default {
  namespaced: true,
  
  state: {
    token: localStorage.getItem('token') || null,
    user: JSON.parse(localStorage.getItem('user')) || null
  },
  
  getters: {
    isAuthenticated: state => !!state.token,
    user: state => state.user
  },
  
  mutations: {
    SET_TOKEN(state, token) {
      state.token = token
    },
    SET_USER(state, user) {
      state.user = user
    },
    CLEAR_AUTH(state) {
      state.token = null
      state.user = null
    }
  },
  
  actions: {
    async login({ commit, dispatch }, credentials) {
      const response = await api.post('/token/', credentials)
      const token = response.data.access
      
      localStorage.setItem('token', token)
      commit('SET_TOKEN', token)
      
      await dispatch('fetchUser')
      return response
    },
    
    async fetchUser({ commit }) {
      const response = await api.get('/users/me/')
      const user = response.data
      
      localStorage.setItem('user', JSON.stringify(user))
      commit('SET_USER', user)
      return user
    },
    
    logout({ commit }) {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      commit('CLEAR_AUTH')
    }
  }
}


Copy
API Service:

// frontend/src/services/api.js
import axios from 'axios'
import store from '@/store'
import router from '@/router'

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://localhost:8000/api'
})

// Request interceptor
api.interceptors.request.use(
  config => {
    const token = store.state.auth.token
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  error => Promise.reject(error)
)

// Response interceptor
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      store.dispatch('auth/logout')
      router.push('/login')
    }
    return Promise.reject(error)
  }
)

export default api


Copy
These components and configurations provide a solid foundation for your Vue.js frontend. You can expand on this by creating specific views and components for each module as needed.


