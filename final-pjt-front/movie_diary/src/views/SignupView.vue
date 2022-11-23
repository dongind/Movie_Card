<template>
  <div>
    <form @submit.prevent="signUp">
      <div class="container">
        <form class="needs-validation" novalidate @submit.prevent="signUp">
          <div class="signup-class">
            <h1 class="mb-5">SignUp Page</h1>
            <div class="form-floating mb-3">
              <input type="email" :class="{'form-control':true, 'is-invalid': !isValidUsername}" id="floatingInput" placeholder="name" required v-model.trim="username">
              <label for="floatingInput">Username / 아이디</label>
              <div v-if="!isValidUsername" class="input-error text-danger">
                Username을 입력해주세요.
              </div>
            </div>  
            <div class="form-floating mb-3">
              <input type="password" :class="{'form-control':true, 'is-invalid': !isValidPassword1}" id="floatingPassword1" placeholder="Password" required v-model.trim="password1" @input="checkPassword1">
              <label for="floatingPassword1">Password / 비밀번호</label>
              <div v-if="!isValidPassword1" class="input-error text-danger">
                영문,숫자,특수문자를 조합하여 입력해주세요.
              </div>
            </div>
            <div class="form-floating mb-3">
              <input type="password" :class="{'form-control':true, 'is-invalid': !isValidPassword2}" id="floatingPassword2" placeholder="Password" required v-model.trim="password2" @input="checkPassword2">
              <label for="floatingPassword2">Password Check / 비밀번호 확인</label>
              <div v-if="!isValidPassword2" class="input-error text-danger">
                비밀번호를 정확히 입력해주세요.
              </div>
            </div>
            <input class="form-control" type="submit" value="회원가입" data-bs-toggle="modal" data-bs-target="#SelectFirstMovieModal" @click="getPopularMovies">
          </div>
        </form>
      </div>
    </form>
    <!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#SelectFirstMovieModal" @click="getPopularMovies">
      Launch demo modal
    </button> -->
    <!-- Modal -->
    <div class="modal fade" id="SelectFirstMovieModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Select First Movie</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <FirstMovie
              v-for= "movie in popularRecommend" :key="movie.id"
              :movie="movie"
              @select-movie="selectMovie"
            />
            선택 영화 목록 : {{ selectedMoviesId }}
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="baseRating">Movie Rating</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FirstMovie from '@/components/FirstMovie.vue'
import axios from 'axios'
export default {
  name: 'SignupView',
  components: {
    FirstMovie,
  },
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      isValidUsername: true,
      // 올바른 비밀번호 입력 여부 확인
      isValidPassword1: false,
      // 확인용 비밀번호 일치 여부 확인
      isValidPassword2: false,
      selectedMoviesId: [],
      key: null,
    }
  },
  computed: {
    popularRecommend() {
      return this.$store.state.popularRecommend
    },
  },
  methods: {
    isValid() {
      if (this.username === null || this.username ==="") {
        this.isValidUsername = false
      } else {
        this.isValidUsername = true
      }
    },
    checkPassword1() {
      // 비밀번호 형식 검사(영문, 숫자, 특수문자)
      const validatePassword = /^(?=.*[a-zA-z])(?=.*[0-9])(?=.*[$`~!@$!%*#^?&\\(\\)\-_=+]).{8,16}$/
      if (!validatePassword.test(this.password1) || !this.password1) {
        this.isValidPassword1 = false
        return
      } else {
        this.isValidPassword1 = true
      }
    },
    checkPassword2() {
      if (this.password1 === this.password2) {
        this.isValidPassword2 = true
      } else {
        this.isValidPassword2 = false
      }
    },
    signUp() {
      this.isValid()
      if (this.isValidUsername || this.isValidPassword1 || this.isValidPassword2) {
        const username = this.username
        const password1 = this.password1
        const password2 = this.password2
        const payload = {
          username, password1, password2
        }
        this.$store.dispatch('signUp', payload)
      } else {
        console.log('no')
      }
    },
    getPopularMovies() {
      this.$store.dispatch('getPopularMovies')
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
      // console.log(String(year+'-'+month+'-'+date))
      // console.log(today)
      // console.log(API_KEY)
      this.$store.dispatch('getArticleList')
      for (let id of this.selectedMoviesId) {
        // console.log(id)
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
            console.log('됨ㅋ')
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
                // this.$store.dispatch('getArticleList')
                this.$router.push('home')
              })
              .catch((error) => {
                console.log(error)
              })
          })
          .catch((error) => {
            console.log(error)
            console.log(error.response.data)
            console.log(error.response.status)
            console.log(error.response.headers)
          })
      }
    }
  }
}
</script>

<style>
.signup-class {
    width:550px;
    
    margin-left:auto;
    margin-right:auto;
    
    margin-top:18vh;
    margin-bottom:auto;

}
.input-error {
    line-height: 16px;
    font-size: 11px;
    text-align: start;
  }
</style>