import { RootState } from '../types';
import { MainState } from './types';
import { ActionTree, ActionContext } from 'vuex';
import axios from 'axios';
import { AxiosResponse, AxiosError } from 'axios';

const baseUrl = process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:8080' : 'http:127.0.0.1:8080';

export const actions: ActionTree<MainState, RootState> = {
};
