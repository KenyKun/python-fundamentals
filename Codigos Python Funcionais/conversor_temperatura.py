#Implemente uma classe ConversorTemperatura que converte temperaturas de Celsius para Fahrenheit. A classe deve incluir um método chamado celsius_para_fahrenheit que realiza o cálculo de conversão. A fórmula para converter de Celsius para Fahrenheit é:

#Fahrenheit=(Celsius×95)+32Fahrenheit=(Celsius×59​)+32

#Você também deverá criar uma instância do conversor e utilizar essa instância para realizar a conversão.

# Classe para converter temperaturas de Celsius para Fahrenheit
class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

# Entrada do usuário
celsius = float(input())

# Criação da instância do conversor
conversor = ConversorTemperatura()

# Realizando a conversão
fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)