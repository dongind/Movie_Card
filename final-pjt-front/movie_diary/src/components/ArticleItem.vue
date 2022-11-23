<template>
  <div>
    <div class="col">
      <div class="card">
        <!-- 구조 ㅄ 같으면, 다 지워도 됨요..ㅎㅎ ㅜ -->
        <!-- 이미지를 클릭할 경우, 이동하는 방식 -->
        <!-- click에 들어간 함수는, 
        순서대로 
        1. 클릭된 카드의 정보 가져오는 함수 : getCardDetail()
        2. 클릭된 카드의 이미지를 불러오기 위한 함수 : modalImgSrcSet()
        3. 클릭된 카드 중에서 현재 유저와 같은 id 값을 가지는 rate 값을 불러오는 함수 : rateLoad()
        -->
        <img :src="imgSrc" class="card-img-top" alt="..." data-bs-toggle="modal" data-bs-target="#cardModal" @click="[getCardDetail(), modalImgSrcSet(), rateLoad()]">
        <div class="card-body">
          <span class="date">{{ article.plannedAt }}</span>
          <h5 class="card-title">{{ movieTitle }}</h5>
          <p class="card-text">{{ article.content }}</p>
        </div>
        <div class="card-footer text-muted">{{ plannedAt }}</div>
      </div>
      <ArticleDetail/>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="cardModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Card Detail</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <!-- <img :src="imgSrc" class="card-img-top" alt="..."> -->
            <p>{{ this.detailCard?.movie.title }}</p>
            <!-- 시청 안했을 경우, 예정된 시청일을 보여줌 -->
            <div v-if="!this.detailCard?.is_watched">
              <p>시청예정일 : {{ this.detailCard?.planned_at }}</p>
            </div>
            <!-- 시청했을 경우, 하단의 watched change 버튼을 누르면 후기를 작성할 수 있도록 전환 -->
            <div v-if="this.detailCard?.is_watched">
              <p>봤구나!</p>
              <!-- <p v-for="set of this.detailCard?.movie.rate_set" :key="set.id">별점 : {{ set.id }}</p> -->
              <p>평점 : {{ this?.detailCardRate }}</p>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" v-if="!this.detailCard?.is_watched" @click="watchedChange">Watched change</button>
            <button type="button" class="btn btn-primary">Save changes</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleDetail from '@/components/ArticleDetail.vue'
export default {
  name: 'ArticleItem',
  components: {
    ArticleDetail
  },
  props: {
    article: Object,
  },
  data() {
    return {
      detailCard: null,
      detailCardId: null,
      movieTitle: this.article.movie.title,
      plannedAt: this.article.planned_at,
      modalImgSrc: null,
      detailCardRate: null,
    }
  },
  computed: {
    imgSrc() {
      return `https://image.tmdb.org/t/p/original${this.article.movie.poster_path}`
    }
  },
  methods:{
    // 클릭된 카드의 정보를 불러오는 메서드
    getCardDetail() {
      const cardId = this.article.id
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/cards/${cardId}/`,
      })
        .then((response) => {
          console.log(response.data)
          this.detailCardId = response.data.id
          console.log(this.detailCardId)
          // this.detailCard = response.data.filter(id=this.detailCardId)
          console.log(this.detailCard)
        })
        .catch(() => {
        })
    },
    // 클릭된 카드 모달 내에서 isWatched의 상태를 바꿔주는 메서드
    watchedChange() {
      this.detailCard.is_watched = !this.detailCard.is_watched
    },
    // 클릭된 카드의 영화 이미지를 따로 저장하는 메서드
    modalImgSrcSet() {
      // console.log(this.modalImgSrc)
      this.modalImgSrc = `https://image.tmdb.org/t/p/original${this.detailCard?.movie.poster_path}`
      // console.log(this.modalImgSrc)
    },
    // 클릭된 카드의 영화에서 rate_set 내에서 현재 user의 id값과 같은 user가 작성한 rate값을 불러오는 메서드 
    rateLoad() {
      for (let set of this.detailCard.movie.rate_set) {
        if (set.user === this.detailCard.user) {
          this.detailCardRate = set.rate
          console.log(this.detailCardRate)
        }
      }
    }
  },
  created() {
  }
}
</script>

<style>
.card-stats {
  grid-area: stats;
}
.card-body {
  grid-area: text;
  margin: 25px;
}
.card-body span {
  color: rgb(255, 7, 110);
  font-size:13px;
}
.card-body .card-text{
  color: grey;
  font-size:15px;
  font-weight: 300;
}
.card-body h5 {
  margin-top:0px;
  font-size:28px;
}
.card-stats {
  grid-area: stats; 
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr;

  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  background: rgb(255, 7, 110);
}
</style>