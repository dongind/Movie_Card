import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import ProfileView from '@/views/ProfileView'
import LoginView from '@/views/LoginView'
import LogoutView from '@/views/LogoutView'
import SignupView from '@/views/SignupView'

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
  },
  {
    path: '/account/signup/',
    name: 'signup',
    component: SignupView,
  },

  // {
  //   path: '/account/signup/',
  //   name: 'signup',
  //   component: SignupView,
  // },
  // {
  //   path: '/account/signup/',
  //   name: 'signup',
  //   component: SignupView,
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
