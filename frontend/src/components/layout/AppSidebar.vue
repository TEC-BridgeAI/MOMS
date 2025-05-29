<!-- frontend/src/components/layout/AppSidebar.vue -->
<template>
  <aside class="app-sidebar">
    <nav>
      <ul>
        <li><router-link to="/">Dashboard</router-link></li>
        <li><router-link to="/hr">HR</router-link></li>
        <li><router-link to="/analytics">Analytics</router-link></li>
        <li><router-link to="/automation">Automation</router-link></li>
        <li><router-link to="/collaboration">Collaboration</router-link></li>
        <li><router-link to="/compliance">Compliance</router-link></li>
        <li><router-link to="/crm">CRM</router-link></li>
        <li><router-link to="/finance">Finance</router-link></li>
        <li><router-link to="/project">Project</router-link></li>
        <li><router-link to="/strategy">Strategy</router-link></li>
        <li><router-link to="/supply-chain">Supply Chain</router-link></li>
      </ul>
    </nav>
  </aside>
</template>

<script>
export default {
  name: 'AppSidebar'
}
</script>

<style scoped>
.app-sidebar {
  width: 200px;
  background-color: #f5f5f5;
  height: calc(100vh - 60px);
  padding: 20px 0;
}

.app-sidebar ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.app-sidebar li {
  padding: 10px 20px;
}

.app-sidebar a {
  color: #2c3e50;
  text-decoration: none;
}

.app-sidebar a.router-link-active {
  font-weight: bold;
}
</style>
