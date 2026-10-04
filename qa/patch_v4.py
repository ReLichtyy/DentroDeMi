import re, json

# ---------------------------------------------------------------- CSS
s = open('styles.css', encoding='utf8').read()
a = s.index("/* Fondo con identidad")
b = s.index("/* Barra superior */")
bg = '''/* Fondo tipo lienzo: puntos + figuras variadas (estilo papel tapiz de chat) con los íconos de la historia. */
body { --wash: var(--yellow); --wash2: var(--sky); }
body[data-wash="coral"] { --wash: var(--coral); }
body[data-wash="sky"] { --wash: var(--sky); }
body[data-wash="yellow"] { --wash: #e0a800; }
body[data-wash="teal"] { --wash: var(--teal); }
body[data-wash="ink"] { --wash: #6f8f86; }
body::before {
  content: ""; position: fixed; inset: 0; z-index: -2; pointer-events: none;
  background-image: radial-gradient(color-mix(in srgb, var(--ink) 14%, transparent) 1.2px, transparent 1.4px); background-size: 22px 22px;
}
#doodle { position: fixed; inset: 0; z-index: -1; pointer-events: none; overflow: hidden; color: color-mix(in srgb, var(--wash) 55%, var(--ink)); opacity: .15; transition: color .8s; }
#doodle i { position: absolute; line-height: 1; }
@media (prefers-color-scheme: dark) { #doodle { opacity: .2; } }

'''
s = s[:a] + bg + s[b:]

s += '''
/* Mochila: los objetos se suman a medida que aparecen en las etapas */
.inv { display: grid; gap: 8px; padding-top: 4px; border-top: 3px dashed var(--edge); }
.inv-h { display: flex; align-items: center; gap: 8px; font-family: "Fredoka", sans-serif; font-weight: 600; font-size: 1.05rem; padding-top: 10px; }
.inv-n { margin-left: auto; min-width: 26px; padding: 0 8px; text-align: center; border: 2.5px solid var(--edge); border-radius: 999px; background: var(--yellow); color: #10231e; font-size: .85rem; }
.inv-grid { display: flex; flex-wrap: wrap; gap: 8px; }
.inv-empty { color: var(--ink-2); font-size: .88rem; }
.inv .obj { min-height: 42px; padding: 0 12px; font-size: .88rem; gap: 6px; }
.inv .obj i { font-size: 1.15rem; }
.obj.new { animation: pop-in .5s var(--ease) both; }
.obj.new::before { content: "nuevo"; position: absolute; top: -9px; right: -6px; padding: 0 7px; border: 2px solid var(--edge); border-radius: 999px; background: var(--coral); color: #10231e; font-size: .62rem; font-weight: 700; letter-spacing: .03em; text-transform: uppercase; z-index: 1; }

/* Contexto = referencia + resumen */
.refbtn { display: flex; align-items: flex-start; gap: 10px; width: 100%; padding: 8px 10px; margin-bottom: 8px; border: 2.5px solid var(--edge); border-radius: 12px; background: var(--card-2); color: #10231e; font: inherit; text-align: left; cursor: pointer; transition: transform .15s, background .15s; }
.refbtn:hover { transform: translateX(3px); background: var(--yellow); }
.refbtn i { font-size: 1.2rem; margin-top: 1px; flex: none; }
.refbtn b { display: block; font-family: "Fredoka", sans-serif; font-size: .95rem; line-height: 1.1; }
.refbtn small { display: block; font-size: .78rem; opacity: .8; line-height: 1.25; }
.sum b { font-family: "Fredoka", sans-serif; font-size: .8rem; text-transform: uppercase; letter-spacing: .03em; margin-right: 4px; }
.frow .ctxcol { min-width: 0; }
'''
open('styles.css', 'w', encoding='utf8').write(s)

# ---------------------------------------------------------------- index.html
h = open('index.html', encoding='utf8').read()
if 'id="doodle"' not in h:
    h = h.replace('<body>', '<body>\n  <div id="doodle" aria-hidden="true"></div>', 1)
