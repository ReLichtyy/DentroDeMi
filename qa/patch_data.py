import re, json
s = open('data.js', encoding='utf8').read()

# 1) hechos: contexto + efecto (el texto largo queda como "more")
F = {
 "El juicio se apaga primero": ("El alcohol frena la zona del cerebro que mide riesgos, antes de que te sientas borracho.", "Sientes que estás bien. Tu juicio ya no lo está."),
 "Qué le hace el alcohol al cuerpo": ("Es un depresor: ralentiza la comunicación entre neuronas.", "Reflejos, equilibrio y memoria empeoran. Pueden aparecer lagunas."),
 "Por qué un segundo pesa tanto": ("Con alcohol, el cerebro tarda más en reaccionar.", "A 60 km/h, ese retraso son metros sin frenar."),
 "Menos borracho no es sobrio": ("El alcohol afecta atención y reacción aunque te sientas bien.", "No puedes medirte por cómo te sientes. Si bebiste, no manejas."),
 "La resaca es tu cuerpo, no un castigo": ("Deshidratación, sueño roto e inflamación.", "El café despierta, no sobria. Solo el tiempo elimina el alcohol."),
 "Lo que hace el THC mientras dura": ("El THC actúa donde se forman los recuerdos y se sostiene la atención.", "Cuesta concentrarse y guardar lo nuevo mientras dura."),
 "El THC también puede dar pánico": ("Más THC puede subir la ansiedad y el pulso.", "Asusta mucho. No se sabe de antemano quién reacciona así."),
 "Dormir es parte de estudiar": ("El sueño consolida la memoria.", "Dormir poco después de estudiar borra parte de lo aprendido."),
 "Por qué engancha tan rápido": ("La nicotina activa el sistema de recompensa en segundos.", "El efecto dura poco, así que tu cerebro pide otro."),
 "El antojo pasa solo": ("Un antojo de nicotina dura pocos minutos.", "Cada vez que lo dejas pasar, pierde fuerza."),
 "La dependencia es real": ("La nicotina crea dependencia, y el cerebro madura hasta cerca de los 25.", "Sin ella llegan irritabilidad, ansiedad y mala concentración. Mejora en días."),
 "Recetada para otro no es segura para ti": ("Estos medicamentos se recetan tras evaluar a cada persona.", "Sin evaluación pueden subir el pulso y dar insomnio. Muchas pastillas sin receta son falsas."),
 "Te sientes más listo, no necesariamente lo eres": ("Sin TDAH, el beneficio para estudiar es pequeño o poco claro.", "Sientes más alerta y rindes parecido, con pulso alto y sueño roto."),
 "Cuando el cuerpo avisa, hay que escucharlo": ("Dolor de pecho, latidos muy irregulares o confusión son señales de emergencia.", "Se llama al 911. No se espera a que pase."),
 "Café y ducha: mitos que retrasan la ayuda": ("Nada sobria a alguien salvo el tiempo.", "Café y ducha no ayudan, y retrasan la llamada."),
 "Cómo distinguir sueño de emergencia": ("Mira la respiración y si despierta.", "Si no despierta, o respira lento o con pausas, es emergencia."),
 "Qué hacer mientras llega la ayuda": ("Alcohol con sedantes puede frenar la respiración.", "Llama al 911, ponla de lado, no la dejes sola y di qué tomó."),
}
def fix(m):
    h, t = m.group(1), m.group(2)
    ctx, fx = F[h]
    return 'h: "%s", ctx: %s, fx: %s, more: "%s"' % (h, json.dumps(ctx, ensure_ascii=False), json.dumps(fx, ensure_ascii=False), t)
s, n = re.subn(r'h: "([^"]+)", t: "((?:[^"\\]|\\.)*)"(?=, s: )', fix, s)
print("hechos convertidos:", n)

