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
  background: #2c3e50;
  color: white;
  text-align: center;
  padding: 15px;
  font-size: 1.5rem;
  font-weight: bold;
  display: flex;
  justify-content: center;
  align-items: center;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: space-around;
  font-size: 25px;
  align-items: center;
}

.logo {
  height: 50px;
  width: auto;
  margin-right: 1em;
  border-radius: 10px;
}

.nav ul li {
  margin-right: 1em;
}

.nav ul li a {
  color: #fff;
  text-decoration: none;
  padding: 0.5em 1em;
  border-radius: 5px;
  background-color: #34495e; 
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s, box-shadow 0.3s;
}

.nav ul li a:hover {
  background-color: #1abc9c;
}
</style>