<template>
    <nav>
        <ul>
            <li>
                <router-link to="/">Home</router-link>
            </li>
            <li>
                <router-link to="/">My BookShelf</router-link>
            </li>
            <li>
                <router-link to="/"></router-link>
            </li>
        </ul>
    </nav>
</template>

<script>
export default {
    name: 'Nav'
}
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