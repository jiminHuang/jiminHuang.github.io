// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://jiminhuang.github.io",
  integrations: [
    sitemap({
      changefreq: "weekly",
      filter: (page) => !page.includes("404"),
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
