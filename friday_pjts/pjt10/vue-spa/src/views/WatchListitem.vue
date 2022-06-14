<template>
  <div>
     {{ movie.movie }}
  </div>
</template>

<script>

export default {
  name: 'MovieListItem',
  props: {
    movie : Object,
  },
  methods: {
  },
}
</script>

<style scoped>
div {
  border: 2px solid black;
  margin: 2px;
  padding: 2px;
}
span {
  cursor: pointer;
}
</style>
