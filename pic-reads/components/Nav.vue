<template>
    <nav class="nav">
      <img src="@/public/logo.png" alt="PicReads Logo" class="logo" />

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
.nav {
  background-color: #333;
  color: #fff;
  width: 100%;
  display: flex;
  padding: 0.5em 1em;
}

.nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: space-around;
}

.logo {
  height: 30px;
  width: auto;
  margin-right: 1em;
}

.nav ul li {
  margin-right: 1em;
}

.nav ul li a {
  color: #fff;
  text-decoration: none;
  padding: 0.5em 1em;
  transition: background-color 0.3s;
}

.nav ul li a:hover {
  background-color: #555;
}
</style>