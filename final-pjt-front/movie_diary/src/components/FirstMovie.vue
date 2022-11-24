<template>
      <div class="modal fade" id="SelectFirstMovieModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Select First Movie</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <FirstMovieItem
              v-for= "movie in popularRandomRecommend" :key="movie.id"
              :movie="movie"
              @select-movie="selectMovie"
            />
            선택 영화 목록 : {{ selectedMoviesId }}
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="baseRating">Movie Rating</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import FirstMovieItem from '@/components/FirstMovieItem.vue'

export default {
  name: "FirstMovie",
  comments: {
    FirstMovieItem,
  },
  computed: {

  },
  methods: {
    
  }
}
</script>

<style>

</style>