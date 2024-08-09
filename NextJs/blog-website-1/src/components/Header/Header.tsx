import "../../app/globals.css";
import Link from "next/link";
import Image from "next/image";
import SiteNav from "../SiteNav/SiteNav";

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

      <SiteNav />
    </header>
  );
}
