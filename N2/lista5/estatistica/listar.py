import csv

def ler_csv(caminho):
    dados = []
    with open(caminho, newline='') as f:
        leitor = csv.DictReader(f)

        for  linha in leitor:

            for chave, valor in linha.items():
                try:
                    linha[chave] = int(float(valor))
                except ValueError:
                    pass

            dados.append(linha)
    return dados
    