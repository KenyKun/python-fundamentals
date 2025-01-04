def verifica_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return "SIM"
    else:
        return "NÃO"

# Exemplo de uso
ano = int(input())
print(verifica_bissexto(ano))
