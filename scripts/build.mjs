import { cpSync, mkdirSync, rmSync } from 'node:fs';

// Copies the pre-built site into dist/ verbatim — no re-bundling, so the
// output is byte-identical to the original production build.
const entries = [
  'index.html',
  'js',
  'css',
  'fonts',
  'images',
  'work',
  'about',
  'assets',
  'case',
  'index',
  'share',
  'share.jpg',
  'logo-sadiq.svg',
];

rmSync('dist', { recursive: true, force: true });
mkdirSync('dist', { recursive: true });
for (const entry of entries) {
  cpSync(entry, `dist/${entry}`, { recursive: true });
}
console.log(`dist/ built (${entries.length} entries copied)`);
