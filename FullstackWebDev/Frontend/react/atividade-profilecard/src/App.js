import "./App.css";
import ProfileCard from "./components/ProfileCard";

function App() {
  const userData = require("./userData.json");

  const appStyle = {
    display: "grid",
    "grid-template-columns": `repeat(${Math.min(Math.ceil(userData.length / 2), 5)}, 1fr)`,
    "justify-items": "center",
    gap: "2rem",
    padding: "2rem",
  };

  return (
    <div style={appStyle}>
      {userData.map((user) => (
        <ProfileCard name={user.name} bio={user.bio} imageUrl={user.imageUrl} />
      ))}
    </div>
  );
}

export default App;
