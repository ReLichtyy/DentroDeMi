import { chromium } from "playwright";
const b = await chromium.launch(); const p = await b.newPage();
await p.addInitScript(() => { localStorage.setItem("dm2-reduce", "true"); });
p.on("console", (m) => console.log("console:", m.type(), m.text())); p.on("pageerror", (e) => console.log("pageerror:", e.message));
await p.goto("http://127.0.0.1:5180/#/jugar/llaves/n3"); await p.waitForTimeout(1500);
console.log((await p.evaluate(() => document.getElementById("app").innerText)).slice(0, 400));
await b.close();
