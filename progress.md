Original prompt: Terminar el juego-app "Dentro de Mí" como está pensado en el plan (doc "Dentro de Mí - Contenido del MVP", pasos 1 a 5), stack simple, web, con puerto para verlo.

# Estado

App estática: `index.html`, `styles.css`, `data.js` (contenido del doc), `app.js` (SPA por hash). Sin build.
Servidor: `python -m http.server 5173` en esta carpeta. URL: http://localhost:5173

QA con Playwright: `cd qa && node run.mjs` (capturas en `qa/shots/`). Recorre los 5 escenarios, prueba decisión de riesgo primero en los escenarios pares, comprueba desborde móvil y errores de consola.

# Hecho

- 5 escenarios completos (efecto, decisión, día siguiente, repetición/recuperación, cierre, pregunta).
- Niveles con color + icono + texto + borde (no solo color), rangos, dato incierto, certeza y fuente.
- Reglas de transición: decisión de riesgo sube solo el indicador respaldado en la etapa siguiente; la protectora lo marca como ayuda.
- Cierre sin culpa si el primer intento fue de riesgo.
- Funciones sobre el personaje (se tocan y llevan a la explicación).
- Efectos por concepto (atención, memoria, coordinación, juicio, pulso, sueño), ciclo de nicotina, capas de combinación.
- Emergencia: riesgo crítico muestra 911 e IAFA en grande. Ayuda fija en todas las pantallas.
- Modo docente, reducir movimiento, sonido opcional con volumen, modo oscuro automático.
- Pausa real ante riesgo crítico (hay que confirmar "Entendí qué hacer" para continuar) y animación de amanecer en recuperación.
- Modo oscuro verificado con capturas (`qa/dark.mjs`).
- Bug corregido: `[hidden]` era anulado por `.btn`, los botones ocultos se veían.
- Progreso: decisiones protectoras y preguntas acertadas (sin puntos por consumir).

# Pendiente / sugerencias

- Personaje es un SVG simple; falta ilustración final y expresiones por función.
- Revisión profesional de todo lo marcado TODO_REVISAR_PROFESIONAL antes de publicar. Fuentes no verificadas en origen.
- Probar en dispositivo táctil y con lector de pantalla.

---
# v2 (rediseño): juego de historias

Original prompt v2: hacer la página más sencilla e interactiva, que se sienta como juego, con casos específicos a los que entrar, historia detrás y lenguaje directo sobre lo que de verdad pasa. Ya sin seguir el plan original.

- 5 casos con historia y ramas (53 caminos, 21 finales). Cuerpo en vivo con 4 niveles por función, puntos de cuidado, volver a la última decisión.
- Entrada directa: `#/caso/ID`, `#/jugar/ID` y `#/jugar/ID/ESCENA`. Guía por sustancia: `#/guia/ID`.
- QA: `cd qa && node run.mjs` recorre todos los caminos por la UI.
- Pendiente: ilustraciones propias, revisión profesional del contenido (las fuentes no se verificaron en origen), probar en táctil y lector de pantalla.
