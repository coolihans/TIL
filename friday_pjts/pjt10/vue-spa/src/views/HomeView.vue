<template>
  <div class="container">
    <ul>
      <movie-card
        v-for="movie in homeMovies" :key="movie.id" :movie="movie">
      </movie-card>
    </ul>
  </div>
</template>

<script>
import {  mapState, mapActions } from 'vuex'
import MovieCard from './MovieCard.vue'
export default {
  components: { MovieCard },
  name: 'HomeView',
  computed: {
    ...mapState(['homeMovies'])
  },
  methods: {
    ...mapActions(['setMovies'])
  },

  created() {
    this.setMovies()
  }
}
</script>

<style>

</style>