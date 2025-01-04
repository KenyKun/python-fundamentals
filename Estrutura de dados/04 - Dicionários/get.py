contatos = {"kenny@gmail.com": {"nome": "Kenny", "telefone": "94211-3045"}}

resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {})
print(resultado)

resultado = contatos.get(
    "kenny@gmail.com", {}
)
print(resultado)