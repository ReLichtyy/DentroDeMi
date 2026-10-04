s = open('styles.css', encoding='utf8').read()
new = open('qa/new_play.css', encoding='utf8').read()
a = s.index("/* Juego */")
b = s.index("/* Final */")
c = s.index("/* Guía */")
d = s.index("#toasts")
e = s.index("/* Personaje */")
# Orden en el archivo: Juego .. Final .. Guía .. #toasts .. Personaje .. Movimiento (hasta el final)
final_and_guide = s[b:d]          # Final + Guía + (hasta toasts)
toasts = s[d:e]                   # toasts y .toast
out = s[:a] + final_and_guide + toasts + new
# la regla .home-art .char y .float usan .char: mantener compat con .port
out = out.replace(".home-art .char { width: min(250px, 60%); }", ".home-art .port { width: min(250px, 60%); }")
open('styles.css', 'w', encoding='utf8').write(out)
print(len(out))
