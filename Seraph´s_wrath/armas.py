from pygame import mixer
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


    def explosion_bala(self, explosion):
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
        if self.rect.centerx > 1540 or self.rect.centerx < 0:
            self.kill()
        if self.rect.centery > 1250 or self.rect.centery < 0:
            self.kill()

    def update(self, enemigo_cerca, dicc_cartas, grupo_enemigos, explosion, dicc_rect_img, dicc_sonidos):
        if dicc_cartas["glass_cannon"] and self.bandera_cannon:
            self.daño = self.daño * 2
            self.bandera_cannon = False

        if dicc_cartas["suicide_king"] and self.suicide_king:
            self.daño = self.daño * 2
            self.suicide_king = False

        self.cargar_partes_bala()       
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        self.tiempo_actual = pygame.time.get_ticks()

        if self.anim_muerte:
            self.explosion_bala(explosion)
        if self.muerte:
            dicc_sonidos["explosion"].play()
            self.kill()

class Bala_guiada(Bala):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad_x, velocidad_y):
        super().__init__(dir_imagen, medidas, pos_x, pos_y, velocidad_x, velocidad_y)

    def movimiento_guiado(self, enemigo):
        if enemigo.rect.centerx < self.rect.centerx:
            self.rect.centerx += (-5)
        if enemigo.rect.centerx > self.rect.centerx:
            self.rect.centerx += 5
        if enemigo.rect.centery < self.rect.centery:
            self.rect.centery += (-5)
        if enemigo.rect.centery > self.rect.centery:
            self.rect.centery += 5

    def update(self, enemigo_cerca, dicc_cartas, grupo_enemigos, explosion, dicc_rect_img, dicc_sonidos):
        if dicc_cartas["glass_cannon"] and self.bandera_cannon:
            self.daño = self.daño * 2
            self.bandera_cannon = False

        if dicc_cartas["suicide_king"] and self.suicide_king:
            self.daño = self.daño * 2
            self.suicide_king = False

        self.cargar_partes_bala_guiada()
        self.movimiento_guiado(enemigo_cerca)

        self.tiempo_actual = pygame.time.get_ticks()

        if self.anim_muerte:
            self.explosion_bala(explosion)
        if self.muerte:
            dicc_sonidos["explosion"].play()
            self.kill()

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


    def update(self, enemigo_cerca, dicc_cartas, grupo_enemigos, explosion, dicc_rect_img, dicc_sonidos):
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



class BalaSlimeVerde(Bala):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad_x, velocidad_y):
        super().__init__(dir_imagen, medidas, pos_x, pos_y, velocidad_x, velocidad_y)
        self.ultimo_daño = 0
        self.cooldown_daño = 600


    def cargar_partes_bala(self):
        self.diccionario_rectangulos["main"] = self.rect

        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left + 4, self.rect.top, self.rect.width - 5, 10)

        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right - 8, self.rect.top, 8, self.rect.height)

        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left, self.rect.top, 8, self.rect.height)

        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left + 5, self.rect.bottom - 10, self.rect.width - 5, 10)



    def colision_jugador(self, objeto, lados_colisionar):
            if self.diccionario_rectangulos[lados_colisionar[0]].colliderect(objeto.diccionario_rectangulos[lados_colisionar[1]]):
                offset = (objeto.rect.x - self.rect.x, objeto.rect.y - self.rect.y)
                if self.mask.overlap(objeto.mask, offset):
                    if lados_colisionar[0] == "bottom":
                        self.colision_piso = True
                    elif lados_colisionar[0] == "top":
                        self.colision_arriba = True
                    elif lados_colisionar[0] == "right":
                        self.colision_derecha = True
                    elif lados_colisionar[0] == "left":
                        self.colision_izquierda = True

                    objeto.vidas -= 1
                    self.ultimo_daño = self.tiempo_actual


    def update(self, pantalla, jugador):
        self.colision_piso = False
        self.colision_arriba = False
        self.colision_derecha = False
        self.colision_izquierda = False

        self.cargar_partes_bala()       

        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.tiempo_actual - self.ultimo_daño > self.cooldown_daño:            
            self.colision_jugador(jugador, (("bottom", "top")))
            self.colision_jugador(jugador, (("top", "bottom")))
            self.colision_jugador(jugador, (("right", "left")))
            self.colision_jugador(jugador, (("left", "right")))


        self.tiempo_actual = pygame.time.get_ticks()

        self.diccionario_rectangulos["top"]

        # pygame.draw.rect(pantalla, (0,255,255), self.diccionario_rectangulos["right"])
        # pygame.draw.rect(pantalla, (255,255,255), self.diccionario_rectangulos["left"])
        # pygame.draw.rect(pantalla, (0,255,255), self.diccionario_rectangulos["bottom"])
        # pygame.draw.rect(pantalla, (0,0,255), self.diccionario_rectangulos["top"])


