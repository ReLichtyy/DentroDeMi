import re
miss = []

def sub_file(path, pairs):
    t = open(path, encoding='utf8').read()
    for old, new in pairs:
        if old not in t:
            miss.append((path, old[:60]))
            continue
        t = t.replace(old, new)
    open(path, 'w', encoding='utf8').write(t)

# ------------------------------------------------------------------ index.html
sub_file('index.html', [
    ('content="Juego de decisiones reales. Tú eliges, tu cuerpo responde, y te contamos lo que de verdad pasa."',
     'content="Juego de historias para estudiantes: eliges qué hacer, ves qué le pasa a tu cuerpo y lees datos con su fuente."'),
    ('<span>Lo que de verdad pasa</span>', '<span>Guía</span>'),
])

# ------------------------------------------------------------------ app.js: hero, pasos, nav
sub_file('app.js', [
    ('<span class="kicker"><i class="ph-bold ph-game-controller"></i>Juego de decisiones reales</span>',
     '<span class="kicker"><i class="ph-bold ph-game-controller"></i>Juego para estudiantes</span>'),
    ('<p class="lead">Una noche. Una decisión. Tu cuerpo responde. Sin sermones: aquí se cuenta lo que de verdad pasa.</p>',
     '<p class="lead">Eliges qué hacer en situaciones de la vida universitaria y ves qué le pasa a tu cuerpo. Con datos claros y su fuente.</p>'),
    ('<h3>Elige qué haces</h3><p>Cada caso es una historia corta. Tus decisiones cambian cómo termina.</p>',
     '<h3>Elige una opción</h3><p>Lees una escena y decides. Cada opción lleva a un final distinto.</p>'),
    ('<h3>Toca todo</h3><p>Objetos, barras del cuerpo y fuentes: cada uno te da su contexto y su efecto.</p>',
     '<h3>Revisa lo que te rodea</h3><p>Los objetos y las barras del cuerpo se pueden tocar para ver qué significan.</p>'),
    ('<h3>Entérate de lo real</h3><p>Datos directos, con fuente, sin rodeos ni miedo barato.</p>',
     '<h3>Lee el dato</h3><p>Cada dato dice qué pasa, qué efecto tiene y de dónde sale.</p>'),
    ('<h1>Lo que de verdad pasa</h1><p>Sin rodeos: qué sientes, qué le pasa a tu cuerpo, qué es mito, cuándo es urgente y qué ayuda.</p>',
     '<h1>Guía por tema</h1><p>Qué se siente, qué le pasa al cuerpo, qué se cree sin ser cierto, cuándo es urgente y qué ayuda.</p>'),
    ('<i class="ph-bold ph-book-open-text"></i>Qué pasa de verdad</a>', '<i class="ph-bold ph-book-open-text"></i>Ver la guía</a>'),
    ('<h3><i class="ph-bold ph-flask"></i>Lo que de verdad pasó</h3>', '<h3><i class="ph-bold ph-flask"></i>Qué pasó</h3>'),
    ('<p>Cada caso es una historia distinta. Entra a donde quieras. Los puntos de abajo son los finales que ya viste.</p>',
     '<p>Cada caso es una historia distinta. Los puntos de abajo son los finales que ya viste.</p>'),
    ('Cada uno es una historia distinta. Entra a donde quieras. Los puntos de abajo son los finales que ya viste.',
     'Cada uno es una historia distinta. Los puntos de abajo son los finales que ya viste.'),
    ('Salta directo a un momento clave del caso.', 'Entra directo a un momento del caso.'),
])

