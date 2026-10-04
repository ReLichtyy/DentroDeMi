j = open('app.js', encoding='utf8').read()

old_open = '    <section class="steps">'
assert old_open in j
j = j.replace(old_open, '    <h2 class="sec-h">Cómo se juega</h2>\n    <section class="steps">', 1)

anchor = '''<p>Datos directos, con fuente, sin rodeos ni miedo barato.</p></div>
    </section>`;'''
assert anchor in j
new_tail = '''<p>Datos directos, con fuente, sin rodeos ni miedo barato.</p></div>
    </section>
    ${aboutHTML()}`;'''
j = j.replace(anchor, new_tail, 1)

fn = '''
  /* ---------- portada: qué es la app, por qué importa, objetivo ---------- */
  const miniTile = (k, v) => `<div class="tile v${v} mini" aria-hidden="true"><i class="ph-bold ${STAT[k].i} ic"></i><span class="nm">${STAT[k].n}</span><span class="cells">${[1, 2, 3, 4].map((n) => `<span class="${n <= v ? "on" : ""}"></span>`).join("")}</span><span class="lab">${STAT[k].l[v]}</span></div>`;
  function aboutHTML() {
    const ends = CASES.reduce((a, c) => a + Object.values(c.nodes).filter((n) => n.end).length, 0);
    const cast = ["Andrés", "Sofi", "Mateo", "Vale", "Rafa"].map((n) => avatar(NPCS[n], "happy")).join("");
    return `
    <h2 class="sec-h">Qué es Dentro de Mí</h2>
    <section class="bento" aria-label="Qué es la app">
      <article class="card bc b-yellow span4"><span class="bc-ic"><i class="ph-bold ph-game-controller"></i></span><h3>Un juego de decisiones reales</h3>
        <p>Vives historias cortas de la vida universitaria: una fiesta, la noche antes de un examen, un amigo que no responde. Tú decides qué haces, y cada decisión cambia cómo termina.</p>
        <div class="bc-foot"><span class="cast-stack">${cast}</span><span class="bc-count"><b>${CASES.length}</b> casos y <b>${ends}</b> finales</span></div></article>
      <article class="card bc span2"><span class="bc-ic"><i class="ph-bold ph-heartbeat"></i></span><h3>Tu cuerpo, en vivo</h3>
        <p>Reflejos, memoria, corazón y más suben o bajan según lo que eliges.</p>
        <div class="bc-demo">${miniTile("reflejos", 4)}${miniTile("foco", 2)}${miniTile("corazon", 1)}</div></article>
      <article class="card bc b-sky span3"><span class="bc-ic"><i class="ph-bold ph-flask"></i></span><h3>Datos con referencia</h3>
        <p>Cada dato real llega en dos partes: el contexto, con su referencia y resumen, y el efecto, qué cambia para ti.</p>
        <div class="bc-demo fact-mini"><div class="fm-row"><b>Contexto</b><span class="fm-ref"><i class="ph-bold ph-file-text"></i>NIAAA</span><span>Resumen breve de lo que dice la fuente.</span></div><div class="fm-row fx"><b>Efecto</b><span>Lo que cambia en ti, en una línea.</span></div></div></article>
      <article class="card bc span3"><span class="bc-ic"><i class="ph-bold ph-chat-circle-text"></i></span><h3>Sin sermones, sin miedo barato</h3>
        <p>No te dice qué está bien o mal. Te muestra qué pasa de verdad y qué decisión te cuida a ti y a los demás.</p></article>
    </section>

    <h2 class="sec-h">Por qué importa, como estudiante</h2>
    <section class="why" aria-label="Por qué importa">
      <article class="card wc"><span class="bc-ic"><i class="ph-bold ph-clock-countdown"></i></span><h3>Se decide rápido y bajo presión</h3><p>Casi nunca eliges con calma: es la fiesta, la víspera del examen o las 2 de la mañana. Practicar antes ayuda a no improvisar.</p></article>
      <article class="card wc w-coral"><span class="bc-ic"><i class="ph-bold ph-brain"></i></span><h3>Tu cerebro sigue madurando</h3><p>Hasta cerca de los 25 años sigue en desarrollo, y eso pesa en la atención y el aprendizaje.</p><span class="chipbtn static"><i class="ph-bold ph-file-text"></i>CDC, NIDA</span></article>
      <article class="card wc w-teal"><span class="bc-ic"><i class="ph-bold ph-graduation-cap"></i></span><h3>También se juega tu rendimiento</h3><p>Sueño, memoria y concentración dependen del cuerpo. Una mala noche se paga en el examen.</p></article>
      <article class="card wc w-yellow"><span class="bc-ic"><i class="ph-bold ph-users-three"></i></span><h3>Cuidar a otros también es cosa tuya</h3><p>Muchas veces eres quien está cuando alguien se ve mal. Saber qué hacer y cuándo llamar al 911 marca la diferencia.</p></article>
    </section>

    <h2 class="sec-h">El objetivo</h2>
    <section class="goal card" aria-label="Objetivo">
      <div class="goal-main"><span class="kicker light"><i class="ph-bold ph-target"></i>Objetivo</span><h3>Que decidas con información, antes de la noche difícil.</h3>
        <p>No buscamos que nadie sea perfecto. Buscamos que sepas lo que pasa, reconozcas las señales y pidas ayuda a tiempo.</p></div>
      <div class="goal-list">
        <div class="gl"><i class="ph-bold ph-eye"></i><div><b>Reconocer señales</b><span>Saber cuándo algo no es normal.</span></div></div>
        <div class="gl"><i class="ph-bold ph-scales"></i><div><b>Elegir con cuidado</b><span>Ver las consecuencias antes de decidir.</span></div></div>
        <div class="gl"><i class="ph-bold ph-hand-heart"></i><div><b>Pedir ayuda a tiempo</b><span>Tener claro a quién llamar.</span></div></div>
      </div>
    </section>

    <h2 class="sec-h">Qué es y qué no es</h2>
    <section class="isnt" aria-label="Qué es y qué no es">
      <article class="card ic-card is"><h3><i class="ph-bold ph-check-circle"></i>Esto es</h3>
        <ul><li>Educación para decidir mejor.</li><li>Historias inventadas, basadas en situaciones reales.</li><li>Información con referencia, en contexto y efecto.</li></ul></article>
      <article class="card ic-card not"><h3><i class="ph-bold ph-x-circle"></i>Esto no es</h3>
        <ul><li>Un diagnóstico ni un tratamiento.</li><li>Un reemplazo de profesionales de salud.</li><li>Una invitación a consumir: consumir nunca da puntos.</li></ul></article>
      <p class="honest"><i class="ph-bold ph-info"></i>El contenido está en revisión: las referencias están atribuidas pero pendientes de verificar en su fuente original.</p>
    </section>

    <section class="cta-row" aria-label="Ayuda y empezar">
      <article class="card help-card"><span class="bc-ic"><i class="ph-bold ph-lifebuoy"></i></span><div><h3>Si necesitas ayuda ahora</h3><p class="big">IAFA 800-IAFA-800</p><p>Emergencias: <b>911</b>. Si alguien no despierta o respira lento, llama sin esperar.</p></div><a class="btn btn-ghost btn-sm" href="#/guia/mezclas"><i class="ph-bold ph-book-open-text"></i>Qué hacer</a></article>
      <article class="card start-card"><h3>Empieza por un caso</h3><p>Son historias cortas. Puedes entrar por el que más te suene.</p><a class="btn btn-go" href="#/casos">Ver los casos<i class="ph-bold ph-arrow-right"></i></a></article>
    </section>`;
  }
'''
marker = '  function wireHome() {'
assert marker in j
j = j.replace(marker, fn + marker, 1)
open('app.js', 'w', encoding='utf8').write(j)

