import { useSelector } from "react-redux";

const useCartItems = () => useSelector((state) => state.cart);

const useTotalValue = () =>
  useSelector((state) =>
    state.cart.reduce((total, item) => total + item.price * item.quantity, 0),
  );

const useCartLastId = () =>
  useSelector((state) =>
    state.cart.reduce((max, item) => Math.max(max, item.id), 0),
  );

export { useCartItems, useTotalValue, useCartLastId };
