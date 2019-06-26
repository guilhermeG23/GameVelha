#Imports
from time import sleep
from random import randint

#Versao 1 -> Feita a logica
#Versao 2 -> Criado os andares
#Versao 3 -> Criado os monstros
#Versao 4 -> Feito o combate
#Versao 5 -> Ajuste do menu de combate
#Versao 6 -> Criado baus aleatorios de XP

#Criando um personagem
class Personagem:

    #Caracteristicas dos personagens
    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1
        self.andar = 1
        self.xp = 0
        self.pontos = 0
        self.vida = 0
        self.vida_atual = 0
        self.ataque = 0
        self.defesa = 0
        self.velocidade = 0
        self.agilidade = 0
        self.mana = 0
        self.mana_atual = 0
        self.classe = ""
        self.pocao_vida = 1
        self.pocao_mana = 1
        #self.habilidade1 = ""
        #self.habilidade2 = ""
        #self.habilidade3 = ""

    #Criando caracteristicas meio que aleatorios
    def atribuir_aleatorio(self):

        classes = ['Guerreiro', 'Mago', 'Ladino']
        valor_decisao = randint(0,2)

        if valor_decisao == 0:
            self.vida = randint(6, 10)
            self.ataque = randint(4, 10)
            self.defesa = randint(4, 8)
            self.velocidade = randint(1, 3)
            self.agilidade = randint(1, 3)
            self.mana = randint(1, 3)
            self.classe = classes[0]

        elif valor_decisao == 1:
            self.vida = randint(4, 7)
            self.ataque = randint(2, 6)
            self.defesa = randint(2, 4)
            self.velocidade = randint(2, 4)
            self.agilidade = randint(2, 4)
            self.mana = randint(4, 8)
            self.classe = classes[1]

        else:
            self.vida = randint(4, 6)
            self.ataque = randint(2, 4)
            self.defesa = randint(2, 4)
            self.velocidade = randint(4, 10)
            self.agilidade = randint(4, 10)
            self.mana = randint(2, 6)
            self.classe = classes[2]

        self.vida_atual = self.vida
        self.mana_atual = self.mana

        return True

    #Menu do personagem
    def menu_personagem(self, passos, andar, tipo):

        qtd_passos = int(passos)
        self.andar = andar

        while True:
            print("\n")
            print("*-" * 20)
            print("Opcoes:\n1 - Caminhar\n2 - Equipamentos\n3 - Atribuir pontos\n4 - Status\n5 - Suicidio\nH - Ajuda")
            print("*-" * 20)
            try:
                escolha = input("Entre com a opcoes: ")
                if escolha.isnumeric():
                    escolha = int(escolha)

                    #Selecao de opcoes
                    if escolha == 1:

                        #Confirmar se o andar e para produzir um BOSS

                        andar_produz_boos = int(andar) % 10

                        if  andar_produz_boos != 0:

                            #Movimento do person no andar
                            mover_aleatorio = randint(1,6)
                            qtd_passos = qtd_passos - mover_aleatorio

                            #Verificar quantidade de passos
                            if qtd_passos <= 0:
                                qtd_passos = 0
                            
                            #Mensagem  de localizacao
                            print("\n")
                            print("*-" * 20)
                            print("Andar atual: {}".format(andar))
                            print("Tamanho do andar: {} movimentos necessarios maximos".format(passos))
                            print("Quantidade restante para se mover para o proximo andar {}".format(qtd_passos))
                            print("*-" * 20)
                            print("\n")

                            if (randint(0,11) % 2) == 0:
                                #Caminho seguro
                                print("Local seguro sem monstros")
                            else:
                                #Inimigo comum
                                inimigo = Monstro()
                                inimigo.monstro_aleatorio(andar, tipo)
                                print("Local com monstros")
                                print("Monstro {} veio ataca-lo".format(inimigo.retorno_tipo()))
                                espera(2)
                                self.combate(inimigo)

                        else:
                            #Criando o BOSS
                            print("Andar do Boss!\nLute com ele para prosseguir para o proximo andar!\n Ou tente fugir a a sorte e sua mesmo!")
                            inimigo = Monstro()
                            inimigo.monstro_aleatorio(andar, tipo)
                            print("O boss {} veio ataca-lo".format(inimigo.retorno_tipo()))
                            espera(2)
                            self.combate(inimigo)

                        #Bau do tesouro
                        if randint(0,100) > 90:
                            if randint(0,100) > 51:
                                xp_receber = randint(1 ,3) * andar
                                self.xp += xp_receber

                                print("Voce encontrou um tesouro!")
                                print("Receba a quantidade de Xp do tesouro!")
                                print("Voce recebeu {} de XP".format(xp_receber))

                                self.subir_nivel()
                            else:
                                
                                if randint(0,100) > 51:
                                    print("Voce encontrou uma pocao de vida!")
                                    self.pocao_vida += 1
                                    print("Voce tem {} pocoes de vida!".format(int(self.pocao_vida)))
                                else:
                                    print("Voce encontrou uma pocao de mana!")
                                    self.pocao_mana += 1
                                    print("Voce tem {} pocoes de mana!".format(int(self.pocao_mana)))

                        #Ver se ja terminou o andar
                        if qtd_passos <= 0:
                            print("\n")
                            print("*-" * 20)
                            print("Mudar de andar!")
                            print("Voce saiu do andar {} e foi para o andar {}, parabens por ainda estar vivo!".format(int(andar), int(andar) + 1))
                            self.andar = int(andar) + 1
                            print("*-" * 20)
                            print("\n")
                            break

                    elif escolha == 2:
                        self.equipamentos()
                    elif escolha == 3:
                        self.atribuir_pontos()
                    elif escolha == 4:
                        self.status()
                    elif escolha == 5:
                        self.finalizar(True)
                    else:
                        pass
                
                else:
                    #Ajuda
                    if escolha.lower() == 'h':
                        self.ajuda()

            #Tentar interromper 
            except (KeyboardInterrupt):
                print("\n")
                print("*-" * 20)
                print("Finalizando o jogo!")
                print("*-" * 20)
                break

    #Funcao de entrar em combate
    def combate(self, inimigo):
        partidas = 0
        while True:
            if (partidas % 2) == 0:

                print("\n")
                print("*-" * 20)
                print("Opcoes:\n1 - Atacar\n2 - Status - Jogador - Inimigo\n3 - Fugir\n4 - Suicidio")
                print("*-" * 20)
                escolha = int(input("Entre com a opcoes: "))

                if escolha == 1:
                    print("Voce atacou o inimigo")

                    espera(2)
                    chance_desviar = (inimigo.velocidade + inimigo.agilidade / 2)
                    chance_acertar = (self.velocidade + self.agilidade / 2)
                    possivel_desviar = 0
                    if chance_desviar > chance_acertar:
                        possivel_desviar = 75
                    elif chance_desviar == chance_acertar:
                        possivel_desviar = 50
                    else:
                        possivel_desviar = 25

                    if randint(0, 101) >= possivel_desviar:
                        causar_dano = 0

                        if inimigo.defesa >= self.ataque:
                            causar_dano = int(self.ataque / 2)
                        else:
                            causar_dano = self.ataque
                            
                        inimigo.vida = inimigo.vida - causar_dano

                        print("Voce causou {} de dano no monstro {}".format(causar_dano, inimigo.retorno_tipo()))

                        if inimigo.vida <= 0:
                            print("Voce derrotou o monstro {}".format(inimigo.retorno_tipo()))
                            print("Voce obteve {} de XP".format(inimigo.xp))
                            self.xp += inimigo.xp
                            self.subir_nivel()
                            break
                    else:
                        print("Monstro desviou do seu golpe")

                elif escolha == 2:
                    self.status()
                    inimigo.status_mnt()
                elif escolha == 3:
                    velocidade_Jogador_fuga = (self.velocidade + self.agilidade) / 2
                    velocidade_inimigo_evitar_fuga = (inimigo.velocidade + inimigo.agilidade) / 2

                    if velocidade_Jogador_fuga > velocidade_inimigo_evitar_fuga:
                        print("Voce conseguiu fujir do monstro {}".format(inimigo.retorno_tipo()))
                        break
                    else:
                        print("Inimigo e mais rapido que voce, impossivel fugir, lute ou morra covarde!")
                elif escolha == 4:
                    self.finalizar(True)
                else:
                    print("Escolheu errado! Perdeu uma oportunidade de fazer alguma coisa!")
                
            else:
                print("Voce foi atacado")
                espera(2)
                chance_desviar = (inimigo.velocidade + inimigo.agilidade / 2)
                chance_acertar = (self.velocidade + self.agilidade / 2)
                possivel_desviar = 0
                if chance_desviar > chance_acertar:
                    possivel_desviar = 75
                elif chance_desviar == chance_acertar:
                    possivel_desviar = 50
                else:
                    possivel_desviar = 25

                if randint(0, 101) >= possivel_desviar:

                    causar_dano = 0

                    if self.defesa >= inimigo.ataque:
                        causar_dano = int(inimigo.ataque / 2)
                    else:
                        causar_dano = inimigo.ataque

                    print("Voce levou um golpe!")

                    self.vida_atual = self.vida_atual - causar_dano
                    print("Voce perdeu {} de vida".format(causar_dano))

                    if self.vida_atual <= 0:
                        print("Voce foi derrota pelo monstro {}".format(inimigo.retorno_tipo()))
                        self.finalizar(False)
                        break

                else:
                    print("Voce desviou do seu golpe")

            partidas = partidas + 1

    #Funcao de ajuda
    def ajuda(self):
        print("\n")
        print("*-" * 20)
        print("Chamou minha ajuda!")
        print("Bem preste atencao\nApertar 1 vai caminhar, se caminhar voce achar um monstro, lute ou fuja mas o mais realista e que voce morra\nAperte 2 vai mostrar as pocoes\nAperte 3 e tente melhorar voce caso possua pontos\nAperte 4 e mostre seus status\nAperte 5 e se mate, esta uma opcao realista\nAperte H se quiser conversar denovo, mas vou repetir o que acabei de falar.")
        print("*-" * 20)
        print("Bem boa sorte e se vira, essas sao as unicas coisas que posso te falar mesmo... Bye!")
        print("*-" * 20)
        print("\n")

    #Funcao de equipamentos
    def equipamentos(self):
        while True:
            print("\n")
            print("*-" * 20)
            print("Equipamentos")
            print("*-" * 20)
            print("1 - Pocao de recuperacao de vida\n2 - Pocao de recuperacao de mana\n0 - Sair do menu de equipamentos")
            print("*-" * 20)
            escolha = int(input("Entre com a opcoes: "))

            if escolha == 1:
                
                andar_contagem = int(self.andar)
                if self.pocao_vida != 0:
                    while True:
                        print("Pocao vida")
                        print("Voce tem {} para usar".format(self.pocao_vida))
                        print("Cada pocao recupera {} de vida".format(2 * andar_contagem))
                        escolha = int(input("Deseja usar quantas? Se nao quiser usar coloque 0: "))

                        if escolha == 0:
                            print("Saindo do menu de pocoes de vida!")
                            break
                        elif escolha <= self.pocao_vida:
                            
                            recuperar = escolha * (2 * andar_contagem)

                            possivel_recuperar = self.vida - self.vida_atual
                        
                            if recuperar >= possivel_recuperar:
                                retirar = possivel_recuperar - recuperar
                                recuperar = recuperar - retirar
                                print("Voce usou {} de pocoes para recuperar {} de vida!".format(escolha, recuperar))
                                self.vida_atual = self.vida + recuperar
                            else:
                                print("Voce usou {} de pocoes para recuperar {} de vida!".format(escolha, recuperar))
                                self.vida_atual = self.vida + recuperar

                            break
                        else:
                            print("Voce selecionou mais pocoes do que tem, selecione denovo ou saia!")

            elif escolha == 2:

                andar_contagem = int(self.andar)
                if self.pocao_mana != 0:
                    while True:
                        print("Pocao mana")
                        print("Voce tem {} para usar".format(self.pocao_mana))
                        print("Cada pocao recupera {} de mana".format(2 * andar_contagem))
                        escolha = int(input("Deseja usar quantas? Se nao quiser usar coloque 0: "))

                        if escolha == 0:
                            print("Saindo do menu de pocoes de mana!")
                            break
                        elif escolha <= self.pocao_mana:
                            
                            recuperar = escolha * (2 * andar_contagem)

                            possivel_recuperar = self.mana - self.mana_atual
                        
                            if recuperar >= possivel_recuperar:
                                retirar = possivel_recuperar - recuperar
                                recuperar = recuperar - retirar
                                print("Voce usou {} de pocoes para recuperar {} de mana!".format(escolha, recuperar))
                                self.mana_atual = self.mana_atual + recuperar
                            else:
                                print("Voce usou {} de pocoes para recuperar {} de mana!".format(escolha, recuperar))
                                self.mana_atual = self.mana_atual + recuperar

                            break
                        else:
                            print("Voce selecionou mais pocoes do que tem, selecione denovo ou saia!")

            elif escolha == 0:
                print("Saindo menu!")
                break
            else:
                pass

    #Finalizar o jogo
    def finalizar(self, sematou):
        espera(2)
        print("\n")
        print("*-" * 20)
        if sematou:
            print("Voce se matou!\nFim do jogo!")
        else:
            print("Voce morreu!\nFim do jogo!")
        print("*-" * 20)
        print("\n")
        espera(2)
        exit()

    #Mostrar status do jogador
    def status(self):
        print("\n")
        print("*-" * 20)
        print("Status - Jogador")
        print("*-" * 20)
        print("Nome: {}\nClasse: {}\nExperiencia: {} - P.N {}\nPontos de habilidade: {}".format(self.nome, self.classe, self.xp, (self.nivel * 10), self.pontos))
        print("*-" * 20)
        print("Vida: {} - QTD Atual: {}\nAtaque: {}\nDefesa: {}\nVelocidade: {}\nAgilidade: {}\nMana: {} - QTD Atual: {}".format(self.vida, self.vida_atual, self.ataque, self.defesa, self.velocidade, self.agilidade, self.mana, self.mana_atual))
        print("*-" * 20)
        print("\n")
        return True
    
    #Subir de nivel
    def subir_nivel(self):
        if (self.nivel * 10) <= self.xp:
            print("*-" * 20)
            print("Subiu de nivel!")
            print("Voce subiu do nivel {} para {}!".format(self.nivel, self.nivel+1))
            print("Voce ganhou 3 pontos de atributos!")
            print("Sua vida foi recuperada!")
            print("*-" * 20)
            self.nivel += 1
            self.pontos += 3
            self.vida_atual = self.vida
            self.xp = 0
        return True

    #Atribuir ponto 
    def atribuir_pontos(self):
            if self.pontos != 0:
                print("*-" * 20)
                print("Atribuir pontos de habilidades")
                print("*-" * 20)
                print("Quantidade de pontos atuais: {}".format(self.pontos))
                self.status()
                print("Selecione onde colocar os pontos de habilidades")
                print("1 - Vida\n2 - Ataque\n3 - Defesa\n4 - Velocidade\n5 - Agilidade\n6 - Mana\n7 - Para sair e voltar ao jogo")
                print("*-" * 20)
                while True:
                    escolha = int(input("Entre com a opcao: "))

                    if escolha == 7:
                        print("*-" * 20)
                        print("Saindo da melhoria!")
                        print("*-" * 20)
                        break
                    else:
                        while True:
                            quantos = int(input("Quantos pontos? "))
                            if quantos > self.pontos:
                                print("*-" * 20)
                                print("Quantidade acima do que voce possui, entre com o valor correto")
                                print("*-" * 20)
                            else:
                                break

                        certeza = input("Tem ceterza sobre a melhoria?(S/N): ")

                        if certeza.upper() == "S":
                                
                            categoria = ""

                            if escolha == 1:
                                self.vida += quantos
                                self.vida_atual += quantos
                                categoria = "Vida"
                            elif escolha == 2:
                                self.ataque += quantos
                                categoria = "Ataque"
                            elif escolha == 3:
                                self.defesa += quantos
                                categoria = "Defesa"
                            elif escolha == 4:
                                self.velocidade += quantos
                                categoria = "Velocidade"
                            elif escolha == 5:
                                self.agilidade += quantos
                                categoria = "Agilidade"
                            elif escolha == 6:
                                self.mana += quantos
                                self.mana_atual += quantos
                                categoria = "Mana"
                            
                            print("*-" * 20)
                            print("Foram atribuidos {} pontos para o atributo {}!".format(quantos, categoria))
                            print("*-" * 20)

                        elif certeza.upper() == "N":
                            pass
                else:
                    pass

                print("*-" * 20)
                print("Escolha novamente!")
                print("*-" * 20)
            else:
                print("*-" * 20)
                print("Voce nao tem pontos a atribuir no momento!")

            return True

    def retorno_andar_jogador(self):
        return self.andar