c = open('styles.css', encoding='utf8').read()
c += '''
/* Portada: secciones en cards */
.sec-h { font-size: clamp(1.6rem, 3.4vw, 2.3rem); margin: clamp(44px, 7vw, 76px) 0 20px; }
.bento { display: grid; gap: 18px; grid-template-columns: 1fr; }
@media (min-width: 860px) { .bento { grid-template-columns: repeat(6, 1fr); } .bento .span4 { grid-column: span 4; } .bento .span2 { grid-column: span 2; } .bento .span3 { grid-column: span 3; } }
.bc { padding: 22px; display: grid; gap: 10px; align-content: start; }
.bc h3, .wc h3 { font-size: 1.35rem; }
.bc p, .wc p { color: var(--ink-2); }
.bc-ic { display: grid; place-items: center; width: 52px; height: 52px; border: 3px solid var(--edge); border-radius: 16px; background: var(--card); color: var(--ink); font-size: 1.6rem; box-shadow: var(--shadow-sm); transform: rotate(-4deg); }
.b-yellow { background: var(--yellow); color: #10231e; } .b-yellow p { color: #10231e; opacity: .85; }
.b-sky { background: var(--sky); color: #10231e; } .b-sky p { color: #10231e; opacity: .85; }
.b-yellow .bc-ic, .b-sky .bc-ic { background: #fff; color: #10231e; }
.bc-foot { display: flex; align-items: center; gap: 14px; flex-wrap: wrap; margin-top: 6px; }
.cast-stack { display: inline-flex; } .cast-stack .cast-av { --s: 44px; margin-left: -10px; border-width: 3px; background: #fff; } .cast-stack .cast-av:first-child { margin-left: 0; }
.bc-count { font-weight: 500; } .bc-count b { font-family: "Fredoka", sans-serif; font-size: 1.2rem; }
.bc-demo { display: grid; gap: 8px; margin-top: 6px; }
.tile.mini { cursor: default; pointer-events: none; }
.fact-mini { padding: 0; border: 2.5px solid var(--edge); border-radius: 14px; overflow: hidden; background: #fff; color: #10231e; }
.fm-row { display: grid; grid-template-columns: 78px minmax(0, 1fr); gap: 4px 10px; padding: 10px 12px; font-size: .9rem; align-items: center; }
.fm-row b { font-family: "Fredoka", sans-serif; font-size: .75rem; text-transform: uppercase; letter-spacing: .03em; grid-row: span 2; }
.fm-row.fx { background: #fff7d6; border-top: 2.5px solid var(--edge); } .fm-row.fx b { grid-row: auto; }
.fm-ref { display: inline-flex; align-items: center; gap: 6px; width: fit-content; padding: 1px 10px; border: 2px solid var(--edge); border-radius: 999px; background: var(--card-2); font-weight: 600; font-size: .8rem; }

.why { display: grid; gap: 18px; grid-template-columns: 1fr; }
@media (min-width: 760px) { .why { grid-template-columns: repeat(2, 1fr); } }
.wc { padding: 22px; display: grid; gap: 10px; align-content: start; }
.w-coral { background: color-mix(in srgb, var(--coral) 24%, var(--card)); } .w-teal { background: color-mix(in srgb, var(--teal) 22%, var(--card)); } .w-yellow { background: color-mix(in srgb, var(--yellow) 32%, var(--card)); }
.wc .bc-ic { background: var(--card); }
.chipbtn.static { width: fit-content; cursor: default; background: var(--card); color: var(--ink); } .chipbtn.static:hover { transform: none; background: var(--card); }

.goal { display: grid; gap: 22px; padding: clamp(20px, 4vw, 34px); background: var(--ink); color: var(--bg); }
@media (min-width: 900px) { .goal { grid-template-columns: 1.15fr .85fr; align-items: center; } }
.goal h3 { font-size: clamp(1.8rem, 4vw, 2.7rem); margin: 12px 0 10px; }
.goal p { color: color-mix(in srgb, var(--bg) 82%, transparent); max-width: 46ch; }
.kicker.light { background: var(--yellow); color: #10231e; border-color: var(--bg); box-shadow: none; }
.goal-list { display: grid; gap: 12px; }
.gl { display: grid; grid-template-columns: 48px minmax(0, 1fr); gap: 14px; align-items: center; padding: 12px 14px; border: 2.5px solid color-mix(in srgb, var(--bg) 45%, transparent); border-radius: 16px; background: color-mix(in srgb, var(--bg) 8%, transparent); }
.gl i { display: grid; place-items: center; width: 48px; height: 48px; border-radius: 14px; background: var(--yellow); color: #10231e; font-size: 1.5rem; }
.gl b { display: block; font-family: "Fredoka", sans-serif; font-size: 1.1rem; } .gl span { font-size: .92rem; opacity: .85; }

.isnt { display: grid; gap: 18px; grid-template-columns: 1fr; }
@media (min-width: 760px) { .isnt { grid-template-columns: repeat(2, 1fr); } .isnt .honest { grid-column: 1 / -1; } }
.ic-card { padding: 22px; } .ic-card h3 { font-size: 1.35rem; display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.ic-card.is h3 i { color: var(--good); } .ic-card.not h3 i { color: var(--bad); }
.ic-card ul { margin: 0; padding-left: 20px; display: grid; gap: 8px; }
.honest { display: flex; align-items: flex-start; gap: 10px; max-width: none; padding: 12px 16px; border: 2.5px dashed var(--edge); border-radius: 14px; color: var(--ink-2); font-size: .92rem; }
.honest i { font-size: 1.2rem; color: var(--ink); flex: none; }

.cta-row { display: grid; gap: 18px; grid-template-columns: 1fr; margin-top: 26px; }
@media (min-width: 860px) { .cta-row { grid-template-columns: 1.3fr 1fr; } }
.help-card { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 16px; align-items: center; padding: 22px; background: color-mix(in srgb, var(--coral) 22%, var(--card)); }
.help-card .btn { grid-column: 1 / -1; width: fit-content; }
.help-card h3 { font-size: 1.3rem; } .help-card .big { font-family: "Fredoka", sans-serif; font-weight: 700; font-size: clamp(1.5rem, 3.4vw, 2rem); color: var(--ink); margin: 2px 0; }
.start-card { padding: 22px; display: grid; gap: 12px; align-content: center; background: var(--yellow); color: #10231e; } .start-card p { color: #10231e; opacity: .85; } .start-card h3 { font-size: 1.6rem; }
.start-card .btn { width: fit-content; }
'''
open('styles.css', 'w', encoding='utf8').write(c)
print("ok")
