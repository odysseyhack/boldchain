import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Redeem from './views/Redeem.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/redeem',
      name: 'redeem',
      component: Redeem,
    },
  ],
});
