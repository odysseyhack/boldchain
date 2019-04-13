<template>
  <div class="pivot-login">
    Pivot login
    Er staat zoveel euro op je kaart
    Pivot login
    <input v-model="username" placeholder="Pivot ID/ Digid" />
    <input v-model="password" placeholder="Wachtwoord" />
    <md-button @click="submit">Voeg to aan pensioen!</md-button>
  </div>
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