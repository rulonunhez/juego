from dis import dis

import pygame, sys
import random
from pygame.locals import *

ANCHO = 1200
ALTO = 700
FPS = 60
NEGRO = (0, 0, 0)
WHITE = (255, 255, 255)
VELDISPARO = 8
VELPERSONAJE = 6
VELENEMIGO = 3
LEFT = 125
RIGHT = 1065
TOP = 100
BOTTOM = 565

movimiento_abajo = ['img/abajo1.png', 'img/abajo1.png', 'img/abajo1.png', 'img/abajo2.png', 'img/abajo2.png', 'img/abajo2.png',
                    'img/abajo4.png', 'img/abajo4.png', 'img/abajo4.png', 'img/abajo5.png', 'img/abajo5.png', 'img/abajo5.png']

movimiento_arriba = ['img/arriba1.png', 'img/arriba1.png', 'img/arriba1.png', 'img/arriba2.png', 'img/arriba2.png', 'img/arriba2.png',
                     'img/arriba3.png', 'img/arriba3.png', 'img/arriba3.png', 'img/arriba4.png', 'img/arriba4.png', 'img/arriba4.png']

movimiento_derecha = ['img/derecha1.png', 'img/derecha1.png', 'img/derecha2.png', 'img/derecha2.png', 'img/derecha3.png', 'img/derecha3.png',
                      'img/derecha4.png', 'img/derecha4.png', 'img/derecha5.png', 'img/derecha5.png', 'img/derecha6.png', 'img/derecha6.png',
                      'img/derecha7.png', 'img/derecha7.png', 'img/derecha8.png', 'img/derecha8.png', 'img/derecha9.png', 'img/derecha9.png',
                      'img/derecha10.png', 'img/derecha10.png']

movimiento_izquierda = ['img/izquierda1.png', 'img/izquierda1.png', 'img/izquierda2.png', 'img/izquierda2.png', 'img/izquierda3.png', 'img/izquierda3.png',
                      'img/izquierda4.png', 'img/izquierda4.png', 'img/izquierda5.png', 'img/izquierda5.png', 'img/izquierda6.png', 'img/izquierda6.png',
                      'img/izquierda7.png', 'img/izquierda7.png', 'img/izquierda8.png', 'img/izquierda8.png', 'img/izquierda9.png', 'img/izquierda9.png',
                      'img/izquierda10.png', 'img/izquierda10.png']

