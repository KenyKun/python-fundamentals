arquivo = open('Manipulação de Arquivos\lorem.txt', 'r')

#print(arquivo.read()) - ler tudo de uma vez
#print(arquivo.readline()) - ler linha a linha
#print(arquivo.readlines()) - ler tudo como lista

#tip
#while len(linha := arquivo.readline()):
#    print(linha)
arquivo.close()