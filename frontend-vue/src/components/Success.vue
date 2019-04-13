<template>
<md-card class="success">
  <md-card-header>
      <div class="md-title">Success! Wij hebben je pensioen toegevoegd aan je onderstaande pensioenfonds:</div>
  </md-card-header>
  <md-card>
    <md-card-header>
      <md-card-header-text>
        <b-row>
          <b-col md="4">
            <img :src="getImgUrl(pensionName)" v-bind:alt="pensionName">
          </b-col>
          <b-col md="8">
            <div class="md-title">Pensioenfonds {{ pensionName }}</div>
          </b-col>
        </b-row>
      </md-card-header-text>
    </md-card-header>
  </md-card>
  <md-card-content>
    <trend
      :data="[0, 3, 4, 5, 6, 7, 9, 13, 21, 34]"
      :gradient="['#DD63C5', '#DD63C5', '#DD63C5']"
      auto-draw
      smooth>
    </trend>
  <transition name="component-fade" mode="out-in">
    <span v-show="showSpan"><h1>€ 10000</h1></span>
  </transition>
  </md-card-content>
  <md-card-actions>
    <md-button class="md-raised md-primary" @click="$emit('goto', 0)">Nog een keer</md-button>
    <md-button class="md-raised md-primary">Leer meer</md-button>
  </md-card-actions>
</md-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';

@Component
export default class Success extends Vue {
  @Prop() private pensionName!: string;

  private showSpan: boolean = false;

  private mounted() {
    setTimeout(() => { this.showSpan = true }, 2000)
  }
  private getImgUrl (picture: string) {
      return require('../assets/' + picture + '.png');
  };
}
</script>

<style scoped lang="scss">
</style>