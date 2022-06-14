import Vue from 'vue'
import Vuex from 'vuex'
// import _ from 'lodash'
import axios from 'axios'

Vue.use(Vuex)
// VUE_APP_YOUTUBE_API_KEY = '04c08caa3c3ade3d88e6c71bcfb450cb'
const API_URL = 'https://api.themoviedb.org/3'
const API_KEY = '04c08caa3c3ade3d88e6c71bcfb450cb'

export default new Vuex.Store({
  state: {
    homeMovies: [],
    movies : [],

  },
  getters: { 
    homeMovies: (state) => state.homeMovies,
  },
  mutations: {
    SET_MOVIES: (state, movies) => (state.homeMovies=movies),

    CREATE_MOVIE(state, newMovie) {
      state.movies.push(newMovie)
    },

  },
  
  
  actions: {
    setMovies({ commit } ) {
      axios
        .get(`${API_URL}/movie/popular?api_key=${API_KEY}&language=ko`)
        .then(res => commit('SET_MOVIES', res.data.results))
        .catch(err => console.error(err))
    },
    // saveMovie({ state }) {
    //   const jsonData = JSON.stringify(state.movies)
    //   localStorage.setItem('movies', jsonData)
    // },
    createMovie(context, newMovie) {
      context.commit('CREATE_MOVIE', newMovie)
    },
  },
})
