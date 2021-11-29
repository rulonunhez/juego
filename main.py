from dis import dis

import pygame, sys
import random
from pygame.locals import *

ancho = 1000
alto = 600
fps = 30
negro = (0, 0, 0)
VELDISPARO = 12
VELPERSONAJE = 8
VELENEMIGO = 5
LEFT = 100
RIGHT = 890
TOP = 85
BOTTOM = 485


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/frente1.png').convert(), (45, 45))
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.center = (ancho // 2, alto // 2)

        self.cadencia = 250
        self.ultimo_disparo = pygame.time.get_ticks()

    def update(self):
        ventana.blit(fondo, (0, 0))

        # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()

        # Movimiento del personaje
        if teclas[pygame.K_w] and teclas[pygame.K_d]:
            self.rect.y -= VELPERSONAJE / 1.5
            self.rect.x += VELPERSONAJE / 1.5
        elif teclas[pygame.K_w] and teclas[pygame.K_a]:
            self.rect.y -= VELPERSONAJE / 1.5
            self.rect.x -= VELPERSONAJE / 1.5
        elif teclas[pygame.K_s] and teclas[pygame.K_d]:
            self.rect.y += VELPERSONAJE / 1.5
            self.rect.x += VELPERSONAJE / 1.5
        elif teclas[pygame.K_s] and teclas[pygame.K_a]:
            self.rect.y += VELPERSONAJE / 1.5
            self.rect.x -= VELPERSONAJE / 1.5
        elif teclas[pygame.K_a]:
            self.rect.x -= VELPERSONAJE
        elif teclas[pygame.K_d]:
            self.rect.x += VELPERSONAJE
        elif teclas[pygame.K_s]:
            self.rect.y += VELPERSONAJE
        elif teclas[pygame.K_w]:
            self.rect.y -= VELPERSONAJE

        # Disparo
        if teclas[pygame.K_SPACE]:
            tiempo = pygame.time.get_ticks()
            if tiempo - self.ultimo_disparo > self.cadencia:
                jugador.disparo()
                self.ultimo_disparo = tiempo

        # Limite de margenes
        if self.rect.left < LEFT:
            self.rect.left = LEFT
        if self.rect.right > RIGHT:
            self.rect.right = RIGHT
        if self.rect.top < TOP:
            self.rect.top = TOP
        if self.rect.bottom > BOTTOM:
            self.rect.bottom = BOTTOM

    def disparo(self):
        teclas = pygame.key.get_pressed()
        direccion = 0
        if teclas[pygame.K_w] and teclas[pygame.K_d]:
            direccion = 5
        elif teclas[pygame.K_w] and teclas[pygame.K_a]:
            direccion = 6
        elif teclas[pygame.K_s] and teclas[pygame.K_d]:
            direccion = 7
        elif teclas[pygame.K_s] and teclas[pygame.K_a]:
            direccion = 8
        elif teclas[pygame.K_d]:
            direccion = 2
        elif teclas[pygame.K_s]:
            direccion = 3
        elif teclas[pygame.K_a]:
            direccion = 1
        elif teclas[pygame.K_w]:
            direccion = 4

        bala = Disparos(self.rect.centerx, self.rect.centery, direccion)
        balas.add(bala)


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/frente2.png').convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ancho - self.rect.width)
        self.rect.y = random.randrange(alto - self.rect.height)

        self.velocidad_x = VELENEMIGO
        self.velocidad_y = VELENEMIGO

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limite de margenes
        if self.rect.left <= LEFT:
            self.rect.left = LEFT
            self.velocidad_x += VELENEMIGO
        if self.rect.right >= RIGHT:
            self.rect.right = RIGHT
            self.velocidad_x -= VELENEMIGO
        if self.rect.top <= TOP:
            self.rect.top = TOP
            self.velocidad_y += VELENEMIGO
        if self.rect.bottom >= BOTTOM:
            self.rect.bottom = BOTTOM
            self.velocidad_y -= VELENEMIGO


class Disparos(pygame.sprite.Sprite):
    dis = 0

    def __init__(self, x, y, direccion):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/tears.png').convert(), (15, 15))
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.dis = direccion

    def update(self):
        if self.dis == 4 or self.dis == 0:
            self.rect.y -= VELDISPARO
        elif self.dis == 2:
            self.rect.x += VELDISPARO
        elif self.dis == 1:
            self.rect.x -= VELDISPARO
        elif self.dis == 3:
            self.rect.y += VELDISPARO
        elif self.dis == 5:
            self.rect.y -= VELDISPARO / 1.5
            self.rect.x += VELDISPARO / 1.5
        elif self.dis == 6:
            self.rect.y -= VELDISPARO / 1.5
            self.rect.x -= VELDISPARO / 1.5
        elif self.dis == 7:
            self.rect.y += VELDISPARO / 1.5
            self.rect.x += VELDISPARO / 1.5
        elif self.dis == 8:
            self.rect.y += VELDISPARO / 1.5
            self.rect.x -= VELDISPARO / 1.5

        if self.rect.right >= 890:
            self.kill()
        if self.rect.top <= 85:
            self.kill()
        if self.rect.bottom >= 485:
            self.kill()
        if self.rect.left <= 100:
            self.kill()


# Inicialización
pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()

# Título
pygame.display.set_caption('The Binding of Isaac')

# Icono y fondo
icono = pygame.image.load('img/icono.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('img/fondo.png')

# Grupos de sprites, interpretación del objeto jugador.
sprites = pygame.sprite.Group()
spritesE = pygame.sprite.Group()
colisiones = pygame.sprite.Group()
balas = pygame.sprite.Group()

for i in range(random.randrange(3, 7)):
    enemigo = Enemigo()
    spritesE.add(enemigo)

jugador = Jugador()
sprites.add(jugador)

# Bucle de juego
ejecutando = True

while ejecutando:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    sprites.update()
    spritesE.update()
    balas.update()

    for enemigo in spritesE.sprites():
        colisiones.add(enemigo)
        # Colision entre el personaje y algún enemigo
        colision = pygame.sprite.spritecollide(jugador, colisiones, False)
        # Colision entre la bala y algún enemigo
        colision2 = pygame.sprite.spritecollide(enemigo, balas, False)
        if colision:
            # Perder vidas y comprobar si le quedan vidas
            jugador.image = pygame.image.load('img/explosion.png')
        else:
            colisiones.empty()
        if colision2:
            # Eliminar al enemigo tocado por la bala
            enemigo.kill()

    sprites.draw(ventana)
    spritesE.draw(ventana)
    balas.draw(ventana)
    pygame.display.flip()

pygame.quit()
