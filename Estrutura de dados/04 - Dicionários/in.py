contatos = {
    "kenny@gmail.com": {"nome": "Kenny", "telefone": "94211-3045"},
    "kaue@gmail.com": {"nome": "Kaue", "telefone": "94211-3046"},
    "skyler@gmail.com": {"nome": "Skyler", "telefone": "94211-3047"},
    "skye@gmail.com": {"nome": "Skye", "telefone": "94211-3048"},
}

resultado = "kenny@gmail.com" in contatos
print(resultado)

resultado = "meken@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["kenny@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["kaue@gmail.com"]
print(resultado)