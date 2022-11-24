<template>
  <div class="page-container">
    <div class="login-form-container shadow">
      <div class="login-form-right-side-login">
        <div class="top-logo-wrap">
        </div>
        <h1 style="color:white">Movie Card</h1>
        <h5 style="color:white">Remember the movie with</h5>
        <p style="color:white">We all like movies, but often miss movies in our busy life. Let's plan, record and read the film for those of us with Movie Card</p>
      </div>
      <div class="login-form-left-side">
        <div class="login-top-wrap">
          <span>Don't have an account?</span>
          <router-link class="btn" :to="{'name': 'signup'}">
            <button class="create-account-btn shadow-light">
              Create Profile
            </button>
          </router-link> 
        </div>
        <div class="login-input-container">
  
          <form class="needs-validation " novalidate @submit.prevent="logIn">
            <div class="login-form">
              <div class="form-floating mb-3" style="font-family:nanumsquare">
                <input type="email" :class="{'form-control':true, 'is-invalid': isValidUsername}" id="floatingInput" placeholder="name" required v-model.trim="username">
                <label for="floatingInput" style="font-family:nanumsquare">Username</label>
                <div v-if="isValidUsername"  class="input-error text-danger">
                  Please enter username.
                </div>
              </div>  
              <div class="form-floating mb-3">
                <input type="password" :class="{'form-control':true, 'is-invalid': isValidPassword}" id="floatingPassword" placeholder="Password" required v-model.trim="password">
                <label for="floatingPassword" style="font-family:nanumsquare">Password</label>
                <div v-if="isValidPassword" class="input-error text-danger">
                  Please enter a password.
                </div>
              </div>
              <div v-if="isWrongLogin" :class="{ 'text-danger': isWrongLogin }">
                아이디 or 비밀번호가 잘못되었습니다.
              </div>
              <input class="form-control" type="submit" value="로그인" style="background-color:black; color:white">
            </div>
          </form>
      </div>

      </div>

    </div>
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
.input-error {
    line-height: 16px;
    font-size: 11px;
    text-align: start;
  }

*{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

@font-face {
    font-family: 'Jeju';
    src: url('https:////fonts.googleapis.com/earlyaccess/jejumyeongjo.css') format('woff');
    font-weight: normal;
    font-style: normal;
}
@font-face {
    font-family: 'MapoFlowerIsland';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoFlowerIslandA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@import url('https://cdn.rawgit.com/moonspam/NanumSquare/master/nanumsquare.css');

.page-container{
    width: 100vw;
    height: 100vh;
    background: #eff0f2;
    display: flex;
    justify-content: center;
    align-items: center;

}
.login-form {
  font-family: nanumsquare;
}
.shadow{
    -webkit-box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
    -moz-box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
    box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
}/*
.shadow-light{
    -webkit-box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);
    -moz-box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);
    box-shadow: 45px 45px 104px -33px rgba(38,38,38,0.92);

}*/
.login-form-container{
 
    background:#f5f5f5 ;
    width:860px;
    height: 540px;
    display: flex;
    flex-direction: row;
    box-shadow: 10px black;
    border-radius: 10px;

}
.login-form-right-side-login{
    width: 50%; 
    border-radius: 10px 0px 0px 10px;
    padding:60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: rgb(0, 0, 0);
    background-image: linear-gradient(80deg, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.98)),url(@/assets/background1.png) ;
    width: 100%;
    background-size: cover;
}
.login-form-right-side h1{
    color: rgb(255, 255, 255);
    width:100%;
    text-align: right;
    opacity: 0.9;

}
.login-form-right-side h5{
    color: rgb(255, 255, 255);
    width:100%;
    text-align: right;
    opacity: 0.9;

}
.login-form-right-side p{
    padding-top: 50px;
    font-size:12px;
    text-align: right;
    opacity: 0.8;
}
.login-form-left-side{
    width: 50%;
    border-radius: 0px 10px 10px 0px;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding:40px;
    background: rgb(255,255,255);
    background: linear-gradient(287degrgb(94, 94, 94)10%, rgba(243,244,244,1) 0%, rgba(255,255,255,1) 100%);
}
.login-form-left-side .login-top-wrap{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    width:100%;
}
.login-form-left-side .login-top-wrap span{
    color: gray;
    font-size: 11px;
    padding-right:20px;
    font-family: nanumsqare;

}
.login-form-left-side .login-top-wrap .create-account-btn {
    background: rgb(10, 10, 10);
    border:  0;
    width:85px;
    height: 35px;
    font-size: 11px;
    color: #ffffff;
    border-radius: 3px;
    font-family: nanumsquare;

}
.login-input-container{
    padding-top:120px;
    width:300px;
}
.login-input-container .login-input-wrap{
    width:300px;
    height: 45px;
    margin-top: 20px;
    border-radius: 2px;
    border-bottom: solid 2px #2178ff;
   
}
.login-input-container .login-input-wrap i{
    color: #2178ff;
    line-height: 45px;
}

.login-input-container .login-input-wrap input{
    background: none;
   
    border: none;
    line-height: 45px;
    padding-left:10px;
    width:267px;
    font-family: 'Alata', sans-serif;
}
.login-input-container .login-input-wrap input:focus{
    outline: none;
}
.login-btn-wrap{
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    align-items: center;;
}
.login-btn-wrap .login-btn{
    width:95px;
    height:35px;
    color:white;
    border: 0;
    border-radius: 4px;

    background: rgb(105,163,255);
background: linear-gradient(162deg, rgba(105,163,255,1) 0%, rgba(43,125,254,1) 50%, rgba(43,125,254,1) 100%);
}
.login-btn-wrap a{
    margin-top:10px;
    text-decoration: none;
    font-size: 11px;
    color: gray;

}

</style>