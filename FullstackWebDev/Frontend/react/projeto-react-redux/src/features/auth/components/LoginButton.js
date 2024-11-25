import { useDispatch } from "react-redux";
import { login } from "../authReducer";

const LoginButton = () => {
  const dispatch = useDispatch();
  return (
    <button
      onClick={() =>
        dispatch(login({ name: "joão", email: "joao@example.com" }))
      }
    >
      Login
    </button>
  );
};

export { LoginButton };
