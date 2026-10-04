import { chromium } from "playwright";
const b = await chromium.launch();
for (const [name, w, h, scheme] of [["d", 1280, 900, "light"], ["m", 390, 800, "light"], ["dk", 1280, 900, "dark"]]) {
  const ctx = await b.newContext({ viewport: { width: w, height: h }, colorScheme: scheme });
  await ctx.addInitScript(() => localStorage.setItem("dm2-reduce", "true"));
  const p = await ctx.newPage(); const errs = []; p.on("pageerror", (e) => errs.push(e.message));
  await p.goto("http://127.0.0.1:5180/#/"); await p.waitForTimeout(700);
  await p.screenshot({ path: `shots/home-${name}.png`, fullPage: true });
  const off = await p.evaluate(() => document.documentElement.scrollWidth > innerWidth);
  console.log(name, "scroll horizontal:", off, "errores:", errs.length ? errs : "ninguno");
  await ctx.close();
}
await b.close();
