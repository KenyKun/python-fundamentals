def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, motor, combustivel)

criar_carro("Palio", 2023, "ABC-1234", marca="Hyundai", motor="1.0", combustivel="Gasolina")