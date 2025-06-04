// frontend/src/store/index.js
import { createStore } from 'vuex'

export default createStore({
  state: {
    auth: {
      user: null,
      token: localStorage.getItem('token')
    }
  },
  getters: {
    isAuthenticated: state => !!state.auth.token,
    user: state => state.auth.user
  },
  mutations: {
    SET_USER(state, user) {
      state.auth.user = user
    },
    SET_TOKEN(state, token) {
      state.auth.token = token
      localStorage.setItem('token', token)
    },
    CLEAR_AUTH(state) {
      state.auth.user = null
      state.auth.token = null
      localStorage.removeItem('token')
    }
  },
  actions: {
    login({ commit }, credentials) {
      // This would be an API call in a real app
      console.log('Login with:', credentials)
      commit('SET_TOKEN', 'sample-token')
      commit('SET_USER', { username: credentials.username || 'admin' })
      return Promise.resolve()
    },
    logout({ commit }) {
      commit('CLEAR_AUTH')
      return Promise.resolve()
    }
  },
  modules: {
  }
})