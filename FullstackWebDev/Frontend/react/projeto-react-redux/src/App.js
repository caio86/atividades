import { LoginButton } from "./components/LoginButton";
import { LogoutButton } from "./components/LogoutButton";
import { UserProfile } from "./components/UserProfile";

function App() {
  return (
    <div>
      <LoginButton />
      <LogoutButton />
      <UserProfile />
    </div>
  );
}

export default App;