open('index.html', 'w', encoding='utf8').write(h)

# ---------------------------------------------------------------- data: más objetos y tipo de fuente
d = open('data.js', encoding='utf8').read()
OBJ = {
 "llaves": {
  "n2b": [("tragos","ph-beer-bottle","Los tragos","Nadie está contando cuántos lleva Andrés.","Sin cuenta, el juicio se apaga primero y nadie lo nota.")],
  "n4taxi": [("app","ph-taxi","La app","El carro llegó en 12 minutos.","Costó plata y evitó el riesgo más grande de la noche.")],
 },
 "examen": {
  "n3sleep": [("alarma","ph-alarm","La alarma","Suena a las 7.","Con seis horas de sueño, la mente rinde mejor que sin dormir.")],
  "n2smoke": [("reloj","ph-clock","El reloj","Pasa el tiempo y no avanzas.","El THC estira la sensación de tiempo: parece que estudiaste más.")],
 },
 "vapeo": {
  "n4hook": [("vape2","ph-cloud","Tu propio vape","Ya lo llevas a todas partes.","Tenerlo cerca hace más difícil esperar a que pase el antojo.")],
 },
 "pastillas": {
  "n2take": [("pulso","ph-heartbeat","Tu pulso","Late rápido y casi no lo notas.","Con estimulantes el pulso y la presión suben aunque te sientas bien.")],
 },
 "sofi": {
  "n2check": [("resp","ph-wind","Su respiración","La escuchas lenta.","Respiración lenta o con pausas largas es señal de emergencia.")],
 },
}
for case, nodes in OBJ.items():
    a_ = d.index('id: "%s",' % case)
    nxt = [d.find('id: "%s",' % c, a_ + 5) for c in ["llaves","examen","vapeo","pastillas","sofi"]]
    nxt = [x for x in nxt if x > a_] + [d.index("/* Guía real")]
    z = min(nxt)
    seg = d[a_:z]
    for node, objs in nodes.items():
        extra = ", o: " + json.dumps([dict(k=a2, ic=b2, l=c2, ctx=d2, fx=e2) for a2, b2, c2, d2, e2 in objs], ensure_ascii=False)
        pat = r'(\n      %s: \{ npc: "[^"]+", m: "[^"]+")(, o: \[.*?\])?(, t:)' % node
        seg, n = re.subn(pat, lambda m: m.group(1) + extra + m.group(3), seg, count=1)
        assert n == 1, (case, node)
    d = d[:a_] + seg + d[z:]
# tipo de fuente para la referencia
d = d.replace('"NIAAA": { n: "NIAAA", full:', '"NIAAA": { n: "NIAAA", type: "Instituto de investigación del gobierno de EE. UU.", full:')
d = d.replace('"NIDA":  { n: "NIDA", full:', '"NIDA":  { n: "NIDA", type: "Instituto de investigación del gobierno de EE. UU.", full:')
d = d.replace('"CDC":   { n: "CDC", full:', '"CDC":   { n: "CDC", type: "Agencia de salud pública de EE. UU.", full:')
open('data.js', 'w', encoding='utf8').write(d)

# ---------------------------------------------------------------- app.js
j = open('app.js', encoding='utf8').read()
def rep(old, new, cnt=1):
    global j
    assert old in j, old[:70]
    j = j.replace(old, new, cnt)

# quitar objetos del bloque "debajo": ahora viven en la mochila
rep('''    if (n.o) html += `<div><div class="objs-h"><i class="ph-bold ph-hand-pointing" aria-hidden="true"></i>Mira a tu alrededor</div><div class="objs" role="group" aria-label="Objetos de la escena">${n.o.map((o) => `<button class="obj ${G.seen[id + o.k] ? "seen" : ""}" type="button" data-peek="1" data-o="${o.k}"><i class="ph-bold ${o.ic}" aria-hidden="true"></i>${esc(o.l)}</button>`).join("")}</div></div>`;\n''', '')
rep('''    under.querySelectorAll("[data-o]").forEach((b) => b.addEventListener("click", () => {
      const o = n.o.find((x) => x.k === b.dataset.o);
      if (!G.seen[id + o.k]) { G.seen[id + o.k] = 1; b.classList.add("seen"); addCare(2, "Observaste"); }
      peek(o.ic, o.l, o.ctx, o.fx);
    }));
''', '')

