import pygame, time, sys
from config import *
from modulo_funciones import *
import random

pygame.init()
pygame.font.init()


ventana = pygame.display.set_mode((width, height))
pygame.display.set_caption("Seraph´s wrath")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        ventana.blit(fondo,(0,0))

    pygame.display.flip()