# ------------------------------------------------------------------ app.js: reemplazar aboutHTML completo
j = open('app.js', encoding='utf8').read()
a = j.index("  function aboutHTML() {")
b = j.index("  function wireHome() {")
new_about = r'''  function aboutHTML() {
    const ends = CASES.reduce((a, c) => a + Object.values(c.nodes).filter((n) => n.end).length, 0);
    const cast = ["Andrés", "Sofi", "Mateo", "Vale", "Rafa"].map((n) => avatar(NPCS[n], "happy")).join("");
    const bag = [["ph-wine", "El vaso"], ["ph-key", "Las llaves"], ["ph-device-mobile", "Tu celular", 1]].map((o) => `<span class="obj ${o[2] ? "new" : ""}"><i class="ph-bold ${o[0]}"></i><span>${o[1]}</span></span>`).join("");
    return `
    <h2 class="sec-h">Qué es Dentro de Mí</h2>
    <section class="bento" aria-label="Qué es la app">
      <article class="card bc b-yellow span4"><span class="bc-ic"><i class="ph-bold ph-game-controller"></i></span><h3>Historias de la vida universitaria</h3>
        <p>Cada caso parte de algo que puede pasarte: una fiesta con auto, el examen de mañana, una amiga que no responde. Decides tú, y la historia sigue según lo que elijas.</p>
        <div class="choices-mini" aria-hidden="true"><span><b>1</b>Pedir un taxi para Sofi y para ti</span><span><b>2</b>Subirte: él dice que está bien</span></div>
        <div class="bc-foot"><span class="cast-stack">${cast}</span><span class="bc-count"><b>${CASES.length}</b> casos y <b>${ends}</b> finales</span></div></article>
      <article class="card bc span2"><span class="bc-ic"><i class="ph-bold ph-heartbeat"></i></span><h3>Barras del cuerpo</h3>
        <p>Reflejos, memoria, corazón y otras barras suben o bajan con cada decisión.</p>
        <div class="bc-demo">${miniTile("reflejos", 4)}${miniTile("foco", 2)}${miniTile("corazon", 1)}</div></article>
      <article class="card bc b-sky span3"><span class="bc-ic"><i class="ph-bold ph-flask"></i></span><h3>Datos con fuente</h3>
        <p>Cada dato tiene dos partes. Contexto: la fuente y un resumen. Efecto: qué cambia en ti.</p>
        <div class="bc-demo fact-mini"><div class="fm-row"><b>Contexto</b><span class="fm-ref"><i class="ph-bold ph-file-text"></i>NIAAA</span><span>Resumen breve de lo que dice la fuente.</span></div><div class="fm-row fx"><b>Efecto</b><span>Lo que cambia en ti, en una línea.</span></div></div></article>
      <article class="card bc span3"><span class="bc-ic"><i class="ph-bold ph-backpack"></i></span><h3>Una mochila que se llena</h3>
        <p>A medida que avanza la historia aparecen objetos en tu mochila. Tócalos para ver qué significan.</p>
        <div class="inv-grid bag-demo" aria-hidden="true">${bag}</div></article>
    </section>

    <h2 class="sec-h">Por qué importa si estudias</h2>
    <section class="why" aria-label="Por qué importa">
      <article class="card wc"><span class="bc-ic"><i class="ph-bold ph-clock-countdown"></i></span><h3>Se decide con prisa</h3><p>Casi siempre pasa en una fiesta, antes de un examen o de madrugada, sin tiempo para pensar. Practicar antes te da una idea de qué hacer.</p></article>
      <article class="card wc w-coral"><span class="bc-ic"><i class="ph-bold ph-brain"></i></span><h3>El cerebro termina de formarse tarde</h3><p>Sigue desarrollándose hasta cerca de los 25 años, y eso afecta la atención y el aprendizaje.</p><span class="chipbtn static"><i class="ph-bold ph-file-text"></i>CDC, NIDA</span></article>
      <article class="card wc w-teal"><span class="bc-ic"><i class="ph-bold ph-graduation-cap"></i></span><h3>Afecta tus notas</h3><p>Dormir poco, perder concentración o no recordar lo estudiado se nota en el examen.</p></article>
      <article class="card wc w-yellow"><span class="bc-ic"><i class="ph-bold ph-users-three"></i></span><h3>A veces te toca ayudar</h3><p>Si alguien se ve mal en una reunión, puedes ser tú quien esté ahí. Conviene saber cuándo llamar al 911.</p></article>
    </section>

    <h2 class="sec-h">Para qué sirve</h2>
    <section class="goal card" aria-label="Objetivo">
      <div class="goal-main"><span class="kicker light"><i class="ph-bold ph-target"></i>Objetivo</span><h3>Que sepas qué hacer antes de que pase.</h3>
        <p>Que puedas notar cuándo algo va mal, pensar en las consecuencias de cada opción y saber a quién pedir ayuda.</p></div>
      <div class="goal-list">
        <div class="gl"><i class="ph-bold ph-eye"></i><div><b>Notar cuando algo va mal</b><span>Qué señales indican que no es normal.</span></div></div>
        <div class="gl"><i class="ph-bold ph-scales"></i><div><b>Pensar en las consecuencias</b><span>Ver qué pasa con cada opción antes de elegir.</span></div></div>
        <div class="gl"><i class="ph-bold ph-hand-heart"></i><div><b>Saber a quién llamar</b><span>Tener a mano el 911 y el IAFA.</span></div></div>
      </div>
    </section>

    <h2 class="sec-h">Qué incluye y qué no</h2>
    <section class="isnt" aria-label="Qué incluye y qué no">
      <article class="card ic-card is"><h3><i class="ph-bold ph-check-circle"></i>Incluye</h3>
        <ul><li>Historias inventadas, basadas en situaciones reales.</li><li>Datos con su fuente.</li><li>Opciones con consecuencias distintas.</li></ul></article>
      <article class="card ic-card not"><h3><i class="ph-bold ph-x-circle"></i>No incluye</h3>
        <ul><li>Diagnósticos ni tratamientos.</li><li>Consejos médicos personales: para eso están los profesionales de salud.</li><li>Puntos por consumir. Solo suman las decisiones de cuidado.</li></ul></article>
      <p class="honest"><i class="ph-bold ph-info"></i>El contenido sigue en revisión. Las fuentes están indicadas, pero falta confirmarlas en el documento original.</p>
    </section>

    <section class="cta-row" aria-label="Ayuda y empezar">
      <article class="card help-card"><span class="bc-ic"><i class="ph-bold ph-lifebuoy"></i></span><div><h3>Si necesitas ayuda ahora</h3><p class="big">IAFA 800-IAFA-800</p><p>Emergencias: <b>911</b>. Si alguien no despierta o respira muy lento, llama sin esperar.</p></div><a class="btn btn-ghost btn-sm" href="#/guia/mezclas"><i class="ph-bold ph-book-open-text"></i>Ver qué hacer</a></article>
      <article class="card start-card"><h3>Elige un caso</h3><p>Son historias cortas. Entra por la que quieras.</p><a class="btn btn-go" href="#/casos">Ver los casos<i class="ph-bold ph-arrow-right"></i></a></article>
    </section>`;
  }

'''
j = j[:a] + new_about + j[b:]
open('app.js', 'w', encoding='utf8').write(j)

