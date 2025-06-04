<template>
  <div class="module-header">
    <h1>{{ title }}</h1>
    <div class="actions">
      <logout-button />
    </div>
  </div>
</template>

<script>
import LogoutButton from './LogoutButton.vue'

export default {
  name: 'ModuleHeader',
  components: {
    LogoutButton
  },
  props: {
    title: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
.module-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  background-color: #f5f5f5;
  border-bottom: 1px solid #ddd;
  margin-bottom: 20px;
}

.module-header h1 {
  margin: 0;
  font-size: 1.5rem;
}
</style>