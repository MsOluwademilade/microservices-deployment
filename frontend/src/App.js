import React, { useEffect, useState } from 'react';

function App() {
  const [users, setUsers] = useState([]);
  const [orders, setOrders] = useState([]);
  const [payments, setPayments] = useState([]);

  useEffect(() => {
    fetch('/api/users/1')
      .then((response) => response.json())
      .then((data) => setUsers(data));

    fetch('/api/orders/1')
      .then((response) => response.json())
      .then((data) => setOrders(data));

    fetch('/api/payments/1')
      .then((response) => response.json())
      .then((data) => setPayments(data));
  }, []);

  return (
    <div>
      <h1>Microservices Frontend</h1>
      <h2>Users</h2>
      <pre>{JSON.stringify(users, null, 2)}</pre>
      <h2>Orders</h2>
      <pre>{JSON.stringify(orders, null, 2)}</pre>
      <h2>Payments</h2>
      <pre>{JSON.stringify(payments, null, 2)}</pre>
    </div>
  );
}

export default App;