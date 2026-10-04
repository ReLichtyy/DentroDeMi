global.window = global; eval(require("fs").readFileSync("data.js", "utf8"));
const nodes = CASES.flatMap((c) => Object.values(c.nodes));
const miss = []; for (const c of CASES) for (const [k, n] of Object.entries(c.nodes)) if (!n.npc && !c.fixedNpc) miss.push(c.id + ":" + k);
console.log("nodos sin personaje:", miss.join(" ") || "ninguno");
console.log("hechos con ctx/fx:", nodes.filter((n) => n.fact && n.fact.ctx && n.fact.fx).length, "de", nodes.filter((n) => n.fact).length);
console.log("objetos:", nodes.reduce((a, n) => a + (n.o ? n.o.length : 0), 0));
const srcs = new Set(nodes.filter((n) => n.fact).flatMap((n) => n.fact.s.split(",").map((x) => x.trim()))); console.log("fuentes:", [...srcs].join(","), [...srcs].every((x) => SOURCES[x]));
