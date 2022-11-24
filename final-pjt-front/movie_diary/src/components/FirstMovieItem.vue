<template>
  <div @click="selectMovieId" :class="{'first-movies': true, 'my-5': true, 'pt-3': true, 'selected': isClicked}">
    <img :src="imgSrc" alt="" width="200px" :class="{'mx-auto': true, 'card-shadow': true, 'selected':isClicked}">
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
.first-movies {
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  cursor: pointer;
  transition: all 0.5s;
}

.first-movies:hover {
  transform: scale(1.05)
}

.selected {
  border: 8px, rgb(11, 94, 248), solid;
}
</style>