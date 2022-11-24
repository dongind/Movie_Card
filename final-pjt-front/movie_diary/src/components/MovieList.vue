<template>
  <div>
    <div class="movie-container">
      <div class="movies">
        <div v-if="isUserRecommend" class="movie-list" style="padding-top:10px;">
          <MovieItem
          v-for="movie in userRecommend" :key="movie.id"
          :movie="movie"
          type="userRecommend"
          />
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
          <p>사용자 추천 </p> 
        </div>
        <div @click="switchLatestRecommend" :class="{'selection': true, 'selected': isLatestRecommend}">
          <p>최신 영화  </p> 
        </div>
        <div @click="switchPopularRecommend" :class="{'selection': true, 'selected': isPopularRecommend}">
          <p>인기 영화  </p> 
        </div>
        <div data-bs-toggle="modal" data-bs-target="#genreModal" :class="{'selection': true, 'selected': isGenreRecommend}">
          <p>장르별 영화 </p>
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
            <div>
              <span
              v-for="genre of genres" :key="genre"
              >
                <button data-bs-dismiss="modal" @click="getGenreMovies(genre)">{{ genre }}</button>
              </span>

            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
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
  background-color: black;
  border-bottom-right-radius: 20px;
}

.selection {
  padding-top: 15px;
  padding-bottom: 10px;
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
</style>