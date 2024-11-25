const login = (userData) => ({
  type: "LOGIN",
  payload: userData,
});

const logout = () => ({
  type: "LOGOUT",
});

const initialState = {
  user: null,
};

const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case "LOGIN":
      return { ...state, user: action.payload };
    case "LOGOUT":
      return { ...state, user: null };
    default:
      return state;
  }
};

export { login, logout };
export default authReducer;
