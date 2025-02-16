<script setup lang="ts">
// You might choose this based on an API call or logged-in status
const layout = "logged-out-layout";
</script>

<template>
  <NuxtLayout :name="layout">
  </NuxtLayout>
  <NuxtPage />
</template>