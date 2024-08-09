import React from "react";
import "../../app/globals.css";

export default function Container({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return <div className="container ">{children}</div>;
}