# estado e inventario
rep('npc: null, mood: null, seen: {} };', 'npc: null, mood: null, seen: {}, inv: [] };')
rep('''<p class="tiles-hint">Toca una barra para saber qué significa.</p>`}</aside>''', '''<p class="tiles-hint">Toca una barra para saber qué significa.</p>`}
        <div class="inv" id="inv" aria-label="Tus objetos"></div></aside>''')
rep('''    $app.querySelector(".play").addEventListener("click", tileClick);''', '''    $app.querySelector(".play").addEventListener("click", tileClick);
    $app.querySelector(".play").addEventListener("click", invClick);
    paintInv();''')
rep('''  function paintYou() {''', '''  /* Mochila: los objetos se suman cuando aparecen en cada etapa. */
  function paintInv() {
    const box = document.getElementById("inv"); if (!box) return;
    box.innerHTML = `<div class="inv-h"><i class="ph-bold ph-backpack" aria-hidden="true"></i>Tus objetos<span class="inv-n">${G.inv.length}</span></div>` +
      (G.inv.length ? `<div class="inv-grid">${G.inv.map((o) => `<button class="obj ${o.seen ? "seen" : ""} ${o.isNew ? "new" : ""}" type="button" data-peek="1" data-o="${esc(o.uid)}" aria-label="${esc(o.l)}. Toca para ver contexto y efecto."><i class="ph-bold ${o.ic}" aria-hidden="true"></i><span>${esc(o.l)}</span></button>`).join("")}</div>`
        : `<p class="inv-empty">Aún no ves nada. Los objetos aparecen a medida que avanza la historia.</p>`);
  }
  function addObjects(n, id) {
    (n.o || []).forEach((o) => { const uid = `${G.c.id}:${id}:${o.k}`; if (!G.inv.some((x) => x.uid === uid)) G.inv.push({ ...o, uid, isNew: true, seen: false }); });
    paintInv(); G.inv.forEach((o) => { o.isNew = false; });
  }
  function invClick(e) {
    const b = e.target.closest("[data-o]"); if (!b || !G) return;
    const o = G.inv.find((x) => x.uid === b.dataset.o); if (!o) return;
    if (!o.seen) { o.seen = true; b.classList.add("seen"); addCare(2, "Observaste"); }
    peek(o.ic, o.l, o.ctx, o.fx);
  }
  function paintYou() {''')
rep('''    paintNpc(n);
    const talk =''', '''    paintNpc(n);
    if (!restore) addObjects(n, id);
    const talk =''')
rep('G.hist.push({ node: G.node, stats: { ...G.stats }, care: G.care, echo: G.echo, seen: { ...G.seen } });', 'G.hist.push({ node: G.node, stats: { ...G.stats }, care: G.care, echo: G.echo, seen: { ...G.seen }, inv: G.inv.map((o) => ({ ...o, isNew: false })) });')
rep('G.seen = snap.seen || {};', 'G.seen = snap.seen || {}; G.inv = snap.inv || [];')
rep('document.getElementById("care").textContent = G.care; paintYou(); enter(snap.node, true);', 'document.getElementById("care").textContent = G.care; paintYou(); paintInv(); enter(snap.node, true);')

