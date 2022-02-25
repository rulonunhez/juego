import sqlite3
from dis import dis

import pygame
import sys
import random

from PyQt5 import QtSql
from pygame.locals import *

ANCHO = 1200
ALTO = 700
FPS = 60
NEGRO = (0, 0, 0)
WHITE = (255, 255, 255)
ROJO = (255, 0, 0)
VELDISPARO = 8
VELDISPAROE = 5
VELPERSONAJE = 6
VELENEMIGO = 3
LEFT = 125
RIGHT = 1065
TOP = 100
BOTTOM = 565

movimiento_abajo = ['img/abajo1.png', 'img/abajo1.png', 'img/abajo1.png', 'img/abajo2.png', 'img/abajo2.png',
                    'img/abajo2.png',
                    'img/abajo4.png', 'img/abajo4.png', 'img/abajo4.png', 'img/abajo5.png', 'img/abajo5.png',
                    'img/abajo5.png']

movimiento_arriba = ['img/arriba1.png', 'img/arriba1.png', 'img/arriba1.png', 'img/arriba2.png', 'img/arriba2.png',
                     'img/arriba2.png',
                     'img/arriba3.png', 'img/arriba3.png', 'img/arriba3.png', 'img/arriba4.png', 'img/arriba4.png',
                     'img/arriba4.png']

movimiento_derecha = ['img/derecha1.png', 'img/derecha1.png', 'img/derecha2.png', 'img/derecha2.png',
                      'img/derecha3.png', 'img/derecha3.png',
                      'img/derecha4.png', 'img/derecha4.png', 'img/derecha5.png', 'img/derecha5.png',
                      'img/derecha6.png', 'img/derecha6.png',
                      'img/derecha7.png', 'img/derecha7.png', 'img/derecha8.png', 'img/derecha8.png',
                      'img/derecha9.png', 'img/derecha9.png',
                      'img/derecha10.png', 'img/derecha10.png']

movimiento_izquierda = ['img/izquierda1.png', 'img/izquierda1.png', 'img/izquierda2.png', 'img/izquierda2.png',
                        'img/izquierda3.png', 'img/izquierda3.png',
                        'img/izquierda4.png', 'img/izquierda4.png', 'img/izquierda5.png', 'img/izquierda5.png',
                        'img/izquierda6.png', 'img/izquierda6.png',
                        'img/izquierda7.png', 'img/izquierda7.png', 'img/izquierda8.png', 'img/izquierda8.png',
                        'img/izquierda9.png', 'img/izquierda9.png',
                        'img/izquierda10.png', 'img/izquierda10.png']

movimiento_spider = ['img/spider_abajo.png', 'img/spider_abajo2.png', 'img/spider_abajo3.png']

movimiento_peep = ['img/peeps/peep2.png', 'img/peeps/peep1.png']

movimiento_widow = ['img/widow/widow1.png', 'img/widow/widow2.png']

