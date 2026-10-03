import { chromium } from "playwright";
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1000, height: 700 } });
await p.goto("http://localhost:5173/#/jugar/sofi"); await p.waitForTimeout(800);
await p.screenshot({ path: "shots/probe.png" });
console.log(await p.evaluate(() => getComputedStyle(document.querySelector(".hud .char .body")).fill));
await b.close();
