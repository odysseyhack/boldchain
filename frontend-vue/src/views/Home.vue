<template>
  <div class="home">
    <b-row>
      <b-col md="3"></b-col>
      <b-col md="6">
      <transition name="component-fade" mode="out-in">
        <component
          v-bind:is="currentComponent"
          @redeem="(response) => redeem(response)"
          @login="(response) => login(response)"
          @goto="(step) => currentStep = step"
          :code="redeemCode"
          :amount="amount"
        />
      </transition>
      </b-col>
      <b-col md="3"></b-col>
    </b-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Redeem from '@/components/Redeem.vue';
import PivotLogin from '@/components/PivotLogin.vue';
import Success from '@/components/Success.vue';
import NewPension from '@/components/NewPension.vue';

@Component({
  components: {
    Redeem,
    PivotLogin,
    Success,
    NewPension,
  },
})
export default class Home extends Vue {
  private currentStep: number = 0;
  private amount: number = 0;
  private redeemCode: string = '';

  get currentComponent(): string {
    const components = ['redeem', 'pivot-login', 'success', 'new-pension'];
    return components[this.currentStep];
  }

  private redeem(response: { barcode: string, amount: number }): void {
    this.redeemCode = response.barcode;
    this.amount = response.amount;
    this.currentStep = 1;
  }

  private login(response: {}): void {
    this.currentStep = 2;
  }
}
</script>

<style lang="scss">
.component-fade-enter-active, .component-fade-leave-active {
  transition: opacity .3s ease;
}
.component-fade-enter, .component-fade-leave-to
/* .component-fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.home {
  padding-top: 10rem;
}
.card {
  padding: 5rem;
}
</style>