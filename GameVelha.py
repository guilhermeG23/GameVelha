#Jogoda velha simples
#Jogo para dois jogadores

#Title
print('=-' * 20)
print('Jogo da Velha - Simples')
print('=-' * 20)

#Variaveis
V, jogada, peca, pecaM, primeiro, segundo, terceiro, quarto, quinto, sexto, setimo, oitavo, nono = 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

#Escolha a peça
while peca != 'x' or peca != 'o':
    peca = str(input('Escolha sua peca(X \ O): ')).lower()
    if peca == 'x':
        print('Voce escolheu X\nVamos Comecar!\n')
        peca = 'X'
        pecaInverte = 'O'
        break
    elif peca == 'o':
        print('Voce escolheu O\nVamos Comecar!\n')
        peca = 'O'
        pecaInverte = 'X'
        break
    else:
        print('Voce escolheu outra coisa\nNao vale\nEscolha denovo!\n')

#Visao tabuleiro
print('=-' * 16)
print('Tabeuleiro')
print('=-' * 16)
print('[1\t2\t3]\n[4\t5\t6]\n[7\t8\t9]')

#Logica do Jogo
while jogada != 9:
    #Peça principal
    if (jogada % 2) == 0:
        while True:
            print('Sua Peça: {}'.format(peca))
            casa = int(input('Escolha a casa: '))
            #Posicionamento da peca
            if casa == primeiro:
                primeiro = peca
                break
            if casa == segundo:
                segundo == peca
                break
            if casa == terceiro:
                terceiro = peca
                break
            if casa == quarto:
                quarto = peca
                break
            if casa == quinto:
                quinto = peca
                break
            if casa == sexto:
                sexto = peca
                break
            if casa == setimo:
                setimo = peca
                break
            if casa == oitavo:
                oitavo = peca
                break
            if casa == nono:
                nono = peca
                break
            else:
                print('A casa esta em uso\nEscolha outro!\n')
    #Peça invertida
    else:
        while True:
            if peca == 'X':
                pecaM == 'O'
            else:
                pecaM == 'X'
            print('Sua Peça: {}'.format(pecaM))
            casa = int(input('Escolha a casa: '))
            #Posicionamento da peca
            if casa == primeiro:
                primeiro = pecaInverte
                break
            elif casa == segundo:
                segundo = pecaInverte
                break
            elif casa == terceiro:
                terceiro = pecaInverte
                break
            elif casa == quarto:
                quarto = pecaInverte
                break
            elif casa == quinto:
                quinto = pecaInverte
                break
            elif casa == sexto:
                sexto = pecaInverte
                break
            elif casa == setimo:
                setimo = pecaInverte
                break
            elif casa == oitavo:
                oitavo = pecaInverte
                break
            elif casa == nono:
                nono = pecaInverte
                break
            else:
                print('Valor escolhido não existe\nEscolha outro!\n')
    
    #Contador de jogadas validas
    jogada += 1
    
    #Print resultado da jogada
    print('[{}\t{}\t{}]\n[{}\t{}\t{}]\n[{}\t{}\t{}]'.format(primeiro, segundo, terceiro, quarto, quinto, sexto, setimo, oitavo, nono))
    
    #Gerador de vitoria
    #X
    if primeiro == 'X' and segundo == 'X' and terceiro == 'X':
        V = 1
        break
    elif quarto == 'X' and quinto == 'X' and sexto == 'X':
        V = 1
        break
    elif setimo == 'X' and oitavo == 'X' and nono == 'X':
        V = 1
        break
    elif primeiro == 'X' and quarto == 'X' and setimo == 'X':
        V = 1
        break
    elif segundo == 'X' and quinto == 'X' and oitavo == 'X':
        V = 1
        break
    elif terceiro == 'X' and sexto == 'X' and nono == 'X':
        V = 1
        break
    elif primeiro == 'X' and quinto == 'X' and nono == 'X':
        V = 1
        break
    elif terceiro == 'X' and quinto == 'X' and setimo == 'X':
        V = 1
        break
    #O
    elif primeiro == 'O' and segundo == 'O' and terceiro == 'O':
        V = 2
        break
    elif quarto == 'O' and quinto == 'O' and sexto == 'O':
        V = 2
        break
    elif setimo == 'O' and oitavo == 'O' and nono == 'O':
        V = 2
        break
    elif primeiro == 'O' and quarto == 'O' and setimo == 'O':
        V = 2
        break
    elif segundo == 'O' and quinto == 'O' and oitavo == 'O':
        V = 2
        break
    elif terceiro == 'O' and sexto == 'O' and nono == 'O':
        V = 2
        break
    elif primeiro == 'O' and quinto == 'O' and nono == 'O':
        V = 2
        break
    elif terceiro == 'O' and quinto == 'O' and setimo == 'O':
        V = 2    
        break

#Confirma o vitorioso
if V == 0:
    print('Empate')
elif V == 1:
    print('X Ganhou!\nO derrotado')
elif V == 2:
    print('O Ganhou!\nX derrotado')
else:
    print('Erro Geral!')
