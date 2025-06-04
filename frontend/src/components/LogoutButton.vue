<template>
  <button class="logout-btn" @click="logout">Log out</button>
</template>

<script>
export default {
  name: 'LogoutButton',
  methods: {
    logout() {
      this.$store.dispatch('logout').then(() => {
        this.$router.push('/')
      })
    }
  }
}
</script>

<style scoped>
.logout-btn {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}
</style>