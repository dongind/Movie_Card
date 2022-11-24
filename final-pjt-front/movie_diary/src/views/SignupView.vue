<template>
  <div class="page-container">
    <form @submit.prevent="signUp">
      <div class="container">
        <div class="login-form-container shadow">
          <div class="login-form-right-side">
            <div class="top-logo-wrap">
            </div>
            <h1>Movie Card</h1>
            <h5>Remember the movie with</h5>
            <p>We all like movies, but often miss movies in our busy life. Let's plan, record and read the film for those of us with Movie Card</p>
          </div>
          <div class="login-form-left-side">
            <div class="login-top-wrap">
              <span>Login Page</span>
              <router-link class="btn" :to="{'name': 'login'}">
                <button class="create-account-btn shadow-light">
                  Log In
                </button>
              </router-link>
            </div>
            <div class="login-input-container">

              <form class="needs-validation" novalidate @submit.prevent="signUp">
                <div class="signup-class">
                  <div class="form-floating mb-3" style="font-family:nanumsquare">
                    <input type="email" :class="{'form-control':true, 'is-invalid': !isValidUsername}" id="floatingInput" placeholder="name" required v-model.trim="username">
                    <label for="floatingInput" style="font-family:nanumsquare">Username / 아이디</label>
                    <div v-if="!isValidUsername" class="input-error text-danger">
                      Username을 입력해주세요.
                    </div>
                  </div>  
                  <div class="form-floating mb-3">
                    <input type="password" :class="{'form-control':true, 'is-invalid': !isValidPassword1}" id="floatingPassword1" placeholder="Password" required v-model.trim="password1" @input="checkPassword1">
                    <label for="floatingPassword1" style="font-family:nanumsquare">Password / 비밀번호</label>
                    <div v-if="!isValidPassword1" class="input-error text-danger">
                      영문,숫자,특수문자를 조합하여 입력해주세요.
                    </div>
                  </div>
                  <div class="form-floating mb-3">
                    <input type="password" :class="{'form-control':true, 'is-invalid': !isValidPassword2}" id="floatingPassword2" placeholder="Password" required v-model.trim="password2" @input="checkPassword2">
                    <label for="floatingPassword2" style="font-family:nanumsquare">Password Check / 비밀번호 확인</label>
                    <div v-if="!isValidPassword2" class="input-error text-danger">
                      비밀번호를 정확히 입력해주세요.
                    </div>
                  </div>
                  <input style="background-color:black; color:white;font-family: nanumsquare;" class="form-control" type="submit" value="회원가입">
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  components: {},
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
      key: null,
    }
  },
  computed: {},
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
  }
}
</script>

<style>
/* .signup-class {
    width:550px;
} */
.input-error {
    line-height: 16px;
    font-size: 11px;
    text-align: start;
    font-family:nanumsquare;
  }

  *{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
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
.login-form-right-side{
    width: 50%; 
    border-radius: 10px 0px 0px 10px;
    padding:75px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: rgb(0, 0, 0);
    /* background-image: ; */
}
.login-form-right-side h1{
    color: rgb(0, 0, 0);
    width:100%;
    text-align: right;
    opacity: 0.9;

}
.login-form-right-side h5{
    color: rgb(0, 0, 0);
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
background: linear-gradient(287deg, rgba(255,255,255,1) 0%, rgba(243,244,244,1) 0%, rgba(255,255,255,1) 100%);
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
    padding-top:80px;
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