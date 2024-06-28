from typing import Any
import pygame, os
from pygame.sprite import *


directorio = os.getcwd()   


class Plataforma(pygame.sprite.Sprite):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad, piso):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(dir_imagen), ((medidas)))
        self.rect = self.image.get_rect(centerx = pos_x, centery = pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.diccionario_rectangulos = {}
        self.velocidad = velocidad
        self.cooldown_animacion = 100
        self.ultima_animacion = 0
        self.velocidad = 3
        self.piso = piso


    def cargar_partes_rectangulos_plataformas(self):
        self.diccionario_rectangulos["main"] = self.rect

        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left, self.rect.top - 5, self.rect.width , 10)

        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right - 55, self.rect.top + 13, 50, self.rect.height -15)

        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left + 15, self.rect.top + 15, 50, self.rect.height - 15)

        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left + 30, self.rect.bottom -18, self.rect.width - 55, 15)

    # def cargar_partes_rectangulos_piso(self):
    #     self.diccionario_rectangulos["main"] = self.rect

    #     self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left, self.rect.top - 5, self.rect.width , 15)

    #     self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right -23, self.rect.top + 13, 15, self.rect.height -15)

    #     self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left + 15, self.rect.top + 15, 15, self.rect.height - 15)

    #     self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left + 30, self.rect.bottom -18, self.rect.width - 55, 15)

    def cargar_partes_rectangulos_piso(self):
        self.diccionario_rectangulos["main"] = self.rect

        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left, self.rect.top, self.rect.width , 15)

        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right, self.rect.top, 15, self.rect.height)

        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left, self.rect.top, 15, self.rect.height)

        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left, self.rect.bottom, self.rect.width, 15)

    def update(self, pantalla):
        if self.piso == "si":
            self.cargar_partes_rectangulos_piso()
        else:
            self.cargar_partes_rectangulos_plataformas()

        
        # pygame.draw.rect(pantalla, (0,255,255), self.diccionario_rectangulos["right"])
        # pygame.draw.rect(pantalla, (255,255,255), self.diccionario_rectangulos["left"])
        # pygame.draw.rect(pantalla, (0,0,0), self.diccionario_rectangulos["bottom"])

        # pygame.draw.rect(pantalla, (0,0,255), self.diccionario_rectangulos["top"])