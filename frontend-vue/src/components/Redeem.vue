<template>
  <md-card class="redeem">
    <md-card-header><h1>Haal je pensioenbijdrage op</h1></md-card-header>
    <md-card-content>
    <b-row>
    <b-col cols="8">
      <md-field>
        <md-input id="code" name="code" v-model="code" maxlength="20" placeholder="Voer hier je kaartcode in" />
      </md-field>
    </b-col>
    <b-col cols="4">
      <md-button class="md-raised md-primary" @click="submit">Kassa!</md-button>
    </b-col>
    </b-row>
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
  private redeeming: boolean = false;

  private submit(): void {
    this.redeeming = true;
    this.redeemCode(this.code).then((response: { [key: string]: any }) => {
      console.log(response);
      this.$emit('redeem', response);
    }).catch((error: string) => {
      console.log(error);
    }).finally(() => {
      this.redeeming = false;
    })
  }
}

</script>

<style scoped lang="scss">
</style>

