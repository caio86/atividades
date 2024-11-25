import Cart from "./features/cart/components/Cart";
import Product from "./features/cart/components/Product";

function App() {
  const produtosAVenda = [
    {
      name: "caneta",
      price: 0.99,
    },
    {
      name: "fone de ouvidos",
      price: 9.99,
    },
  ];

  const produtosAVendaStyle = {
    display: "flex",
    justifyContent: "space-between",
    flexDirection: "column",
  };

  const appStyle = {
    display: "flex",
    flexDirection: "row-reverse",
    padding: "2rem",
    justifyContent: "space-between",
  };

  return (
    <div style={appStyle}>
      <div style={produtosAVendaStyle}>
        <h1>Produtos</h1>
        {produtosAVenda.map((produto) => (
          <Product key={produto.name} {...produto} />
        ))}
      </div>
      <Cart />
    </div>
  );
}

export default App;
