import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import { main } from './main/index';

Vue.use(Vuex);

const storeOptions: StoreOptions<RootState> = {
  state: {
    version: '1.0.0',
  },
  modules: {
    main,
  },
};

export default new Vuex.Store<RootState>(storeOptions);
