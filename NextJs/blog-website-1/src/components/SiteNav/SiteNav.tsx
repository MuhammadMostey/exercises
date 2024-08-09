import "../../app/globals.css";
import Link from "next/link";

const RoutePaths = [
  { Label: "Home", path: "/" },
  { Label: "Posts", path: "/posts" },
];

export default function SiteNav() {
  return (
    <nav>
      <ul className="flex gap-x-5 text-[14px]">
        {RoutePaths.map((route) => (
          <li key={route.path}>
            <Link href={route.path}>{route.Label}</Link>
          </li>
        ))}
      </ul>
    </nav>
  );
}
