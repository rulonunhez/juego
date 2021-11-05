import pygame, sys
import random
from pygame.locals import *

ancho = 1000
alto = 600
fps = 30
negro = (0, 0, 0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/frente1.png').convert(), (45, 45))
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.center = (ancho // 2, alto // 2)

        # Velocidad predeterminada a 0 para que no se mueva si no pulsamos ninguna tecla
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):
        ventana.blit(fondo, (0, 0))
        self.velocidad_x = 0
        self.velocidad_y = 0

        # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()

        # Movimiento del personaje
        if teclas[pygame.K_a]:
            self.velocidad_x = -10
        if teclas[pygame.K_d]:
            self.velocidad_x = 10
        if teclas[pygame.K_s]:
            self.velocidad_y = 10
        if teclas[pygame.K_w]:
            self.velocidad_y = -10

        # Disparo
        if teclas[pygame.K_SPACE]:
            jugador.disparo()

        # Actualiza las posiciones
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #Limite de margenes
        if self.rect.left < 100:
            self.rect.left = 100
        if self.rect.right > 890:
            self.rect.right = 890
        if self.rect.top < 85:
            self.rect.top = 85
        if self.rect.bottom > 485:
            self.rect.bottom = 485

    def disparo(self):
        bala = Disparos(self.rect.centerx, self.rect.centery)
        balas.add(bala)

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/frente2.png').convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ancho - self.rect.width)
        self.rect.y = random.randrange(alto - self.rect.height)

        # Velocidad predeterminada a 0 para que no se mueva si no pulsamos ninguna tecla
        self.velocidad_x = 5
        self.velocidad_y = 5

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limite de margenes
        if self.rect.left <= 100:
            self.rect.left = 100
            self.velocidad_x += 5
        if self.rect.right >= 890:
            self.rect.right = 890
            self.velocidad_x -= 5
        if self.rect.top <= 85:
            self.rect.top = 85
            self.velocidad_y += 5
        if self.rect.bottom >= 485:
            self.rect.bottom = 485
            self.velocidad_y -= 5


class Disparos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/tears.png').convert(),(10,10))
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 100:
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