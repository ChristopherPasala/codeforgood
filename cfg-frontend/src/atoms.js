import { atom } from "recoil";

export const authState = atom({
  key: "authState",
  default: {
    loggedIn: false,
    name: "",
    user_id: null,
  },
  persistence_UNSTABLE: {
    type: "authState",
  },
});
