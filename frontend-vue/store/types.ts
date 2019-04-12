import { MainState } from './main/types';

export interface RootState {
  version: string;
  main: MainState | (() => MainState) | undefined;
}
