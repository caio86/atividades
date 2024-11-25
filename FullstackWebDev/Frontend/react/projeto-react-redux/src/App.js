import { LoginButton } from "./features/auth/components/LoginButton";
import { LogoutButton } from "./features/auth/components/LogoutButton";
import { UserProfile } from "./features/auth/components/UserProfile";

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
