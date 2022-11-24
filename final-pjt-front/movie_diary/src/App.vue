<template>
  <div id="app">
    <nav>
      <router-link :to="{'name': 'login'}" > login </router-link>
      <router-link :to="{'name': 'signup'}" > signup </router-link>
      <router-link :to="{'name': 'logout'}" > logout </router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>

</script>

<style>

</style>
