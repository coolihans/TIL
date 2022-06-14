<template>
  <div class="card" style="width: 18rem;">

  <div class="card-body">
    <h5 class="card-title">{{ movie.title }}</h5>
    <p class="card-text">{{ movie.overview }}</p>
    <a href="#" class="btn btn-primary">Detail</a>
  </div>
</div>
  <!-- <div>
    
    <h2>
      {{ movie.title }}
    </h2>
    {{ movie.overview }}
  </div> -->
</template>

<script>

// import { mapActions, mapState } from 'vuex'

export default {
  name: 'MovieCard',
  props: {
    homeMovies:Object,
    movie:Object
  },
}
</script>

<style>

</style>