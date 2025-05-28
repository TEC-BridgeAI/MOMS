# Vue.js Frontend Setup

## Initial Setup

1. Install Vue CLI:
   ```bash
   npm install -g @vue/cli
   ```

2. Create a new Vue project:
   ```bash
   vue create frontend
   ```
   
   Select the following options:
   - Vue 3
   - Manually select features
   - Choose: Babel, Router, Vuex, CSS Pre-processors, Linter
   - Use history mode for router: Yes
   - Choose Sass/SCSS with dart-sass
   - Choose ESLint with Prettier
   - Lint on save
   - Place config in dedicated files
   - Save as a preset for future projects: Optional

3. Install additional dependencies:
   ```bash
   cd frontend
   npm install axios vue-axios vuetify@next @mdi/font chart.js vue-chartjs vee-validate yup
   ```

## Project Structure

Organize the project structure as follows:

```
frontend/
├── public/
│   ├── favicon.ico
│   └── index.html
├── src/
│   ├── assets/
│   │   ├── logo.png
│   │   ├── scss/
│   │   │   ├── _variables.scss
│   │   │   └── main.scss
│   │   └── images/
│   ├── components/
│   │   ├── common/
│   │   │   ├── AppHeader.vue
│   │   │   ├── AppFooter.vue
│   │   │   ├── AppSidebar.vue
│   │   │   └── AppBreadcrumb.vue
│   │   ├── hr/
│   │   ├── analytics/
│   │   ├── automation/
│   │   ├── collaboration/
│   │   ├── compliance/
│   │   ├── crm/
│   │   ├── finance/
│   │   ├── project/
│   │   ├── strategy/
│   │   └── supply_chain/
│   ├── views/
│   │   ├── Home.vue
│   │   ├── Login.vue
│   │   ├── Dashboard.vue
│   │   ├── hr/
│   │   ├── analytics/
│   │   ├── automation/
│   │   ├── collaboration/
│   │   ├── compliance/
│   │   ├── crm/
│   │   ├── finance/
│   │   ├── project/
│   │   ├── strategy/
│   │   └── supply_chain/
│   ├── router/
│   │   └── index.js
│   ├── store/
│   │   ├── index.js
│   │   └── modules/
│   │       ├── auth.js
│   │       ├── hr.js
│   │       ├── analytics.js
│   │       ├── automation.js
│   │       ├── collaboration.js
│   │       ├── compliance.js
│   │       ├── crm.js
│   │       ├── finance.js
│   │       ├── project.js
│   │       ├── strategy.js
│   │       └── supply_chain.js
│   ├── services/
│   │   ├── api.js
│   │   ├── auth.service.js
│   │   ├── hr.service.js
│   │   ├── analytics.service.js
│   │   └── ...
│   ├── utils/
│   │   ├── helpers.js
│   │   └── validators.js
│   ├── App.vue
│   └── main.js
├── .env
├── .env.development
├── .env.production
├── .eslintrc.js
├── babel.config.js
├── package.json
└── vue.config.js
```

## Configure Vue Router

```javascript
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { guest: true }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  },
  // HR routes
  {
    path: '/hr',
    name: 'HR',
    component: () => import('../views/hr/HRDashboard.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/hr/employees',
    name: 'Employees',
    component: () => import('../views/hr/EmployeeList.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/hr/employees/:id',
    name: 'EmployeeDetail',
    component: () => import('../views/hr/EmployeeDetail.vue'),
    meta: { requiresAuth: true }
  },
  // Add routes for other modules similarly
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters['auth/isAuthenticated']) {
      next({ name: 'Login', query: { redirect: to.fullPath } })
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.guest)) {
    if (store.getters['auth/isAuthenticated']) {
      next({ name: 'Dashboard' })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
```

## Configure Vuex Store

