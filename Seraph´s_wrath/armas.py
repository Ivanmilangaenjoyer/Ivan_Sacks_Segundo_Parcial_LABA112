
from config import *
import pygame
import sys, os
from modulo_funciones import *
from pygame.sprite import *
import random, math

# Clase Bala
class Bala(pygame.sprite.Sprite):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad_x, velocidad_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(dir_imagen), ((medidas)))
        self.rect = self.image.get_rect(centerx = pos_x, centery = pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.diccionario_rectangulos = {}
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        self.tiempo_actual = pygame.time.get_ticks()
        self.indice = 0
        self.ultima_animacion = 0
        self.cooldown_animacion = 1000
        self.anim_muerte = False
        self.muerte = False
        self.daño = 1
        self.bandera_cannon = True
        self.suicide_king = True

    def cargar_partes_bala(self):
        self.diccionario_rectangulos["main"] = self.rect

        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left + 8, self.rect.top + 6, self.rect.width - 10, 10)

        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right - 13, self.rect.top, 10, self.rect.height)

        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left, self.rect.top, 15, self.rect.height)

        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left + 5, self.rect.bottom - 15, self.rect.width - 10, 10)


    def cargar_partes_bala_guiada(self):
        self.diccionario_rectangulos["main"] = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height)

        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left + 7 , self.rect.top + 8, self.rect.width - 15, 5)

        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right - 12,  self.rect.top, 5, self.rect.height - 5)

        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left + 10, self.rect.top, 5, self.rect.height)

        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left + 10, self.rect.bottom - 10, self.rect.width - 15, 5)


    def explosion_bala(self):
        if self.indice < (len(explosion)-1):
            if self.tiempo_actual - self.ultima_animacion > self.cooldown_animacion:
                self.indice += 1
                self.rect.centery -= 5
                self.rect.centerx -= 5
                self.image = explosion[self.indice]
                self.mask = pygame.mask.from_surface(self.image)
        else:
            self.indice = 0
            self.muerte = True


    def limpiar_proyectiles(self):
        if self.rect.centerx > 2000 or self.rect.centerx < 0:
            self.kill()
        if self.rect.centery > 2000 or self.rect.centery < 0:
            self.kill()

    def movimiento_guiado(self, enemigo):
        if enemigo.rect.centerx < self.rect.centerx:
            self.rect.centerx += (-3)
        if enemigo.rect.centerx > self.rect.centerx:
            self.rect.centerx += 3
        if enemigo.rect.centery < self.rect.centery:
            self.rect.centery += (-3)
        if enemigo.rect.centery > self.rect.centery:
            self.rect.centery += 3


    def update(self, pantalla, jugador, grupo_proyectiles, que_hace, grupo_enemigos, dicc_cartas):
        if dicc_cartas["glass_cannon"] and self.bandera_cannon:
            self.daño = self.daño * 2
            self.bandera_cannon = False

        if dicc_cartas["suicide_king"] and self.suicide_king:
            self.daño = self.daño * 2
            self.suicide_king = False

        if dicc_cartas["telepatia"]:
            self.cargar_partes_bala_guiada()
        else:
            self.cargar_partes_bala()       

        if len(grupo_enemigos) != 0 and dicc_cartas["telepatia"]:
                ultimo_enemigo = grupo_enemigos.sprites()[0]
                self.movimiento_guiado(ultimo_enemigo)
        else:
            self.rect.x += self.velocidad_x
            self.rect.y += self.velocidad_y

        self.tiempo_actual = pygame.time.get_ticks()

        if self.anim_muerte:
            self.explosion_bala()
        if self.muerte:
            self.kill()

        

        # pygame.draw.rect(pantalla, (0,255,255), self.diccionario_rectangulos["main"])
        # pygame.draw.rect(pantalla, (255,255,255), self.diccionario_rectangulos["left"])
        # pygame.draw.rect(pantalla, (0,255,255), self.diccionario_rectangulos["bottom"])
        # pygame.draw.rect(pantalla, (0,0,255), self.diccionario_rectangulos["top"])
        # pygame.draw.rect(pantalla, (0,0,255), self.diccionario_rectangulos["right"])


class Cuchillo(pygame.sprite.Sprite):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad_x, velocidad_y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(dir_imagen), ((medidas)))
        self.rect = self.image.get_rect(centerx = pos_x, centery = pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.diccionario_rectangulos = {}
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        self.tiempo_actual = 0
        self.cargar_partes_cuchillo()
        self.anim_muerte = False
        self.gravedad = False   
        self.desplazamiento = True
        self.dir_x = random.randint(1, 2)
        self.contador = 0
        self.daño = 1
        self.bandera_cannon = True
        self.bandera_suicide_king = True
    def cargar_partes_cuchillo(self):
        self.diccionario_rectangulos["main"] = self.rect

        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left + 8, self.rect.top + 6, self.rect.width - 10, 10)

        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right - 37, self.rect.top, 12, self.rect.height - 40)

        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left, self.rect.top, 15, self.rect.height)

        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left + 5, self.rect.bottom - 15, self.rect.width - 10, 10)

    def limpiar_proyectiles(self):
        if self.rect.centerx > 2000 or self.rect.centerx < 0:
            self.kill()
        if self.rect.centery > 2000 or self.rect.centery < 0:
            self.kill()

    def movimiento(self):
        if self.contador > 15 and self.gravedad == False:
            self.gravedad = True
            self.velocidad_y = self.velocidad_y * -1
            self.dir_x = 0
        if self.dir_x == 1:
            self.rect.x += self.velocidad_x
        elif self.dir_x == 2:
            self.rect.x -= self.velocidad_x
        
        self.rect.y -= self.velocidad_y


    def update(self, pantalla, jugador, grupo_proyectiles, que_hace, grupo_enemigo, dicc_cartas):
        if dicc_cartas["glass_cannon"] and self.bandera_cannon:
            self.daño = self.daño * 2
            self.bandera_cannon = False

        if dicc_cartas["suicide_king"] and self.bandera_suicide_king:
            self.daño = self.daño * 2
            self.suicide_king = False

        if self.anim_muerte:
            self.kill()

        self.movimiento()
        
        self.contador += 1
        self.cargar_partes_cuchillo()







