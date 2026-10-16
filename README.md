<div align="center">

<h1>Vikas Kushwaha</h1>

<p><strong>Software Engineer</strong> · Full-stack web developer working with <strong>JavaScript, TypeScript, React, Next.js and Node.js</strong></p>

<h3><code>vikas@github ~ $ ./contributions.sh</code></h3>

<img src="./contrib-heatmap.svg" width="860" alt="Vikas Kushwaha GitHub contribution heatmap" />

<br><br>

<h3><code>vikas@github ~ $ whoami</code></h3>

<table>
  <tr>
    <td valign="top"><img src="./vikas-ascii.svg" width="370" alt="ASCII art portrait of Vikas Kushwaha, software engineer" /></td>
    <td valign="top"><img src="./info-card.svg" width="490" alt="Vikas Kushwaha, Software Engineer at Square Yards: JavaScript, TypeScript, React, Next.js, Tailwind CSS, Node.js, MongoDB, MySQL" /></td>
  </tr>
</table>

<p>
I'm Vikas Kushwaha, a software engineer building web apps at Square Yards.<br>
I work across the stack: React, Next.js and Tailwind CSS on the frontend, Node.js, MongoDB and MySQL on the backend.<br>
Right now I'm learning Next.js internals and React Server Components.
</p>

<br>

<h3><code>vikas@github ~ $ ls ./projects</code></h3>

<table>
  <tr>
    <td><a href="https://vikaskushwaha.vercel.app/"><strong>Portfolio</strong></a></td>
    <td>My developer portfolio (<a href="https://github.com/Tracevikas/portfoliov2">source</a>)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Tracevikas/scrawlspace"><strong>Scrawlspace</strong></a></td>
    <td>Real-time multiplayer whiteboard with live cards: to-dos, code snippets, tables, Mermaid diagrams and runnable API requests, end-to-end encrypted</td>
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

<a href="https://vikaskushwaha.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-vikaskushwaha.vercel.app-39d353?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Vikas Kushwaha portfolio" /></a>
<a href="https://www.linkedin.com/in/vikas-kushwaha-098844297/"><img src="https://img.shields.io/badge/LinkedIn-vikas--kushwaha-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Vikas Kushwaha on LinkedIn" /></a>
<a href="https://github.com/Tracevikas"><img src="https://img.shields.io/badge/GitHub-Tracevikas-181717?style=for-the-badge&logo=github&logoColor=white" alt="Vikas Kushwaha on GitHub" /></a>

</div>
