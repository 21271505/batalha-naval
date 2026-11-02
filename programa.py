from funcoes import define_posicoes, preenche_frota, posicao_valida, posiciona_frota, faz_jogada, afundados, monta_tabuleiros
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
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador  = posiciona_frota(dic_frota)
tabuleiro = monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente)
print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
qtd_afundada_jogador =0
while qtd_afundada_jogador<=9:
    linha = int(input())
    while linha < 0 or linha > 9:
        print("Linha inválida!")
        linha = int(input())
    coluna = int(input())
    while coluna < 0 or coluna > 9:
        print("Coluna inválida!")
        coluna = int(input())
    if tabuleiro_oponente[linha][coluna] == 'X' or tabuleiro_oponente[linha][coluna] == "-":
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        continue
    else:
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
        qtd_afundada_jogador = afundados(frota_oponente, tabuleiro_oponente)
        if qtd_afundada_jogador == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
        else:
            print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    



