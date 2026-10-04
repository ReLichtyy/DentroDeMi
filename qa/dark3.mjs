import { chromium } from "playwright";
const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, colorScheme: "dark" });
await ctx.addInitScript(() => { localStorage.setItem("dm2-reduce", "true"); localStorage.setItem("dm2-name", '"Alex"'); });
const p = await ctx.newPage(); const errs = []; p.on("pageerror", (e) => errs.push(e.message));
await p.goto("http://127.0.0.1:5180/#/jugar/pastillas/n4bad"); await p.waitForSelector(".choice"); await p.waitForTimeout(300);
await p.screenshot({ path: "shots/v3-dark.png" });
console.log("errores:", errs.length ? errs : "ninguno"); await b.close();
