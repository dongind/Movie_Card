<template>
  <div>
    <h1>home</h1>
    <ArticleList/>
    <hr>
    <MovieList/>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'HomeView',
  components: {
    ArticleList,
    MovieList,
  },
  computed: {
    // isLoggedin() {
    //   return this.$store.getters.isLoggedin
    // }
  },
  methods: {
    // isLogin() {
    //   if (this.isLoggedin === true) {
    //     console.log(this.isLoggedin)
    //   } else {
    //     alert('로그인이 필요한 서비스 입니다.')
    //     this.$router.push({ name: 'login'})
    //   }
    // }
  },
  mounted() {
    console.log(this.isLoggedin)
    // this.isLogin()
  },
}
</script>

<style>

</style>