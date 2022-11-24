<template>
      <div class="modal fade" id="SelectFirstMovieModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Select First Movie</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="container-fluid">
              <div class="row row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-2">
                <FirstMovieItem
                  v-for= "movie in popularRandomRecommend" :key="movie.id"
                  :movie="movie"
                  @select-movie="selectMovie"
                />
              </div>
            </div>
          </div>
          <div class="modal-footer">
            선택 영화 목록 : {{ selectedMoviesId }}
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