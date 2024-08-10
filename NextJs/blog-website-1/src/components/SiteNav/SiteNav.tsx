"use client";

import "../../app/globals.css";
import Link from "next/link";
import { usePathname } from "next/navigation";

const RoutePaths = [
  { Label: "Home", path: "/" },
  { Label: "Posts", path: "/posts" },
  { Label: "Write a post", path: "/submit-post" },
];

export default function SiteNav() {
  const pathname = usePathname();
  // console.log(pathname);
  return (
    <nav>
      <ul className="flex gap-x-5 text-[14px]">
        {RoutePaths.map((route) => (
          <li key={route.path}>
            <Link
              href={route.path}
              className={`transition font-bold text-white ${
                pathname === route.path ? "text-blue-300" : ""
              }`}
            >
              {route.Label}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
}
