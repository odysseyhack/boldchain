<template>
<md-card class="contribute">
    <md-card-header>
        <div class="md-title">In je cadeau bij een van je active pensioenfondsen:</div>
    </md-card-header>

    <!-- Cards per pension //-->
  <md-card v-for="(pension, index) in pensions" :key="index">
    <md-card-header>
      <md-card-header-text>
        <div class="md-title">Stichting pensioenfoends ABP</div>
        <div class="md-title">€ 37 opgebouwd</div>
        <div class="md-subhead">Vanaf 67 jaar en 3 maanden</div>
      </md-card-header-text>

      <md-card-media>
        <img src="../assets/U0202.png" alt="ABP">
      </md-card-media>
    </md-card-header>
  </md-card>

  <md-card-content></md-card-content>
  <md-card-actions>
    <md-button class="md-raised md-primary" @click="$emit('goto', 0)">Nog een keer</md-button>
    <md-button class="md-raised md-primary">Leer meer</md-button>
  </md-card-actions>
</md-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';

@Component
export default class Contribute extends Vue {
  @Prop() private pensions!: { [key: string]: string }[];
}
</script>

<style scoped lang="scss">
</style>