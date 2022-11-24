<template>
  <div>
    <div class="container articles">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-2">
        <ArticleItem
          v-for="article in articles" :key="article.id"
          :article="article"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem.vue'
export default {
  name: 'ArticleList',
  components:{
    ArticleItem,
  },
  data() {
    return {
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
  methods: {
    getArticleList() {
      this.$store.dispatch('getArticleList')
    }
  },
  created() {
    this.getArticleList()
  }
}
</script>

<style>
.articles {
  width: 100%;
  height: 83vh;
  display:flex;
  flex-direction: column;
  overflow: auto;
  font-family: nanumsquare;
}
.articles::-webkit-scrollbar {
    display: none;
    width: 10px;  /* 스크롤바의 너비 */
}

.articles::-webkit-scrollbar-thumb {
    height: 30px; /* 스크롤바의 길이 */
    background: #2f3542; /* 스크롤바의 색상 */
    
    /* border-radius: 10px; */
}

.articles::-webkit-scrollbar-track {
    background: rgb(85, 85, 85);  /*스크롤바 뒷 배경 색상*/
}
</style>