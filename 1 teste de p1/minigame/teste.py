import pygame
from pygame.locals import *
from sys import exit
import os
import random
 
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'sprites')
diretorio_musicas = os.path.join(diretorio_principal, 'music')
pygame.init()

#Criar janela
largura = 640
altura = 480
y = 400
velocidade_jogo = 10

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Marcelinho Delivery')

#Função para texto
def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}' 
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

#Tela inicial
def menu():
  #Musica da tela inicial
  pygame.mixer.music.load(os.path.join(diretorio_musicas, 'dressup.mp3'))
  pygame.mixer.music.play()
  #Arte da tela inicial
  tela.fill((0,0,0))
  texto_inicial = exibe_mensagem('Pressione ESPAÇO', 35, ('yellow'))
  tela.blit(texto_inicial, (160, 300))
  arte_logo = pygame.transform.scale(LOGO, (largura,altura/2))
  tela.blit(arte_logo, (0,0))
  nome_hugo = exibe_mensagem('Ilustração por Hugo Albuquerque', 10, ('white'))
  tela.blit(nome_hugo, (altura, altura / 2))
  texto_desenvolvido = exibe_mensagem('Desenvolvido por:', 15, ('white'))
  tela.blit(texto_desenvolvido, (240, 400))
  texto_desenvolvido = exibe_mensagem('Beatriz Helena, Larissa Gomes, Maria Antônia, Williams Andrade', 18, ('white'))
  tela.blit(texto_desenvolvido, (28, 420))
  pygame.display.flip()

#Tela final
def tela_final():
  tela.fill((0,0,0))
  texto_inicial = exibe_mensagem('Pressione ESPAÇO', 20, ('yellow'))
  tela.blit(texto_inicial, (220, 400 ))
  texto_final = exibe_mensagem('GAME OVER', 50, ('red'))
  tela.blit(texto_final, (160, 300))
  score_total = exibe_mensagem(f'SCORE TOTAL {total}', 15, ('white'))
  tela.blit(score_total, (240, 360))
  arte_logo = pygame.transform.scale(LOGO, (largura,altura/2))
  tela.blit(arte_logo, (0,0))
  nome_hugo = exibe_mensagem('Ilustração por Hugo Albuquerque', 10, ('white'))
  tela.blit(nome_hugo, (altura, altura / 2))
  pygame.display.flip()
  pressionar_espaço()

#Pressionar espaço
def pressionar_espaço():
  pressione = True
  while pressione:
    relogio.tick(30)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pressione = False
        run = False
      if event.type == pygame.KEYDOWN:
        pressione = False
        run = True
  return run

#Sprites usadas
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'persona_1.png')).convert_alpha()
GUARDINHA = pygame.image.load(os.path.join(diretorio_imagens, 'guardinha.png')).convert_alpha()
CAFE = pygame.image.load(os.path.join(diretorio_imagens, 'coffee.png')).convert_alpha()
PIZZA = pygame.image.load(os.path.join(diretorio_imagens, 'pizza.png')).convert_alpha()
COXINHA = pygame.image.load(os.path.join(diretorio_imagens, 'coxinha.png')).convert_alpha()
LOGO = pygame.image.load(os.path.join(diretorio_imagens, 'logo.png')).convert_alpha()
LIFE = pygame.image.load(os.path.join(diretorio_imagens, 'life.png')).convert_alpha()

#Funçao para reiniciar
def reiniciar():
  global pontos, velocidade_jogo, colidiu, escolha_obstaculo, pizzaa, cafee, coxinhaa
  velocidade_jogo = 10
  colidiu = False
  estagiario.rect.y = altura - 64 - 96 // 2
  estagiario.pulo = False
  guardinha.rect.x = largura
  cafe.rect.x = largura
  pizza.rect.x = largura
  coxinha.rect.x = largura

