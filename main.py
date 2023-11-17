import pygame
import sys
from pygame import Rect

#Funções
def carregar_pergunta():
    global resposta, num_pergunta, nivel, qt_perguntas, dica
    arquivo = "nivel"+str(nivel)+".txt"
    fonte = pygame.font.Font('arial.ttf',36)

    texto = fonte.render(str(nivel), True, (0, 0, 0))
    screen.blit(texto, (100, 50))

    if num_pergunta == 0:
      num = 0
    else:
      num = (num_pergunta*10)-1

    with open(arquivo, 'r', encoding='utf-8') as arquivo2:
        numero_de_linhas = len(arquivo2.readlines())
        qt_perguntas = (numero_de_linhas)/10+1

    with open(arquivo, 'r', encoding='utf-8') as arquivo:
        for i in range(numero_de_linhas):
            linha = arquivo.readline()
            if not linha:
                break
            if i == num:
                #carregando pergunta linha1
                texto = fonte.render(linha.strip(), True, (0,0,0))
                screen.blit(texto, (80, 270))
            if i == num+1:
                # carregando pergunta linha2
                texto = fonte.render(linha.strip(), True, (0,0,0))
                screen.blit(texto, (80, 320))
            if i == num+2:
                # carregando alternativa 1
                texto = fonte.render(linha.strip(), True, ( 255,255,255))
                screen.blit(texto, (115, 695))
            if i == num+3:
                # carregando alternativa 2
                texto = fonte.render(linha.strip(), True, (255,255,255))
                screen.blit(texto, (485, 695))
            if i == num+4:
                # carregando alternativa 3
                texto = fonte.render(linha.strip(), True, (255,255,255))
                screen.blit(texto, (115, 870))
            if i == num+5:
                # carregando alternativa 4
                texto = fonte.render(linha.strip(), True, (255,255,255))
                screen.blit(texto, (485, 870))
            if i == num + 6:
                # carregando dica
                dica = linha.strip()
            if i == num + 7:
                # carregando dica
                resposta = int(linha.strip())
                if mostra_dica == dica:
                    fonte = pygame.font.Font('arial.ttf', 22)
                    texto = fonte.render(dica, True, (0, 0, 0))
                    screen.blit(texto, (200, 280))


def pontuacao():

    arquivo = "nivel1.txt"
    with open(arquivo, 'r', encoding='utf-8') as arquivo1:
        numero_de_linhas = len(arquivo1.readlines())
        nivel1_qtperguntas = int((numero_de_linhas)/10+1)
    arquivo = "nivel2.txt"
    with open(arquivo, 'r', encoding='utf-8') as arquivo2:
        numero_de_linhas = len(arquivo2.readlines())
        nivel2_qtperguntas = int((numero_de_linhas)/10+1)
    arquivo = "nivel3.txt"
    with open(arquivo, 'r', encoding='utf-8') as arquivo3:
        numero_de_linhas = len(arquivo3.readlines())
        nivel3_qtperguntas = int((numero_de_linhas)/10+1)
    arquivo = "nivel4.txt"
    with open(arquivo, 'r', encoding='utf-8') as arquivo4:
        numero_de_linhas = len(arquivo4.readlines())
        nivel4_qtperguntas = int((numero_de_linhas)/10+1)

    fonte = pygame.font.Font('arial.ttf',42)
    texto = fonte.render(str(nivel1_acertos)+"/"+str(nivel1_qtperguntas), True, (255, 255, 255))
    screen.blit(texto, (130, 425))

    texto = fonte.render(str(nivel2_acertos)+"/"+str(nivel2_qtperguntas), True, (255, 255, 255))
    screen.blit(texto, (485, 425))

    texto = fonte.render(str(nivel3_acertos)+"/"+str(nivel3_qtperguntas), True, (255, 255, 255))
    screen.blit(texto, (130, 730))

    texto = fonte.render(str(nivel4_acertos)+"/"+str(nivel4_qtperguntas), True, (255, 255, 255))
    screen.blit(texto, (485, 730))




def acertou():

    global num_pergunta, nivel, nivel1_acertos, nivel2_acertos, nivel3_acertos, nivel4_acertos
    som_acerto.play()

    num_pergunta += 1
    if nivel == 1:
        nivel1_acertos += 1
    if nivel == 2:
        nivel2_acertos += 1
    if nivel == 3:
        nivel3_acertos += 1
    if nivel == 4:
        nivel4_acertos += 1


def errou():
    global num_pergunta
    som_erro.play()
    num_pergunta += 1

# --------------Fim Funções

pygame.init()
res = (750, 1000)
screen = pygame.display.set_mode(res)

transparente = pygame.Surface((100, 100), pygame.SRCALPHA)
transparente.fill((0, 0, 0, 0))  # preenche a superfície com cor totalmente transparente