# 2) personaje y animo por escena, objetos tocables
NPC = {
 "llaves": {"n1":("Andrés","happy"),"n2a":("Andrés","happy"),"n2b":("Andrés","tipsy"),"n2c":("Dani","calm"),"n3":("Andrés","tipsy"),"n4crash":("Sofi","hurt"),"n4you":("Andrés","worried"),"n4taxi":("Andrés","angry"),"n4keys":("Andrés","angry"),"n5":("Andrés","tired"),"endok":("Andrés","tired"),"endgood":("Dani","proud")},
 "examen": {"n1":("Mateo","happy"),"n2smoke":("Mateo","relaxed"),"n3study":("Mateo","tired"),"n3sleep":("Mateo","calm"),"n3panic":("Mateo","worried"),"n4breathe":("Mateo","calm"),"n4alone":("Mateo","worried"),"n2break":("Mateo","relaxed"),"n2vale":("Vale","happy"),"n3good":("Vale","proud")},
 "vapeo": {"n1":("Valeria","happy"),"n2no":("Valeria","calm"),"n2try":("Valeria","happy"),"n3":("Valeria","calm"),"n4wait":("Valeria","calm"),"n4talk":("Camilo","calm"),"n4hook":("Valeria","worried"),"n5relapse":("Camilo","worried"),"n5help":("Camilo","proud"),"endbad":("Valeria","worried"),"endok":("Camilo","calm"),"endgood2":("Camilo","proud")},
 "pastillas": {"n1":("Rafa","happy"),"n2ask":("Rafa","calm"),"n2take":("Rafa","happy"),"n3":("Rafa","tired"),"n4bad":("Lucía","scared"),"n4rest":("Rafa","tired"),"n4help":("Lucía","calm"),"endcall":("Lucía","worried"),"endbad":("Lucía","scared"),"n2no":("Rafa","calm")},
 "sofi": {"n1":("Sofi","sleepy"),"n2sleep":("Sofi","sleepy"),"n2coffee":("Sofi","sleepy"),"n2check":("Sofi","sleepy"),"n3":("Sofi","out"),"n4call":("Sofi","sleepy"),"n4wait":("Sofi","out"),"n4car":("Sofi","out")},
}
OBJ = {
 "llaves": {
  "n1": [("vaso","ph-wine","El vaso","Un trago no es un vaso: depende de qué y cuánto te sirvan.","Contar vasos no sirve si no sabes qué hay dentro.")],
  "n3": [("llaves","ph-key","Las llaves","Quien tiene las llaves decide por todos.","Pedirlas incomoda diez segundos. No es una pelea."),("celu","ph-device-mobile","Tu celular","Una app de transporte llega en minutos.","Doce minutos de espera valen más que un trayecto dudoso.")],
  "n5": [("agua","ph-drop","El agua","El alcohol deshidrata.","Agua y comida ayudan al cuerpo. El café no sobria.")],
 },
 "examen": {
  "n1": [("porro","ph-flame","El porro","Fumado, el THC se siente en minutos.","Dura horas: justo las que necesitas para estudiar."),("cuaderno","ph-notebook","Tus apuntes","Llevas la mitad del temario.","Seis horas de sueño rinden más que dos de estudio nublado.")],
  "n3panic": [("pulso","ph-heartbeat","Tu pulso","El THC acelera el corazón.","Parece peligro, pero en general baja en horas. Acompañado baja más rápido.")],
 },
 "vapeo": {
  "n1": [("vape","ph-cloud","El vape","Sabor a mango y casi sin raspar.","Eso lo vuelve fácil de repetir, no menos adictivo.")],
  "n3": [("reloj","ph-timer","El reloj","Un antojo dura pocos minutos.","Cinco minutos de espera lo desarman.")],
 },
 "pastillas": {
  "n1": [("pastilla","ph-pill","La pastilla","Recetada para otra persona.","Tu cuerpo no es el suyo: no sabes cómo reaccionará."),("cafe","ph-coffee","El café","Es el tercero de la noche.","Más cafeína suma pulso y quita sueño.")],
  "n3": [("reloj","ph-alarm","El reloj","Son las 4 y el examen es a las 8.","Dormir aunque sea poco ayuda más que otra pastilla.")],
 },
 "sofi": {
  "n1": [("pastilla","ph-pill","La pastilla","Dani se la dio sin decir qué era.","Nadie sabe qué contiene ni cómo se suma al alcohol."),("vaso","ph-wine","Su vaso","Sofi tomó toda la noche.","El alcohol solo ya baja la respiración si es mucho.")],
  "n3": [("labios","ph-eye","Sus labios","Se ven pálidos.","Es falta de oxígeno: señal de emergencia."),("tel","ph-phone","El teléfono","El 911 atiende las 24 horas.","Decir qué tomó ayuda a tratarla mejor.")],
 },
}
CASE_META = {"llaves":("Andrés",None),"examen":("Mateo",None),"vapeo":("Valeria",None),"pastillas":("Rafa",None),"sofi":("Sofi","Sofi")}
ids = ["llaves","examen","vapeo","pastillas","sofi"]
pos = [s.index('id: "%s",' % i) for i in ids] + [s.index("/* Guía real")]
out = s[:pos[0]]
for k, i in enumerate(ids):
    seg = s[pos[k]:pos[k+1]]
    d, fixed = CASE_META[i]
    add = 'id: "%s", npc0: "%s", ' % (i, d) + ('fixedNpc: "%s", owner: "npc", ' % fixed if fixed else '')
    seg = seg.replace('id: "%s",' % i, add, 1)
    for node, (who, mood) in NPC[i].items():
        extra = ""
        if node in OBJ.get(i, {}):
            extra = ", o: " + json.dumps([dict(k=a, ic=b, l=c, ctx=d_, fx=e) for a, b, c, d_, e in OBJ[i][node]], ensure_ascii=False)
        seg, c = re.subn(r'(\n      %s: \{ )t:' % node, lambda m: m.group(1) + 'npc: "%s", m: "%s"%s, t:' % (who, mood, extra), seg, count=1)
        assert c == 1, (i, node)
    out += seg
out += s[pos[-1]:]
s = out

