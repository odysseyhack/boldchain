<template>
<md-card class="success">
  <md-card-header>
    <div class="md-title">Gelukt! Je cadeau is toegevoegd.</div>
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
    <span v-show="showSpan">
      <p>Dat kan in je pensoenfonds</p>
      <h1>€ 10.000</h1>
      <p> worden </p>
      </span>
  </transition>
  <transition name="component-fade" mode="out-in">
    <span v-show="showMsg">Top, klaar. Ik wil nu:</span>
  </transition>
  <md-card-actions v-show="showMsg" class="md-alignment-center">
    <b-row>
      <b-col md="6">
        <md-button class="md-raised md-primary" @click="$emit('goto', 0)">extra kaart toevoegen</md-button>
      </b-col>
      <b-col md="6">
        <md-button class="md-raised md-primary">Leer over pensioenen</md-button>
      </b-col>
    </b-row>
  </md-card-actions>
  </md-card-content>
</md-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import ImgUrls from '@/mixins/ImgUrls.vue';

@Component
export default class Success extends ImgUrls {
  @Prop() private pensionName!: string;
  @Prop() private pensionUrl!: string;

  private showSpan: boolean = false;
  private showMsg: boolean = false;

  private mounted() {
    setTimeout(() => { this.showSpan = true }, 2000);
    setTimeout(() => { this.showMsg = true }, 3500);
  }
}
</script>

<style scoped lang="scss">
</style>