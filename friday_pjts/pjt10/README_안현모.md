# pjt10 

## Vue를 활용한 SPA 구성

```javascript
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
   
    createMovie(context, newMovie) {
      context.commit('CREATE_MOVIE', newMovie)
    },
  },
})
```

1. homeview

- axios를 적용하는 것에 어려움이 있었다! 복습의 부족함을 느꼈다..
- actions => mutation => state 로 이어지는 흐름
- 이를 개별 컴포넌트에서 불러오는 흐름까지 잘 이어가지 못해서 어려웠다. +로 axios로 통신해 영화 정보를 불러오는 것에서 많이 막혔다.



2. watchlistview

- watchlistview, wathlistform, watchlistitem 의 관계는 전에 했던 todolist 작성하기와 유사한 흐름으로 진행 되었다.
- 검색을 통해 추가를 하는 경우에 대해서도 생각해보았다.



3. 후기

- bootstrap까지의 적용이 문제가 아니라 앞에서 시간을 너무 잡아먹어 완성치 못했다.
- randomview 까지 차후에 따로 서버 켜보면서 작동을 하도록 만들어 봐야겠다.
- router 와 vuex 배운 것을 모두 써볼 수 있는 과제였는데 생각만큼 제대로 하기 어려웠다..
- 페어프로젝트는 최대한 잘 준비를 했었는데 최근에 복습에도 어려움을 겪었던 것이 그대로 나타난 것 같아 수홍님께도 죄송하고 아쉬웠다!