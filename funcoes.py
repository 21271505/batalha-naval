def define_posicoes(linha,coluna,orientacao,tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao=="vertical":
            posicoes.append([linha + i,coluna])
        else:
            posicoes.append([linha,coluna+i])
    return posicoes
def preenche_frota(dic_frota,nome_navio,linha,coluna,orientacao,tamanho):
    if nome_navio not in dic_frota:
        dic_frota[nome_navio] = []
    dic_frota[nome_navio].append(define_posicoes(linha,coluna,orientacao,tamanho))
    return dic_frota
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(dic_frota):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0]*10)
    for lista_total in dic_frota.values():
        for lista in lista_total:
            for linha , coluna in lista:
                tabuleiro[linha][coluna] = 1
    return tabuleiro
def afundados(frota,tabuleiro):
    total = 0
    for tipo in frota:
        for navio in frota[tipo]:
            afundou = True
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
            if afundou:
                total +=1 
    return total             
def posicao_valida(dic_frota,linha,coluna,orientacao,tamanho):
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    for linha , coluna in posicoes:
        if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
            return False
        for lista_total in dic_frota.values():
            for navio in lista_total:
                if [linha , coluna] in navio:
                    return False
    return True