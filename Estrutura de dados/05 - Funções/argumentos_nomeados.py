def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Hyundai", "Creta", 2023, "ABC-1234")
salvar_carro(marca="Hyundai", modelo="Creta", ano=2023, placa="ABC-1234")
salvar_carro(**{"marca": "Hyundai", "modelo": "Creta", "ano": 2023, "placa": "ABC-1234"})