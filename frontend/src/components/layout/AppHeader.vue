<!-- frontend/src/components/layout/AppHeader.vue -->
<template>
  <header class="app-header">
    <div class="logo">
      <router-link to="/">MOMS</router-link>
    </div>
    <div class="user-menu">
      <span v-if="user">{{ user.username }}</span>
      <button @click="logout">Logout</button>
    </div>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
  computed: {
    user() {
      return this.$store?.state?.auth?.user || null;
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout');
      this.$router.push('/login');
    }
  }
}
</script>

<style scoped>
.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  height: 60px;
  background-color: #2c3e50;
  color: white;
}

.logo a {
  color: white;
  text-decoration: none;
  font-size: 1.5rem;
  font-weight: bold;
}

.user-menu {
  display: flex;
  align-items: center;
}

.user-menu span {
  margin-right: 10px;
}

.user-menu button {
  background-color: transparent;
  border: 1px solid white;
  color: white;
  padding: 5px 10px;
  cursor: pointer;
}
</style>
