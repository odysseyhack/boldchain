import { RootState } from '../types';
import { MainState } from './types';
import { ActionTree, ActionContext } from 'vuex';
import axios from 'axios';
import { AxiosResponse, AxiosError } from 'axios';

export const actions: ActionTree<MainState, RootState> = {

  redeemCode(store: ActionContext<MainState, RootState>, code: string): Promise<{}> {
    return new Promise((resolve, reject) => {
      resolve({});
    });
  },

  contribute(
    store: ActionContext<MainState, RootState>,
    payload: { username: string, password: string, code: string }): Promise<{}> {
    return new Promise((resolve, reject) => {
      resolve({});
    });
  },
};
