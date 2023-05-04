import pygame
from pygame.locals import *
from sys import exit
import os
import random
 
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'sprites')
pygame.init()

#criar janela
largura = 640
altura = 480
y = 400
velocidade_jogo = 10

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Marcelinho Delivery')
tela_fundo = pygame.image.load('faculdade.jpeg')
background = pygame.transform.scale(tela_fundo, (640, 480))

#função para pontuação

def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}' 
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

#sprites usadas

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'persona_1.png')).convert_alpha()
GUARDINHA = pygame.image.load(os.path.join(diretorio_imagens, 'guardinha.png')).convert_alpha()
CAFE = pygame.image.load(os.path.join(diretorio_imagens, 'coffee.png')).convert_alpha()
PIZZA = pygame.image.load(os.path.join(diretorio_imagens, 'pizza.png')).convert_alpha()
COXINHA = pygame.image.load(os.path.join(diretorio_imagens, 'coxinha.png')).convert_alpha()

#funçao para reiniciar

def reiniciar():
  global pontos, velocidade_jogo, colidiu, escolha_obstaculo, pizzaa, cafee
  pontos = 0
  velocidade_jogo = 10
  colidiu = False
  estagiario.rect.y = altura - 64 - 96 // 2
  estagiario.pulo = False
  guardinha.rect.x = largura
  cafe.rect.x = largura
  pizza.rect.x = largura
  pizzaa = 0
  cafee = 0

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
    self.index_lista += 0.25
    self.image = self.imagens_estagiario[int(self.index_lista)]
  def colisao(self, sprite: pygame.sprite.Sprite):
    return self.rect.colliderect(sprite.rect)


#GUARDINHA CLASS
class Guardinha(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.imagens_guardinha = []
    for i in range(3):
      img = GUARDINHA.subsurface((16*3, (i * 16)+1), (16, 16))
      img = pygame.transform.scale(img, (16 * 3, 16 * 3))
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
    self.rect.x -= velocidade_jogo


#COFFEE CLASS
class Cafe(pygame.sprite.Sprite):
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
    self.rect.x -= velocidade_jogo

#pizza CLASS
class Pizza(pygame.sprite.Sprite):
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
    self.rect.x -= (velocidade_jogo - 5)

#adicionando as listas

colecao_sprites = pygame.sprite.Group()
estagiario = Estagiario()
colecao_sprites.add(estagiario)

guardinha = Guardinha()
colecao_sprites.add(guardinha)

cafe = Cafe()
colecao_sprites.add(cafe)

pizza = Pizza()
colecao_sprites.add(pizza)

coletaveis = pygame.sprite.Group()
coletaveis.add(cafe)
coletaveis.add(pizza)

#auxiliares
run = True
relogio = pygame.time.Clock()
game_speed = 20
obstacles = []
death_count = 0
cafee = 0
pizzaa = 0
move = 0
move_2 = 640
flag = 0

#loop principal
while run:
  total = cafee + pizzaa
  relogio.tick(30)

# background inicio
  tela_fundo = pygame.image.load('faculdade.jpeg')
  background = pygame.transform.scale(tela_fundo, (640, 480))
  if flag == 0:
    tela.fill((255,255,255))
    tela.blit(background, (move,0))
    tela.blit(background, (move + move_2,0))
    move -= 8
    if move == -move_2:
        tela.blit(background, (move + move_2,0))
        move = 0
  else:
    tela.blit(background, (move,0))
# background final
   
  texto_pontos_cafee = exibe_mensagem(cafee, 40, (0,0,0))
  texto_pontos_pizzaa = exibe_mensagem(pizzaa, 40, (0,0,0))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYDOWN:
      if event.key == K_SPACE:
        estagiario.pular()
      if event.key == K_r and estagiario.colisao(guardinha):
        reiniciar()
        flag = 0
 
  if estagiario.colisao(cafe):
    colisoes = pygame.sprite.spritecollide(estagiario, coletaveis, False)
    cafee += 10
  if estagiario.colisao(pizza):
    colisoes = pygame.sprite.spritecollide(estagiario, coletaveis, False)
    pizzaa += 50
  
  if estagiario.colisao(guardinha):
    flag = 1
    pass
    print('GAME OVER')
  else:
    guardinha.update()
    estagiario.update()
    colecao_sprites.update()

  tela.blit(texto_pontos_cafee, (520, 30)) 
  tela.blit(texto_pontos_pizzaa, (380 , 30))
  colecao_sprites.draw(tela)
  pygame.display.flip()