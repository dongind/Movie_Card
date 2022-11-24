<template>
  <div>

    <div class="article-page">
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
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

.head-title1{
  padding-left: 1%;
  margin-top: 0px;
  margin-bottom: 0px;
  font-size: 30px;
  color: rgb(240, 240, 240);
  background-color: rgb(32, 32, 32);
  border-top-left-radius: 2px;
  border-bottom-left-radius: 2px;
}
.head-title2{
  margin-top: 0px;
  margin-bottom: 0px;
  font-size: 30px;
  color: black;
  /* background-color: white; */
}

.article-page {
    width: 100vw;
    height: 100vh;
    background: #ffffff;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.article-container{
  margin-top: 50px;
  background:#ffffff ;
  width: 90%;
  height: 85%;
  display: flex;
  flex-direction: row;
  box-shadow: 10px black;
  border-radius: 10px;

}

.card-side {
  width: 65%;
  height: 100%;
  overflow: auto;
  padding: 5px;
  border-right-style: solid;
  border-right-width: 1px;
  border-right-color: darkgray;
}

.movie-side {
  width: 35%;
  height: 100%;
  display: flex;
  flex-direction: column;
  padding-right: 0.5%;
  padding-left: 0.5%;
  color: white;
  background-color: rgb(32, 32, 32);
}
</style>