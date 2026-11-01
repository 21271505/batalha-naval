from funcoes import define_posicoes, preenche_frota, posicao_valida
i = 0 
dic_frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     
while i<10:
    if  i<1:
        tamanho = 4
        nome = "porta-aviões"
    elif i<3:
        tamanho = 3
        nome = "navio-tanque"
    elif i<6:
        tamanho = 2
        nome = "contratorpedeiro"
    else:
        tamanho = 1
        nome =  "submarino"
    print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
    linha = int(input())
    coluna = int(input())
    if i<6:
        orientacao = int(input())
        if orientacao == 1:
            orientacao = 'vertical'
        else:
            orientacao = 'horizontal'
    else:
        orientacao = "horizontal"
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    valido = posicao_valida(dic_frota,linha,coluna,orientacao,tamanho)
    if valido == False:
        print("Esta posição não está válida!")
        continue  
    dic_frota =  preenche_frota(dic_frota,nome,linha,coluna,orientacao,tamanho)
    i += 1
print(dic_frota)

