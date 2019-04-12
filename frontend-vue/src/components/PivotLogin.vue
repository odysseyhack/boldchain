<template>
  <b-card class="pivot-login">
    <b-card-header>
      Pivot login
    </b-card-header>
    <b-card-body>
      Er staat zoveel euro op je kaart
      Pivot login
      <b-form-input v-model="username" placeholder="Pivot ID/ Digid"></b-form-input>
      <b-form-input v-model="password" placeholder="Wachtwoord"></b-form-input>
        <b-button variant="secondary" @click="submit">Voeg to aan pensioen!</b-button>
    </b-card-body>
  </b-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import { Action } from 'vuex-class';
import * as types from '@/store/main/types';

const namespace: string = 'main';

@Component
export default class PivotLogin extends Vue {

  @Prop() private code!: string;
  @Action('contribute', { namespace }) private contribute!: types.ContributeAction;

  private username: string = '';
  private password: string = '';

  private submit(): void {
    this.contribute({
      username: this.username,
      password: this.password,
      code: this.code })
    .then((response: {}) => {
      this.$emit('contributed', response);
    }).catch(() => {
      
    })
  }
}
</script>

<style scoped lang="scss">

</style>