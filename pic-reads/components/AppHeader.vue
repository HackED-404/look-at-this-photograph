<script setup lang="ts">
    const { login, logout } = useAuth();
    console.log("AppHeader component loaded")

</script>

<template>
    <footer class="header">
        <div class="container">
            <button @click=""login>Login</button>
            <button @click="logout">Logout</button>
        </div>
    </footer>
</template>

<style scoped>
.header {
  background-color: #f8f9fa;
  padding: 1em 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1em;
}
</style>