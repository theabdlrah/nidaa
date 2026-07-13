import "./globals.css";
import "leaflet/dist/leaflet.css";

export const metadata = {
  title: "Nidaa — نداء",
  description: "Offline-first community needs & services board for Syria.",
  manifest: "/manifest.json",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ar" dir="rtl">
      <body>{children}</body>
    </html>
  );
}
