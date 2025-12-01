import type { ReactNode } from "react";
import type { Metadata } from "next";
import { ConfigProvider } from "antd";
import "./globals.css";

export const metadata: Metadata = {
  title: "Blaziken Fund",
  description: "Pokemon RWA Fund Manager Agent for Poketrade.fun on Base",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <ConfigProvider
          theme={{
            token: {
              colorPrimary: "#f97316",
              colorBgLayout: "#020617",
            },
          }}
        >
          {children}
        </ConfigProvider>
      </body>
    </html>
  );
}