# ------------------------------------------------------------------ data.js: títulos y frases de finales
sub_file('data.js', [
    # llaves
    ('h: "El segundo que faltó"', 'h: "Choque en la curva"'),
    ('"Andrés no mentía: de verdad se sentía bien. Ese es justo el problema."', '"Andrés creía estar bien. Con alcohol tampoco lo notas."'),
    ('h: "Menos borracho, igual de arriesgado"', 'h: "Manejaste tomando menos que él"'),
    ('h: "Despierto, pero no del todo"', 'h: "Manejaste con resaca"'),
    ('h: "Bien a las 2 y bien a las 10"', 'h: "Bien a las 2 y también a las 10"'),
    ('"Elegiste bien en la noche y también en la mañana."', '"Decidiste bien de noche y también de mañana."'),
    ('"El cuerpo no pide castigo: pide agua, comida y horas."', '"Al cuerpo le sirven agua, comida y horas de sueño."'),
    ('"Anota esto: la mejor decisión de esa noche costó 12 minutos de espera."', '"La mejor decisión de esa noche costó 12 minutos de espera."'),
    # examen
    ('h: "Menos preparado, pero entero"', 'h: "Dormiste y rendiste con lo que sabías"'),
    ('h: "Pasó. Con compañía pasó más fácil"', 'h: "El pánico pasó con compañía"'),
    ('h: "La peor versión de la noche"', 'h: "Pasaste el pánico solo"'),
    ('h: "Llegaste con la cabeza completa"', 'h: "Llegaste descansado al examen"'),
    ('"No estudiaste menos tiempo: estudiaste peor."', '"Estudiaste las mismas horas, pero se guardó menos."'),
    ('"Acompañar y bajar el ritmo funciona mejor que pelear con el pánico."', '"Acompañar y bajar el ritmo ayuda más que pelear con el pánico."'),
    ('"Una persona al lado ayuda más que cualquier truco."', '"Una persona al lado ayuda más que cualquier truco para calmarte."'),
    # vapeo
    ('h: "Una pausa menos"', 'h: "Dijiste que no"'),
    ('h: "El impulso pasó. Tú te quedaste"', 'h: "Esperaste y el antojo pasó"'),
    ('"Esperar no es debilidad: es la técnica que mejor funciona."', '"Esperar sirve: el antojo baja solo en pocos minutos."'),
    ('h: "Contarlo lo desarma"', 'h: "Se lo contaste a tu hermano"'),
    ('"Lo que se cuenta en voz alta pesa menos."', '"Decirlo en voz alta ayuda a armar un plan."'),
    ('h: "Pedir ayuda no es rendirse"', 'h: "Pediste ayuda"'),
    ('h: "Ahora manda el vape"', 'h: "Sigues usándolo"'),
    ('"La dependencia no se nota hasta que quieres parar."', '"La dependencia suele notarse cuando intentas parar."'),
    ('h: "Un día más, el ciclo sigue"', 'h: "Volviste al vape"'),
    ('"Una recaída es información, no un fracaso."', '"Una recaída pasa, y se puede volver a intentar."'),
    ('"Lo que cambia las cosas es volver a intentarlo con plan."', '"Ayuda más volver a intentarlo con un plan."'),
    ('h: "Salir toma días, no años"', 'h: "Lo dejaste con un plan"'),
    # pastillas
    ('h: "Evitaste lo peor, no la noche"', 'h: "Dormiste poco, pero sin pastilla"'),
    ('"Lo que ya sabías valía más que cualquier pastilla."', '"Lo que ya sabías servía más que la pastilla."'),
    ('h: "Pedir ayuda a tiempo"', 'h: "Pediste ayuda"'),
    ('"Hay gente cuyo trabajo es ayudarte con esto, sin juzgarte."', '"Hay personas cuyo trabajo es ayudarte con esto."'),
    ('h: "Llamar a tiempo"', 'h: "Llamaste al 911"'),
    ('h: "Aguantar no era la opción"', 'h: "Esperaste con el pecho apretado"'),
    ('"Esperar a que pase es lo que más se arrepiente después."', '"Esperar a que pase es la opción de la que más gente se arrepiente."'),
    ('h: "Sin atajos, con memoria"', 'h: "Estudiaste sin la pastilla"'),
    ('"Una pastilla de otro es una apuesta con tu cuerpo, no un atajo."', '"Una pastilla de otra persona es una apuesta con tu cuerpo."'),
    # sofi
    ('h: "Una llamada cambió la noche"', 'h: "Llamaste al 911"'),
    ('h: "Diez minutos pesan"', 'h: "Esperaste diez minutos"'),
    ('"No sabes cómo termina por sí sola. No tenías por qué descubrirlo."', '"No hay forma de saber cómo habría terminado si seguías esperando."'),
    ('h: "Una ambulancia sí sabe qué hacer"', 'h: "La llevaste en carro"'),
    # hooks
    ('hook: "Dice que está perfecto para manejar. Tú decides si le crees."', 'hook: "Andrés dice que puede manejar. Tú decides si lo dejas."'),
    ('hook: "Mañana es el final. Esta noche, Mateo ofrece relajarte."', 'hook: "Mañana es el examen final y Mateo te ofrece un porro."'),
    ('hook: "Empezó con un vape de mango entre dos clases."', 'hook: "Valeria te ofrece un vape de mango entre clases."'),
    ('hook: "Una pastilla de otro, una noche, ocho horas de rendimiento. ¿Cuánto se paga?"', 'hook: "Rafa te ofrece la pastilla de su hermano para estudiar toda la noche."'),
    ('hook: "Sofi se quedó dormida en el sofá. No parece sueño normal."', 'hook: "Sofi duerme en el sofá y no responde cuando le hablas."'),
])

