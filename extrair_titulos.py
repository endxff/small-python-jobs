"""Baixa uma pagina HTML e salva titulos (h1-h3) e links em CSV."""
import csv, sys, urllib.request
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(s): super().__init__(); s.rows=[]; s.tag=None; s.href=None; s.buf=""
    def handle_starttag(s, t, a):
        if t in ("h1","h2","h3"): s.tag=t; s.buf=""
        if t=="a": s.href=dict(a).get("href")
    def handle_data(s, d):
        if s.tag: s.buf+=d
    def handle_endtag(s, t):
        if t==s.tag and s.buf.strip(): s.rows.append((t, s.buf.strip(), "")); s.tag=None

def extrair(origem, saida):
    html = open(origem, encoding="utf-8").read() if not origem.startswith("http") else urllib.request.urlopen(origem, timeout=20).read().decode("utf-8","ignore")
    p = P(); p.feed(html)
    with open(saida,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["nivel","texto"]); w.writerows([(a,b) for a,b,_ in p.rows])
    return len(p.rows)

if __name__ == "__main__": print(extrair(sys.argv[1], sys.argv[2]), "titulos salvos")
