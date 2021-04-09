''' 0 1 1 l 1
    0 0 0 l 1
    1 _ I r 2
'''
arq = input("Digite o nome do arquivo a ser lido: ")

#arq = 'sameamount10-nowildcard.txt'
#arq = 'odd.txt'


with open(arq,'r') as file:
    dados = file.readlines()

linha =[]
nv_linha = []

for lin in dados:
        lin = lin.replace('\n','')
        linha.append(lin)

if linha[0] == ';S':
    esquerdas = []
    direitas = []
    novas = []
    blacklist = []
    for lin in linha:
        lin = lin.split(' ')
        if lin[0].find(';') == -1: #somando 2 ao numero dos estados pois vão ser adicionados dois no inicio
            num = int(lin[0])
            num += 2
            lin[0] = str(num)
            try:
                num2 = int(lin[4])
                num2 += 2
                lin[4] = str(num2)
            except:
                pass
            if lin[3] == 'l' and lin[4] != 'halt-accept': #quais estados são chamados apos o cabeçote ser movido a esquerda ou direita
                esquerdas.append(lin[4])
            elif lin[3] == 'r' and lin[4] != 'halt-accept':
                direitas.append(lin[4])
                if lin[0] in esquerdas and lin[1] == '_' and lin[0] not in blacklist: #salvando os que possuem movimento ao _ e criando novos movimentos estacionarios
                    novas.append(lin[0]+" I I r "+lin[4])
                    blacklist.append(lin[0])
        lin = ' '.join(lin)
        nv_linha.append(lin)
    esquerdas = list(dict.fromkeys(esquerdas))
    direitas = list(dict.fromkeys(direitas))
    for e in esquerdas:
        if e not in blacklist:
            nv_linha.append(e+" I I r "+e)

    for nova in novas:
        nv_linha.append(nova)

    i=0
    for i in range(0,len(nv_linha)-1):
        nv_linha[i] = nv_linha[i]+'\n'

    nv_linha = ''.join(nv_linha)
    nv_linha = nv_linha[0:2]+'\n0 1 1 l 1\n0 0 0 l 1\n1 _ I r 2'+nv_linha[2:]
    print(nv_linha)

    with open('novo_arquivo_S.txt','w+') as file:
        file.write(nv_linha)

elif linha[0] == ';I':
    for lin in linha: 
        lin = lin.split(' ')
        if lin[0].find(';') == -1:
            num = int(lin[0])
            num += 2
            lin[0] = str(num)
            try:
                num2 = int(lin[4])
                num2 += 2
                lin[4] = str(num2)
            except:
                pass
        lin = ' '.join(lin)
        nv_linha.append(lin)
    print(nv_linha)

#mover todos para o lado, codigo da rotina (nao funciona):
'''
0 1 x r 3
0 0 x r 3
1 _ _ r 2
2 _ X r 3
2 1 1 l 3
2 0 0 l 3
3 1 0 r 4
3 0 1 r 5
3 _ t l 3
3 x x r 3
3 t _ l 8
8 0 t r halt-accept
8 1 t r halt-accept
4 1 1 r 3
4 0 1 r 3
4 t 1 r 6
5 1 0 r 3
5 0 0 r 3
5 t 0 r 6
5 _ t l 3
6 _ t l 7
7 1 1 l 7
7 0 0 l 7
7 x x r 2
7 _ _ r 7
'''