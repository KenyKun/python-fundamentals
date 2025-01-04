def conta_vogais(texto):
    # Definindo um conjunto de vogais tanto minúsculas quanto maiúsculas
    vogais = set("aeiouAEIOU")
    
    # Inicializando um contador para contar as vogais
    contador = 0
    
    # Iteramos pelos caracteres da string
    for char in texto:
        # Verificando se o caractere atual é uma vogal
        if char in vogais:
            contador += 1
    
    return contador

# Solicitamos ao usuário que insira uma string
texto = input()

# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")
