import pygame, sys
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((1000, 600))

#Título
pygame.display.set_caption('The binding of Isaac')

#Icono y fondo
icono = pygame.image.load('img/icono.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('img/fondo.png')
ventana.blit(fondo, (0,0))

'''
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
'''

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()