movimiento_spider = ['img/spider_abajo.png', 'img/spider_abajo2.png', 'img/spider_abajo3.png']


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
        ventana.blit(fondo, (0, 0))

        # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()

        # Movimiento del personaje
        if teclas[pygame.K_w] and teclas[pygame.K_d]:
            self.rect.y -= VELPERSONAJE / 1.5
            self.rect.x += VELPERSONAJE / 1.5
            self.image = pygame.transform.scale(pygame.image.load(movimiento_arriba[self.frameArriba]).convert(), (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameArriba += 1
            self.ultimaDireccion = 'arriba'
            if self.frameArriba == len(movimiento_arriba):
                self.frameArriba = 0
        elif teclas[pygame.K_w] and teclas[pygame.K_a]:
            self.rect.y -= VELPERSONAJE / 1.5
            self.rect.x -= VELPERSONAJE / 1.5
            self.image = pygame.transform.scale(pygame.image.load(movimiento_arriba[self.frameArriba]).convert(), (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameArriba += 1
            self.ultimaDireccion = 'arriba'
            if self.frameArriba == len(movimiento_arriba):
                self.frameArriba = 0
        elif teclas[pygame.K_s] and teclas[pygame.K_d]:
            self.rect.y += VELPERSONAJE / 1.5
            self.rect.x += VELPERSONAJE / 1.5
            self.image = pygame.transform.scale(pygame.image.load(movimiento_abajo[self.frameAbajo]).convert(), (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameAbajo += 1
            self.ultimaDireccion = 'abajo'
            if self.frameAbajo == len(movimiento_abajo):
                self.frameAbajo = 0
        elif teclas[pygame.K_s] and teclas[pygame.K_a]:
            self.rect.y += VELPERSONAJE / 1.5
            self.rect.x -= VELPERSONAJE / 1.5
            self.image = pygame.transform.scale(pygame.image.load(movimiento_abajo[self.frameAbajo]).convert(), (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameAbajo += 1
            self.ultimaDireccion = 'abajo'
            if self.frameAbajo == len(movimiento_abajo):
                self.frameAbajo = 0
        elif teclas[pygame.K_a]:
            self.rect.x -= VELPERSONAJE
            self.image = pygame.transform.scale(pygame.image.load(movimiento_izquierda[self.frameIzq]).convert(), (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameIzq += 1
            self.ultimaDireccion = 'izquierda'
            if self.frameIzq == len(movimiento_izquierda):
                self.frameIzq = 0
        elif teclas[pygame.K_d]:
            self.rect.x += VELPERSONAJE
            self.image = pygame.transform.scale(pygame.image.load(movimiento_derecha[self.frameDer]).convert(), (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameDer += 1
            self.ultimaDireccion = 'derecha'
            if self.frameDer == len(movimiento_derecha):
                self.frameDer = 0
        elif teclas[pygame.K_s]:
            self.rect.y += VELPERSONAJE
            self.image = pygame.transform.scale(pygame.image.load(movimiento_abajo[self.frameAbajo]).convert(), (40, 40))
            self.image.set_colorkey(NEGRO)
            self.frameAbajo += 1
            self.ultimaDireccion = 'abajo'
            if self.frameAbajo == len(movimiento_abajo):
                self.frameAbajo = 0
        elif teclas[pygame.K_w]:
            self.rect.y -= VELPERSONAJE
            self.image = pygame.transform.scale(pygame.image.load(movimiento_arriba[self.frameArriba]).convert(), (40, 40))
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
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/fondoPerder.png').convert(), (400, 504))
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
        self.image = pygame.transform.scale(pygame.image.load('img/peep2.png').convert(), (100, 100))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.frame = 0

    def disparo(self, posJugadorX, posJugadorY):
        bala = DisparoPeep(self.rect.centerx, self.rect.centery, posJugadorX, posJugadorY)
        spritesDisparosPeep.add(bala)

    def update(self):
        self.frame += 1
        if self.frame == 125:
            self.disparo(jugador.rect.centerx, jugador.rect.centery)
            # peep2.disparo(jugador.rect.centerx, jugador.rect.centery)
            # peep3.disparo(jugador.rect.centerx, jugador.rect.centery)
            # peep4.disparo(jugador.rect.centerx, jugador.rect.centery)
            self.frame = 0

class DisparoPeep(pygame.sprite.Sprite):
    def __init__(self, x, y, posJugadorX, posJugadorY):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/bloodTears.png').convert(), (30, 30))
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

    # peep1 = Peep(200, 140)
    # peep2 = Peep(1000, 140)
    # peep3 = Peep(200, 525)
    # peep4 = Peep(1000, 525)


# Inicialización
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

# Título
pygame.display.set_caption('The Binding of Isaac')

# Icono y fondo
icono = pygame.image.load('img/icono.png')
pygame.display.set_icon(icono)
fondo = pygame.transform.scale(pygame.image.load('img/fondo.png').convert(), (1200, 700))

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

xE = 150
yE = 150

fase = 2
arañasCreadas = False
peepsCreados = False

jugador = Jugador()
sprites.add(jugador)

# Bucle de juego
ejecutando = True

eliminados = 0
cuentaVidas = 2
i = 1

vidaPeep1 = 5
vidaPeep2 = 5
vidaPeep3 = 5
vidaPeep4 = 5
peepsEliminados = 0

peep1 = None

vida1 = Vida(1)
vida2 = Vida(2)
spritesVidas.add(vida1, vida2)

while ejecutando:
    clock.tick(FPS)

    if fase == 2 and arañasCreadas == False:
        # Cambiar a 8 antes de seguir con las pruebas
        araña1 = Enemigo(150, 150)
        araña2 = Enemigo(250, 150)
        # araña3 = Enemigo(700, 150)
        # araña4 = Enemigo(800, 150)
        # araña5 = Enemigo(800, 500)
        # araña6 = Enemigo(700, 500)
        # araña7 = Enemigo(250, 500)
        # araña8 = Enemigo(150, 500)
        # spritesE.add(araña1, araña2, araña3, araña4, araña5, araña6, araña7, araña8)
        spritesE.add(araña1, araña2)
        arañasCreadas = True

    elif fase == 3 and peepsCreados == False:
        peep1 = Peep(200, 140)
        peep2 = Peep(1000, 140)
        peep3 = Peep(200, 525)
        peep4 = Peep(1000, 525)
        spritesPeeps.add(peep1, peep2, peep3, peep4)
        peepsCreados = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    sprites.update()
    spritesE.update()
    balas.update()

    colision = pygame.sprite.spritecollide(jugador, spritesE, False)
    if colision:
        momento_colision = pygame.time.get_ticks()
        spritesVidas.remove(vida2)
        if momento_colision - jugador.ultima_colision > jugador.delay_colision:
            cuentaVidas -= 1
            jugador.ultima_colision = momento_colision
            if cuentaVidas == 0:
                spritesVidas.empty()
                jugador.disparar = False
                # jugador.update = False
                mensajePerdida = Perder()
                spritesPerder.add(mensajePerdida)
                spritesE.empty()
                balas.empty()
                jugador.image.fill(NEGRO)

    colision2 = pygame.sprite.groupcollide(spritesE, balas, True, True)
    if colision2:
        eliminados += 1

    # Cambiar a 8
    if eliminados == 2:
        vida = Vida(ANCHO // 2 - 30, ALTO // 2)
        spritesVidas.add(vida)
        llave = Llave()
        spritesLlaves.add(llave)

    colisionVidaJugador = pygame.sprite.spritecollide(jugador, spritesVidas, True)
    if colisionVidaJugador:
        cuentaVidas += 1
        vida3 = Vida(cuentaVidas)
        spritesVidas.add(vida3)
        eliminados = 0

    colisionLlaveJugador = pygame.sprite.spritecollide(jugador, spritesLlaves, True)
    if colisionLlaveJugador:
        spritesLlaves.empty()
        flecha = Flecha(160, 340, 270)
        flecha2 = Flecha(1030, 340, 90)
        flecha3 = Flecha(600, 140, 180)
        spritesFlechas.add(flecha)
        spritesFlechas.add(flecha2)
        spritesFlechas.add(flecha3)
        eliminados = 0

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
        flecha4 = Flecha(600, 140, 180)
        spritesFlechas.add(flecha4)
        peepsEliminados = 0

    colisionFlechaJugador = pygame.sprite.spritecollide(jugador, spritesFlechas, False)
    if colisionFlechaJugador:
        spritesFlechas.empty()
        fase += 1

    colisionBalasJugador = pygame.sprite.spritecollide(jugador, spritesDisparosPeep, True)
    if colisionBalasJugador:
        momento_colision = pygame.time.get_ticks()
        # Solo se elimina la ultima vida
        if spritesVidas.has(vida3):
            spritesVidas.remove(vida3)
        elif spritesVidas.has(vida2):
            spritesVidas.remove(vida2)
        if momento_colision - jugador.ultima_colision > jugador.delay_colision:
            cuentaVidas -= 1
            jugador.ultima_colision = momento_colision
            if cuentaVidas == 0:
                spritesVidas.empty()
                jugador.disparar = False
                # jugador.update = False
                mensajePerdida = Perder()
                spritesPerder.add(mensajePerdida)
                spritesPeeps.empty()
                spritesDisparosPeep.empty()
                jugador.image.fill(NEGRO)

    spritesPeeps.update()
    spritesDisparosPeep.update()

    sprites.draw(ventana)
    spritesE.draw(ventana)
    balas.draw(ventana)
    spritesVidas.draw(ventana)
    spritesPerder.draw(ventana)
    spritesLlaves.draw(ventana)
    spritesFlechas.draw(ventana)
    spritesPeeps.draw(ventana)
    spritesDisparosPeep.draw(ventana)

    pygame.display.flip()

pygame.quit()
