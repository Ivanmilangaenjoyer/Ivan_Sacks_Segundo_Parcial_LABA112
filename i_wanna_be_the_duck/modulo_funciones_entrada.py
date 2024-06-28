import pygame
from config import *


def entrada_teclas(pato, keys):
    """Recibe instrucciones del usuario para moverse en x e y.
    Luego modifica un diccionario para luego calcular estos movimientos.

    Args:
        pato (dict): Diccionario de un rectangulo
        keys (tuple): Una tupla con todas las teclas del teclado
    """
    if keys[pygame.K_w]:
        pato["arriba"] = True
    else:
        pato["arriba"] = False
    if keys[pygame.K_s]:
        pato["bajando"] = True
    else:
        pato["bajando"] = False
    if keys[pygame.K_a]:
        pato["izquierda"] = True
    else:
        pato["izquierda"] = False
    if keys[pygame.K_d]:
        pato["derecha"] = True
    else:
        pato["derecha"] = False

