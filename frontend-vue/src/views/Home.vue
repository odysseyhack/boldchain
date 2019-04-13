<template>
  <div class="home">
    <transition name="component-fade" mode="out-in">
      <component v-bind:is="currentComponent" @goto="(step) => currentStep = step" />
    </transition>
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

  get currentComponent(): string {
    const components = ['redeem', 'pivot-login', 'success', 'new-pension'];
    return components[this.currentStep];
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
</style>