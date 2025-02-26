import React, { useEffect, useState } from "react";

interface Stock {
  symbol: string;
  price: number;
  id: number;
  volume: number;
}

const App: React.FC = () => {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [error, setError] = useState<string>("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/stocks")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch stocks");
        }
        return response.json();
      })
      .then((data) => setStocks(data))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div>
      <h1>Stock Market Monitor</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <table border={1} cellPadding={10}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Symbol</th>
            <th>Price</th>
            <th>Volume</th>
          </tr>
        </thead>
        <tbody>
          {stocks.map((stock) => (
            <tr key={stock.id}>
              <td>{stock.id}</td>
              <td>{stock.symbol}</td>
              <td>{stock.price}</td>
              <td>{stock.volume}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default App;