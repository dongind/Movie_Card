import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token') || "",
    userRecommend: [],
    latestRecommend: [],
    popularRecommend: [],
    articles: [],
  },
  getters: {
    isLoggedIn(state) {
      if (state.token) {
        return true
      } else {
        return false
      }
    },
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      localStorage.setItem("token", token)
    },
    LOG_OUT(state) {
      state.token = null
      localStorage.setItem("token", null)
    },
    GET_MY_MOVIES(state, movies) {
      state.userRecommend = movies 
    },
    GET_LATEST_MOVIES(state, movies) {
      state.latestRecommend = movies
    },
    GET_POPULAR_MOVIES(state, movies) {
      state.popularRecommend = movies
    },
    GET_ARTICLE_LIST(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    // 회원가입
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      
      axios({
        method: 'post',
        url : `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((response) => {
          // 회원가입이 성공하면 Home으로 이동 => 추후 아이템 선택창으로 이동
          context.commit('SAVE_TOKEN', response.data.key)
          router.push({ name: "home"})
        })
        .catch((error) => {
          console.log(error)
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`
      })
        .then(() => {
          context.commit("LOG_OUT")
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getMyMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v2/movies/recommend/user/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((response) => {
          context.commit("GET_MY_MOVIES", response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getLatestMovies(context){
      // console.log(data, TMDB_URL)
      axios({
        method: 'get',
        url:'http://127.0.0.1:8000/api/v2/movies/latest/',
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('GET_LATEST_MOVIES', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getPopularMovies(context){
      // console.log(data, TMDB_URL)
      axios({
        method: 'get',
        url:'http://127.0.0.1:8000/api/v2/movies/popular/',
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          context.commit('GET_POPULAR_MOVIES', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getArticleList(context){
      axios({
        method: 'get',
        url:'http://127.0.0.1:8000/api/v1/cards/',
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
          context.commit('GET_ARTICLE_LIST', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getArticleMyList(context){
      axios({
        method: 'get',
        url:'http://127.0.0.1:8000/api/v1/cards/my/',
        headers: {
          'Authorization': `Token ${context.state.token}`
        }
      })
        .then((response) => {
          console.log(response)
          context.commit('GET_ARTICLE_LIST', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  modules: {
  }
})
