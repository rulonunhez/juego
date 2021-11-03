import pygame, sys
import random
from pygame.locals import *

'''
# Personaje
quieto = pygame.image.load('img/frente1.png')

caminaDerecha = []

caminaIzquierda = []

caminaAbajo = [pygame.image.load('img/frente1.png'),
               pygame.image.load('img/frente2.png'),
               pygame.image.load('img/frente3.png'),
               pygame.image.load('img/frente4.png'),
               pygame.image.load('img/frente5.png'),
               pygame.image.load('img/frente6.png'),
               pygame.image.load('img/frente7.png'),
               pygame.image.load('img/frente8.png'),
               pygame.image.load('img/frente9.png'),
               pygame.image.load('img/frente10.png')]

disparo = []

x = 0
px = 500
py = 300
velocidad = 10

# Control de FPS
reloj = pygame.time.Clock()

# Variables dirección
izquierda = False
derecha = False
abajo = False
arriba = False

# Pasos
cuentaPasos = 0

# Movimiento
def recargaPantalla():
    ventana.blit(fondo, (0, 0))

    # Variables globales
    global cuentaPasos
    global x

    # Contador de pasos
    if cuentaPasos + 1 >= 10:
        cuentaPasos = 0

    # Movimiento a la izquierda
    if izquierda:
        ventana.blit(caminaAbajo[cuentaPasos], (int(px), int(py)))
        cuentaPasos += 1

    # Movimiento a la derecha
    elif derecha:
        ventana.blit(caminaAbajo[cuentaPasos], (int(px), int(py)))
        cuentaPasos += 1

    # Movimiento abajo
    elif abajo:
        ventana.blit(caminaAbajo[cuentaPasos], (int(px), int(py)))
        cuentaPasos += 1

    # Movimiento abajo
    elif arriba:
        ventana.blit(caminaAbajo[cuentaPasos], (int(px), int(py)))
        cuentaPasos += 1

    else:
        ventana.blit(quieto, (int(px), int(py)))

ejecuta = True

# Bucle de acciones y controles
while ejecuta:
    # FPS
    reloj.tick(15)

    # Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    # Opción tecla pulsada
    keys = pygame.key.get_pressed()

    # Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and px > 105:
        px -= velocidad
        izquierda = True
        derecha = False
        abajo = False
        arriba = False

    # Tecla D - Moviemiento a la derecha
    elif keys[pygame.K_d] and px < 845:
        px += velocidad
        izquierda = False
        derecha = True
        abajo = False
        arriba = False

    # Tecla W - Moviemiento hacia arriba
    elif keys[pygame.K_w] and py > 85:
        py -= velocidad
        abajo = False
        arriba = True
        derecha = False
        izquierda = False

    # Tecla S - Moviemiento hacia abajo
    elif keys[pygame.K_s] and py < 450:
        py += velocidad
        abajo = True
        arriba = False
        derecha = False
        izquierda = False

    # Personaje quieto
    else:
        izquierda = False
        derecha = False
        abajo = False
        arriba = False
        cuentaPasos = 0

    # Actualización de la ventana
    pygame.display.update()
    # Llamada a la función de actualización de la ventana
    recargaPantalla()

# Salida del juego
pygame.quit()


blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)

ventana.fill(blanco)

rectangulo = pygame.draw.rect(ventana, rojo, (100, 50, 100, 50))
pygame.draw.line(ventana, verde, (100, 104), (199, 104), 20)
pygame.draw.circle(ventana, negro, (122, 250), 20, 0)
pygame.draw.ellipse(ventana, azul, (275, 200, 50, 100), 10)
puntos = [(200, 100), (200, 200), (240, 300)]
pygame.draw.polygon(ventana, (120, 120, 255), puntos)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
'''

ancho = 1000
alto = 600
fps = 30
negro = (0, 0, 0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/frente1.png').convert()
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

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/frente2.png').convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ancho - self.rect.width)
        self.rect.y = random.randrange(alto - self.rect.height)

        # Velocidad predeterminada a 0 para que no se mueva si no pulsamos ninguna tecla
        self.velocidad_x = random.randrange(1, 10)
        self.velocidad_y = random.randrange(1, 10)

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limite de margenes
        if self.rect.left < 100:
            self.rect.left = 100
            self.velocidad_x += random.randrange(1, 10)
        if self.rect.right > 890:
            self.rect.right = 890
            self.velocidad_x -= random.randrange(1, 10)
        if self.rect.top < 85:
            self.rect.top = 85
            self.velocidad_y += random.randrange(1, 10)
        if self.rect.bottom > 485:
            self.rect.bottom = 485
            self.velocidad_y -= random.randrange(1, 10)

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

for i in range(random.randrange(3, 7)):
    enemigo = Enemigo()
    sprites.add(enemigo)


jugador = Jugador()
sprites.add(jugador)

#Bucle de juego
ejecutando = True
while ejecutando:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    sprites.update()
    sprites.draw(ventana)
    pygame.display.flip()

pygame.quit()