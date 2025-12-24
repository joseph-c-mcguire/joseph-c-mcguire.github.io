import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// Use an environment-provided site URL to ensure consistent absolute links
// Fallback to localhost:3000 for Docker/dev usage
const SITE_URL = process.env.PUBLIC_SITE_URL || 'http://localhost:3000';

export default defineConfig({
  site: SITE_URL,
  integrations: [tailwind()],
});
