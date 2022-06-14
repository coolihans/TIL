<template>
  <div>
      <input type="text"
      v-model.trim="movieList"
      @keyup.enter="createMovie">

  </div>
</template>

<script>


export default {
  name: 'MovieListForm',
  components: {

  },
  data() {
		return {
			movieList:''
		}
	},

  methods: {
		createMovie(){
			const newMovie = {
				movie : this.movieList,
				date : new Date().getTime()
			}
		this.$store.dispatch('createMovie', newMovie)
		this.movieList = ''
		}
	}
}
</script>

<style>

</style>
