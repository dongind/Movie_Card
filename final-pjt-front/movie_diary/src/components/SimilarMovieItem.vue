<template>
  <div @click="getSimilarMovie">
    <img :src="imgSrc" alt="" height="200px">
    <p>{{ similarMovie.title }}</p>
  </div>
</template>

<script>
export default {
  name: "SimilarMovieItem",
  props: {
    similarMovie:Object,
  },
  computed: {
    imgSrc() {
      return `https://image.tmdb.org/t/p/original${this.similarMovie.poster_path}`
    },
  },
  methods: {
    getSimilarMovie() {
      // console.log(this.similarMovie.pk)
      this.$emit('get-similar-movie', this.similarMovie.pk)
    }
  }
}
</script>

<style>

</style>