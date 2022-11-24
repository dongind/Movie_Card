<template>
  <div>
    <div class="movie-container">
      <div class="movies">
        <div v-if="isUserRecommend" class="movie-list" style="padding-top:10px;">
          <div v-if="!isLoading">
            <!--loading-->
            <body>
              <div class="loading">
                <span></span>   <!--1. span은 하나의 원이다. -->
                <span></span>
                <span></span>
              </div>
            </body>
            <!--loading-->
          </div>
          <div v-if="isLoading">
            <MovieItem
            v-for="movie in userRecommend" :key="movie.id"
            :movie="movie"
            type="userRecommend"
            />
          </div>

        </div>
        <div v-if="isLatestRecommend" class="movie-list">
          <MovieItem
          v-for="movie in latestRecommend" :key="movie.id"
          :movie="movie"
          type="latestRecommend"
          />
        </div>
        <div v-if="isPopularRecommend" class="movie-list">
          <MovieItem
          v-for= "movie in popularRecommend" :key="movie.id"
          :movie="movie"
          type="popularRecommend"
          />
        </div>
        <div v-if="isGenreRecommend" class="movie-list">
          <MovieItem
          v-for= "movie in genreRecommend" :key="movie.id"
          :movie="movie"
          type="genreRecommend"
          />
        </div>
      </div>
      <div class="selection-list" >
        <div @click="switchUserRecommend" :class="{'selection': true, 'selected': isUserRecommend}">
          <p class="mb-0">사용자 추천 </p> 
        </div>
        <div @click="switchLatestRecommend" :class="{'selection': true, 'selected': isLatestRecommend}">
          <p class="mb-0">최신 영화  </p> 
        </div>
        <div @click="switchPopularRecommend" :class="{'selection': true, 'selected': isPopularRecommend}">
          <p class="mb-0">인기 영화  </p> 
        </div>
        <div data-bs-toggle="modal" data-bs-target="#genreModal" :class="{'selection': true, 'selected': isGenreRecommend}">
          <p class="mb-0">장르별 영화 </p>
        </div>
      </div>
    </div>


    <!-- Genre Modal -->

    <!-- Modal -->
    <div class="modal fade" id="genreModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-xl">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">장르 선택</h1>
            <button type="button"  class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-6 g-2 mx-auto">
              <span
              v-for="genre of genres" :key="genre"
              >
                <button data-bs-dismiss="modal" @click="getGenreMovies(genre)" class="btn btn-outline-dark">{{ genre }}</button>
              </span>
            </div>
            </div>
          </div>
        </div>
      </div>
    </div>

</template>