#carregando sons
som_acerto = pygame.mixer.Sound("acerto.wav")
som_erro = pygame.mixer.Sound("erro.wav")

# Carregando as imagens
# Elas devem estar dentro da pasta imagens
img_inicio   = pygame.image.load("imagens\\tela1.png")
img_config   = pygame.image.load("imagens\\tele de conf.png")
img_sobre    = pygame.image.load("imagens\\sobre.png")
img_creditos = pygame.image.load("imagens\\tela de cred.png")
img_niveis = pygame.image.load("imagens\\niveis.png")
img_nivel1 = pygame.image.load("imagens\\nivel1.png")
img_nivel2 = pygame.image.load("imagens\\nivel2.png")
img_nivel3 = pygame.image.load("imagens\\nivel3.png")
img_nivel4 = pygame.image.load("imagens\\nivel4.png")

img_pergunta = pygame.image.load("imagens\pergunta.png")


# Criando os botões (são retangulos posicionados acima da imagem da janela)
botao_config = pygame.Rect(35, 20, 60, 75)
botao_config_voltar = pygame.Rect(680, 10, 60, 75)

botao_sobre = pygame.Rect(195, 620, 363, 115)
botao_sobre_voltar = pygame.Rect(680, 10, 60, 75)

botao_creditos = pygame.Rect(195,370,363,115)
botao_creditos_voltar = pygame.Rect(680, 10, 60, 75)

botao_niveis = pygame.Rect(235, 535, 250,80)
botao_niveis_voltar = pygame.Rect(680, 10, 60, 75)

botao_nivel1 = pygame.Rect(60, 330, 220,80)
botao_nivel2 = pygame.Rect(415, 330, 220,80)
botao_nivel3 = pygame.Rect(45, 625, 220,100)
botao_nivel4 = pygame.Rect(415, 625, 220,100)

botao_nivel1_voltar = pygame.Rect(650, 10, 90, 90)
botao_nivel2_voltar = pygame.Rect(650, 10, 90, 90)
botao_nivel3_voltar = pygame.Rect(650, 10, 90, 90)
botao_nivel4_voltar = pygame.Rect(650, 10, 90, 90)

botao_nivel1_comecar = pygame.Rect(110, 503, 530, 130)
botao_nivel2_comecar = pygame.Rect(110, 503, 530, 130)
botao_nivel3_comecar = pygame.Rect(110, 503, 530, 130)
botao_nivel4_comecar = pygame.Rect(110, 503, 530, 130)

botao_pergunta_voltar = pygame.Rect(650, 10, 90, 90)
botao_pergunta_dica = pygame.Rect(1300, 260, 50, 50)

botao_resposta1 = pygame.Rect(10, 665,300, 100)
botao_resposta2 = pygame.Rect(350, 665, 300, 100)
botao_resposta3 = pygame.Rect(10, 840, 300, 100)
botao_resposta4 = pygame.Rect(350, 840, 300, 100)

botao_sair = pygame.Rect(1125, 60, 50, 50)


# Definindo a tela ativa
tela_ativa = "inicio"


#Variáveis do sistema
nivel = 1
acertos = 0
erros = 0
num_pergunta = 0
resposta = 0
qt_perguntas = 0
nivel1_acertos = 0
nivel2_acertos = 0
nivel3_acertos = 0
nivel4_acertos = 0
dica = ""
mostra_dica = ""


