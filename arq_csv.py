import csv
with open("pessoas.csv", "r", encoding="utf-8") as arq:
    csv_leitor = csv.reader(arq)

    prim_linha = next(csv_leitor)

    for linha in csv_leitor:
        print(linha )
        reposta = input("Aluno esta presente(p) ou ausente(a)?")
        if reposta == "p":
            print("O aluno " + linha[0] + " da cidade " + linha[2] + " está presente!!!\n")