<template>
<md-card class="contribute">
    <md-card-header>
        <div class="md-title">In je cadeau bij een van je active pensioenfondsen:</div>
    </md-card-header>

    <!-- Cards per pension //-->
  <md-card v-for="(pension, index) in pensions" :key="index">
    <md-card-header>
      <md-card-header-text>
        <b-row>
          <b-col md="4">
            <img :src="getImgUrl(pension.ascription)" v-bind:alt="pension.ascription">
          </b-col>
          <b-col md="8">
            <div class="md-title">Pensioenfonds {{ pension.ascription }}</div>
          </b-col>
        </b-row>
      </md-card-header-text>
      <md-card-actions>
        <md-button class="md-raised md-accent" @click="submit(pension.ascription)">Toevoegen</md-button>
      </md-card-actions>
    </md-card-header>
  </md-card>

  <md-card-content></md-card-content>
</md-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import ImgUrls from '@/mixins/ImgUrls.vue';

@Component
export default class Contribute extends ImgUrls {
  @Prop() private pensions!: { [key: string]: string }[];

  private submit(pensionName: string): void {
    this.$emit('contribute', pensionName);
  }
}
</script>

<style scoped lang="scss">
</style>