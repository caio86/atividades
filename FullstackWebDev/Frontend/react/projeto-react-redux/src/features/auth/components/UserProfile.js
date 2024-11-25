import { useSelector } from "react-redux";

const UserProfile = () => {
  const user = useSelector((state) => state.user);
  return user ? <h2>Bem-vindo, {user.name}</h2> : <h2>Faça login</h2>;
};

export { UserProfile };
