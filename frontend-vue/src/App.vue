<template>
  <b-container id="app" class="page-container">
    <router-view />
  </b-container>
</template>

<style lang="scss">
@import "~vue-material/dist/theme/engine"; // Import the theme engine

@include md-register-theme("default", (
  primary: #DD63C5, // The primary color of your application
  accent: green // The accent or secondary color
));

@import "~vue-material/dist/theme/all"; // Apply the theme

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
body {
  background: url('/src/assets/bg.png') repeat-y;
}

</style>