#Class monstro
class Monstro:

    #Construtor
    def __init__(self):
        self.tipo = ""
        self.vida = 0
        self.ataque = 0
        self.defesa = 0
        self.velocidade = 0
        self.agilidade = 0
        self.xp = 0

    #Produzir forca do monstro baseado no andar que esta
    def produzir_boss(self, andar):
        melhoria = int(andar)
        valor_aleatorio = randint(1 ,3)
        if (melhoria % 10) == 0:
            melhoria = melhoria + ((melhoria / 100) * 20)
            valor_aleatorio = randint(2, 4)

        return valor_aleatorio + melhoria

    #Produzir monstro
    def monstro_aleatorio(self, andar, ambiente):

        modelos = ["Esqueleto", "Aranha", "Goblin"]
        aleatorio = randint(0, 2)
        self.tipo = modelos[aleatorio]
        self.vida = self.produzir_boss(andar)
        self.ataque = self.produzir_boss(andar)
        self.defesa = self.produzir_boss(andar)
        self.velocidade = self.produzir_boss(andar)
        self.agilidade = self.produzir_boss(andar)
        self.xp = self.produzir_boss(andar)

    #Retorna o tipo do monstro
    def retorno_tipo(self):
        return self.tipo

    #Status do monstro
    def status_mnt(self):
        print("\n")
        print("*-" * 20)
        print("Status - Monstro")
        print("*-" * 20)
        print("Tipo: {}\nExperiencia: {}".format(self.tipo, self.xp))
        print("*-" * 20)
        print("Vida: {}\nAtaque: {}\nDefesa: {}\nVelocidade: {}\nAgilidade: {}".format(self.vida, self.ataque, self.defesa, self.velocidade, self.agilidade))
        print("*-" * 20)
        print("\n")
        return True

