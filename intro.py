arq = open("chamada.txt", "r", encoding="utf-8")

for linha in arq:
    print(linha.strip())
    reposta = input("Aluno esta presente(p) ou ausente(a)?")
    if reposta == "p":
        with open("presentes", "a", encoding="utf-8") as arq:
            arq.write(linha)
    else:
        with open("ausentes", "a", encoding="utf-8") as arq:
            arq.write(linha)
