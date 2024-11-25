import { useTheme } from "../context/ThemeContext";

const ThemeSwitcher = () => {
  const { toggleTheme } = useTheme();

  return <button onClick={toggleTheme}>Alternar tema</button>;
};

export default ThemeSwitcher;
