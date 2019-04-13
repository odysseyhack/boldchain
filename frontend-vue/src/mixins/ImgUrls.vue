<template>
  <div class="img-urls">
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component, Mixin, Mixins } from 'vue-mixin-decorator';

@Mixin
export default class MyMixin extends Vue {
  private getImgUrl (picture: string) {
    return require('../assets/' + picture + '.png');
  };
}
</script>
