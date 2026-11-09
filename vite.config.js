import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// The site ships as a pre-built production bundle (js/, css/) — Vite is used
// as the dev server here, and `npm run build` copies the files to dist/
// untouched so the deployed output stays identical to the original site.
// When components get extracted into src/, Vite/Rollup will take over bundling.
export default defineConfig({
  plugins: [react()],
});
