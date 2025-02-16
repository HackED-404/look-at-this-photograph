<script setup lang="ts">

</script>

<template>
  <div>
    <!-- Header Section -->
    <header>
      <div class="header-content">
        <NuxtLink to="/">Home</NuxtLink>
        <NuxtLink to="/resultTable">TempResultTable</NuxtLink>
      </div>
    </header>

  </div>
</template>

<style scoped>
header {
  background-color: #333;
  padding: 1rem;
}

.header-content {
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center; /* Vertically center the items */
  font-size: 24px;
}
</style>