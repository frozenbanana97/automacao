# Biblioteca para utilizar zip e unzip
import shutil
# acessa o arquivo de máscara, para mostrar as opções de back-up

with open("mascara_backup.txt") as file_object:
    # le todas as linhas
    mascaras = file_object.readlines()

caminho = []
opcao = []
tupla = ()
for i in range(len(mascaras)):
    tupla = mascaras[i].split(',')
    opcao.append(tupla[1].replace('\n', ''))
    caminho.append(tupla[0])

print('Opções de back-up...')
for i in range(len(opcao)):
    print(i,'-',opcao[i])
opc = input('Digite a opção desejada: ')

if len(opcao) > int(opc) >= 0:
    shutil.make_archive(opcao[int(opc)], 'zip', './', caminho[int(opc)])
else:
    texto = (f"Bye")
    print(texto)