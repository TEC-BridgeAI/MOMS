<!-- frontend/src/components/layout/AppFooter.vue -->
<template>
  <footer class="app-footer">
    <p>&copy; {{ currentYear }} <a href="https://TEC-Bridge.AI">TEC-Bridge AI</a></p>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter',
  computed: {
    currentYear() {
      return new Date().getFullYear();
    }
  }
}
</script>

<style scoped>
.app-footer {
  padding: 10px 20px;
  background-color: #f5f5f5;
  text-align: center;
  font-size: 0.9rem;
  color: #666;
  border-top: 1px solid #ddd;
}
</style>
