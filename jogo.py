### Jogo Educativo/Projeto final 1 semestre ###
###importacoes###
import random
import time
import pygame

###Tamano da tela###
pygame.init()
relogio = pygame.time.Clock()
largura = 600
altura = 600
display = pygame.display.set_mode((largura, altura))
background = pygame.image.load("assets/Fundo.png")
pygame.display.set_caption("Fuga da professora")

###dados menino###
men = pygame.image.load("assets/menino.png")
menLargura = 60
menPosicaoX = 360
menPosicaoY = 470
menMovimento = 0
velocidademen = 10

###dados professora###
prof = pygame.image.load("assets/professora.png")
profLargura = 50
profAltura = 80
profPosicaoX = 360
profPosicaoY = 10 - profAltura
profMovimento = 0
velocidadeprof = 5

###Sons###
pygame.mixer.music.load('assets/Musica.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

###Funcoes###
def escrevendoPlacar(contador):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Nota: "+str(contador), True, (255, 255, 255))
    display.blit(texto, (10, 10))
def dead():
    font = pygame.font.SysFont(None, 100)
    texto = font.render("Você Morreu!", True, (0, 0, 0))
    display.blit(texto, (100, 200))
    pygame.display.update()
    time.sleep(5)
contador = 0


while True:
    ###Trabalhar com o fundo###
    display.fill((255, 255, 255))
    display.blit(background, (0, 0))

    ###movimentacao###
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                menMovimento = velocidademen * -1
            elif evento.key == pygame.K_RIGHT:
                menMovimento = velocidademen
        if evento.type == pygame.KEYUP:
            menMovimento = 0
    menPosicaoX = menPosicaoX + menMovimento
    if menPosicaoX < 0:
        menPosicaoX = 0
    elif menPosicaoX > largura - menLargura:
        menPosicaoX = largura - menLargura
    display.blit(men, (menPosicaoX, menPosicaoY))
    profPosicaoY = profPosicaoY + velocidadeprof
    escrevendoPlacar(contador)
    
    ###movimento professora###
    if profPosicaoY > altura:
        profPosicaoY = 10 - profAltura
        velocidadeprof = velocidadeprof + 1
        profPosicaoX = random.randrange(0, largura)
        contador += 1 
    display.blit(prof, (profPosicaoX, profPosicaoY))

    ###Verificando Colisões###
    if menPosicaoY < profPosicaoY + profAltura:
        if menPosicaoX < profPosicaoX and menPosicaoX + menLargura > profPosicaoX or profPosicaoX+profLargura > menPosicaoX and profPosicaoX+profLargura < menPosicaoX+menLargura:
            dead()
            velocidadeprof = 5
            profPosicaoY = 0 - profAltura
            contador = 0
    pygame.display.update()
    relogio.tick(60)