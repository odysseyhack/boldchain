<template>
  <div class="home">
    <header id="header">
      <h1>Pension Present</h1>
    </header>
    <b-row>
      <b-col lg="2"></b-col>
      <b-col lg="8">
      <transition name="component-fade" mode="out-in">
        <component
          v-bind:is="currentComponent"
          @redeem="(response) => redeem(response)"
          @login="(response) => login(response)"
          @contribute="(pensionName) => contribute(pensionName)"
          @goto="(step) => currentStep = step"
          :code="redeemCode"
          :amount="amount"
          :pensions="pensions"
          :pension-name="contributedPension"
        />
      </transition>
      </b-col>
      <b-col lg="2"></b-col>
    </b-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Redeem from '@/components/Redeem.vue';
import PivotLogin from '@/components/PivotLogin.vue';
import Success from '@/components/Success.vue';
import NewPension from '@/components/NewPension.vue';
import Contribute from '@/components/Contribute.vue';

@Component({
  components: {
    Contribute,
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
  private pensions: { [key: string]: string }[] = [];
  private contributedPension: string = '';
  private firstName: string = '';
  private lastName: string = '';

  get currentComponent(): string {
    const components = ['redeem', 'pivot-login', 'contribute', 'success', 'new-pension'];
    return components[this.currentStep];
  }

  private redeem(response: { barcode: string, amount: number }): void {
    this.redeemCode = response.barcode;
    this.amount = response.amount;
    this.currentStep = 1;
  }

  private login(response: { 
    pension_funds: {
      [key: string]: string }[],
      first_name: string,
      last_name: string
    }): void {
    this.pensions = response.pension_funds;
    this.lastName = response.last_name;
    this.firstName = response.first_name;
    this.currentStep = 2;
  }

  private contribute(pensionName: string) {
    this.contributedPension = pensionName;
    this.currentStep = 3;
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
#header {
  position: absolute;
  top: 0;
  left: 0;
  padding: 1rem;
  background-color: orange;
}
#header h1 {
  color: #FFF;
  text-align: left;
  font-size: 2em;
  font-weight: bold
}

.home {
  padding-top: 10rem;
}
.md-card {
  padding: 2rem !important;
  .md-card {
    margin: 2rem;
  }
}
</style>