# contexto = referencia + resumen
a1 = j.index("  function factHTML(f) {")
b1 = j.index("  function renderUnder(n, id) {")
j = j[:a1] + '''  function factHTML(f) {
    const srcs = f.s.split(",").map((x) => x.trim());
    const refs = srcs.map((s) => { const r = SOURCES[s] || { n: s, full: s, type: "" }; return `<button class="refbtn" type="button" data-peek="1" data-src="${esc(s)}" aria-label="Referencia: ${esc(r.n)}. Toca para ver quién es."><i class="ph-bold ph-file-text" aria-hidden="true"></i><span><b>${esc(r.n)}</b><small>${esc(r.full)}</small></span></button>`; }).join("");
    return `<div class="fact"><div class="fact-h"><i class="ph-bold ph-flask" aria-hidden="true"></i>${esc(f.h)}</div>
      <div class="frow"><span class="lb"><i class="ph-bold ph-info" aria-hidden="true"></i>Contexto</span><div class="ctxcol">${refs}<p class="sum"><b>Resumen</b>${esc(f.ctx)}</p></div></div>
      <div class="frow fx"><span class="lb"><i class="ph-bold ph-lightning" aria-hidden="true"></i>Efecto</span><p>${esc(f.fx)}</p></div>
      ${f.more ? `<div class="fact-f"><button class="chipbtn" type="button" data-peek="1" data-more="1"><i class="ph-bold ph-plus"></i>Saber más</button></div><div class="more" hidden>${esc(f.more)}</div>` : ""}</div>`;
  }
''' + j[b1:]
# la hoja de la fuente muestra el tipo
rep('''peek("ph-file-text", `${s.n}: ${s.full}`, s.what, "Respalda el dato de esta tarjeta.", "Atribuida por conocimiento previo. Pendiente de verificar en la fuente original.");''', '''peek("ph-file-text", `${s.n}: ${s.full}`, `${s.type ? s.type + ". " : ""}${s.what}`, "Respalda el resumen de esta tarjeta.", "Atribuida por conocimiento previo. Pendiente de verificar en la fuente original.");''')

# fondo de figuras variadas
rep('''  /* ---------- hoja de contexto y efecto ---------- */''', '''  /* ---------- fondo: figuras variadas con la identidad del juego ---------- */
  const DOODLE = ["ph-heartbeat", "ph-brain", "ph-lightning", "ph-pill", "ph-wine", "ph-cloud", "ph-moon", "ph-key", "ph-phone", "ph-scales", "ph-wind", "ph-eye", "ph-smiley", "ph-book-open-text", "ph-drop", "ph-coffee", "ph-notebook", "ph-car-profile", "ph-lifebuoy", "ph-flask", "ph-alarm", "ph-hand-heart", "ph-first-aid-kit", "ph-chats-circle", "ph-taxi", "ph-backpack"];
  function paintDoodle() {
    const el = document.getElementById("doodle"); if (!el) return;
    let seed = 7; const rnd = () => { seed |= 0; seed = (seed + 0x6D2B79F5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
    const cell = 96, rows = Math.ceil(innerHeight / cell) + 1, cols = Math.ceil(innerWidth / cell) + 1; let html = "", idx = 0;
    for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
      if (rnd() < 0.22) continue;                                   // huecos: se ve irregular, no una cuadrícula
      const ic = DOODLE[(idx++ * 7 + Math.floor(rnd() * 5)) % DOODLE.length];
      const x = c * cell + (r % 2 ? cell / 2 : 0) + (rnd() - .5) * 26, y = r * cell + (rnd() - .5) * 26;
      html += `<i class="ph ${ic}" style="left:${x.toFixed(0)}px;top:${y.toFixed(0)}px;font-size:${(24 + rnd() * 16).toFixed(0)}px;transform:rotate(${((rnd() - .5) * 56).toFixed(0)}deg)"></i>`;
    }
    el.innerHTML = html;
  }
  paintDoodle(); let rz; window.addEventListener("resize", () => { clearTimeout(rz); rz = setTimeout(paintDoodle, 200); });

  /* ---------- hoja de contexto y efecto ---------- */''')
open('app.js', 'w', encoding='utf8').write(j)
print("ok")
