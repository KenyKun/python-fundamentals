contatos = {
    "kenny@gmail.com": {"nome": "Kenny", "telefone": "94211-3045"},
    "kaue@gmail.com": {"nome": "Kaue", "telefone": "94211-3046"},
    "skyler@gmail.com": {"nome": "Skyler", "telefone": "94211-3047"},
    "skye@gmail.com": {"nome": "Skye", "telefone": "94211-3048"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)