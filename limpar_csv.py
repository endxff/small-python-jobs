"""Limpa um CSV: remove duplicados, apara espacos, padroniza e-mails e telefones."""
import csv, re, sys

def limpar(entrada, saida):
    vistos, linhas = set(), []
    with open(entrada, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            r = {k.strip().lower(): (v or "").strip() for k, v in r.items()}
            r["nome"] = r["nome"].title()
            r["email"] = r["email"].lower()
            r["telefone"] = re.sub(r"\D", "", r["telefone"])
            if r["email"] in vistos or not r["email"]:
                continue
            vistos.add(r["email"])
            linhas.append(r)
    with open(saida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["nome", "email", "telefone"])
        w.writeheader(); w.writerows(linhas)
    return len(linhas)

if __name__ == "__main__":
    print(limpar(sys.argv[1], sys.argv[2]), "linhas salvas")
