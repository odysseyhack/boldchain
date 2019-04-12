<template>
  <div class="redeem">
    <b-card>
      <b-card-header>Start your future today</b-card-header>
      <b-card-body>
        <b-form-input v-model="redeemCode" placeholder="Enter your code"></b-form-input>
         <b-button variant="success" @click="submit">Redeem</b-button>
      </b-card-body>
    </b-card>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Redeem extends Vue {
  private redeemCode: string = '';

  private submit(): void {

  }
}
</script>

<style scoped lang="scss">

</style>