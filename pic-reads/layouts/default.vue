<script setup lang="ts">
</script>

<template>
  <div class="app-container">
    <div class="content">
  <!--
  <div class="min-h-screen bg-gray-100 dark:bg-gray-900">
    <div class="w-full"> -->
    <AppHeader />
    <slot />
    <AppFooter />
  </div>
  </div>
</template>

<style scoped>
.app-container {
  background: linear-gradient(to bottom, #f0f4f8, #d9e2ec); /* Light gradient */
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.content {
  background: white;
  border-left: 5px solid #007bff; /* Blue left border */
  border-right: 5px solid #007bff; /* Blue right border */
  padding: 20px;
  max-width: 1200px;
  width: 100%;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}
</style>