#Criando a class da masmorra
class Masmorra:

    #Valores iniciais
    qtd_andares = 0
    andares = 1
    qtd_passos = 0
    tpd_andar = "normal"

    #Construor
    def __init__(self):
        self.qtd_andares = randint(10, 100)

    #Criando tipo do andar
    def tipo_andar(self):
        tipos = ["normal", "venenoso", "fogo", "gelo"]
        escolher = randint(0,3)
        return tipos[escolher]

    #Criando o andar
    def criar_andar(self, andar):

        self.andares = andar
        self.tpd_andar = self.tipo_andar()

        andar_atual = int(andar) % 10

        if andar_atual == 0:
            self.qtd_passos = 1
        else:
            self.qtd_passos = randint(10, 80)
        
        print("Voce entrou no andar {} do tipo {}!".format(self.andares, self.tpd_andar))

    #Retorna o andar
    def retorno_andar(self):
        return "{}".format(self.andares)

    #Retorna o tipo do andar
    def retorno_tipo(self):
        return "{}".format(self.tpd_andar)

    #Retorna a quantidade de passos do andar
    def retorno_passos(self):
        return "{}".format(self.qtd_passos)

#Espera
def espera(entrada):
    sleep(entrada)

#Introducao
def introducao():
    print("Ola, bem vindo!")
    espera(2)
    print("Meu nome e Midna, assistente do deus louco que crio este lugar!")
    espera(2)
    print("Voce foi escolhi para passar por esta provacao, bem vindo a dungeon do deus louco!")
    espera(2)
    print("Com isso vamos a introducao, atualmente voce esta no Andar 1 de uma masmorra que nao se sabe a profundidade")
    espera(2)
    print("Agora, voce foi transportado para este mundo para passar por esta masmorra, voce so tem uma vida e sua classe e forca e escolhida de forma aleatoria!")
    espera(2)
    print("Voce pode usar itens que encotrar, nesta dugeon so existem simples armadilhas, sempre que precisar de ajuda aperte H para me chamar")
    espera(2)
    nome = input("Com isso explicado, peco que fale seu nome, te trazemos de forma aleatoria entao nao sabemos que e voce, fale seu nome: ")
    espera(2)
    print("Certo, com tudo isso explicado, comecemos, boa sorte {}... tente nao morrer, afinal voce so tem uma vida".format(nome))
    espera(2)
    return nome

#Funcao do jogo
def Jogo():

    Masmorra_mapa = Masmorra()
    Jogador = Personagem(introducao())
    Jogador.atribuir_aleatorio()

    while True:
        Masmorra_mapa.criar_andar(Jogador.retorno_andar_jogador())
        Jogador.menu_personagem(Masmorra_mapa.retorno_passos(), Masmorra_mapa.retorno_andar(), Masmorra_mapa.retorno_tipo())

#Funcao principal  
if __name__ == "__main__":
    Jogo()