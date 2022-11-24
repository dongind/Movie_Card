<template>
  <div>
    <div class="card shadow-card"
      data-bs-toggle="modal" :data-bs-target="modalBtn1" @click="newIsUpdated"
      :style="{ backgroundImage: 'linear-gradient(30deg, rgba(0, 0, 0, 1)0%, rgba(0, 0, 0, 0.8)30%, rgba(0, 0, 0, 0.3)70% ),url(' + this.imgSrc + ')'}">
      <p>{{ movieTitle }}</p>
      <div>
        <span class="star">★ </span>
        <span> {{ rate }}</span>
      </div>
    </div>
    
    <!-- <div class="col">
      <div class="card" data-bs-toggle="modal" :data-bs-target="modalBtn1" @click="newIsUpdated">
        <img :src="imgSrc" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-title">{{ movieTitle }}</p>
          <p class="card-text">{{ rate }}</p>
        </div>
        <div class="card-footer text-muted">{{ plannedAt }}</div>
      </div>
    </div> -->

    <!-- Modal -->
    <!-- 첫번째 모달 : Movie Detail -->
    <div class="modal fade" :id="modalId1" aria-hidden="true" aria-labelledby="exampleModalToggleLabel" tabindex="-1">
      <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content">
          <!-- <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalToggleLabel">Movie Card</h1>
          </div> -->
          <div class="modal-body p-0">
            <div class="modal-container">
              <img :src="imgSrc" alt="" height="750px">
              <div class="content" width="400px">
                <div class="content-position my-3">
                  <span class="mx-3 my-3"  style="text-align: start; font-weight:bold;"> 관람 계획 일자 :</span>
                  <span>{{ article.planned_at }} </span>
                  <div v-if="article.is_watched">
                    <div class="mx-3" style="text-align: start">
                      <div>
                        <span style="font-weight:bold;"> 평점 : </span>
                        <span>{{ rate }}</span>
                      </div>
                      <p class="my-3"> {{ article.content }}</p>
                    </div>
                </div>
                </div>
                <div class="btn-position">
                  <button type="button" class="btn btn-secondary text-white me-3" data-bs-dismiss="modal">Close</button>
                  <button class="btn btn-primary" :data-bs-target="modalBtn2" data-bs-toggle="modal">Update</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 두번째 모달 : Movie Update / Delete -->
    <div class="modal fade" :id="modalId2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalToggleLabel2">Card Update</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body" v-if="!isUpdated">
            
            <div class="form-control" novalidate>
              <div class="mb-3">
                <label class="form-label" for="plannedAt" required>{{ planWord }}</label><br>
                <input type="date" v-model="plannedAt" id="plannedAt" :class="{'form-control': true, 'is-invalid': isWrongDate}">
                <div class="invalid-feedback">
                  계획 일자를 작성하시오
                </div>
              </div>
              <!-- 만일 이전에 본 작품이라면 -->
              <div v-if="isWatched">
                <div class="mb-3">
                  <label for="validationTextarea" class="form-label">영화 감상평</label>
                  <textarea :class="{'form-control': true, 'is-invalid': isWrongContent}" id="validationTextarea" placeholder="감상평을 작성해주세요" v-model="content" required></textarea>
                  <div class="invalid-feedback">
                    영화 감상평을 작성하시오
                  </div>
                </div>
                <div class="mb-3">
                  <label for="validationRate" :class="{'form-label':true, 'text-danger': isWrongRate}">영화 평점</label>
                  <div id="myform">
                    <fieldset>
                      <input type="radio" name="reviewStar" value="5" :id="radioId1" @click="getRate" :checked="isSelected[4]"><label
                        :for="radioId1">★</label>
                      <input type="radio" name="reviewStar" value="4" :id="radioId2" @click="getRate" :checked="isSelected[3]"><label
                        :for="radioId2">★</label>
                      <input type="radio" name="reviewStar" value="3" :id="radioId3" @click="getRate" :checked="isSelected[2]"><label
                        :for="radioId3">★</label>
                      <input type="radio" name="reviewStar" value="2" :id="radioId4" @click="getRate" :checked="isSelected[1]"><label
                        :for="radioId4">★</label>
                      <input type="radio" name="reviewStar" value="1" :id="radioId5" @click="getRate" :checked="isSelected[0]"><label
                        :for="radioId5">★</label>
                    </fieldset>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer" v-if="!isUpdated">
            <button type="button" class="btn btn-secondary text-white" data-bs-dismiss="modal">Close</button>
            <button class="btn btn-danger text-white" @click="deleteArticle" data-bs-dismiss="modal">Delete</button>
            <button class="btn btn-primary" :data-bs-target="modalBtn1" data-bs-toggle="modal">Back to Card</button>
            <button class="btn btn-primary" :data-bs-dismiss="{'modal': false}" @click="updateArticle">Update</button>
          </div>
          <div class="modal-body" id="modal-body" v-if="isUpdated">
            <p>성공적으로 수정되었습니다.</p>
          </div>
          <div class="modal-footer" id="modal-footer" v-if="isUpdated">
            <button type="button" class="btn btn-secondary text-white" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  data() {
    return {
      detailCard: null,
      detailCardId: null,
      movieTitle: this.article.movie.title,
      plannedAt: this.article.planned_at,
      content: this.article.content,
      modalImgSrc: null,
      detailCardRate: null,
      rate: null,
      isWrongDate: false,
      isWrongContent: false,
      isWrongRate: false,
      isSelected: [false, false, false, false, false],
      movieId: this.article.movie.pk,
      isUpdated: false
    }
  },
  computed: {
    imgSrc() {
      return `https://image.tmdb.org/t/p/original${this.article.movie.poster_path}`
    },
    modalId1() {
      return `modalId1-${this.article.id}`
    },
    modalId2() {
      return `modalId2-${this.article.id}`
    },
    modalBtn1() {
      return `#modalId1-${this.article.id}`
    },
    modalBtn2() {
      return `#modalId2-${this.article.id}`
    },
    planWord() {
      if (this.isWatched) {
        return '영화 감상일'
      } else {
        return '영화 감상 계획일'
      }
    },
    nowDate() {
      return new Date()
    },
    isWatched() {
      const plannedAt = new Date(this.plannedAt)
      if (this.plannedAt === null) {
        return false
      } else if (plannedAt < this.nowDate) {
        return true
      } else {
        return false
      }
    },
    radioId1() {
      return `rate1-${this.article.id}`
    },
    radioId2() {
      return `rate2-${this.article.id}`
    },
    radioId3() {
      return `rate3-${this.article.id}`
    },
    radioId4() {
      return `rate4-${this.article.id}`
    },
    radioId5() {
      return `rate5-${this.article.id}`
    },
  },
  methods:{
    getMovieRate() {
      const rates = this.article.movie.rate_set
      rates.forEach((rate) => {
        if (rate.user === this.article.user) {
          this.rate = rate.rate
          this.isSelected[Number(this.rate) - 1] = true
        }
      })
    },
    isValidated() {
      if (this.plannedAt === null) {
        this.isWrongDate = true
      } else {
        this.isWrongDate = false
      }
      if (this.content === null) {
        this.isWrongContent = true
      } else {
        this.isWrongContent = false
      }
      if (this.rate === null) {
        this.isWrongRate = true
      } else {
        this.isWrongRate = false
      }
    },
    getRate(event) {
      const value = Number(event.target.value)
      this.rate = value
      for (const i in this.isSelected) {
        if (Number(i) + 1 === value) {
          this.isSelected[i] = true 
        } else {
          this.isSelected[i] = false
        }
      }
    },
    updateArticle() {
      const API_URL = `http://127.0.0.1:8000/api/v1/cards/${this.article.id}/`
      const API_KEY = `Token ${this.$store.state.token}`
      this.isValidated()
      if (!this.isWatched) {
        if (this.isWrongDate) {
          return
        } else {
          // axios 연결 => card 제작 요청
          axios({
            method: 'put',
            url: API_URL,
            headers: {'Authorization': API_KEY},
            data: {
            'movie': this.movieId,
            'content': null,
            'planned_at': this.plannedAt,
            'is_watched': false,
            },
          })
            .then(() =>{
              this.$store.dispatch('getArticleList')
              this.isUpdated = true
            })
            .catch((error) => {
              console.log(error)
            })
        }
      } else {
        if (this.isWrongContent === true || this.isWrongDate === true || this.isWrongRate === true) {
          // console.log(this.isWrongDate, this.isWrongContent, this.isWrongRate)
        } else {
          // axios 연결 => card 제작 요청
          axios({
            method: 'put',
            url: API_URL,
            headers: {'Authorization': API_KEY},
            data: {
            'movie': this.movieId,
            'content': this.content,
            'planned_at': this.plannedAt,
            'is_watched': true,
            },
          })
            .then(() =>{
              // axios 연결 => rate 기록 요청 => 이 때 rate가 있는지 없는지 확인!
              if (this.article.movie.rate_set.length === 0) {
                axios({
                  method: 'post',
                  url: 'http://127.0.0.1:8000/api/v2/movies/rate/',
                  headers: {'Authorization': API_KEY},
                  data: {
                    'movie_pk': this.movieId,
                    'rate': this.rate
                  },
                })
                .then(() => {
                  this.$store.dispatch('getArticleList')
                  this.isUpdated = true
                })
                .catch((error) => {
                  console.log(error)
                })
              } else {
                axios({
                  method: 'put',
                  url: 'http://127.0.0.1:8000/api/v2/movies/rate/',
                  headers: {'Authorization': API_KEY},
                  data: {
                    'movie_pk': this.movieId,
                    'rate': this.rate
                  },
                })
                .then(() => {
                  this.$store.dispatch('getArticleList')
                  this.isUpdated = true
                })
                .catch((error) => {
                  console.log(error)
                })
              }
            })
            .catch((error) => {
              console.log(error)
            })
        }
      }
    },
    deleteArticle() {
      const API_URL = `http://127.0.0.1:8000/api/v1/cards/${this.article.id}/`
      const API_KEY = `Token ${this.$store.state.token}`
      const is_rated = this.article.movie.rate_set.length
      axios({
            method: 'delete',
            url: API_URL,
            headers: {'Authorization': API_KEY},
      })
        .then(() => {
          if (is_rated) {
            axios({
              method: 'delete',
              url: 'http://127.0.0.1:8000/api/v2/movies/rate/',
              headers: {'Authorization': API_KEY},
              data: {
                'movie_pk': this.movieId,
              }
            })
              .then(() => {
                // console.log(response)
              })
              .catch((error) => {
                console.log(error)
              })
          }

          this.$store.dispatch('getArticleList')
        })
        .catch((error) => {
          console.log(error)
        })
    },
    newIsUpdated() {
      this.isUpdated = false
    }
  },
  created() {
    this.getMovieRate()
  }
}
</script>