```javascript
// src/store/index.js
import { createStore } from 'vuex'
import auth from './modules/auth'
import hr from './modules/hr'
import analytics from './modules/analytics'
import automation from './modules/automation'
import collaboration from './modules/collaboration'
import compliance from './modules/compliance'
import crm from './modules/crm'
import finance from './modules/finance'
import project from './modules/project'
import strategy from './modules/strategy'
import supply_chain from './modules/supply_chain'

export default createStore({
  state: {
    loading: false,
    error: null
  },
  mutations: {
    SET_LOADING(state, loading) {
      state.loading = loading
    },
    SET_ERROR(state, error) {
      state.error = error
    }
  },
  actions: {
    setLoading({ commit }, loading) {
      commit('SET_LOADING', loading)
    },
    setError({ commit }, error) {
      commit('SET_ERROR', error)
    }
  },
  modules: {
    auth,
    hr,
    analytics,
    automation,
    collaboration,
    compliance,
    crm,
    finance,
    project,
    strategy,
    supply_chain
  }
})
```

```javascript
// src/store/modules/auth.js
import AuthService from '@/services/auth.service'

export default {
  namespaced: true,
  state: {
    token: localStorage.getItem('token') || null,
    refreshToken: localStorage.getItem('refreshToken') || null,
    user: JSON.parse(localStorage.getItem('user')) || null
  },
  getters: {
    isAuthenticated: state => !!state.token,
    getUser: state => state.user
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.token = token
    },
    SET_REFRESH_TOKEN(state, refreshToken) {
      state.refreshToken = refreshToken
    },
    SET_USER(state, user) {
      state.user = user
    },
    LOGOUT(state) {
      state.token = null
      state.refreshToken = null
      state.user = null
    }
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await AuthService.login(credentials)
        
        localStorage.setItem('token', response.access)
        localStorage.setItem('refreshToken', response.refresh)
        
        commit('SET_TOKEN', response.access)
        commit('SET_REFRESH_TOKEN', response.refresh)
        
        return response
      } catch (error) {
        throw error
      }
    },
    async getUser({ commit }) {
      try {
        const user = await AuthService.getUser()
        
        localStorage.setItem('user', JSON.stringify(user))
        commit('SET_USER', user)
        
        return user
      } catch (error) {
        throw error
      }
    },
    async refreshToken({ commit, state }) {
      try {
        const response = await AuthService.refreshToken(state.refreshToken)
        
        localStorage.setItem('token', response.access)
        commit('SET_TOKEN', response.access)
        
        return response
      } catch (error) {
        commit('LOGOUT')
        localStorage.removeItem('token')
        localStorage.removeItem('refreshToken')
        localStorage.removeItem('user')
        throw error
      }
    },
    logout({ commit }) {
      commit('LOGOUT')
      localStorage.removeItem('token')
      localStorage.removeItem('refreshToken')
      localStorage.removeItem('user')
    }
  }
}
```

## API Service Setup

```javascript
// src/services/api.js
import axios from 'axios'
import store from '@/store'
import router from '@/router'

const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
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
  error => {
    return Promise.reject(error)
  }
)

// Response interceptor
api.interceptors.response.use(
  response => {
    return response
  },
  async error => {
    const originalRequest = error.config
    
    // If error is 401 and not already retrying
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      
      try {
        // Try to refresh the token
        await store.dispatch('auth/refreshToken')
        
        // Retry the original request with new token
        originalRequest.headers.Authorization = `Bearer ${store.state.auth.token}`
        return api(originalRequest)
      } catch (refreshError) {
        // If refresh token fails, redirect to login
        store.dispatch('auth/logout')
        router.push('/login')
        return Promise.reject(refreshError)
      }
    }
    
    return Promise.reject(error)
  }
)

export default api
```

```javascript
// src/services/auth.service.js
import api from './api'

class AuthService {
  login(credentials) {
    return api.post('/token/', credentials)
      .then(response => response.data)
  }
  
  refreshToken(refreshToken) {
    return api.post('/token/refresh/', { refresh: refreshToken })
      .then(response => response.data)
  }
  
  getUser() {
    return api.get('/users/me/')
      .then(response => response.data)
  }
}

export default new AuthService()
```

