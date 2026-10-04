// QA v2: recorre TODOS los caminos de todos los casos por la interfaz real.
import { chromium } from "playwright";
import fs from "node:fs";
import { fileURLToPath } from "node:url";
const BASE = process.env.URL || "http://127.0.0.1:5180/";
const out = fileURLToPath(new URL("./shots/", import.meta.url));
fs.mkdirSync(out, { recursive: true });
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
await ctx.addInitScript(() => { localStorage.setItem("dm2-reduce", "true"); localStorage.setItem("dm2-name", '"Alex"'); });
const page = await ctx.newPage();
const errors = [];
page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
page.on("pageerror", (e) => errors.push("pageerror: " + e.message));
const shot = (n) => page.screenshot({ path: `${out}${n}.png` });

await page.goto(BASE, { waitUntil: "networkidle" }); await shot("home");
await page.goto(BASE + "#/casos"); await page.waitForTimeout(300); await shot("casos");

// enumerar caminos desde los datos
const paths = await page.evaluate(() => {
  const res = {};
  for (const c of CASES) {
    const all = [];
    const walk = (id, seq, seen) => {
      const n = c.nodes[id];
      if (!n) { all.push({ seq, bad: "nodo faltante " + id }); return; }
      if (seen.includes(id)) { all.push({ seq, bad: "ciclo en " + id }); return; }
      if (n.end) { all.push({ seq, end: id }); return; }
      if (n.go) return walk(n.go, seq, [...seen, id]);
      n.c.forEach((ch, k) => walk(ch.to, [...seq, k], [...seen, id]));
    };
    walk(c.start, [], []);
    res[c.id] = all;
  }
  return res;
});
let total = 0, ok = 0;
for (const [id, list] of Object.entries(paths)) {
  const ends = new Set();
  for (const p of list) {
    total++;
    if (p.bad) { console.log("DATA ERROR", id, p.bad); continue; }
    await page.goto(BASE + "#/casos"); await page.waitForSelector(".grid");
    await page.goto(BASE + "#/jugar/" + id); await page.waitForSelector("#scene"); await page.waitForTimeout(60);
    let safe = 0, k = 0;
    while (safe++ < 40) {
      if (await page.$(".end")) break;
      if (await page.$(".choice")) { await page.click(`.choice[data-k="${p.seq[k++]}"]`); }
      else if (await page.$("#go")) { await page.click("#go"); }
      else await page.waitForTimeout(50);
    }
    const title = await page.textContent(".end h2").catch(() => null);
    if (title) { ok++; ends.add(title); }
    else console.log("NO LLEGO AL FINAL", id, JSON.stringify(p.seq));
    if (!fs.existsSync(`${out}${id}-${p.end}.png`)) await shot(`${id}-${p.end}`);
  }
  console.log(id, "caminos:", list.length, "finales distintos:", ends.size);
}
console.log("caminos completados:", ok, "de", total);

// captura de una escena a media historia (HUD con cambios) y escena inicial
await page.goto(BASE + "#/jugar/llaves"); await page.waitForTimeout(200);
await shot("play-start");
await page.click('.choice[data-k="1"]'); await page.waitForTimeout(500); await shot("play-risk");
await page.goto(BASE + "#/caso/examen"); await shot("intro");
await page.goto(BASE + "#/guia/alcohol"); await shot("guia");

// movil + overflow
await page.setViewportSize({ width: 390, height: 800 });
for (const [n, h] of [["m-home", "#/"], ["m-casos", "#/casos"], ["m-play", "#/jugar/sofi/n3"], ["m-guia", "#/guia/mezclas"]]) {
  await page.goto(BASE + h); await page.waitForTimeout(250); await shot(n);
  const off = await page.evaluate(() => [...document.querySelectorAll("body *")].filter((e) => e.getBoundingClientRect().right > innerWidth + 1 && getComputedStyle(e).position !== "fixed" && !e.closest("#doodle")).slice(0, 4).map((e) => e.tagName + "." + e.className));
  console.log("overflow", n, off.length ? off : "ok");
}
// rewind
await page.setViewportSize({ width: 1280, height: 800 });
await page.goto(BASE + "#/jugar/sofi/n3"); await page.waitForTimeout(100);
await page.click('.choice[data-k="2"]'); await page.waitForSelector(".end");
await page.click("#rew"); await page.waitForTimeout(150);
console.log("rewind vuelve a decision:", !!(await page.$(".choice")));
console.log("errores de consola:", errors.length ? errors : "ninguno");
await browser.close();
