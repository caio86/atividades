import { useDispatch } from "react-redux";
import { logout } from "../authReducer";

const LogoutButton = () => {
  const dispatch = useDispatch();
  return <button onClick={() => dispatch(logout())}>Logout</button>;
};

export { LogoutButton };