while True:
    # Abertura da tela ativa e inserção dos botões correspondentes
    # Dica: você pode enxergar os botões mudando de transparente para screen
    if tela_ativa == "inicio":
        screen.blit(img_inicio, (0, 0))
        pygame.draw.rect(transparente, (0, 0, 0), botao_config)
        pygame.draw.rect(transparente, (0, 0, 0), botao_niveis)
        pygame.draw.rect(transparente, (0, 0, 0), botao_sair)
    elif tela_ativa == "config":
        screen.blit(img_config, (0, 0))
        pygame.draw.rect(transparente, (0, 0, 0), botao_config_voltar)
        pygame.draw.rect(transparente, (0, 0, 0), botao_sobre)
        pygame.draw.rect(transparente, (0, 0, 0), botao_creditos)

    elif tela_ativa == "sobre":
        screen.blit(img_sobre, (0, 0))
        pygame.draw.rect(transparente, (0, 0, 0), botao_sobre_voltar)

    elif tela_ativa == "creditos":
        screen.blit(img_creditos, (0, 0))
        pygame.draw.rect(transparente, (0, 0, 0), botao_creditos_voltar)

    elif tela_ativa == "niveis":
        screen.blit(img_niveis, (0, 0))
        pygame.draw.rect(transparente, (0, 0, 0), botao_niveis_voltar)
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel1)
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel2)
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel3)
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel4)
        pontuacao()
    elif tela_ativa == "nivel1":
        screen.blit(img_nivel1, (0, 0))
        nivel = 1
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel1_voltar)
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel1_comecar)
    elif tela_ativa == "nivel2":
        screen.blit(img_nivel2, (0, 0))
        nivel = 2
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel2_voltar)
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel2_comecar)
    elif tela_ativa == "nivel3":
        screen.blit(img_nivel3, (0, 0))
        nivel = 3
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel3_voltar)
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel3_comecar)
    elif tela_ativa == "nivel4":
        screen.blit(img_nivel4, (0, 0))
        nivel = 4
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel4_voltar)
        pygame.draw.rect(transparente, (0, 0, 0), botao_nivel4_comecar)
    elif tela_ativa == "pergunta":
        screen.blit(img_pergunta, (0, 0))
        pygame.draw.rect(transparente, (0, 0, 0), botao_pergunta_voltar)
        pygame.draw.rect(transparente, (0, 0, 0), botao_resposta1)
        pygame.draw.rect(transparente, (0, 0, 0), botao_resposta2)
        pygame.draw.rect(transparente, (0, 0, 0), botao_resposta3)
        pygame.draw.rect(transparente, (0, 0, 0), botao_resposta4)
        pygame.draw.rect(transparente, (0, 0, 0), botao_pergunta_dica)
        carregar_pergunta()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        elif ev.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()

            if tela_ativa == "inicio":
                if botao_config.collidepoint(mouse) :
                     tela_ativa = "config"
                if botao_niveis.collidepoint(mouse):
                    tela_ativa = "niveis"
                if botao_sair.collidepoint(mouse):
                    pygame.quit()
            elif tela_ativa == "config":
                if botao_config_voltar.collidepoint(mouse):
                    tela_ativa = "inicio"
                if botao_sobre.collidepoint(mouse):
                    tela_ativa = "sobre"
                if botao_creditos.collidepoint(mouse):
                    tela_ativa = "creditos"
            elif tela_ativa == "sobre":
               if botao_sobre_voltar.collidepoint(mouse):
                    tela_ativa = "config"
            elif tela_ativa == "creditos":
                if botao_creditos_voltar.collidepoint(mouse):
                    tela_ativa = "config"
            elif tela_ativa == "niveis":
                if botao_niveis_voltar.collidepoint(mouse):
                    tela_ativa = "inicio"
                if botao_nivel1.collidepoint(mouse):
                    tela_ativa = "nivel1"
                if botao_nivel2.collidepoint(mouse):
                    tela_ativa = "nivel2"
                if botao_nivel3.collidepoint(mouse):
                    tela_ativa = "nivel3"
                if botao_nivel4.collidepoint(mouse):
                    tela_ativa = "nivel4"
            elif tela_ativa == "nivel1":
                if botao_nivel1_voltar.collidepoint(mouse):
                    tela_ativa = "niveis"
                if botao_nivel1_comecar.collidepoint(mouse):
                    tela_ativa = "pergunta"
                    nivel1_acertos = 0
            elif tela_ativa == "nivel2":
                if botao_nivel2_voltar.collidepoint(mouse):
                    tela_ativa = "niveis"
                if botao_nivel2_comecar.collidepoint(mouse):
                    tela_ativa = "pergunta"
                    nivel2_acertos = 0
            elif tela_ativa == "nivel3":
                if botao_nivel3_voltar.collidepoint(mouse):
                    tela_ativa = "niveis"
                if botao_nivel3_comecar.collidepoint(mouse):
                    tela_ativa = "pergunta"
                    nivel3_acertos = 0
            elif tela_ativa == "nivel4":
                if botao_nivel4_voltar.collidepoint(mouse):
                    tela_ativa = "niveis"
                if botao_nivel4_comecar.collidepoint(mouse):
                    tela_ativa = "pergunta"
                    nivel4_acertos = 0
            elif tela_ativa == "pergunta":

                if botao_pergunta_voltar.collidepoint(mouse):
                    tela_ativa = "niveis"
                if botao_resposta1.collidepoint(mouse):

                    if resposta == 1:
                        print("1")
                        acertou()
                    else:
                        errou()
                if botao_resposta2.collidepoint(mouse):

                    if resposta == 2:
                        print("2")
                        acertou()
                    else:
                        errou()
                if botao_resposta3.collidepoint(mouse):

                    if resposta == 3:
                        print("3")
                        acertou()
                    else:
                        errou()
                if botao_resposta4.collidepoint(mouse):
                    if resposta == 4:
                        print("4")
                        acertou()
                    else:
                        errou()
                if botao_pergunta_dica.collidepoint(mouse):
                    mostra_dica = dica
                if num_pergunta >= qt_perguntas-1:
                    num_pergunta = 0
                    tela_ativa = "niveis"

    pygame.display.update()