## Create Main App Components

```vue
<!-- src/App.vue -->
<template>
  <div id="app">
    <app-header v-if="isAuthenticated" />
    <app-sidebar v-if="isAuthenticated" />
    <div :class="{ 'content-with-sidebar': isAuthenticated, 'content': !isAuthenticated }">
      <app-breadcrumb v-if="isAuthenticated" />
      <router-view />
    </div>
    <app-footer v-if="isAuthenticated" />
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import AppHeader from '@/components/common/AppHeader.vue'
import AppSidebar from '@/components/common/AppSidebar.vue'
import AppFooter from '@/components/common/AppFooter.vue'
import AppBreadcrumb from '@/components/common/AppBreadcrumb.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppSidebar,
    AppFooter,
    AppBreadcrumb
  },
  setup() {
    const store = useStore()
    const isAuthenticated = computed(() => store.getters['auth/isAuthenticated'])
    
    return {
      isAuthenticated
    }
  }
}
</script>

<style lang="scss">
@import '@/assets/scss/main.scss';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.content-with-sidebar {
  margin-left: 250px;
  padding: 20px;
}

.content {
  padding: 20px;
}
</style>
```

## Create Login View

```vue
<!-- src/views/Login.vue -->
<template>
  <div class="login-container">
    <div class="login-form">
      <h1>Login</h1>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="username">Username</label>
          <input 
            type="text" 
            id="username" 
            v-model="username" 
            required 
            placeholder="Enter your username"
          />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            required 
            placeholder="Enter your password"
          />
        </div>
        <div v-if="error" class="error-message">
          {{ error }}
        </div>
        <button type="submit" :disabled="loading">
          {{ loading ? 'Logging in...' : 'Login' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter, useRoute } from 'vue-router'

export default {
  name: 'Login',
  setup() {
    const store = useStore()
    const router = useRouter()
    const route = useRoute()
    
    const username = ref('')
    const password = ref('')
    const loading = ref(false)
    const error = ref(null)
    
    const handleLogin = async () => {
      loading.value = true
      error.value = null
      
      try {
        await store.dispatch('auth/login', {
          username: username.value,
          password: password.value
        })
        
        await store.dispatch('auth/getUser')
        
        // Redirect to the requested page or dashboard
        const redirectPath = route.query.redirect || '/dashboard'
        router.push(redirectPath)
      } catch (err) {
        error.value = err.response?.data?.detail || 'Login failed. Please check your credentials.'
      } finally {
        loading.value = false
      }
    }
    
    return {
      username,
      password,
      loading,
      error,
      handleLogin
    }
  }
}
</script>

<style scoped lang="scss">
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.login-form {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  
  h1 {
    text-align: center;
    margin-bottom: 2rem;
  }
  
  .form-group {
    margin-bottom: 1rem;
    
    label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: bold;
    }
    
    input {
      width: 100%;
      padding: 0.75rem;
      border: 1px solid #ddd;
      border-radius: 4px;
      font-size: 1rem;
    }
  }
  
  .error-message {
    color: #dc3545;
    margin-bottom: 1rem;
  }
  
  button {
    width: 100%;
    padding: 0.75rem;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    
    &:hover {
      background-color: #45a049;
    }
    
    &:disabled {
      background-color: #cccccc;
      cursor: not-allowed;
    }
  }
}
</style>
```

## Configure Environment Variables

```
# .env.development
VUE_APP_API_URL=http://localhost:8000/api
```

```
# .env.production
VUE_APP_API_URL=/api
```

## Configure Vue Config

```javascript
// vue.config.js
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  },
  css: {
    loaderOptions: {
      sass: {
        additionalData: `@import "@/assets/scss/_variables.scss";`
      }
    }
  }
}
```

## Build for Production

```bash
npm run build
```

This will create a `dist` directory with the compiled assets that can be served by a web server or deployed to AWS.