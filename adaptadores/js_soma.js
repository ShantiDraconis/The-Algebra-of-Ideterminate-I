// Decisor JavaScript para o teste de lote cego (`../lote_cego.py`).
// Regra idiomática: `termos.reduce((s, [a, b]) => s + a / b, 0) >= 0`.
// Em JavaScript, `x / 0` é `±Infinity` ou `NaN`, sem exceção; `NaN >= 0` é `false`.
// Uso: node js_soma.js casos.txt saidas.txt
const fs = require("fs");
const [entrada, saida] = process.argv.slice(2);
const linhas = fs.readFileSync(entrada, "utf8").split("\n").filter((l) => l.trim() !== "");
const saidas = linhas.map((linha) => {
  const n = linha.trim().split(/\s+/).map(Number);
  let s = 0;
  for (let k = 0; k + 1 < n.length; k += 2) s += n[k] / n[k + 1];
  return s >= 0 ? "aprova" : "reprova";
});
fs.writeFileSync(saida, saidas.join("\n") + "\n");
