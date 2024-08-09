import "../../globals.css";
import Link from "next/link";
import Image from "next/image";

export default function Header() {
  return (
    <header className="header">
      <Link href="/">
        <Image
          src="https://static.vecteezy.com/system/resources/previews/018/930/721/non_2x/blogger-logo-blogger-icon-transparent-free-png.png"
          className="logo"
          height="50"
          width="50"
          alt="logo"
        />
      </Link>

      <nav className="nav">
        <Link href="/"> Home </Link>
        <Link href="../../posts"> Posts </Link>
      </nav>
    </header>
  );
}
