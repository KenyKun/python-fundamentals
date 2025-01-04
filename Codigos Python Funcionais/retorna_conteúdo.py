#Desenvolva uma função que receba duas listas de números inteiros separados por espaço e retorne uma lista contendo apenas os elementos que são comuns a ambas as listas, sem duplicatas.

# Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:
def elementos_comuns(lista1, lista2):
    # Converte os elementos das listas para inteiros e cria conjuntos
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    
    # Retorna a lista dos elementos comuns
    return list(set1.intersection(set2))

# Leitura das listas sem prompts de entrada
lista1 = input().split()
lista2 = input().split()

# Verifica se todos os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")