<style>

#myform fieldset{
    display: inline-block;
    direction: rtl;
    border:0;
}
#myform fieldset legend{
    text-align: right;
}
#myform input[type=radio]{
    display: none;
}
#myform label{
    font-size: 3em;
    color: transparent;
    text-shadow: 0 0 0 #f0f0f0;
}
#myform label:hover{
    text-shadow: 0 0 0 rgba(250, 208, 0, 0.99);
}
#myform label:hover ~ label{
    text-shadow: 0 0 0 rgba(250, 208, 0, 0.99);
}
#myform input[type=radio]:checked ~ label{
    text-shadow: 0 0 0 rgba(250, 208, 0, 0.99);
}

.card {
  width: 170px;
  height: 240px;
  background-size: cover;
  box-shadow: 5px;
  border: none;
  color: white;
  display: flex;
  flex-direction: column-reverse;
  margin-top: 20px;
  transition: all 0.5s;
  cursor:pointer;
}
.card:hover {
  transform: scale(1.1)
}

.card p {
  padding-left: 10px;
  padding-right: 5px;
  font-size: 20px;
  margin-bottom: 5px;
}

.star {
  padding-left: 10px;
  color: rgba(250, 208, 0, 0.99);
}

.modal-container {
  display: flex;
  flex-direction: row;
}

.modal-container img {
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
}

.shadow-card{
    -webkit-box-shadow: 27px 43px 43px -26px rgba(17, 17, 17, 0.39);
    -moz-box-shadow: 30px 30px 43px -26px rgba(8, 8, 8, 1);
    box-shadow: 20px 20px 20px -26px rgb(0, 0, 0);
}

.content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.btn-position {
  display: flex;
  justify-content: right;
  margin-bottom: 10px;
  margin-left: 90px;
}

</style>