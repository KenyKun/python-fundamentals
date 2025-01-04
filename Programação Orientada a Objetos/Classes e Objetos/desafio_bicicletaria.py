# João tem uma biciletaria e gostaria de registrar as vendas de suas bicicletas. 
# Crie um Programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. 
# Uma Bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada")

    def correr(self):
        print("Vrummm")


        
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2.cor, b2.modelo, b2.ano)