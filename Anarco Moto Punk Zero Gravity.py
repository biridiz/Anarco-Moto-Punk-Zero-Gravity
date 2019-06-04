#Por Luiz Roberto Dendena <luiz.dendena@gmail.com>

#IMPORTANDO BIBLIOTECAS:
import pygame
import time

pygame.init()

#VARIAVEIS GLOBAIS:

largura = 800
altura = 600
tamanho = 50

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#INICIANDO ALGUMAS FUNCOES, CARREGANDO IMAGENS, DANDO NOME AO JOGO, DEFININDO O RELOGIO(TEMPO):

fundo = pygame.display.set_mode((largura, altura))
moto = pygame.image.load ("/home/luiz/Imagens/moto.png")
imagem = pygame.image.load ("/home/luiz/Imagens/fundo.png")
uno = pygame.image.load ("/home/luiz/Imagens/uno.png")
pygame.display.set_caption('Anarco Moto Punk Zero Gravity')
clock = pygame.time.Clock()

#FUNCOES ESPECIFICAS DO JOGO:

def placar(placar_x, placar_y):
    pygame.draw.rect(fundo, black, [placar_x, placar_y, 200, 30])

def texto(mensagem, cor, tam, x, y):
    fonte = pygame.font.SysFont(None, tam)
    texto1 = fonte.render(mensagem, True, cor)
    fundo.blit(texto1, [x, y])

def bike(pos_x, pos_y):
    fundo.blit(moto, (pos_x, pos_y))

def chao(chao_x, chao_y):
    pygame.draw.rect(fundo, green, [chao_x, chao_y, largura, altura])

def ceu(ceu_x, ceu_y):
    pygame.draw.rect(fundo, blue, [ceu_x, ceu_y, largura, altura])

def obstaculo(obstaculo_x, obstaculo_y):
    fundo.blit(uno, (obstaculo_x, obstaculo_y))

#FUNCAO DE TELA DE INICIO:

def inicio():
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogo()
                if event.key == pygame.K_s:
                    quit()

        fundo.blit(imagem, (0, 0))

        pygame.draw.rect(fundo, red, [550, 350, 100, 50])
        pygame.draw.rect(fundo, green, [150, 200, 100, 50])

        texto('Play!', black, 50, 150, 200)
        texto('Sair!', black, 50, 550, 350)



        pygame.display.update()
        clock.tick(15)

#FUNCAO PRINCIPAL (LOOP JOGO):

def jogo():

#INICIANDO VARIAVEIS:

    sair = False
    gameover = False
    pos_x = (250)
    pos_y = (450)
    chao_x = 0
    chao_y = 450
    ceu_x = 0
    ceu_y = -300
    obstaculo_x = (1000)
    obstaculo_y = (450)
    placar_x = 10
    placar_y = 10
    velocidade_x = 0
    velocidade_y = 0
    score = 0
    velocidade = 5
    posfinal = - 50
    posinicial = 1000

    while not sair:

#LOOP DE GAME OVER:

        while gameover:

#DEFININDO FUNDO, TEXTOS E EVENTOS DAS TECLAS:

            fundo.fill(black)
            texto('OSTE NO ES PUNK, para continuar aperte ESPAÇO', red, 40, largura/10, altura/5)
            texto('Los Pontos Cabron: '+str(score), red, 40, largura/3, altura/3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jogo()
                        score = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    velocidade_y = 5
                    velocidade_x = 0
                if event.key == pygame.K_DOWN:
                    velocidade_y = -5
                    velocidade_x = 0

#CHAMANDO AS FUNCOES ESPECIFICAS E ATRIBUINDO VALORES AS VARIAVEIS DE MOVIMENTO, ACOES E VELOCIDADE:

        fundo.fill(black)
        ceu(ceu_x, ceu_y)
        chao(chao_x, chao_y)
        fundo.blit(imagem, (0, 0))
        obstaculo(obstaculo_x, obstaculo_y)
        obstaculo_x -= velocidade
        placar(placar_x, placar_y)
        texto('Los pontos cabron: '+str(score), red, 25, 12, 12)
        bike(pos_x, pos_y)
        pos_x += velocidade_x
        pos_y -= velocidade_y

#CONDICOES DE COLISAO COM O OBSTACULO:

        if (pos_x + 40) == obstaculo_x and pos_y == obstaculo_y:
            gameover = True

#CONDICAO DE COLISAO COM O TETO:

        if pos_y == 300:
            gameover = True

#CONDICAO QUE MANTEM A MOTO FIXA NO CHAO APOS CADA SALTO:

        if pos_y == chao_y:
            velocidade_y = 0
            velocidade_x = 0

#CONDICAO DE PONTUACAO:

        if pos_x  > obstaculo_x:
            score += 1

#CONDICAO DE INICIO, FIM E VELOCIDADE DO OBSTACULO:

        if obstaculo_x < posfinal:
            obstaculo_x = posinicial
            obstaculo_y = (450)
            velocidade += 0.4


        pygame.display.update()
        clock.tick(60)

#CHAMANDO MAIS ALGUMAS FUNCOES:

inicio()
jogo()
pygame.quit()
quit()

