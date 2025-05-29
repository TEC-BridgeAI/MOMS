<!-- frontend/src/App.vue -->
<template>
  <div id="app">
    <template v-if="!isAuthenticated">
      <router-view />
    </template>
    <template v-else>
      <app-header />
      <div class="main-container">
        <app-sidebar />
        <main class="content">
          <router-view />
        </main>
      </div>
      <app-footer />
    </template>
  </div>
</template>

<script>
import AppHeader from '@/components/layout/AppHeader.vue'
import AppSidebar from '@/components/layout/AppSidebar.vue'
import AppFooter from '@/components/layout/AppFooter.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppSidebar,
    AppFooter
  },
  computed: {
    ...mapGetters('auth', ['isAuthenticated'])
  },
  created() {
    // Clear any existing auth data on app start
    this.$store.dispatch('auth/logout')
    
    // Redirect to login if not on login page
    if (this.$route.path !== '/login') {
      this.$router.push('/login')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.main-container {
  display: flex;
}

.content {
  flex: 1;
  padding: 20px;
}
</style>
