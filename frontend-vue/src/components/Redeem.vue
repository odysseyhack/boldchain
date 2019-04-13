<template>
  <md-card class="redeem">
    <md-card-header><h1>Voer kaartcode in</h1></md-card-header>
    <md-card-content>
      <md-field>
        <md-input id="code" name="code" v-model="code" />
      </md-field>
      <md-button class="md-raised md-primary" @click="submit">Invoeren</md-button>
    </md-card-content>
  </md-card>
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

