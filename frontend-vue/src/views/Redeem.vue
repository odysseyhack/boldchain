<template>
  <div class="redeem">
    <input type="text" v-model="redeemCode" />
    <input type="submit" value="Redeem code">
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Redeem extends Vue {
  private redeemCode: string = '';

}
</script>

<style scoped lang="scss">

</style>