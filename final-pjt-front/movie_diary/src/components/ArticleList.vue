<template>
  <div>
    <div class="row row-cols-1 row-cols-md-6 g-2">
      <ArticleItem
        v-for="article in articles" :key="article.id"
        :article="article"
      />
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
.article-list{
  width: 100%;
  height: 70vh;
  display:flex;
  flex-direction: column;
  overflow: auto;
  font-family: nanumsquare;
}
.article-list::-webkit-scrollbar {
    width: 8px;  /* 스크롤바의 너비 */
}

.article-list::-webkit-scrollbar-thumb {
    height: 30%; /* 스크롤바의 길이 */
    background: #2f3542; /* 스크롤바의 색상 */
    
    /* border-radius: 10px; */
}

.article-list::-webkit-scrollbar-track {
    background: gray;  /*스크롤바 뒷 배경 색상*/
}
</style>