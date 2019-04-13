export interface MainState {
}

export type RedeemCodeAction = (redeemCode: string) => Promise<{}>;

export type ContributeAction = (payload: { username: string, password: string, code: string }) => Promise<{}>;

export type AuthenticateAction = (payload: { username: string, password: string }) => Promise<{}>;
