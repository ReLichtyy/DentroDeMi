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

---
# v3: contexto y efecto, personaje a la derecha

- Fondo propio: líneas de señal con latido + brillo de color por caso (sin puntos ni cuadrícula).
- Datos en dos partes (Contexto y Efecto) con "Saber más" opcional. Fuente tocable (hoja con quién es y aviso de que está sin verificar).
- Pantalla de juego: tú a la izquierda (cuerpo en vivo), personaje de la historia a la derecha (retrato con 12 expresiones, fondo de escena por caso). En "Alguien no responde" las barras son de Sofi.
- Objetos de la escena tocables (+2 cuidado la primera vez) y barras del cuerpo tocables (qué significa según el nivel).
- Entrar directo a una escena aplica el cambio de cuerpo que corresponde (`jump` en data.js).
- Servidor: `python -m http.server 5180 --bind 127.0.0.1` (el 5173 lo ocupa otra app). QA: `cd qa && node run.mjs`.
- Pendiente: verificar fuentes en origen, ilustración final, probar táctil/lector de pantalla, versión móvil con HUD más compacto.

---
# v4: fondo de lienzo con figuras, mochila y referencia

- Fondo: puntos (lienzo) + figuras variadas tipo papel tapiz de chat, con los íconos de la historia (corazón, píldora, llaves, luna, etc.). Se genera en `paintDoodle()` y toma el color del caso.
- Mochila ("Tus objetos") en la tarjeta del usuario: los objetos se suman a medida que aparecen en las etapas (marca NUEVO). 23 objetos. El rebobinado restaura la mochila.
- Contexto = referencia (organización con nombre completo) + resumen. La referencia se toca para ver quién es. Sin enlaces: las fuentes siguen sin verificar.
- Nota: un parche borró reglas base de styles.css (main, h1, a, hidden); ya restauradas. Copias en `qa/*.v3.bak`.

---
# v5: portada con secciones en cards

Bajo "Cómo se juega": Qué es Dentro de Mí (bento), Por qué importa como estudiante, El objetivo, Qué es y qué no es, ayuda y llamado a jugar. Sin cifras sin verificar (solo 5 casos y 21 finales, calculados de los datos).

---
# v6: textos menos de plantilla, card nueva y boton flotante

- Reescritos titulos de finales, hooks y textos de portada (sin aforismos ni estructuras "no X, sino Y"). Nav "Guia".
- Card "Una mochila que se llena" reemplaza a "Sin sermones".
- Boton flotante Jugar en portada (IntersectionObserver sobre los botones principales).
