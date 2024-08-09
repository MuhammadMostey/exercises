// styling
import "./globals.css";

// components
import Container from "../components/Container/Container";
import Header from "../components/Header/Header";
import Footer from "../components/Footer/Footer";

//
import type { Metadata } from "next";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Computer Science Tech Blog",
  description: "Computer Science Tech Blog",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className={`${inter.className} `}>
        <Container>
          <Header />
          {children}
          <Footer />
        </Container>
      </body>
    </html>
  );
}
