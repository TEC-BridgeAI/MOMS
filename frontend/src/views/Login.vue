<template>
  <div class="login">
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username">
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password">
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    handleLogin() {
      this.$store.dispatch('login', {
        username: this.username,
        password: this.password
      }).then(() => {
        // Redirect to the requested page or default to MOMS page
        const redirectPath = this.$route.query.redirect || '/moms'
        this.$router.push(redirectPath)
      })
    }
  }
}
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

form div {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: #0066cc;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0055aa;
}
</style>