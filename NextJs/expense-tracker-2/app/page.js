"use client";
import React, { useState, useEffect } from "react";

export default function Home() {
  const [items, setItems] = useState([
    { name: "Coffe", price: 4.95 },
    { name: "Movie", price: 24.95 },
    { name: "candy", price: 7.95 },
  ]);

  const [total, setTotal] = useState(0);

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
            />
            <input
              type="text"
              placeholder="Enter Expesnse Amount"
              className="col-span-2"
            />
            <button type="submit" className="btn-1">
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
                <button type="submit" className="btn-x">
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
