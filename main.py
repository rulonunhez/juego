from dis import dis

import pygame, sys
import random
from pygame.locals import *

ANCHO = 1000
ALTO = 600
FPS = 30
NEGRO = (0, 0, 0)
WHITE = (255, 255, 255)
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
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)

        self.cadencia = 250
        self.delay_colision = 500
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

        bala = Disparos(self.rect.centerx, self.rect.centery, direccion)
        balas.add(bala)

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/spider.jpg').convert(), (30, 30))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        posx = random.randint(0, 1)
        posy = random.randint(0, 1)
        if posx == 0:
            self.rect.x = random.randrange(150, 200)
        else:
            self.rect.x = random.randrange(750, 800)
        if posy == 0:
            self.rect.y = random.randrange(100, 150)
        else:
            self.rect.y = random.randrange(450, 500)

        self.velocidad_x = VELENEMIGO
        self.velocidad_y = VELENEMIGO

    def update(self):
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
    def __init__(self, x, y, direccion):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/tears.png').convert(), (15, 15))
        self.image.set_colorkey(NEGRO)
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

class Vida(pygame.sprite.Sprite):
    def __init__(self, x, y=None):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/vida.jpg').convert(), (40, 40))
        self.image.set_colorkey(WHITE)
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

# Inicialización
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
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
spritesVidas = pygame.sprite.Group()
spritesPerder = pygame.sprite.Group()
spritesLlaves = pygame.sprite.Group()
spritesFechas = pygame.sprite.Group()

for i in range(5):
    enemigo = Enemigo()
    spritesE.add(enemigo)

jugador = Jugador()
sprites.add(jugador)

# Bucle de juego
ejecutando = True

eliminados = 0
cuentaVidas = 2
i = 1

while ejecutando:
    clock.tick(FPS)

    while i <= 2:
        x = i*50
        vida = Vida(x, 40)
        spritesVidas.add(vida)
        i += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    sprites.update()
    spritesE.update()
    balas.update()

    colision = pygame.sprite.spritecollide(jugador, spritesE, False)
    if colision:
        momento_colision = pygame.time.get_ticks()
        spritesVidas.remove(vida)
        if momento_colision - jugador.ultima_colision > jugador.delay_colision:
            cuentaVidas -= 1
            jugador.ultima_colision = momento_colision
            if cuentaVidas == 0:
                spritesVidas.empty()
                jugador.disparar = False
                mensajePerdida = Perder()
                spritesPerder.add(mensajePerdida)
                spritesE.empty()
                balas.empty()
                jugador.image.fill(NEGRO)

    colision2 = pygame.sprite.groupcollide(spritesE, balas, True, True)
    if colision2:
        eliminados += 1

    if eliminados == 5:
        vida = Vida(ANCHO // 2 - 30, ALTO // 2)
        spritesVidas.add(vida)
        llave = Llave()
        spritesLlaves.add(llave)
        colisionVidaJugador = pygame.sprite.spritecollide(jugador, spritesVidas, True)
        if colisionVidaJugador:
            cuentaVidas += 1
            vida = Vida(cuentaVidas)
            spritesVidas.add(vida)
            eliminados = 0

    colisionLlaveJugador = pygame.sprite.spritecollide(jugador, spritesLlaves, True)
    if colisionLlaveJugador:
        spritesLlaves.empty()
        flecha = Flecha(145, 300, 270)
        flecha2 = Flecha(845, 295, 90)
        flecha3 = Flecha(500, 140, 180)
        spritesLlaves.add(flecha)
        spritesLlaves.add(flecha2)
        spritesLlaves.add(flecha3)

    # for i in range(vidas):

    # for enemigo in spritesE.sprites():
    #     colisiones.add(enemigo)
    #     # Colision entre el personaje y algún enemigo
    #     colision = pygame.sprite.spritecollide(jugador, colisiones, False)
    #     # Colision entre el enemigo y alguna bala
    #     colision2 = pygame.sprite.spritecollide(enemigo, balas, True)
    #     if colision:
    #         # Perder vidas y comprobar si le quedan vidas
    #         fondo = pygame.image.load('img/fondoPerder.png')
    #         spritesE.empty()
    #         balas.empty()
    #         jugador.image.fill(NEGRO)
    #
    #     else:
    #         colisiones.empty()
    #
    #     if colision2:
    #         # Eliminar al enemigo cuando colisiona con la bala
    #         enemigo.kill()

    # if cuentaVidas <= 0:
    #     fondo = pygame.image.load('img/fondoPerder.png')
    #     jugador.kill()
    #     for enemigo in spritesE.sprites():
    #         enemigo.kill()
    #     for bala in balas.sprites():
    #         bala.kill()
    #

    sprites.draw(ventana)
    spritesE.draw(ventana)
    balas.draw(ventana)
    spritesVidas.draw(ventana)
    spritesPerder.draw(ventana)
    spritesLlaves.draw(ventana)
    spritesFechas.draw(ventana)

    pygame.display.flip()

pygame.quit()
