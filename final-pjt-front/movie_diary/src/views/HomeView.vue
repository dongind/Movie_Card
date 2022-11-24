<template>
  <div>
    <div class="article-page">
      <p class="head-title">Movie Card</p>
      <div class="article-container shadow">
        <div class="card-side">
          <ArticleList/>
        </div>
        <div class="movie-side">
          <MovieList/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'HomeView',
  components: {
    ArticleList,
    MovieList,
  },
}
</script>

<style>

@font-face {
    font-family: 'Chosunilbo_myungjo';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/Chosunilbo_myungjo.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
*{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
.head-title{
  font-size: 50px;
  font-family: 'Chosunilbo_myungjo';
  margin-bottom: 20px;
  margin-top: 20px;
}

.article-page {
    width: 100vw;
    height: 100vh;
    background: #eff0f2;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.article-container{
 
 background:#ffffff ;
 width: 90%;
 height: 80%;
 display: flex;
 flex-direction: row;
 box-shadow: 10px black;
 border-radius: 10px;

}

.card-side {
  width: 70%;
  height: 100%;
  overflow: auto;
  padding: 5px;
  border-right-style: solid;
  border-right-width: 1px;
  border-right-color: darkgray;
}

.movie-side {
  width: 29%;
  height: 100%;
  display: flex;
  flex-direction: column;
  margin-right: 0.5%;
  margin-left: 0.5%;
}
</style>