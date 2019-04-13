import Vue from 'vue';
import { Module } from 'vuex';
import state from './state';
import * as getters from './getters';
import { actions } from './actions';
import * as mutations from './mutations';
import Vuex from 'vuex';
import { RootState } from '../types';
import { MainState } from './types';

Vue.use(Vuex);

const namespaced: boolean = true;

export const main: Module<MainState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations,
};
