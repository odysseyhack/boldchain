import Vue, { PluginObject } from 'vue';

import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import BootstrapVue from 'bootstrap-vue';
import Trend from 'vuetrend';

import App from './App.vue';
import router from './router';
import store from './store/index';

// bootstrap-vue css
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.config.productionTip = false;
Vue.use(VueMaterial as PluginObject<{}>);
Vue.use(BootstrapVue);
Vue.use(Trend as PluginObject<{}>);


new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
