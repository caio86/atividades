import { useEffect } from "react";
import useLocalStorage from "./hooks/useLocalStorage";
import logo from "./logo.svg";
import "./AppContent.css";
import ProfileCard from "./components/ProfileCard";
import { useTheme } from "./ThemeProvider";

function AppContent() {
  const [imageURL, setImageURL] = useLocalStorage("imageURL", null);
  const { theme, toggleTheme } = useTheme();

  useEffect(() => {
    if (imageURL) {
      return;
    }

    fetch("https://picsum.photos/300")
      .then((res) => res.blob())
      .then((blob) => {
        const reader = new FileReader();

        reader.onload = () => {
          const base64Image = reader.result;

          setImageURL(base64Image);
        };

        reader.readAsDataURL(blob);
      })
      .catch((err) => console.error(err));
  }, []);

  console.log(imageURL);

  const userData = {
    name: "Hunt Oneil",
    bio: "Sint Lorem eu reprehenderit sit est consectetur mollit eu occaecat irure aliquip qui magna.",
    imageUrl: imageURL,
  };

  return (
    <div className={theme === "light" ? "light-theme" : "dark-theme"}>
      <header className="App-header">
        {imageURL ? (
          <ProfileCard
            name={userData.name}
            bio={userData.bio}
            imageUrl={userData.imageUrl}
          />
        ) : (
          <img src={logo} className="App-logo" />
        )}
        <button className="btn" onClick={toggleTheme}>
          Alternar tema
        </button>
      </header>
    </div>
  );
}

export default AppContent;
