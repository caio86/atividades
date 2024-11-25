import { useDispatch } from "react-redux";
import { useCartItems, useTotalValue } from "../cartSelectors.js";
import { removeFromCart } from "../cartSlice.js";

const Cart = () => {
  const cartItems = useCartItems();
  const totalValue = useTotalValue();
  const dispatch = useDispatch();

  return (
    <div>
      <h2>Carrinho</h2>
      {cartItems.length === 0 ? (
        <p>Carrinho vazio</p>
      ) : (
        <>
          <p>Valor Total: {totalValue.toFixed(2)}</p>
          <ul>
            {cartItems.map((item) => (
              <li key={item.id}>
                {item.name} - R${item.price.toFixed(2)} - QTD: {item.quantity}{" "}
                <button onClick={() => dispatch(removeFromCart(item.id))}>
                  Remover
                </button>
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
};

export default Cart;
