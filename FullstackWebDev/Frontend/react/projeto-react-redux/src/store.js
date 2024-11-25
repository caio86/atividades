import { createStore } from "redux";
import authReducer from "./redux/auth/authReducer";

const store = createStore(authReducer);

export default store;
