<template>
  <div id="app">
    <nav>
      <router-link :to="{'name': 'home'}">home</router-link> | 
      <router-link :to="{'name': 'profile'}">profile</router-link> | 
      <router-link :to="{'name': 'login'}">login</router-link> | 
      <router-link :to="{'name': 'signup'}">signup</router-link> | 
      <router-link :to="{'name': 'logout'}">logout</router-link>
    </nav>
    <router-view/>
    <nav>
    </nav>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
