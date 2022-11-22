<template>
  <div class="container">
    <form class="needs-validation" novalidate @submit.prevent="logIn">
      <div class="login-class">
        <h1 class="mb-5">Login Page</h1>
        <div class="form-floating mb-3">
          <input type="email" :class="{'form-control':true, 'is-invalid': isValidUsername}" id="floatingInput" placeholder="name" required v-model.trim="username">
          <label for="floatingInput">Username / 아이디</label>
          <div v-if="isValidUsername" class="input-error text-danger">
            Please enter username.
          </div>
        </div>  
        <div class="form-floating mb-3">
          <input type="password" :class="{'form-control':true, 'is-invalid': isValidPassword}" id="floatingPassword" placeholder="Password" required v-model.trim="password">
          <label for="floatingPassword">Password / 비밀번호</label>
          <div v-if="isValidPassword" class="input-error text-danger">
            Please enter a password.
          </div>
        </div>
        <div v-if="isWrongLogin" :class="{ 'text-danger': isWrongLogin }">
          아이디 or 비밀번호가 잘못되었습니다.
        </div>
        <input class="form-control" type="submit" value="로그인">
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
      isValidUsername: false,
      isValidPassword: false,
      isWrongLogin: false,
    }
  },
  methods: {
    isValid() {
      if (this.username === null || this.username ==="") {
        this.isValidUsername = true
      } else {
        this.isValidUsername = false
      }
      if (this.password === null || this.password ==="") {
        this.isValidPassword = true
      } else {
        this.isValidPassword = false
      }
    },
    logIn() {
      this.isValid()
      this.isWrongLogin = false
      const username = this.username
      const password = this.password

      if (this.isValidPassword || this.isValidUsername) {
        return
      } else {
        const API_URL = 'http://127.0.0.1:8000'
        axios({
          method:'post',
          url: `${API_URL}/accounts/login/`,
          data: {
          username, password
          }
        })
          .then((response) => {
            this.$store.commit('SAVE_TOKEN', response.data.key)
          })
          .then(() => {
            this.$router.push({name: 'home'})
          })
          .catch((error) => {
            console.log(error)
            this.isWrongLogin = true
          })
      }
    }
  },
}
</script>

<style>
.login-class {
    width:550px;
    
    margin-left:auto;
    margin-right:auto;
    
    margin-top:18vh;
    margin-bottom:auto;

}

</style>