<script>
import MovieItem from '@/components/MovieItem.vue'
import axios from 'axios'
export default {
  name: 'MovieList',
  components: {
    MovieItem
  },
  data() {
    return {
      genreRecommend : [],
      isUserRecommend: true,
      isLatestRecommend: false,
      isPopularRecommend: false,
      isGenreRecommend: false,
      selectedGenre: null,
      genres: ["액션", "모험", "애니메이션", "코미디", "범죄", "다큐멘터리", "드라마", "가족", "판타지", "역사", "공포", "음악", "미스터리", "로맨스", "SF", "TV 영화", "스릴러", "서부"],
      genreId : {
        "액션": 28, "모험": 12, "애니메이션": 16, "코미디": 35, "범죄": 80, "다큐멘터리": 99, "드라마": 18, "가족": 10751, "판타지": 14, "역사": 36, "공포": 27, "음악": 10402, "미스터리": 9648, "로맨스": 10749, "SF": 878, "TV 영화": 10770, "스릴러": 53, "서부": 10752
      }
    }
  },
  computed: {
    userRecommend() {
      return this.$store.state.userRecommend
    },
    latestRecommend() {
      return this.$store.state.latestRecommend
    },
    popularRecommend() {
      return this.$store.state.popularRecommend
    },
    isLoading() {
      return this.$store.state.isLoading
    }
  },
  methods: {
    getMyMovies() {
      this.$store.dispatch('getMyMovies')
    },
    switchUserRecommend() {
      this.isUserRecommend = true
      this.isLatestRecommend = false
      this.isPopularRecommend = false
      this.isGenreRecommend = false
    },
    switchLatestRecommend() {
      this.isUserRecommend = false
      this.isLatestRecommend = true
      this.isPopularRecommend = false
      this.isGenreRecommend = false
    },
    switchPopularRecommend() {
      this.isUserRecommend = false
      this.isLatestRecommend = false
      this.isPopularRecommend = true
      this.isGenreRecommend = false
    },
    switchGenreRecommend() {
      this.isUserRecommend = false
      this.isLatestRecommend = false
      this.isPopularRecommend = false
      this.isGenreRecommend = true
    },
    getLatestMovies() {
      this.switchLatestRecommend()
      this.$store.dispatch('getLatestMovies')
    },
    getPopularMovies() {
      this.switchPopularRecommend()
      this.$store.dispatch('getPopularMovies')
    },
    getGenreMovies(genre) {
      const genreId = this.genreId[genre]
      const API_KEY = `Token ${this.$store.state.token}`

      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v2/movies/genre/${genreId}/`,
        headers: {'Authorization': API_KEY}
      })
        .then((response) => {
          this.genreRecommend = response.data
        })
        .then(() => {
          this.switchGenreRecommend()
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    this.getMyMovies()
    this.getLatestMovies()
    this.getPopularMovies()
    this.switchUserRecommend()
  }
}
</script>

<style>

.movie-container {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 100%;
}

.movies {
  padding: 10px;
  width: 60%;
  height: 80vh;
  overflow: auto;
}

.movie-list {
  display:flex;
  flex-direction: column;
  font-family: nanumsquare;
}

.selection-list {
  width: 40%;
  height: 83vh;
  color: white;
  background-color: rgb(28, 28, 31);
  border-bottom-right-radius: 20px;
}

.selection {
  padding-top: 15px;
  padding-bottom: 10px;
  transition: all 0.5s;
  cursor:pointer;
}
.selection:hover {
  background-color: rgb(224, 224, 224);
  color: black;
}

.selected {
  background-color: rgb(224, 224, 224);
  color: black;
}

.selection p {
  text-align:center;
  height: 30px;
  margin: 0;
}

.movies::-webkit-scrollbar {
    display: none;
    width: 8px;  /* 스크롤바의 너비 */
}

.movies::-webkit-scrollbar-thumb {
    height: 10px; /* 스크롤바의 길이 */
    background: #2f3542; /* 스크롤바의 색상 */
    
    /* border-radius: 10px; */
}

.movies::-webkit-scrollbar-track {
    background: rgb(85, 85, 85);  /*스크롤바 뒷 배경 색상*/
}

.movie-selection {
  display: flex;
  flex-direction: row;
  font-family:nanumsquare;
  text-align:center;
}

body {
    margin-top: 0px; 
    display: flex;            /*내부 요소들이 차례로 배치 */
    justify-content: center;  /*내부 요소의 좌우 정렬 상태를 가운데로 설정*/
    align-items: center;      /*요소는 세로 중앙 배치*/
    height: 100vh;            /*웹 크기 변화에 따라 변경되는 반응형 수치*/
    background-color: rgb(224, 224, 224);
  }

.loading span {
  display: inline-block; /* span 내부요소들을 한줄로 세우기 */
  width: 10px;
  height: 10px;
  background-color: gray;
  border-radius: 50%;    /* span을 동그랗게 */
  animation: loading 1s 0s linear infinite;
  /* 이벤트명  반복시간  딜레이시간  이벤트처리부드럽게  이벤트무한반복*/
}

.loading span:nth-child(1) {  /*loading의 자식 중 첫번째 span*/
  /*nth-child : 형제 사이에서의 순서*/
  animation-delay: 0s;
  background-color: red;
}

.loading span:nth-child(2) {
  animation-delay: 0.2s;
  background-color: orange;
}

.loading span:nth-child(3) {
  animation-delay: 0.4s;
  background-color: yellowgreen;
}

@keyframes loading {        /*loading이라는 keyframe 애니메이션*/
    0%,                      /* 0, 50, 100은 구간*/
    100% {
      opacity: 0;            /* 안보였다가 */
      transform: scale(0.5); /*transform의 scale로 요소를 확대 또는 축소할 수 있음*/   
    }
    50% {
      opacity: 1;             /* 보였다가 */
      transform: scale(1.2); /* 1.2배 */
    }
  }


</style>