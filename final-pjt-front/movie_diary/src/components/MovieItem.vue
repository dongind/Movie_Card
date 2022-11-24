<template>
  <div>
    <div class="movie-item" @click="newIsCreated" data-bs-toggle="modal" :data-bs-target="modalBtn1">
      <img :src="imgSrc" alt="" height="150px">
      <p>{{ movie.title }}</p>
    </div>   
    
    <!-- Modal -->
    <div class="modal fade movie-detail" :id="modalId1" aria-hidden="true" aria-labelledby="exampleModalToggleLabel" tabindex="-1">
      <div class="modal-dialog modal-dialog-scrollable modal-xl">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalToggleLabel">Movie Detail</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <!-- 카드 본문 -->
          <div class="modal-body" :id="modalBody">
            <p hidden id="scrollHeading1">#</p>
            <img :src="imgSrc" alt="Loading" height="500px">
            <h1>{{ movieTitle }}</h1>
            <p>영화 상영일 : {{ movieReleaseDate }}</p>
            <p>{{ movieOverview }}</p>
            <!-- detail 정보가 있는 경우 -->
            <div v-if="isdetail">
              <span>장르 : </span>
              <span v-for="genre in detailMovie.genres" :key="genre.id">{{ genre.name }} </span>
              <hr>
              <h5>다른 사람의 Card</h5>
                <p>
                  안녕
                  <CardItem
                    v-for="card in cardItems" :key="card.pk"
                    :card="card"
                    @get-card-item="getCardItem"
                  />
                </p>
              <h5>비슷한 영화</h5>
              <SimilarMovieItem v-for="similarMovie in similarMovies" :key="similarMovie.pk" :similarMovie="similarMovie" @get-similar-movie="getSimilarMovie"/>
            </div>
            <!-- detail 정보가 없는 경우 -->
            <div v-if="!isdetail">
              <p>정보가 부족합니다.</p>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button class="btn btn-primary" :data-bs-target="modalBtn2" data-bs-toggle="modal">Movie Card 만들기</button>
          </div>
        </div>
      </div>
    </div>
    <!-- 두번째 Modal -->
    <div class="modal fade" :id="modalId2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
      <div class="modal-dialog modal-dialog-scrollable modal-dialog-centered modal-xl">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalToggleLabel2">Movie Card 작성</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body" id="modal-body" v-if="!isCreated">
            <!-- 영화 정보 -->
            <!-- <img :src="imgSrc" alt="Loading" height="300px">
            <h2>{{ movieTitle }}</h2> -->
            <!-- Movie Card Form -->
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
          <div class="modal-footer" v-if="!isCreated">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button class="btn btn-primary" :data-bs-target="modalBtn1" data-bs-toggle="modal">Back to first</button>
            <button class="btn btn-primary" @click="createArticle" :data-bs-toggle="{'modal': false}">Submit form</button>
          </div>
          <div class="modal-body" id="modal-body" v-if="isCreated">
            <p>성공적으로 생성되었습니다.</p>
          </div>
          <div class="modal-footer" id="modal-footer" v-if="isCreated">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import $ from 'jquery'
