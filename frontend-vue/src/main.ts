import Vue, { PluginObject } from 'vue';

import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';


import App from './App.vue';
import router from './router';
import store from './store/index';

Vue.config.productionTip = false;
Vue.use(VueMaterial as PluginObject<{}>);


new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
