<template>
  <b-card class="redeem">
    <b-card-header>Start your future today</b-card-header>
    <b-card-body>
      <b-form-input v-model="code" placeholder="Enter your code"></b-form-input>
        <b-button variant="secondary" @click="submit()">Redeem</b-button>
    </b-card-body>
  </b-card>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Action } from 'vuex-class';
import * as types from '@/store/main/types';

const namespace: string = 'main';

@Component
export default class Redeem extends Vue {

  @Action('redeemCode', { namespace }) private redeemCode!: types.RedeemCodeAction;

  private code: string = '';
  private error: boolean = false;

  private submit(): void {
    this.redeemCode(this.code).then((response: {}) => {
      this.$emit('redeemed', response);
    }).catch(() => {
      
    })
  }
}
// Pivot kan de contributie doen
// Pivot sturen we een naam/geboortedatum
// ---- netto pensioenproduct voor no-pensioeners
// -- wij sturen pivot de digid/pivid en de geldwaarde en de leeftijd
// -- Pivot doet de transactie voor ons en de prognose

</script>

<style scoped lang="scss">

</style>