# ------------------------------------------------------------------ app.js: botón flotante Jugar (portada)
j = open('app.js', encoding='utf8').read()
old = '''    document.getElementById("start").addEventListener("submit", (e) => { e.preventDefault(); S.name = document.getElementById("nm").value.trim(); save(); location.hash = "#/casos"; });
  }'''
assert old in j
new = '''    const go = () => { S.name = document.getElementById("nm").value.trim(); save(); location.hash = "#/casos"; };
    document.getElementById("start").addEventListener("submit", (e) => { e.preventDefault(); go(); });
    // Botón flotante: aparece cuando ningún botón principal está a la vista.
    const fab = document.createElement("button"); fab.id = "fab"; fab.type = "button"; fab.hidden = true; fab.className = "btn btn-go fab";
    fab.innerHTML = '<i class="ph-bold ph-play"></i>Jugar'; fab.setAttribute("aria-label", "Jugar: ir a los casos");
    fab.addEventListener("click", go); document.body.appendChild(fab);
    const targets = [document.querySelector("#start .btn"), document.querySelector(".start-card .btn")].filter(Boolean);
    const vis = new Set();
    fabObs = new IntersectionObserver((es) => { es.forEach((e) => (e.isIntersecting ? vis.add(e.target) : vis.delete(e.target))); fab.hidden = vis.size > 0; }, { threshold: 0.6 });
    targets.forEach((t) => fabObs.observe(t));
  }
  let fabObs = null;
  function clearFab() { if (fabObs) { fabObs.disconnect(); fabObs = null; } const f = document.getElementById("fab"); if (f) f.remove(); }'''
j = j.replace(old, new, 1)
old2 = '    closePeek(); $toasts.innerHTML = "";'
assert old2 in j
j = j.replace(old2, '    closePeek(); $toasts.innerHTML = ""; clearFab();', 1)
open('app.js', 'w', encoding='utf8').write(j)

c = open('styles.css', encoding='utf8').read()
c += '''
/* Botón flotante Jugar (portada) */
.fab { position: fixed; z-index: 36; right: 16px; bottom: 64px; min-height: 56px; padding: 0 24px; animation: pop-in .4s var(--ease) both; }
.bag-demo { margin-top: 6px; } .bag-demo .obj { pointer-events: none; }
'''
open('styles.css', 'w', encoding='utf8').write(c)
print("no encontrados:", len(miss))
for m in miss: print(" -", m)
