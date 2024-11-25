const initialState = {
  user: null,
};

const authReducer = (state = initialState, action) => {
  switch (action.type) {
    case "LOGIN":
      console.log("Login", { ...state, user: action.payload });
      return { ...state, user: action.payload };
    case "LOGOUT":
      console.log("Logout", { ...state, user: null });
      return { ...state, user: null };
    default:
      return state;
  }
};

export default authReducer;
