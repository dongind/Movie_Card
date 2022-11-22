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
            <input class="form-control" type="submit" value="회원가입">
          </div>
        </form>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
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
    }
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