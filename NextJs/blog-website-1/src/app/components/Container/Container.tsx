import React from "react";
import "../../globals.css";

export default function Container({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <div>
      <div>Container</div>
      <div>{children}</div>
    </div>
  );
}
