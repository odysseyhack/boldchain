<template>
  <div class="home">
    <transition name="fade">
      <redeem v-show="currentStep == 0" @redeemed="currentStep += 1" />
    </transition>
    <pivot-login v-show="currentStep == 1" @contributed="currentStep +=1" />
    <succes v-show="currentStep == 2" />
    <new-pension v-show="currentStep == 3" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Redeem from '@/components/Redeem.vue';
import PivotLogin from '@/components/PivotLogin.vue';
import Succes from '@/components/Succes.vue';
import NewPension from '@/components/NewPension.vue';

@Component({
  components: {
    Redeem,
    PivotLogin,
    Succes,
    NewPension,
  },
})
export default class Home extends Vue {
  private currentStep: number = 0;

}
</script>
