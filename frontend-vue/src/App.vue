<template>
  <div id="app" class="page-container">
    <md-app>
      <md-app-content>
      <router-view />
      </md-app-content>
    </md-app>
  </div>
</template>

<style lang="scss">
@import "~vue-material/dist/theme/engine"; // Import the theme engine

@include md-register-theme("default", (
  primary: md-get-palette-color(blue, A200) // The primary color of your application
));

@import "~vue-material/dist/theme/all"; // Apply the theme


#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
