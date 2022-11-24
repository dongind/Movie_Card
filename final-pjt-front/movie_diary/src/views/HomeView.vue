<template>
  <div>
    <div class="article-page">
      <div class="article-container shadow">
        <div class="content-container">
          <div class="card-side">
            <ArticleList/>
          </div>
          <div class="movie-side">
            <div class="navbar">
              <span class="app-title mb-0">MOVIECARD</span>
              <p class="user-container mb-0">
                <span class="username mb-0">username</span>
                <router-link :to="{'name' : 'logout'}" class="logout mb-0"> Logout</router-link>
              </p>
            </div>
            <MovieList/>
          </div>
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

@font-face {
font-family: 'UhBeeJJIBBABBA';
src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_five@.2.0/UhBeeJJIBBABBA.woff') format('woff');
font-weight: normal;
font-style: normal;
}
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

.navbar {
  height: 10%;
  padding: 0;
  padding-left: 10px;
  padding-right: 30px;
  justify-content: space-between;
  background-color: #f8f8f8;
  color: rgb(56, 56, 56);
  
}

.user-container {
  padding: 0;
  margin-bottom: 0;
}

.app-title {

  font-size: 40px;
  color: rgb(0, 0, 0);

}

.username {
  margin-right: 20px;
  font-size: 15px;
}

.logout {
  text-decoration: none;
  color: rgb(56, 56, 56);
  margin-right: 20px;
  font-size: 15px;
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
  margin-top: 50px;
  background:#f8f8f8 ;
  width: 90vw;
  height: 90%;
  display: flex;
  flex-direction: column;
  box-shadow: 10px black;
  border-radius: 20px;
}

.content-container{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
}
.card-side {
  width: 60%;
  height: 100%;
  overflow: auto;
  padding: 30px;
  /* border-top-color: rgb(224, 224, 224);
  border-top-style: solid;
  border-top-width: 2px; */
}

.movie-side {
  width: 40%;
  height: 100%;
  display: flex;
  flex-direction: column;
  color: black;
  /* background-color: rgb(85, 85, 85); */
  background-color: rgb(224, 224, 224);
}
</style>