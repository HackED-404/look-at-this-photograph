<template>
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/">About</a></li>
      <li><a href="/">Contact</a></li>
    </ul>
  </nav>
</template>

<script setup>
console.log("Nav component loaded")
</script>

<style scoped>
nav {
  background-color: #333;
  color: #fff;
}

nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
}

nav ul li {
  margin-right: 1em;
}

nav ul li a {
  color: #fff;
  text-decoration: none;
}
</style>