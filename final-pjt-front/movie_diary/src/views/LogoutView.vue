<template>
  <div>
    <h1 style="font-family: 'GmarketSansMedium';">
      Logout 되었습니다.
    </h1>

  </div>
</template>

<script>
export default {
  name: 'LogoutView',
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    }
  },
  created() {
    // console.log(this.isLoggedIn)
    this.logOut()
    this.$router.push({ name: 'login' })
  } 
}
</script>

<style>

</style>