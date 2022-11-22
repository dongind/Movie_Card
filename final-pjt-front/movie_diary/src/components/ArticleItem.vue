<template>
  <div>
    <div class="col">
    <div class="card">
      <img :src="imgSrc" class="card-img-top" alt="...">
      <div class="card-body">
        <span class="date">{{ article.plannedAt }}</span>
        <h5 class="card-title">{{ movieTitle }}</h5>
        <p class="card-text">{{ article.content }}</p>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  data() {
    return {
      movieTitle: this.article.movie.title
    }
  },
  computed: {
    imgSrc() {
      return `https://image.tmdb.org/t/p/original${this.article.movie.poster_path}`
    }
  },
  methods:{
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