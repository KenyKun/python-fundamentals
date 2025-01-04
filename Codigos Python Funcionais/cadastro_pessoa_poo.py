#Neste desafio, temos a classe Pessoa com seus atributos que armazenam o nome e a idade de uma pessoa. Implemente um método para retornar uma representação formatada dos dados da pessoa, crie uma instância da pessoa e, por fim, chame o método para retornar as informações formatadas e imprimir o resultado. O objetivo é utilizarmos formas para criar e manipular objetos com POO, usando atributos e métodos para encapsular dados e comportamentos.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método para retornar as informações formatadas
    def formatar_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

# Entrada do usuário
nome = input()
idade = int(input())

# Criação da instância da classe Pessoa
pessoa = Pessoa(nome, idade)

# Chamando o método para retornar as informações formatadas e imprimindo o resultado
informacoes = pessoa.formatar_informacoes()
print(informacoes)
