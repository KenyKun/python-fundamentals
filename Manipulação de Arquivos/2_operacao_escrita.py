arquivo = open("C:/Users/Kenny/Documents/Python/Manipulação de Arquivos/teste.txt", "w")

arquivo.write('Escrevendo dados em um novo arquivo.')
arquivo.writelines(['\n', 'escrevendo', '\n','um', '\n', 'novo', '\n', 'texto'])
arquivo.close()