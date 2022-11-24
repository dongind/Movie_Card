import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import ProfileView from '@/views/ProfileView'
import LoginView from '@/views/LoginView'
import LogoutView from '@/views/LogoutView'
import SignupView from '@/views/SignupView'
import FirstMovieView from '@/views/FirstMovieView'
import store from '@/store/index.js'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/profile/',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/account/login/',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/account/logout/',
    name: 'logout',
    component: LogoutView,
    beforeEnter(to, from, next) {
      const isLoggedIn = store.getters.isLoggedIn
      console.log(isLoggedIn)
      if (isLoggedIn === true) {
        alert('로그아웃')
        next()
      } else {
        router.back()
      }
    },
  },
  {
    path: '/account/signup/',
    name: 'signup',
    component: SignupView,
  },
  {
    path: '/account/signup/firstmovie/',
    name: 'firstmovie',
    component: FirstMovieView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters.isLoggedIn
  const authPages = ['home', 'profile']
  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인 해주십시오')
    next({name: 'login'})
  } else {
    next()
  }
})

export default router
