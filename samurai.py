import pygame
from sys import exit

pygame.init

# Cria uma tela 
# meio da tela: (480, 275)
tamanho = (960, 550)
tela = pygame.display.set_mode(tamanho)

# Título do Jogo 
pygame.display.set_caption("Samurai")

def animacao_personagem():
    global jogador_index

    jogador_retangulo.x += movimento_personagem

    # Limita aonde o retangulo do jogador pode ir na tela
    if jogador_retangulo.right >= 1100:
        jogador_retangulo.right = 1100
    elif jogador_retangulo.left <= -120:
        jogador_retangulo.left = -120

    if movimento_personagem == 0: # Jogador está parado
        jogador_superficie = jogador_parado_superficie
    else: # Jogador está andando
        jogador_superficie = jogador_andando_superficie

    # Avança para o próximo frame
    jogador_index += 0.10
    if jogador_index > len(jogador_superficie) -1 : # Len vem de Lenght
        jogador_index = 0

    if direcao_personagem == 1:
        jogador = pygame.transform.flip(jogador_superficie[int(jogador_index)], True, False)
    else:
        jogador = jogador_superficie[int(jogador_index)]

    # Desenha o jogador na tela
    tela.blit(jogador, jogador_retangulo)

def ataque_personagem():
    pass

def animacao_inimigo():
    global inimigo_index

    inimigo_retangulo.x -= movimento_inimigo

    # Limita aonde o retangulo do jogador pode ir na tela
    if inimigo_retangulo.right >= 1100:
        inimigo_retangulo.right = 1100
    elif inimigo_retangulo.left <= -120:
        inimigo_retangulo.left = -120

    if movimento_inimigo == 0:
        inimigo_superficie = inimigo_parado_superficie
    else:
        inimigo_superficie = inimigo_andando_superficie

    # Avança para o próximo frame
    inimigo_index += 0.12
    if inimigo_index > len(inimigo_superficie) -1 : # Len vem de Lenght
        inimigo_index = 0

    if direcao_inimigo == 1:
        inimigo = pygame.transform.flip(inimigo_superficie[int(inimigo_index)], True, False)
    else:
        inimigo = inimigo_superficie[int(inimigo_index)]

    # Desenha o jogador na tela
    tela.blit(inimigo, inimigo_retangulo)
    
def ataque_inimigo():
    pass

##
## Importa os arquivos necessário
##

# Carrega o plano de fundo 
chao = pygame.image.load('assets/fundo/fundo_1.png').convert_alpha()
cogumelos = pygame.image.load('assets/fundo/fundo_2.png').convert_alpha()
grama = pygame.image.load('assets/fundo/fundo_3.png').convert_alpha()
arvore = pygame.image.load('assets/fundo/fundo_4.png').convert_alpha()
tronco = pygame.image.load('assets/fundo/fundo_5.png').convert_alpha()
fundo_tronco = pygame.image.load('assets/fundo/fundo_6.png').convert_alpha()
cor_fundo = pygame.image.load('assets/fundo/fundo_7.png').convert_alpha()
teste = pygame.image.load('assets/fundo/fundo_7.png').convert_alpha()

# Transforma o tamanho da imagem de fundo
chao = pygame.transform.scale (chao, tamanho)
cogumelos = pygame.transform.scale(cogumelos, tamanho)
grama = pygame.transform.scale(grama, tamanho)
arvore = pygame.transform.scale(arvore, tamanho)
tronco = pygame.transform.scale(tronco, tamanho)
fundo_tronco = pygame.transform.scale(fundo_tronco, tamanho)
cor_fundo = pygame.transform.scale(cor_fundo, tamanho)

## Carrega as imagens do jogador 
jogador_index = 0
jogador_parado_superficie = []
jogador_andando_superficie = []
jogador_atacando_superficie = []

# Carrega as imagens do jogador parado
for imagem in range (1, 6):
    img = pygame.image.load(f'assets/jogador/parado/parado_{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (320, 320))
    jogador_parado_superficie.append(img) 

# Carrega as imagens do jogador andando
for imagem in range (1, 9):
    img = pygame.image.load(f'assets/jogador/andar/andar_{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (320, 320))
    jogador_andando_superficie.append(img)

# Carrega as imagens do jogador atacando
for imagem in range (1, 5):
    img = pygame.image.load(f'assets/jogador/ataque/ataque_{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (320, 320))
    jogador_atacando_superficie.append(img)

# Retângulo do Jogador
jogador_retangulo = jogador_parado_superficie[jogador_index].get_rect(center = (100, 330))
# Retângulo da Espada
ataque_retangulo = pygame.Rect(jogador_retangulo.left + 50, jogador_retangulo.top, 30,10)

## Carrega as imagens do Inimigo(Boss)
inimigo_index = 0
inimigo_parado_superficie = []
inimigo_andando_superficie = []
inimigo_atacando_superficie = []

# Carrega as imagens do Inimigo Parado
for imagem_inimigo in range (1, 7):
    img_inimigo = pygame.image.load(f'assets/boss/01_demon_idle/demon_idle_{imagem_inimigo}.png').convert_alpha()
    img_inimigo = pygame.transform.scale(img_inimigo, (420, 420))
    inimigo_parado_superficie.append(img_inimigo)

# Carrega as imagens do Inimigo Andando
for imagem_inimigo in range (1, 13):
    img_inimigo = pygame.image.load(f'assets/boss/02_demon_walk/demon_walk_{imagem_inimigo}.png').convert_alpha()
    img_inimigo = pygame.transform.scale(img_inimigo, (420, 420))
    inimigo_andando_superficie.append(img_inimigo)

for imagem_inimigo in range (1, 16):
    img_inimigo = pygame.image.load(f'assets/boss/03_demon_cleave/demon_cleave_{imagem_inimigo}.png').convert_alpha()
    img_inimigo = pygame.transform.scale(img_inimigo, (420, 420))
    inimigo_atacando_superficie.append(img)

# Retângulo do Inimigo
inimigo_retangulo = inimigo_parado_superficie[inimigo_index].get_rect(center = (800, 280))

# Cria um relógio para controlar os FPS
relogio = pygame.time.Clock()

# Movimento jogador (negativo esquerda, positivo direita)
movimento_personagem = 0
direcao_personagem = 0

# Movimento Inimigo
movimento_inimigo = 0
direcao_inimigo = 0

# Loop Principal 
while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 6
                direcao_personagem = 0

            if evento.key == pygame.K_LEFT:
                movimento_personagem = -6
                direcao_personagem = 1

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 0
            if evento.key == pygame.K_LEFT:
                movimento_personagem = 0
        
        
             
    # Desenha o fundo na tela
    tela.blit(cor_fundo, (0, 0))
    tela.blit(fundo_tronco, (0, 0))
    tela.blit(tronco, (0, 0))
    tela.blit(arvore, (0, 0))
    tela.blit(grama, (0, 0))
    tela.blit(cogumelos, (0, 0))
    tela.blit(chao, (0, 0))

    # Chama a função animação do personagem
    animacao_personagem()

    # Chama a função animação ataque do personagem
    ataque_personagem()

    # Chama a função animação do Inimigo
    animacao_inimigo()

    # Função ataque do Inimigo
    ataque_inimigo()

    # Atualiza a tela com o conteúdo
    pygame.display.update()
    # Define a quantidade de frames por segundo
    relogio.tick(60)
