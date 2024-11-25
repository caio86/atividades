import { useTheme } from "../context/ThemeContext";

const DisplayTheme = () => {
  const { theme } = useTheme();

  return (
    <div>
      <p>Tema atual: {theme}</p>
    </div>
  );
};

export default DisplayTheme;
