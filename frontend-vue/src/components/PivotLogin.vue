<template>
  <md-card class="pivot-login">
    <md-card-header>
      Digid login
    </md-card-header>
    <md-card-content>
    Er staat {{ amount }} euro op je kaart. Login met Digid om je pensioen te ontvangen!
    <img src="../assets/digid.png">
      <md-field>
        <md-input id="username" name="username" v-model="username" placeholder="Gebruikersnaam" maxlength="20" />
      </md-field>
      <md-field>
        <md-input id="password" name="password" type="password" v-model="password" placeholder="Wachtwoord" maxlength="20" />
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
  @Prop() private amount!: number;
  @Action('authenticate', { namespace }) private authenticate!: types.AuthenticateAction;

  private username: string = '';
  private password: string = '';
  private error: boolean = false;

  private submit(): void {
    this.authenticate({
      username: this.username,
      password: this.password,
    })
    .then((response) => {
      this.$emit('login', response);
    }).catch((error) => {
      this.error = true;
    })
  }
}
</script>

<style scoped lang="scss">
img {
  max-width: 7rem;
  margin-top: 2rem;
}
</style>