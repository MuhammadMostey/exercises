"use client";
// React
import React, { useState, useEffect } from "react";

// firebase
import {
  addDoc,
  getDoc,
  deleteDoc,
  doc,
  collection,
  query,
  onSnapshot,
} from "firebase/firestore";
import { db } from "../firebase";

export default function Home() {
  const [items, setItems] = useState([
    // { name: "Coffe", price: 4.95 },
    // { name: "Movie", price: 24.95 },
    // { name: "candy", price: 7.95 },
  ]);

  const [total, setTotal] = useState(0);
  const [newItem, setNewItem] = useState({ name: "", price: "" });

  const addNewItem = async (e) => {
    e.preventDefault();
    if (newItem.name !== "" && newItem.price !== "") {
      setItems([...items, newItem]);

      // adds a transaction to the database
      await addDoc(collection(db, "items"), {
        name: newItem.name,
        price: newItem.price,
      });
    }
    setNewItem({ name: "", price: "" });
  };

  useEffect(() => {
    const q = query(collection(db, "items"));
    const unsubscribe = onSnapshot(q, (querySnapshot) => {
      let itemsArr = [];

      querySnapshot.forEach((doc) => {
        itemsArr.push({ ...doc.data(), id: doc.id });
      });
      setItems(itemsArr);

      // update total from itemsArr a snapshot of the data in the db
      const calculateTotal = () => {
        const totalPrice = itemsArr.reduce(
          (sum, item) => sum + parseFloat(item.price),
          0
        );

        // const roundedTotalPrice = Math.round(totalPrice);
        const roundedTotalPrice = totalPrice.toFixed(2);

        setTotal(roundedTotalPrice);
      };
      calculateTotal();
      return () => unsubscribe();
    });
  }, []);

  const deleteItem = async (id) => {
    await deleteDoc(doc(db, "items", id));
  };
  return (
    <main className="flex min-h-screen flex-col items-center justify-between sm:p-24 p-4">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <h1>Expense Tracker</h1>

        <div className="new-items-form-div">
          <form className="new-items-form">
            <input
              type="text"
              placeholder="Enter Expense Item"
              className="col-span-3"
              value={newItem.name}
              onChange={(e) => {
                setNewItem({ ...newItem, name: e.target.value });
              }}
            />
            <input
              type="text"
              placeholder="Enter Expesnse Amount"
              className="col-span-2"
              value={newItem.price}
              onChange={(e) => {
                setNewItem({ ...newItem, price: e.target.value });
              }}
            />
            <button type="submit" className="btn-1" onClick={addNewItem}>
              +
            </button>
          </form>

          <ul>
            {items.map((item, id) => (
              <li key={id} className="my-4 bg-slate-950 flex justify-between">
                <div className="items-list">
                  <span className="capitalize">{item.name}</span>
                  <span>{item.price}</span>
                </div>
                <button className="btn-x" onClick={() => deleteItem(item.id)}>
                  X
                </button>
              </li>
            ))}
          </ul>

          {items.length < 1 ? (
            ""
          ) : (
            <div className="flex justify-between p-3">
              <span>Total</span> <span>${total}</span>
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
