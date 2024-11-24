import { useState } from "react";
import "./App.css";
import ProfileCard from "./components/ProfileCard";

function App() {
  const [hasPermission, setHasPermission] = useState(false);
  const userData = require("./userData.json");

  const withPermission = (WrappedComponent) => {
    return (props) => {
      if (!props.hasPermission) {
        return <h1>Permissão negada</h1>;
      }
      return <WrappedComponent {...props} />;
    };
  };

  const appStyle = {
    display: "grid",
    "grid-template-columns": `repeat(${Math.min(Math.ceil(userData.length / 2), 5)}, 1fr)`,
    "justify-items": "center",
    gap: "2rem",
    padding: "2rem",
  };

  const ProfileList = () => (
    <div style={appStyle}>
      {userData.map((user) => (
        <ProfileCard name={user.name} bio={user.bio} imageUrl={user.imageUrl} />
      ))}
    </div>
  );

  const ProtecedProfileList = withPermission(ProfileList);

  return (
    <>
      <ProtecedProfileList hasPermission={hasPermission} />
      {!hasPermission ? (
        <button
          onClick={() => {
            setHasPermission(true);
          }}
        >
          Receber autorização
        </button>
      ) : (
        <></>
      )}
    </>
  );
}

export default App;