import CardItem from '@/components/CardItem.vue'
import SimilarMovieItem from '@/components/SimilarMovieItem.vue'
export default {
  name: "MovieItem",
  components: {
    SimilarMovieItem,
    CardItem
  },
  props:{
    movie:Object,
    type:String,
  },
  data() {
    return {
      detailMovie: null,
      plannedAt: null,
      content: null,
      rate: null,
      isWrongDate: false,
      isWrongContent: false,
      isWrongRate: false,
      isSelected: [false, false, false, false, false],
      movieTitle: this.movie.title,
      movieReleaseDate: this.movie.release_date,
      movieOverview: this.movie.overview,
      moviePosterPath: this.movie.poster_path,
      movieId: this.movie.id,
      cardItems: this.movie?.card_set,
      datax: null,
      isCreated: false,
    }
  },
  computed: {
    planWord() {
      if (this.isWatched) {
        return '영화 감상일'
      } else {
        return '영화 감상 계획일'
      }
    },
    isdetail() {
      if (this.detailMovie === null) {
        return false
      } else {
        return true
      }
    },
    similarMovies() {
      const movie1 = {
        pk: this.detailMovie.similar_set[0].similar1_idx,
        title: this.detailMovie.similar_set[0].similar1_title,
        poster_path: this.detailMovie.similar_set[0].similar1_poster_path,
      }
      const movie2 = {
        pk: this.detailMovie.similar_set[0].similar2_idx,
        title: this.detailMovie.similar_set[0].similar2_title,
        poster_path: this.detailMovie.similar_set[0].similar2_poster_path,
      }
      const movie3 = {
        pk: this.detailMovie.similar_set[0].similar3_idx,
        title: this.detailMovie.similar_set[0].similar3_title,
        poster_path: this.detailMovie.similar_set[0].similar3_poster_path,
      }
      const movie4 = {
        pk: this.detailMovie.similar_set[0].similar4_idx,
        title: this.detailMovie.similar_set[0].similar4_title,
        poster_path: this.detailMovie.similar_set[0].similar4_poster_path,
      }
      const movie5 = {
        pk: this.detailMovie.similar_set[0].similar5_idx,
        title: this.detailMovie.similar_set[0].similar5_title,
        poster_path: this.detailMovie.similar_set[0].similar5_poster_path,
      }
      return [movie1, movie2, movie3, movie4, movie5]
    },
    modalBtn1() {
      return `#modalFirst${this.movie.id}`
    },
    modalId1() {
      return `modalFirst${this.movie.id}`
    },
    modalBtn2() {
      return `#modalSecond${this.movie.id}`
    },
    modalId2() {
      return `modalSecond${this.movie.id}`
    },
    imgSrc() {
      return `https://image.tmdb.org/t/p/original${this.moviePosterPath}`
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
      return `rate1-${this.movie.id}`
    },
    radioId2() {
      return `rate2-${this.movie.id}`
    },
    radioId3() {
      return `rate3-${this.movie.id}`
    },
    radioId4() {
      return `rate4-${this.movie.id}`
    },
    radioId5() {
      return `rate5-${this.movie.id}`
    },
    modalBody() {
      return `modalbody-${this.movie.id}`
    }
  },
  methods: {
    getMovieDetail() {
      // console.log(this.movie)
      const movieId = this.movie.id
      // console.log(movieId)
      const API_KEY = `Token ${this.$store.state.token}`
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v2/movies/${movieId}/`,
        headers: {'Authorization': API_KEY}
      })
        .then((response) => {
          this.detailMovie = response.data
        })
        .catch(() => {
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
    createArticle() {
      const API_URL = 'http://127.0.0.1:8000/api/v1/cards/'
      const API_KEY = `Token ${this.$store.state.token}`
      this.isValidated()
      if (!this.isWatched) {
        if (this.isWrongDate) {
          return
        } else {
          // axios 연결 => card 제작 요청
          axios({
            method: 'post',
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
              console.log('되나?')
              this.$store.dispatch('getArticleList')
              this.isCreated = true
            })
            .catch((error) => {
              console.log(error)
            })
        }
      } else {
        if (this.isWrongContent === true || this.isWrongDate === true || this.isWrongRate === true) {
          console.log(this.isWrongDate, this.isWrongContent, this.isWrongRate)
        } else {
          // axios 연결 => card 제작 요청
          axios({
            method: 'post',
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
              // axios 연결 => rate 기록 요청
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
                this.isCreated = true
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
    getSimilarMovie(movieId) {
      // console.log(this.movie)
      const API_KEY = this.$store.state.token
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v2/movies/${movieId}/`,
        headers: {'Authorization': API_KEY},
      })
        .then((response) => {
          this.movieTitle = response.data.title
          this.movieOverview = response.data.overview
          this.movieReleaseDate = response.data.release_date
          this.moviePosterPath = response.data.poster_path
          this.movieId = response.data.id
          this.detailMovie = response.data
          $(`#${this.modalBody}`).scrollTop(0)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    newIsCreated() {
      this.isCreated = false
    },
    getCardItem() {

    }
  },
  created() {
    this.getMovieDetail()
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

@import url('https://cdn.rawgit.com/moonspam/NanumSquare/master/nanumsquare.css');

.movie-item {
  display: flex;
  flex-direction: row;
}

.movie-detail {
  color: black;
}

</style>