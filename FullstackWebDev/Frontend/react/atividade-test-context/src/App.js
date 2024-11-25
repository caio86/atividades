import DisplayTheme from "./components/DisplayTheme";
import ThemeSwitcher from "./components/ThemeSwitcher";
import { ThemeProvider } from "./context/ThemeContext";

function App() {
  return (
    <ThemeProvider>
      <DisplayTheme />
      <ThemeSwitcher />
    </ThemeProvider>
  );
}

export default App;
