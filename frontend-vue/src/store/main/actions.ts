import { RootState } from '../types';
import { MainState } from './types';
import { ActionTree, ActionContext } from 'vuex';
import axios from 'axios';
import { AxiosResponse, AxiosError } from 'axios';

const baseUrl: string = 'http://172.16.165.8:8000';

export const actions: ActionTree<MainState, RootState> = {

  redeemCode(store: ActionContext<MainState, RootState>, code: string): Promise<{}> {
    return new Promise((resolve, reject) => {
      axios.get(
        baseUrl + `/giftcards/valid?barcode=${ code }`,
      ).then((response: AxiosResponse) => {
        resolve(response.data);
      }).catch((error: AxiosError) => {
        reject(error.message);
      });
    });
  },

  authenticate(
    store: ActionContext<MainState, RootState>,
    payload: {username: string, password: string },
  ): Promise<{}> {
    return new Promise((resolve, reject) => {
      axios.post(
        baseUrl + `/mockdigid/authenticate?username=${ payload.username }&password=${ payload.password }`,
      ).then((response: AxiosResponse) => {
        resolve(response.data);
      }).catch((error: AxiosError) => {
        reject(error.message);
      });
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
