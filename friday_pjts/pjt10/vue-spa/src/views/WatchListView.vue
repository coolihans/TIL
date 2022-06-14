<template>
  <div>
		My Movie List
		<watch-list-form></watch-list-form>
		<watch-list-item 
		v-for="movie in movies" 
		:key="movie.date"
		:movie="movie">
		
		</watch-list-item>

  </div>
</template>

<script>
import WatchListItem from '@/views/WatchListItem.vue'
import WatchListForm from './WatchListForm.vue'
import { mapState } from 'vuex'
export default {
	components: { WatchListForm, WatchListItem },
	name : 'WatchListView',

	computed: {
		...mapState(['movies']),
	},

}
</script>

<style>

</style>