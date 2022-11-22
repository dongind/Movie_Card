<template>
  <div>
    <h1>Movie Cards</h1>
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
      this.$store.dispatch('getArticleMyList')
    }
  },
  created() {
    this.getArticleList()
  }
}
</script>

<style>

</style>