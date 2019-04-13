<template>
  <md-card class="pivot-login">
    <md-card-header>
      Digid login
    </md-card-header>
    Er staat zoveel euro op je kaart. Login met Digid om je pensioen te ontvangen!
    <md-card-content>
      <md-field>
        <md-input id="username" name="username" v-model="username" placeholder="Pivot ID/ Digid login" />
      </md-field>
      <md-field>
        <md-input id="password" name="password" v-model="password" placeholder="Wachtwoord" />
      </md-field>
      <md-button class="md-raised md-primary" @click="submit">Voeg to aan pensioen!</md-button>
    </md-card-content>
  </md-card>
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
      this.$emit('goto', 2);
    }).catch(() => {
      
    })
  }
}
</script>

<style scoped lang="scss">

</style>