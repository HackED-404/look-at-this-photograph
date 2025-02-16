<template>
    <div>
      <h1>Login Page</h1>
      <form @submit.prevent="login">
        <input v-model="credentials.email" type="email" placeholder="Email" />
        <input v-model="credentials.password" type="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script setup>
  //import { reactive } from 'vue'
  //import { useAuth } from '~/composables/useAuth'
  
  const { login } = useAuth()
  
  const credentials = reactive({
    email: '',
    password: '',
  })
  
  async function login() {
    try {
      await login(credentials)
    } catch (error) {
      console.error('Login failed', error)
    }
  }
  </script>