barra_vida = ['img/barraVida/barraVida1.png', 'img/barraVida/barraVida2.png', 'img/barraVida/barraVida3.png',
              'img/barraVida/barraVida4.png', 'img/barraVida/barraVida5.png', 'img/barraVida/barraVida6.png',
              'img/barraVida/barraVida7.png', 'img/barraVida/barraVida8.png', 'img/barraVida/barraVida9.png',
              'img/barraVida/barraVida10.png', 'img/barraVida/barraVida11.png', 'img/barraVida/barraVida12.png',
              'img/barraVida/barraVida13.png', 'img/barraVida/barraVida14.png', 'img/barraVida/barraVida15.png',
              'img/barraVida/barraVida16.png', 'img/barraVida/barraVida17.png', 'img/barraVida/barraVida18.png',
              'img/barraVida/barraVida19.png', 'img/barraVida/barraVida20.png', 'img/barraVida/barraVida21.png']


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load('img/quieto.png')
        self.image = pygame.transform.scale(pygame.image.load('img/abajoQuieto.png').convert(), (40, 40))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)
        self.frameAbajo = 0
        self.frameArriba = 0
        self.frameDer = 0
        self.frameIzq = 0
        self.ultimaDireccion = 'abajo'

        self.cadencia = 500
        self.delay_colision = 1500
        self.ultimo_disparo = pygame.time.get_ticks()
        self.ultima_colision = pygame.time.get_ticks()
        self.disparar = True

    def update(self):
        # ventana.blit(fondo, (0, 0))

        # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()

        # Movimiento del personaje
        if teclas[pygame.K_w] and teclas[pygame.K_d]:
            self.rect.y -= VELPERSONAJE / 1.5
            self.rect.x += VELPERSONAJE / 1.5
            self.image = pygame.transform.scale(pygame.image.load(movimiento_arriba[self.frameArriba]).convert(),
                                                (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameArriba += 1
            self.ultimaDireccion = 'arriba'
            if self.frameArriba == len(movimiento_arriba):
                self.frameArriba = 0
        elif teclas[pygame.K_w] and teclas[pygame.K_a]:
            self.rect.y -= VELPERSONAJE / 1.5
            self.rect.x -= VELPERSONAJE / 1.5
            self.image = pygame.transform.scale(pygame.image.load(movimiento_arriba[self.frameArriba]).convert(),
                                                (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameArriba += 1
            self.ultimaDireccion = 'arriba'
            if self.frameArriba == len(movimiento_arriba):
                self.frameArriba = 0
        elif teclas[pygame.K_s] and teclas[pygame.K_d]:
            self.rect.y += VELPERSONAJE / 1.5
            self.rect.x += VELPERSONAJE / 1.5
            self.image = pygame.transform.scale(pygame.image.load(movimiento_abajo[self.frameAbajo]).convert(),
                                                (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameAbajo += 1
            self.ultimaDireccion = 'abajo'
            if self.frameAbajo == len(movimiento_abajo):
                self.frameAbajo = 0
        elif teclas[pygame.K_s] and teclas[pygame.K_a]:
            self.rect.y += VELPERSONAJE / 1.5
            self.rect.x -= VELPERSONAJE / 1.5
            self.image = pygame.transform.scale(pygame.image.load(movimiento_abajo[self.frameAbajo]).convert(),
                                                (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameAbajo += 1
            self.ultimaDireccion = 'abajo'
            if self.frameAbajo == len(movimiento_abajo):
                self.frameAbajo = 0
        elif teclas[pygame.K_a]:
            self.rect.x -= VELPERSONAJE
            self.image = pygame.transform.scale(pygame.image.load(movimiento_izquierda[self.frameIzq]).convert(),
                                                (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameIzq += 1
            self.ultimaDireccion = 'izquierda'
            if self.frameIzq == len(movimiento_izquierda):
                self.frameIzq = 0
        elif teclas[pygame.K_d]:
            self.rect.x += VELPERSONAJE
            self.image = pygame.transform.scale(pygame.image.load(movimiento_derecha[self.frameDer]).convert(),
                                                (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameDer += 1
            self.ultimaDireccion = 'derecha'
            if self.frameDer == len(movimiento_derecha):
                self.frameDer = 0
        elif teclas[pygame.K_s]:
            self.rect.y += VELPERSONAJE
            self.image = pygame.transform.scale(pygame.image.load(movimiento_abajo[self.frameAbajo]).convert(),
                                                (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameAbajo += 1
            self.ultimaDireccion = 'abajo'
            if self.frameAbajo == len(movimiento_abajo):
                self.frameAbajo = 0
        elif teclas[pygame.K_w]:
            self.rect.y -= VELPERSONAJE
            self.image = pygame.transform.scale(pygame.image.load(movimiento_arriba[self.frameArriba]).convert(),
                                                (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameArriba += 1
            self.ultimaDireccion = 'arriba'
            if self.frameArriba == len(movimiento_arriba):
                self.frameArriba = 0
        else:
            if self.ultimaDireccion == 'abajo':
                self.image = pygame.transform.scale(pygame.image.load('img/abajoQuieto.png').convert(), (40, 40))
                self.image.set_colorkey(NEGRO)
                self.frameAbajo = 0
            elif self.ultimaDireccion == 'arriba':
                self.image = pygame.transform.scale(pygame.image.load('img/arribaQuieto.png').convert(), (40, 40))
                self.image.set_colorkey(NEGRO)
                self.frameArriba = 0
            elif self.ultimaDireccion == 'derecha':
                self.image = pygame.transform.scale(pygame.image.load('img/derecha1.png').convert(), (40, 40))
                self.image.set_colorkey(NEGRO)
                self.frameDer = 0
            elif self.ultimaDireccion == 'izquierda':
                self.image = pygame.transform.scale(pygame.image.load('img/izquierda1.png').convert(), (40, 40))
                self.image.set_colorkey(NEGRO)
                self.frameDer = 0

        # Disparo
        if self.disparar:
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

        bala = Disparos(self.rect.centerx, self.rect.centery, direccion, self.ultimaDireccion)
        balas.add(bala)


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/spider_abajo.png').convert(), (55, 60))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.frame = 1
        self.contador = 0

        self.velocidad_x = random.randrange(2, 4)
        self.velocidad_y = random.randrange(2, 4)

    def update(self):
        self.image = pygame.transform.scale(pygame.image.load(movimiento_spider[self.frame]).convert(), (55, 60))
        self.image.set_colorkey(NEGRO)
        if self.contador % 6 == 0:
            self.frame += 1
            if self.frame == len(movimiento_spider):
                self.frame = 0
        self.contador += 1
        if self.contador == 36:
            self.contador = 0

        jugador.rect.x
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limite de margenes
        if self.rect.left <= LEFT:
            self.rect.left = LEFT
            self.velocidad_x = VELENEMIGO
            if self.rect.y > jugador.rect.y:
                self.velocidad_y = -VELENEMIGO
            elif self.rect.y == jugador.rect.y:
                self.velocidad_y = 0
            elif self.rect.y < jugador.rect.y:
                self.velocidad_y = VELENEMIGO

        if self.rect.right >= RIGHT:
            self.rect.right = RIGHT
            self.velocidad_x = -VELENEMIGO
            if self.rect.y > jugador.rect.y:
                self.velocidad_y = -VELENEMIGO
            elif self.rect.y == jugador.rect.y:
                self.velocidad_y = 0
            elif self.rect.y < jugador.rect.y:
                self.velocidad_y = VELENEMIGO

        if self.rect.top <= TOP:
            self.rect.top = TOP
            self.velocidad_y = VELENEMIGO
            if self.rect.x > jugador.rect.x:
                self.velocidad_x = -VELENEMIGO
            elif self.rect.x == jugador.rect.x:
                self.velocidad_x = 0
            elif self.rect.x < jugador.rect.x:
                self.velocidad_x = VELENEMIGO

        if self.rect.bottom >= BOTTOM:
            self.rect.bottom = BOTTOM
            self.velocidad_y = -VELENEMIGO
            if self.rect.x > jugador.rect.x:
                self.velocidad_x = -VELENEMIGO
            elif self.rect.x == jugador.rect.x:
                self.velocidad_x = 0
            elif self.rect.x < jugador.rect.x:
                self.velocidad_x = VELENEMIGO


class Disparos(pygame.sprite.Sprite):
    dis = 0

    def __init__(self, x, y, direccion, ultimaPosicion):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/tears.png').convert(), (20, 20))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (x + 10, y + 5)
        # self.rect.centerx = x
        self.dis = direccion
        self.ultimaPosicion = ultimaPosicion

    def update(self):
        if self.dis == 4:
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
        elif self.dis == 0:
            if self.ultimaPosicion == 'arriba':
                self.rect.y -= VELDISPARO
            elif self.ultimaPosicion == 'abajo':
                self.rect.y += VELDISPARO
            elif self.ultimaPosicion == 'derecha':
                self.rect.x += VELDISPARO
            elif self.ultimaPosicion == 'izquierda':
                self.rect.x -= VELDISPARO

        if self.rect.right >= RIGHT:
            self.kill()
        if self.rect.top <= TOP:
            self.kill()
        if self.rect.bottom >= BOTTOM:
            self.kill()
        if self.rect.left <= LEFT:
            self.kill()


class Vida(pygame.sprite.Sprite):
    def __init__(self, x, y=None):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/vida.png').convert(), (50, 50))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        if y is None:
            contador = x * 50
            self.rect.center = (contador, 40)
        else:
            self.rect.center = (x, y)


class Perder(pygame.sprite.Sprite):
    def __init__(self, imagen):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(imagen).convert(), (400, 504))
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)


class Llave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/llave.png').convert(), (50, 25))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2 + 30, ALTO // 2)


class Flecha(pygame.sprite.Sprite):
    def __init__(self, x, y, rotacion):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/flecha.png').convert(), (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.image = pygame.transform.rotate(self.image, rotacion)


class Peep(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/peeps/peep2.png').convert(), (100, 100))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.frame = 0

    def disparo(self, posJugadorX, posJugadorY):
        bala = DisparoPeep(self.rect.centerx, self.rect.centery, posJugadorX, posJugadorY)
        spritesDisparosPeep.add(bala)

    def update(self):
        self.frame += 1
        if self.frame == 20:
            self.image = pygame.transform.scale(pygame.image.load('img/peeps/peep2.png').convert(), (100, 100))
            self.image.set_colorkey(NEGRO)
        if self.frame == 125:
            self.image = pygame.transform.scale(pygame.image.load('img/peeps/peep1.png').convert(), (100, 100))
            self.image.set_colorkey(NEGRO)
            self.disparo(jugador.rect.centerx, jugador.rect.centery)
            # peep2.disparo(jugador.rect.centerx, jugador.rect.centery)
            # peep3.disparo(jugador.rect.centerx, jugador.rect.centery)
            # peep4.disparo(jugador.rect.centerx, jugador.rect.centery)
            self.frame = 0


class DisparoPeep(pygame.sprite.Sprite):
    def __init__(self, x, y, posJugadorX, posJugadorY):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/blood_tears.png').convert(), (30, 30))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.posJugadorX = posJugadorX
        self.posJugadorY = posJugadorY

    def update(self):
        direccion = -((self.y - self.posJugadorY) / 60)
        direccion2 = -((self.x - self.posJugadorX) / 60)

        if 1.5 > direccion > -1.5 and 1.5 > direccion2 > -1.5:
            if self.x == 200 and self.y == 140:
                direccion += 3
                direccion2 += 3
            if self.x == 200 and self.y == 525:
                direccion -= 3
                direccion2 += 3
            if self.x == 1000 and self.y == 140:
                direccion += 3
                direccion2 -= 3
            if self.x == 1000 and self.y == 525:
                direccion -= 3
                direccion2 -= 3

        self.rect.x += direccion2
        self.rect.y += direccion

        if self.rect.right >= RIGHT:
            self.kill()
        if self.rect.top <= TOP:
            self.kill()
        if self.rect.bottom >= BOTTOM:
            self.kill()
        if self.rect.left <= LEFT:
            self.kill()


class Widow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/widow/widow1.png').convert(), (210, 109))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (200, 400)
        self.frame = 0
        self.reps = 0
        self.velocidad_x = 3
        self.velocidad_y = 3
        self.direccion = 0
        self.foto = 0

    def update(self, posJugadorX, posJugadorY):
        # Necesario ajustar los valores de la imagen y controlar los bordes (en algunos casos)
        self.frame += 1
        if self.frame == 50 and self.reps <= 3:
            if self.rect.x + 300 > posJugadorX > self.rect.x - 50:
                if posJugadorY > self.rect.y:
                    # Movimiento hacia abajo
                    self.direccion = 5
                else:
                    # Movimiento hacia arriba
                    self.direccion = 1
            elif self.rect.y + 100 > posJugadorY > self.rect.y - 50:
                if posJugadorX < self.rect.x:
                    # Movimiento hacia la izquierda
                    self.direccion = 7
                else:
                    # Movimiento hacia la derecha
                    self.direccion = 3
            elif posJugadorX > self.rect.x + 300:
                if posJugadorY > self.rect.y + 100:
                    # Movimiento en diagonal abajo-derecha
                    self.direccion = 4
                else:
                    # Movimiento en diagonal arriba-derecha
                    self.direccion = 2
            else:
                if posJugadorY > self.rect.y + 100:
                    # Movimiento en diagonal abajo-izquierda
                    self.direccion = 6
                else:
                    # Movimiento en diagonal arriba-izquierda
                    self.direccion = 8
            self.reps += 1

        if 51 < self.frame < 100 and self.reps <= 3:
            if self.frame % 4 == 0:
                self.image = pygame.transform.scale(pygame.image.load(movimiento_widow[self.foto]).convert(),
                                                    (210, 109))
                self.image.set_colorkey(NEGRO)
                self.foto += 1
                if self.foto == 2:
                    self.foto = 0
            self.dash(self.direccion)
        else:
            if self.reps == 3:
                self.image = pygame.transform.scale(pygame.image.load('img/widow/widowCargando.png').convert(),
                                                    (210, 109))
                self.image.set_colorkey(NEGRO)

            elif self.reps == 4:
                self.image = pygame.transform.scale(pygame.image.load('img/widow/widowDisparando.png').convert(),
                                                    (210, 109))
                self.image.set_colorkey(NEGRO)

        if self.frame == 100:
            self.frame = 0

        if self.reps == 4:
            self.velocidad_x = 0
            self.velocidad_y = 0
            self.disparo()
            self.reps = 0
            self.frame = 0

    def dash(self, direccion):
        if direccion == 1:
            self.velocidad_x = 0
            self.velocidad_y = - (VELDISPAROE + 3)
        elif direccion == 2:
            self.velocidad_x = VELDISPAROE
            self.velocidad_y = -VELDISPAROE
        elif direccion == 3:
            self.velocidad_x = VELDISPAROE + 3
            self.velocidad_y = 0
        elif direccion == 4:
            self.velocidad_x = VELDISPAROE
            self.velocidad_y = VELDISPAROE
        elif direccion == 5:
            self.velocidad_x = 0
            self.velocidad_y = VELDISPAROE + 3
        elif direccion == 6:
            self.velocidad_x = -VELDISPAROE
            self.velocidad_y = VELDISPAROE
        elif direccion == 7:
            self.velocidad_x = - (VELDISPAROE + 3)
            self.velocidad_y = 0
        elif direccion == 8:
            self.velocidad_x = -VELDISPAROE
            self.velocidad_y = -VELDISPAROE

        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.bottom >= BOTTOM:
            self.rect.bottom = BOTTOM
        elif self.rect.top <= TOP:
            self.rect.top = TOP
        elif self.rect.right >= RIGHT:
            self.rect.right = RIGHT
        elif self.rect.left <= LEFT:
            self.rect.left = LEFT

    def disparo(self):
        i = 1
        while i <= 8:
            bala = DisparoWidow(self.rect.centerx, self.rect.centery, i)
            spritesDisparosWidow.add(bala)
            i += 1


class DisparoWidow(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/blood_tears.png').convert(), (30, 30))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.direccion = direccion

    def update(self):
        if self.direccion == 1:
            self.rect.centerx += 0
            self.rect.centery -= VELDISPAROE + 3
        elif self.direccion == 2:
            self.rect.centerx += VELDISPAROE
            self.rect.centery -= VELDISPAROE
        elif self.direccion == 3:
            self.rect.centerx += VELDISPAROE + 3
            self.rect.centery += 0
        elif self.direccion == 4:
            self.rect.centerx += VELDISPAROE
            self.rect.centery += VELDISPAROE
        elif self.direccion == 5:
            self.rect.centerx += 0
            self.rect.centery += VELDISPAROE + 3
        elif self.direccion == 6:
            self.rect.centerx -= VELDISPAROE
            self.rect.centery += VELDISPAROE
        elif self.direccion == 7:
            self.rect.centerx -= VELDISPAROE + 3
            self.rect.centery += 0
        elif self.direccion == 8:
            self.rect.centerx -= VELDISPAROE
            self.rect.centery -= VELDISPAROE

        if self.rect.bottom >= BOTTOM:
            self.kill()
        elif self.rect.top <= TOP:
            self.kill()
        elif self.rect.right >= RIGHT:
            self.kill()
        elif self.rect.left <= LEFT:
            self.kill()


class VidaWidow(pygame.sprite.Sprite):
    def __init__(self, ventana):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/barraVida/barraVida1.PNG').convert(), (255, 36))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO - 50
        self.ventana = ventana


class ImagenTeclado(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/instrucciones.png').convert(), (502, 300))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (500, 400)

    def update(self, vidas):
        pygame.draw.rect(self.ventana, ROJO, [ANCHO / 2, ALTO, 275, 55], 0)


# Inicialización
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

# Título
pygame.display.set_caption('The Binding of Isaac')

# Icono y fondo
icono = pygame.image.load('img/icono.png')
pygame.display.set_icon(icono)
fondo = pygame.transform.scale(pygame.image.load('img//fondos/fondo.png').convert(), (ANCHO, ALTO))

# Grupos de sprites, interpretación del objeto jugador.
sprites = pygame.sprite.Group()
spritesE = pygame.sprite.Group()
colisiones = pygame.sprite.Group()
balas = pygame.sprite.Group()
spritesVidas = pygame.sprite.Group()
spritesPerder = pygame.sprite.Group()
spritesLlaves = pygame.sprite.Group()
spritesFlechas = pygame.sprite.Group()
spritesPeeps = pygame.sprite.Group()
spritesDisparosPeep = pygame.sprite.Group()
spriteBossFinal = pygame.sprite.Group()
spritesDisparosWidow = pygame.sprite.Group()
spriteBarraVida = pygame.sprite.Group()
spriteImagenInstrucciones = pygame.sprite.Group()

filename ='bbdd.sqlite'

# Funciones para la conexión con la base de datos
def db_connect(filename):
    try:
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            return False
        else:
            print('Conexión establecida')
            return True
    except Exception as error:
        print('Problemas en conexión ', error)

def add_puntuacion():
    try:
        query = QtSql.QSqlQuery()
        tiempo = momento_win ** (-1) * 1000000
        total = cuentaVidas * tiempo
        query.prepare('insert into puntuaciones (tiempo, vidas, total) values (:tiempo, :vidas, :total)')
        query.bindValue(':tiempo', float(momento_win))
        query.bindValue(':vidas', int(cuentaVidas))
        query.bindValue(':total', float(total))
        print(tiempo, cuentaVidas, total)
        if query.exec_():
            print('Puntuación subida')
        else:
            print(query.lastError().text())
    except Exception as error:
        print('Error subiendo una puntuación', error)

# Funciones para los menús
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def options():
    running = True
    while running:
        ventana.blit(fondo, (0, 0))

        draw_text('Instrucciones', font, (255, 255, 255), ventana, 60, 50)
        lore = pygame.Rect(150, 130, 890, 125)
        pygame.draw.rect(ventana, NEGRO, lore)
        draw_text('Tú y tu hermano entrasteis en esta cueva para jugar un rato pero algo salió de las', font2, WHITE,
                  ventana, 160, 140)
        draw_text('sombras y se lo llevó. Te sientes muy triste y enfadado y decides entrar en la cueva', font2, WHITE,
                  ventana, 160, 160)
        draw_text('a buscarlo. En la cueva acechan monstruos y trampas, ten cuidado, para derrotarlos', font2, WHITE,
                  ventana, 160, 180)
        draw_text('puedes canalizar tu ira y disparar tus lagrimas.', font2, WHITE,
                  ventana, 160, 200)
        draw_text('¡¡¡¡Encuentralo antes de que sea demasiado tarde!!!!', font2, WHITE,
                  ventana, 160, 220)
        instrucciones = ImagenTeclado()
        spriteImagenInstrucciones.add(instrucciones)
        pygame.draw.circle(ventana, NEGRO, (520, 317), 7)
        draw_text('Movimiento', font2, WHITE,
                  ventana, 540, 310)
        pygame.draw.circle(ventana, NEGRO, (380, 419), 7)
        draw_text('Salir / Volver al menú principal', font2, WHITE,
                  ventana, 400, 412)
        pygame.draw.circle(ventana, NEGRO, (800, 510), 7)
        draw_text('Disparar', font2, WHITE,
                  ventana, 820, 503)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        spriteImagenInstrucciones.draw(ventana)
        pygame.display.update()
        clock.tick(60)

def puntuaciones():
    running = True
    while running:
        ventana.blit(fondo, (0, 0))
        tiempo = momento_win ** (-1) * 1000000
        total = cuentaVidas * tiempo
        draw_text('Tu puntuacion: ' + str(round(total, 2)), font, WHITE, ventana, 410, 150)
        draw_text('Mejores puntuaciones ', font, WHITE, ventana, 400, 200)
        draw_text('TIEMPO', font, WHITE, ventana, 200, 300)
        draw_text('VIDAS', font, WHITE, ventana, 500, 300)
        draw_text('TOTAL', font, WHITE, ventana, 800, 300)
        query = QtSql.QSqlQuery()
        query.prepare('select tiempo, vidas, total from puntuaciones order by total desc')
        x, j = (220, 350)
        if query.exec_():
            while query.next() and j <= 490:
                tiempo = str(round(query.value(0), 2))
                vidas = str(query.value(1))
                total = str(round(query.value(2), 2))
                draw_text(tiempo, font2, WHITE, ventana, x, j)
                draw_text(vidas, font2, WHITE, ventana, x + 330, j)
                draw_text(total, font2, WHITE, ventana, x + 610, j)
                j += 70

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)

xE = 150
yE = 150

jugadorCreado = False
arañasCreadas = False
peepsCreados = False
bossCreado = False
barraVidaCreada = False
vidasCreadas = False

# Bucle de juego
ejecutando = True

eliminados = 0
cuentaVidas = 2
i = 1

vidaPeep1 = 5
vidaPeep2 = 5
vidaPeep3 = 5
vidaPeep4 = 5

vidaWidow = 0

peepsEliminados = 0

jugador = None
peep1 = None
bossFinal = None

colisionVidaJugador = False
vida3_item = None
vida4_item = None

fase = 1
click = False

font = pygame.font.SysFont(None, 50)
font2 = pygame.font.SysFont(None, 30)

db_connect(filename)

while ejecutando:
    clock.tick(FPS)

    if fase != 1:
        ventana.blit(fondo, (0, 0))
        if jugadorCreado == False:
            jugador = Jugador()
            sprites.add(jugador)
            jugadorCreado = True

    if fase == 1:
        ventana.blit(fondo, (0, 0))
        draw_text('The Binding of Isaac', font, (255, 255, 255), ventana, 425, 150)
        draw_text('Menú', font2, (255, 255, 255), ventana, 570, 200)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(500, ALTO / 2 - 100, 200, 65)
        button_2 = pygame.Rect(500, ALTO / 2, 200, 65)

        if button_1.collidepoint((mx, my)):
            if click:
                fase = 2
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.ellipse(ventana, NEGRO, button_1, 80)
        pygame.draw.ellipse(ventana, NEGRO, button_2, 80)
        draw_text('Jugar', font2, (255, 255, 255), ventana, 570, 270)
        draw_text('Instrucciones', font2, (255, 255, 255), ventana, 535, 370)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()

    elif fase == 2 and arañasCreadas == False:
        # Cambiar a 8 antes de seguir con las pruebas
        araña1 = Enemigo(150, 150)
        araña2 = Enemigo(250, 150)
        araña3 = Enemigo(700, 150)
        araña4 = Enemigo(800, 150)
        araña5 = Enemigo(800, 500)
        araña6 = Enemigo(700, 500)
        araña7 = Enemigo(250, 500)
        araña8 = Enemigo(150, 500)
        spritesE.add(araña1, araña2, araña3, araña4, araña5, araña6, araña7, araña8)
        arañasCreadas = True

    elif fase == 3 and peepsCreados == False:
        peep1 = Peep(200, 140)
        peep2 = Peep(1000, 140)
        peep3 = Peep(200, 525)
        peep4 = Peep(1000, 525)
        spritesPeeps.add(peep1, peep2, peep3, peep4)
        peepsCreados = True

    elif fase == 4 and bossCreado == False:
        bossFinal = Widow()
        spriteBossFinal.add(bossFinal)
        bossCreado = True

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_ESCAPE] and jugador is not None:
        fase = 1
        jugador.kill()
        spritesE.empty()
        spritesVidas.empty()
        jugadorCreado = False
        arañasCreadas = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # spriteBossFinal.update()

    if sprites.has(jugador):
        # Vidas del contador
        if vidasCreadas == False:
            vida1_contador = Vida(1)
            vida2_contador = Vida(2)
            spritesVidas.add(vida1_contador, vida2_contador)
            vidasCreadas = True

        colision = pygame.sprite.spritecollide(jugador, spritesE, False)
        if colision:
            momento_colision = pygame.time.get_ticks()
            spritesVidas.remove(vida2_contador)
            if momento_colision - jugador.ultima_colision > jugador.delay_colision:
                cuentaVidas -= 1
                jugador.ultima_colision = momento_colision
                if cuentaVidas == 0:
                    spritesVidas.empty()
                    jugador.disparar = False
                    # jugador.update = False
                    mensajePerdida = Perder('img/fondos/fondoPerderAraña.png')
                    spritesPerder.add(mensajePerdida)
                    spritesE.empty()
                    balas.empty()
                    jugador.image.fill(NEGRO)

        if spritesVidas.has(vida3_item) or spritesVidas.has(vida4_item):
            colisionVidaJugador = pygame.sprite.groupcollide(spritesVidas, sprites, True, False)
            if colisionVidaJugador:
                cuentaVidas += 1
                if vida4_item is not None:
                    vida4_item.kill()
                    vida4_contador = Vida(cuentaVidas)
                    spritesVidas.add(vida4_contador)
                else:
                    vida3_item.kill()
                    vida3_contador = Vida(cuentaVidas)
                    spritesVidas.add(vida3_contador)
                eliminados = 0

        colisionBalasJugador = pygame.sprite.spritecollide(jugador, spritesDisparosPeep, True)
        if colisionBalasJugador:
            momento_colision = pygame.time.get_ticks()
            # Solo se elimina la ultima vida
            if momento_colision - jugador.ultima_colision > jugador.delay_colision:
                cuentaVidas -= 1
                if spritesVidas.has(vida3_contador):
                    spritesVidas.remove(vida3_contador)
                elif spritesVidas.has(vida2_contador):
                    spritesVidas.remove(vida2_contador)
                jugador.ultima_colision = momento_colision
                if cuentaVidas == 0:
                    spritesVidas.empty()
                    jugador.disparar = False
                    # jugador.update = False
                    mensajePerdida = Perder('img/fondos/fondoPerderPeep.png')
                    spritesPerder.add(mensajePerdida)
                    spritesPeeps.empty()
                    spritesDisparosPeep.empty()
                    jugador.image.fill(NEGRO)

        colisionLlaveJugador = pygame.sprite.spritecollide(jugador, spritesLlaves, True)
        if colisionLlaveJugador:
            if fase == 2:
                spritesLlaves.empty()
                flecha = Flecha(160, 340, 270)
                flecha2 = Flecha(1030, 340, 90)
                flecha3 = Flecha(600, 140, 180)
                spritesFlechas.add(flecha)
                spritesFlechas.add(flecha2)
                spritesFlechas.add(flecha3)
                eliminados = 0
            elif fase == 3:
                flecha4 = Flecha(600, 140, 180)
                spritesFlechas.add(flecha4)

        colisionFlechaJugador = pygame.sprite.spritecollide(jugador, spritesFlechas, False)
        if colisionFlechaJugador:
            spritesFlechas.empty()
            fase += 1

        spriteBossFinal.update(jugador.rect.centerx, jugador.rect.centery)

    colision2 = pygame.sprite.groupcollide(spritesE, balas, True, True)
    if colision2:
        eliminados += 1

    # Cambiar a 8
    if eliminados == 8:
        vida3_item = Vida(ANCHO // 2 - 30, ALTO // 2)
        spritesVidas.add(vida3_item)
        llave = Llave()
        spritesLlaves.add(llave)

    # Cambiar fondo para abrir la puerta -> Al tocar la puerta cambio de pantalla

    if peep1 is None:
        pass
    else:
        colisionBalaPeep1 = pygame.sprite.spritecollide(peep1, balas, True)
        if colisionBalaPeep1:
            vidaPeep1 -= 1
            if vidaPeep1 == 0:
                spritesPeeps.remove(peep1)
                peep1.kill()
                peepsEliminados += 1
                peep1.disparo = False

        colisionBalaPeep2 = pygame.sprite.spritecollide(peep2, balas, True)
        if colisionBalaPeep2:
            vidaPeep2 -= 1
            if vidaPeep2 == 0:
                spritesPeeps.remove(peep2)
                peep2.kill()
                peepsEliminados += 1

        colisionBalaPeep3 = pygame.sprite.spritecollide(peep3, balas, True)
        if colisionBalaPeep3:
            vidaPeep3 -= 1
            if vidaPeep3 == 0:
                spritesPeeps.remove(peep3)
                peep3.kill()
                peepsEliminados += 1

        colisionBalaPeep4 = pygame.sprite.spritecollide(peep4, balas, True)
        if colisionBalaPeep4:
            vidaPeep4 -= 1
            if vidaPeep4 == 0:
                spritesPeeps.remove(peep4)
                peep4.kill()
                peepsEliminados += 1

    if peepsEliminados == 4:
        vida4_item = Vida(ANCHO // 2 - 30, ALTO // 2)
        spritesVidas.add(vida4_item)
        llave2 = Llave()
        spritesLlaves.add(llave)
        spritesDisparosPeep.empty()
        peepsEliminados = 0

    if bossFinal is not None:
        if barraVidaCreada == False:
            barraVidaWidow = VidaWidow(ventana)
            spriteBarraVida.add(barraVidaWidow)
            barraVidaCreada = True

        colisionBalaWidow = pygame.sprite.spritecollide(bossFinal, balas, True)
        if colisionBalaWidow:
            vidaWidow += 1
            barraVidaWidow.image = pygame.transform.scale(pygame.image.load(barra_vida[vidaWidow]).convert(), (255, 36))
            barraVidaWidow.image.set_colorkey(WHITE)
            spriteBarraVida.update(vidaWidow)
            if vidaWidow == 20:
                spritesDisparosWidow.empty()
                spriteBossFinal.empty()
                spriteBarraVida.empty()
                balas.empty()
                momento_win = pygame.time.get_ticks()
                add_puntuacion()
                puntuaciones()


        colisionJugadorDisparo = pygame.sprite.spritecollide(jugador, spritesDisparosWidow, True)
        if colisionJugadorDisparo:
            cuentaVidas -= 1
            if spritesVidas.has(vida4_contador):
                spritesVidas.remove(vida4_contador)
            elif spritesVidas.has(vida3_contador):
                spritesVidas.remove(vida3_contador)
            elif spritesVidas.has(vida2_contador):
                spritesVidas.remove(vida2_contador)
            if cuentaVidas == 0:
                spritesVidas.empty()
                jugador.disparar = False
                # jugador.update = False
                mensajePerdida = Perder('img/fondos/fondoPerderWidow.png')
                spritesPerder.add(mensajePerdida)
                spritesDisparosWidow.empty()
                spriteBossFinal.empty()
                spriteBarraVida.empty()
                balas.empty()
                jugador.image.fill(NEGRO)

        colisionJugadorWidow = pygame.sprite.spritecollide(jugador, spriteBossFinal, False)
        if colisionJugadorWidow:
            momento_colision = pygame.time.get_ticks()
            if momento_colision - jugador.ultima_colision > jugador.delay_colision:
                cuentaVidas -= 1
                if spritesVidas.has(vida4_contador):
                    spritesVidas.remove(vida4_contador)
                elif spritesVidas.has(vida3_contador):
                    spritesVidas.remove(vida3_contador)
                elif spritesVidas.has(vida2_contador):
                    spritesVidas.remove(vida2_contador)
                jugador.ultima_colision = momento_colision
                if cuentaVidas == 0:
                    spritesVidas.empty()
                    jugador.disparar = False
                    # jugador.update = False
                    mensajePerdida = Perder('img/fondos/fondoPerderWidow.png')
                    spritesPerder.add(mensajePerdida)
                    spritesDisparosWidow.empty()
                    spriteBossFinal.empty()
                    spriteBarraVida.empty()
                    balas.empty()
                    jugador.image.fill(NEGRO)

    spritesPeeps.update()
    spritesDisparosPeep.update()
    sprites.update()
    spritesE.update()
    balas.update()
    spritesDisparosWidow.update()

    sprites.draw(ventana)
    spritesE.draw(ventana)
    balas.draw(ventana)
    spritesVidas.draw(ventana)
    spritesPerder.draw(ventana)
    spritesLlaves.draw(ventana)
    spritesFlechas.draw(ventana)
    spritesPeeps.draw(ventana)
    spritesDisparosPeep.draw(ventana)
    spriteBossFinal.draw(ventana)
    spritesDisparosWidow.draw(ventana)
    spriteBarraVida.draw(ventana)

    pygame.display.flip()

pygame.quit()
