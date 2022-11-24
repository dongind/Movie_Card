<template>
  <div>
    <h2>흥미롭게 즐기셨던 영화를 최대 5까지 골라주세요.</h2>
    <span>
      <FirstMovieItem
        v-for= "movie in popularRandomRecommend" :key="movie.id"
        :movie="movie"
        @select-movie="selectMovie"
      />
    </span>
    <h4>선택 영화 목록 : {{ selectedMoviesId }}</h4>
    <router-link :to="{'name': 'home'}">
      <button type="button" class="btn btn-primary" @click="baseRating">Movie Rating</button>
    </router-link>
  </div>
</template>

<script>
import FirstMovieItem from '@/components/FirstMovieItem.vue'
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'FirstMovieView',
  components: {
    FirstMovieItem
  },
  data() {
    return {
      selectedMoviesId: [],
      key: null,
    }
  },
  computed: {
    popularRandomRecommend() {
      return _.sampleSize(this.$store.state.popularRandomRecommend, 20)
    },
  },
  methods: {
    getRandomPopularMovies() {
      this.$store.dispatch('getRandomPopularMovies')
      this.key = `Token ${this.$store.state.token}`
      console.log(this.key)
    },
    selectMovie(selectedMovie) {
      if (selectedMovie.isClicked) {
        this.selectedMoviesId.push(selectedMovie.id)
      } else {
        const index = this.selectedMoviesId.indexOf(selectedMovie.id)
        this.selectedMoviesId.splice(index, 1)
      }
    },
    baseRating(){
      const API_URL = 'http://127.0.0.1:8000/api/v1/cards/'
      const API_KEY = this.key
      let today = new Date()
      let year = today.getFullYear()
      let month = today.getMonth()
      let date = today.getDay()
      this.$store.dispatch('getArticleList')
      for (let id of this.selectedMoviesId) {
        axios({
          method: 'post',
          url: API_URL,
          headers: {'Authorization': API_KEY},
          data: {
            'movie': id,
            'content': null,
            'planned_at': String(year+'-'+month+'-'+date),
            'is_watched': false,
          },
        })
          .then(() =>{
            axios({
              method: 'post',
              url: 'http://127.0.0.1:8000/api/v2/movies/rate/',
              headers: {'Authorization': API_KEY},
              data: {
                'movie_pk': id,
                'rate': 3
              },
            })
              .then(() => {
                this.$router.push('home')
              })
              .catch((error) => {
                console.log(error)
              })
          })
          .catch((error) => {
            console.log(error)
          })
      }
    }
  },
  created() {
    this.getRandomPopularMovies()
  }
}

// @click="getRandomPopularMovies"
</script>

<style>

</style>