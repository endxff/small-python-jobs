"""Le um CSV de vendas e gera resumo por produto e por mes (total, quantidade, ticket medio)."""
import csv, sys
from collections import defaultdict

def resumir(arquivo):
    prod, mes = defaultdict(lambda: [0, 0.0]), defaultdict(float)
    with open(arquivo, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            v = float(r["valor"].replace(",", "."))
            prod[r["produto"]][0] += int(r["qtd"]); prod[r["produto"]][1] += v
            mes[r["data"][:7]] += v
    print("POR PRODUTO"); 
    for p, (q, t) in sorted(prod.items(), key=lambda x: -x[1][1]):
        print(f"  {p:<10} qtd={q:<3} total=R$ {t:>8.2f} ticket=R$ {t/q:>7.2f}")
    print("POR MES")
    for m, t in sorted(mes.items()): print(f"  {m}  R$ {t:>8.2f}")

if __name__ == "__main__": resumir(sys.argv[1])
