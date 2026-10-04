import { chromium } from "playwright";
const b = await chromium.launch();
for (const scheme of ["light", "dark"]) {
  const p = await b.newPage({ viewport: { width: 1280, height: 800 }, colorScheme: scheme });
  const errs = []; p.on("pageerror", (e) => errs.push(e.message));
  await p.goto("http://127.0.0.1:5180/#/"); await p.waitForTimeout(600); await p.screenshot({ path: `shots/bg-${scheme}-home.png` });
  await p.goto("http://127.0.0.1:5180/#/casos"); await p.waitForTimeout(300);
  await p.goto("http://127.0.0.1:5180/#/jugar/llaves"); await p.waitForTimeout(900); await p.screenshot({ path: `shots/bg-${scheme}-play.png` });
  console.log(scheme, errs.length ? errs : "ok");
}
await b.close();
