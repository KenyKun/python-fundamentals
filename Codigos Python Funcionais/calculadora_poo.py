#O desafio consiste em implementar uma classe Calculadora que utilize os princípios da Programação Orientada a Objetos (POO). A classe deve conter um método para realizar a operação de soma entre dois números inteiros, encapsulando assim a lógica matemática da adição.

def contar_caracteres(string):
    # Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres
    contador = {}
    
    # Itere através de cada caractere na string
    for char in string:
        # Verifique se o caractere já está presente no dicionário contador
        if char in contador:
            # Se estiver, incremente o valor associado a essa chave
            contador[char] += 1
        else:
            # Caso contrário, adicione a chave ao dicionário com valor inicial 1
            contador[char] = 1
    
    return contador

# Solicita entrada do usuário sem prompt
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)
