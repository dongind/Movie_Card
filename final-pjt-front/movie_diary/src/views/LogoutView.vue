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
    isLoggedin() {
      return this.$store.getters.isLoggedin
    }
  },
  methods: {
    logOut() {
      if (this.isLoggedin) {
        this.$store.dispatch('logOut')
        alert('로그아웃 되었습니다.')
        this.$router.push({ name: 'home' })
      } else {
        alert('잘못된 접근입니다.')
        this.$router.back()
      }
    }
  },
  created() {
    console.log(this.isLoggedin)
    this.logOut()
    this.$router.push({ name: 'login' })
  } 
}
</script>

<style>

</style>