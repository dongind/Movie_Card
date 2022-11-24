<template>
  <div @click="selectMovieId">
    <img :src="imgSrc" alt="" height="200px">
    <p>{{ movie.title }}</p>
  </div>   
</template>

<script>
export default {
  name: "FirstMovieItem",
  props: {
    movie: Object,
  },
  data() {
    return {
      moviePosterPath: this.movie.poster_path,
      isClicked: false,
    }
  },
  computed: {
    imgSrc() {
      return `https://image.tmdb.org/t/p/original${this.moviePosterPath}`
    },
  },
  methods: {
    selectMovieId() {
      this.isClicked = !this.isClicked
      const movieClickedInfo = {
        'id': this.movie.id,
        'isClicked': this.isClicked,
      }
      this.$emit("select-movie", movieClickedInfo)
    }
  }
}
</script>

<style>

</style>