# 3) PRESETS con estilo
s = re.sub(r'window\.PRESETS = \[.*?\];', '''window.PRESETS = [
  { skin: "#f1c9a5", hair: "#3b2f2a", body: "#19b394", style: "short" },
  { skin: "#8d5a3c", hair: "#1d1410", body: "#ff6a55", style: "curly" },
  { skin: "#e0ac84", hair: "#a9552b", body: "#4aa8ff", style: "long" },
  { skin: "#c68642", hair: "#2b1b12", body: "#ffd24a", style: "cap" },
];''', s, flags=re.S)

s += '''
/* Personajes de la historia */
window.NPCS = {
  "Andrés":  { skin: "#e0ac84", hair: "#2b1b12", body: "#4a6fa5", style: "short" },
  "Sofi":    { skin: "#8d5a3c", hair: "#1d1410", body: "#ff6a55", style: "curly" },
  "Dani":    { skin: "#f1c9a5", hair: "#a9552b", body: "#2f9e7d", style: "long" },
  "Mateo":   { skin: "#c68642", hair: "#2b1b12", body: "#e8a33d", style: "cap" },
  "Vale":    { skin: "#f1c9a5", hair: "#3b2f2a", body: "#4aa8ff", style: "bun", glasses: true },
  "Valeria": { skin: "#e0ac84", hair: "#1d1410", body: "#ffd24a", style: "long" },
  "Camilo":  { skin: "#c68642", hair: "#1d1410", body: "#10231e", style: "short" },
  "Rafa":    { skin: "#f1c9a5", hair: "#3b2f2a", body: "#6f8f86", style: "curly", glasses: true },
  "Lucía":   { skin: "#8d5a3c", hair: "#1d1410", body: "#ff6a55", style: "bun" },
};
window.MOODS = { calm: "Tranquilidad", happy: "Buen ánimo", tipsy: "Con varios tragos", tired: "Cansancio", worried: "Preocupación", angry: "Enojo", scared: "Susto", sleepy: "Adormecimiento", out: "No reacciona", hurt: "Golpe", proud: "Orgullo", relaxed: "Relajación" };

/* Qué significa cada barra del cuerpo: contexto y efecto según el nivel (bajo, medio, normal). */
window.STATINFO = {
  reflejos:   { ctx: "Qué tan rápido reaccionas ante algo inesperado.", fx: ["Tardas mucho en frenar, esquivar o atrapar algo. En un carro son metros.", "Notas poco, pero ya reaccionas más tarde.", "Reaccionas con normalidad."] },
  foco:       { ctx: "Cuánto puedes sostener la atención en una cosa.", fx: ["Pierdes el hilo todo el tiempo. Leer o seguir una charla cuesta.", "Te distraes más de lo normal.", "Atención clara."] },
  memoria:    { ctx: "Si tu cerebro guarda lo que vives y estudias.", fx: ["Partes de lo que pasa no se guardan. Luego no lo recuerdas.", "Algunos detalles se borran.", "Guardas con normalidad."] },
  juicio:     { ctx: "La parte que mide riesgos y consecuencias.", fx: ["Subestimas el peligro y te sientes bien decidiendo mal.", "Decides un poco más a la ligera.", "Mides los riesgos con claridad."] },
  aire:       { ctx: "Qué tan bien respira el cuerpo, incluso dormido.", fx: ["Respira muy poco o con pausas largas. Es emergencia.", "Respira más lento de lo normal.", "Respiración normal."] },
  corazon:    { ctx: "El pulso y la presión: qué tanto trabaja el corazón.", fx: ["Late muy fuerte o irregular. Puede ser emergencia.", "Late más rápido de lo normal.", "Pulso tranquilo."] },
  animo:      { ctx: "Cómo estás por dentro: calma, nervios, ánimo.", fx: ["Ansiedad o pánico que cuesta controlar.", "Estás más inquieto o irritable.", "Ánimo estable."] },
  sueno:      { ctx: "Si tu cuerpo logra descansar.", fx: ["Casi sin dormir. Mañana el cerebro rinde mucho menos.", "Duermes menos de lo que necesitas.", "Descansado."] },
  conciencia: { ctx: "Si la persona despierta y responde.", fx: ["No despierta ni responde. Llama al 911.", "Muy adormilada: responde poco.", "Despierta y responde."] },
};

/* Quién es cada fuente. Atribuidas por conocimiento previo; pendientes de verificar en el original. */
window.SOURCES = {
  "NIAAA": { n: "NIAAA", full: "Instituto Nacional sobre el Abuso de Alcohol y Alcoholismo (EE. UU.)", what: "Investiga el alcohol y publica guías para público general." },
  "NIDA":  { n: "NIDA", full: "Instituto Nacional sobre el Abuso de Drogas (EE. UU.)", what: "Investiga drogas, adicción y cerebro. Tiene guías por sustancia." },
  "CDC":   { n: "CDC", full: "Centros para el Control y la Prevención de Enfermedades (EE. UU.)", what: "Salud pública: tabaco, vapeo, sueño y seguridad vial." },
};
'''
open('data.js', 'w', encoding='utf8').write(s)