##PLAYER CLASS
class Estagiario(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.imagens_estagiario = []
    for i in range(3):
      img = sprite_sheet.subsurface((16, (i * 16) + 1), (16, 16))
      img = pygame.transform.scale(img, (16 * 3, 16 * 3))
      self.imagens_estagiario.append(img)
    self.index_lista = 0
    self.image = self.imagens_estagiario[self.index_lista]
    self.rect = self.image.get_rect()
    self.pos_y = altura - 64 - 96//2
    self.rect.topleft = (100, self.pos_y)
    self.pulo = False

  def pular(self):
    self.pulo = True
  def update(self):
    if self.pulo == True:
      if self.rect.y <= self.pos_y - 150:
        self.pulo = False
      self.rect.y -= 15
    else:
      if self.rect.y >= self.pos_y:
        self.rect.y = self.pos_y
      else:
        self.rect.y += 15

    if self.index_lista > 2:
      self.index_lista = 0
    self.index_lista += 0.15
    self.image = self.imagens_estagiario[int(self.index_lista)]
  def colisao(self, sprite: pygame.sprite.Sprite):
    return self.rect.colliderect(sprite.rect)

#GUARDINHA CLASS
class Guardinha(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.imagens_guardinha = []
    for i in range(3):
      img = GUARDINHA.subsurface((16*3, (i * 12)+1), (16, 12))
      img = pygame.transform.scale(img, (16 * 3, 12 * 3))
      self.imagens_guardinha.append(img)
    self.index_lista = 0
    self.image = self.imagens_guardinha[self.index_lista]
    self.rect = self.image.get_rect()
    self.pos_y = altura - 64 - 96 // 2 + 25
    self.rect.center = (largura, self.pos_y)
  def update(self):
    #index da sprite
    if self.index_lista > 2:
      self.index_lista = 0
    self.index_lista += 0.25
    self.image = self.imagens_guardinha[int(self.index_lista)]

    if self.rect.topright[0] < 0:
      self.rect.x = largura
    self.rect.x -= 7

#COFFEE CLASS
class Cafe(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = CAFE
    self.image = pygame.transform.scale(self.image, (32,32))
    self.rect = self.image.get_rect()
    self.mask = pygame.mask.from_surface(self.image)
    self.rect.center = (largura, altura - 64 - 96 // 2 + 25)
    self.rect.x = largura
    self.coletado = False
  def update(self):
    if self.rect.right <= 0:
      self.rect.x = largura
      self.coletado = False
    self.rect.x -= 13

#PIZZA CLASS
class Pizza(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = PIZZA
    self.image = pygame.transform.scale(self.image, (32,32))
    self.rect = self.image.get_rect()
    self.mask = pygame.mask.from_surface(self.image)
    self.rect.center = (largura, altura - 64 - 96 // 2 + 25)
    self.rect.x = largura
    self.coletado = False
  def update(self):
    if self.rect.right <= 0:
      self.rect.x = largura
      self.coletado = False
    self.rect.x -= 12

#COXINHA CLASS
class Coxinha(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = COXINHA
    #self.image = pygame.transform.scale(self.image, (32,32))
    self.image = pygame.transform.scale(COXINHA, (16 * 4, 16 * 4))
    self.rect = self.image.get_rect()
    self.mask = pygame.mask.from_surface(self.image)
    self.rect.center = (largura, altura - 64 - 96 // 2 + 25)
    self.rect.x = largura
    self.coletado = False
  def update(self):
    if self.rect.right <= 0:
      self.rect.x = largura
      self.coletado = False
    self.rect.x -= 7

#Adicionando as listas
colecao_sprites = pygame.sprite.Group()
estagiario = Estagiario()
colecao_sprites.add(estagiario)

guardinha = Guardinha()
colecao_sprites.add(guardinha)

cafe = Cafe()
colecao_sprites.add(cafe)

pizza = Pizza()
colecao_sprites.add(pizza)

coxinha = Coxinha()
colecao_sprites.add(coxinha)

coletaveis = pygame.sprite.Group()
coletaveis.add(cafe)
coletaveis.add(pizza)
coletaveis.add(coxinha)

#Auxiliares
relogio = pygame.time.Clock()
game_speed = 20
obstacles = []
cafee = 0
pizzaa = 0
coxinhaa = 0
move = 0
move_2 = 640
flag = 0
game_over_count = 0
lifex_1 = 500
lifex_2 = 520
lifex_3 = 540

#Loop principal
menu()
tecla_espaço = pressionar_espaço()
while tecla_espaço:
  total = cafee + pizzaa + coxinhaa
  relogio.tick(30)

  #Background inicio
  tela_fundo = pygame.image.load('background.jpg')
  background = pygame.transform.scale(tela_fundo, (640, 450))
  if flag == 0:
    tela.blit(background, (move,0))
    tela.blit(background, (move + move_2,0))
    move -= 5
    if move == -move_2:
        tela.blit(background, (move + move_2,0))
        move = 0
  else:
    tela.blit(background, (move,0))
  #Background final

  texto_pontos_cafee = exibe_mensagem(cafee, 40, (0,0,0))
  texto_pontos_pizzaa = exibe_mensagem(pizzaa, 40, (0,0,0))
  texto_pontos_coxinhaa = exibe_mensagem(coxinhaa, 40, (0,0,0))

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYDOWN:
      if event.key == K_SPACE:
        estagiario.pular()
      if event.key == K_SPACE and estagiario.colisao(guardinha):
        reiniciar()
        flag = 0
        game_over_count += 1

  #Contabilizando colisoes
  if estagiario.colisao(cafe):
    colisoes = pygame.sprite.spritecollide(estagiario, coletaveis, False)
    cafe.rect.x = largura
    cafee += 1
  if estagiario.colisao(pizza):
    colisoes = pygame.sprite.spritecollide(estagiario, coletaveis, False)
    pizza.rect.x = largura
    pizzaa += 1
  if estagiario.colisao(coxinha):
    colisoes = pygame.sprite.spritecollide(estagiario, coletaveis, False)
    coxinha.rect.x = largura
    coxinhaa += 1
  
  if estagiario.colisao(guardinha):
    flag = 1
    if game_over_count == 0:
      lifex_1 = largura*2
    elif game_over_count == 1:
      lifex_2 = largura*2
    else:
      lifex_3 = largura*2
      tela_final()
      tecla_espaço = False



  else:
    guardinha.update()
    estagiario.update()
    colecao_sprites.update()

  LIFE = pygame.transform.scale(LIFE, (25, 25))
  tela.blit(LIFE, (lifex_1, 10))
  tela.blit(LIFE, (lifex_2, 10))
  tela.blit(LIFE, (lifex_3, 10))
  tela.blit(texto_pontos_cafee, (560, 30))
  tela.blit(CAFE, (520,45))
  tela.blit(texto_pontos_pizzaa, (460 , 30))
  tela.blit(PIZZA, (420,45))
  img_aumentada = pygame.transform.scale(COXINHA, (16 * 4, 16 * 4))
  tela.blit(texto_pontos_coxinhaa, (360 , 30))
  tela.blit(img_aumentada, (300,25))
  logo_game = pygame.transform.scale(LOGO, (125,58))
  tela.blit(logo_game, (20,20))
  colecao_sprites.draw(tela)
  pygame.display.flip()