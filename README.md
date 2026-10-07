<div align="center">

<h3><code>vikas@github ~ $ ./contributions.sh</code></h3>

<img src="./contrib-heatmap.svg" width="860" alt="Contribution heatmap" />

<br><br>

<h3><code>vikas@github ~ $ whoami</code></h3>

<table>
  <tr>
    <td valign="top"><img src="./vikas-ascii.svg" width="370" alt="ASCII portrait of Vikas" /></td>
    <td valign="top"><img src="./info-card.svg" width="490" alt="Vikas Kushwaha: Software Engineer, JavaScript, TypeScript, React, Next.js, Node.js" /></td>
  </tr>
</table>

<br>

<h3><code>vikas@github ~ $ cat ./projects/scrawlspace.md</code></h3>

<a href="https://scrawlspace.vercel.app"><img src="https://img.shields.io/badge/Live-scrawlspace.vercel.app-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Scrawlspace live" /></a>

</div>

### ✏️ Scrawlspace

A hand-drawn infinite whiteboard with **live cards** (to-dos, code snippets, tables and runnable API requests), real-time multiplayer with **end-to-end encryption**, no sign-in. It also hosts a suite of browser-only developer tools.

**What it does**

- **Canvas engine built from scratch:** infinite pan/zoom, rough sketchy shapes, pressure-style pen, text, images, undo/redo, box-select, layers, lock, search
- **Live cards:** notes, checklists, code with syntax highlighting for 13 languages, editable tables, and an **API client card** that sends requests through a server-side proxy (no CORS problems), with curl import/export
- **Multiplayer:** shareable rooms with live cursors. Boards are encrypted in the browser with **AES-GCM**, and the key stays in the URL fragment, so the server never sees it
- **Multiple boards** with live previews, encrypted read-only snapshot links, PNG and `.scrawl` export
- **Installable PWA:** works offline, opens `.scrawl` files, prompts when an update is ready
- **Tool hub:** diff checker, JSON viewer, CSS formatter, JWT/hash/UUID/encoding/timestamp utilities, an in-browser **PDF editor** (sign, highlight, merge, reorder) and image tools (compress, resize, crop, WebP/AVIF via WebAssembly, SVG optimizer, favicon and OG-image generators)

**How it's built**

| Layer | Tech |
|---|---|
| Frontend | React 19, TypeScript, Vite, a custom canvas renderer, Rough.js, perfect-freehand, Motion for animation |
| Realtime | Socket.IO relay. Clients encrypt and decrypt everything with the Web Crypto API |
| Backend | Node.js and Express: collab relay, encrypted blob storage, an API proxy with SSRF protection (blocks private IPs, checks DNS and redirects) |
| Storage | localStorage + IndexedDB on the client; Vercel Blob for encrypted rooms and links |
| In-browser processing | pdf.js + pdf-lib, libavif (WASM in a Web Worker), SVGO, Prism |
| Deploy | Vercel (static app + serverless functions); Render for the WebSocket server |

Each tool lives in its own folder and is registered in a single `registry.ts`. Routing, the hub card and a separate lazy-loaded bundle are generated from that one entry.

<div align="center">

<br>

<h3><code>vikas@github ~ $ ls ./stack</code></h3>

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="36" alt="JavaScript" />
<img width="10" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" height="36" alt="TypeScript" />
<img width="10" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" height="36" alt="React" />
<img width="10" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg" height="36" alt="Next.js" />
<img width="10" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg" height="36" alt="Tailwind CSS" />
<img width="10" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" height="36" alt="Node.js" />
<img width="10" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" height="36" alt="MongoDB" />
<img width="10" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" height="36" alt="MySQL" />
<img width="10" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="36" alt="HTML5" />
<img width="10" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="36" alt="CSS3" />

<br><br>

<h3><code>vikas@github ~ $ cat contact.txt</code></h3>

<a href="https://www.linkedin.com/in/vikas-kushwaha-098844297/"><img src="https://img.shields.io/badge/LinkedIn-vikas--kushwaha-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="https://github.com/Tracevikas"><img src="https://img.shields.io/badge/GitHub-Tracevikas-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>

</div>
