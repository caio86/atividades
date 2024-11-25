import { useState } from "react";
import { useDispatch } from "react-redux";
import { useCartLastId } from "../cartSelectors";
import { addToCart } from "../cartSlice";

const Product = ({ name, price }) => {
  const [quantity, setQuantity] = useState(1);
  const dispatch = useDispatch();
  const nextID = useCartLastId() + 1;

  const handleAddToCart = () => {
    const id = nextID;
    dispatch(addToCart({ id, name, price, quantity }));
  };

  /**
   * @param e {Event}
   * */
  const handleChange = (e) => {
    e.preventDefault();
    setQuantity(e.target.value);
  };

  return (
    <div>
      <h3>{name}</h3>
      <p>Preço: {price.toFixed(2)}</p>
      <input type={"number"} value={quantity} onChange={handleChange} />
      <button onClick={handleAddToCart}>Adicionar ao carrinho</button>
    </div>
  );
};

export default Product;
