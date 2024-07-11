from typing import Any
import pygame, os
from pygame.sprite import *
from config import *
from modulo_funciones import *
from jugador import *
import random, math
from pygame import mixer

directorio = os.getcwd()   

class Objetos(pygame.sprite.Sprite):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(dir_imagen), ((medidas)))
        self.rect = self.image.get_rect(centerx = pos_x, centery = pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.diccionario_rectangulos = {}
        self.velocidad = velocidad
        self.cooldown_animacion = 100
        self.ultima_animacion = 0
        self.velocidad = 3
        self.colision_piso = False
        self.colision_dercha = False
        self.colision_izquierda = False
        self.colision_arriba = False

    def cargar_partes_rectangulos_paredes(self):
        self.diccionario_rectangulos["main"] = self.rect

        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left, self.rect.top, self.rect.width , 10)

        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right - 21, self.rect.top, 20, self.rect.height)

        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left, self.rect.top, 20, self.rect.height)

        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left, self.rect.bottom - 15, self.rect.width, 15)
    

    def update(self, pantalla, jugador, grupo_vidas):
        self.cargar_partes_rectangulos_paredes()

class OrbeVida(Objetos):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad):
        super().__init__(dir_imagen, medidas, pos_x, pos_y, velocidad)

    def colisiones(self, jugador, lados_colisionar, grupo_vidas, dicc_cartas):
        if self.diccionario_rectangulos[lados_colisionar[0]].colliderect(jugador.diccionario_rectangulos[lados_colisionar[1]]):
            offset = (jugador.rect.x - self.rect.x, jugador.rect.y - self.rect.y)
            if self.mask.overlap(jugador.mask, offset):
                if lados_colisionar[0] == "bottom" or lados_colisionar[0] == "top" or lados_colisionar[0] == "right" or lados_colisionar[0] == "left":
                    if dicc_cartas["suicide_king"] == False:
                        jugador.vidas += 1
                        ultima_vida = grupo_vidas.sprites()[-1]
                        cargar_linea_objetos(Vidas, r"Seraph´s_wrath\assets\items\muertos\Transperent\Icon1.png",ultima_vida.rect.centerx + 50, ultima_vida.rect.centery, 32, 32, 1, grupo_vidas, {"x": 0, "y": 0})
                    self.kill()

    def update(self, pantalla, jugador, grupo_vidas, dicc_cartas):
        self.cargar_partes_rectangulos_paredes()
        self.colision_piso = False
        self.colision_dercha = False
        self.colision_izquierda = False
        self.colision_arriba = False

        self.colisiones(jugador, (("bottom", "top")), grupo_vidas, dicc_cartas)
        self.colisiones(jugador, (("top", "bottom")), grupo_vidas, dicc_cartas)
        self.colisiones(jugador, (("right", "left")), grupo_vidas, dicc_cartas)
        self.colisiones(jugador, (("left", "right")), grupo_vidas, dicc_cartas)

class Arbol(Objetos):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad):
        super().__init__(dir_imagen, medidas, pos_x, pos_y, velocidad)
        self.colision_piso = False
        self.colision_dercha = False
        self.colision_izquierda = False
        self.colision_arriba = False
        self.vida = 1
        self.suerte = 4
        self.bandera_suerte = True

    def soltar_objeto(self, grupo_coleccionables):
        numero_aleatorio = random.randint(1, self.suerte)
        if numero_aleatorio == 1:
            cargar_linea_objetos(OrbeVida, r"Seraph´s_wrath\assets\items\Bonus\Bonus_2_3.png",self.rect.centerx, self.rect.centery, 30, 30, 1, grupo_coleccionables, {"x": 0, "y": 0})
        
    def colisiones(self, grupo_objetos, lados_colisionar, grupo_coleccionables):
        for objeto in grupo_objetos:
            if self.diccionario_rectangulos[lados_colisionar[0]].colliderect(objeto.diccionario_rectangulos[lados_colisionar[1]]):
                    offset = (objeto.rect.x - self.rect.x, objeto.rect.y - self.rect.y)
                    if self.mask.overlap(objeto.mask, offset):
                        if lados_colisionar[0] == "bottom" or lados_colisionar[0] == "top" or lados_colisionar[0] == "right" or lados_colisionar[0] == "left":
                            if objeto.anim_muerte != True:
                                self.vida -= 1
                                objeto.anim_muerte = True
                                if self.vida == 0:
                                    self.soltar_objeto(grupo_coleccionables)
                                    self.kill()


    def cargar_partes_rectangulos_arboles(self):
        self.diccionario_rectangulos["main"] = self.rect
        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left, self.rect.top, self.rect.width , 20)
        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right - 20, self.rect.top, 30, self.rect.height)
        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left, self.rect.top, 30, self.rect.height)
        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left, self.rect.bottom - 15, self.rect.width, 20)

    def update(self, pantalla, grupo, grupo_coleccionables, dicc_cartas):
        if dicc_cartas["lucky_foot"] and self.bandera_suerte:
            self.suerte -= 2
            self.bandera_suerte = False
        self.cargar_partes_rectangulos_arboles()
        self.colision_piso = False
        self.colision_dercha = False
        self.colision_izquierda = False
        self.colision_arriba = False

        self.colisiones(grupo, (("bottom", "top")), grupo_coleccionables)
        self.colisiones(grupo, (("top", "bottom")), grupo_coleccionables)
        self.colisiones(grupo, (("right", "left")), grupo_coleccionables)
        self.colisiones(grupo, (("left", "right")), grupo_coleccionables)

        # pygame.draw.rect(pantalla, (0,255,255), self.diccionario_rectangulos["main"])
        # pygame.draw.rect(pantalla, (255,255,255), self.diccionario_rectangulos["left"])
        # pygame.draw.rect(pantalla, (255,255,255), self.diccionario_rectangulos["right"])
        # pygame.draw.rect(pantalla, (0,255,255), self.diccionario_rectangulos["bottom"])
        # pygame.draw.rect(pantalla, (0,0,255), self.diccionario_rectangulos["top"])


class Xp(Objetos):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad = 0):
        super().__init__(dir_imagen, medidas, pos_x, pos_y, velocidad = 0)


    def ganar_xp(self, grupo_xp, cantidad_xp, subir_nivel):
        subir_nivel[0] += cantidad_xp
        xp_pixels = subir_nivel[0] * 9

        if subir_nivel[1] < 10:
            if subir_nivel[0] < 101:
                x = 0
                while x < xp_pixels:
                    nuevo_xp = Xp(r"Seraph´s_wrath\assets\GUI\Settings\Bar.png",(9, 10), x, 495)
                    grupo_xp.add(nuevo_xp)
                    x += 9
            else:
                print("Sube de nivel", subir_nivel[1])
                grupo_xp.empty()
                cargar_linea_objetos(Xp, r"Seraph´s_wrath\assets\GUI\Settings\Bar BG.png", 15, 495, 30, 10, 30, grupo_xp, {"x": 30, "y": 0})
                nuevo_xp = Xp(r"Seraph´s_wrath\assets\GUI\Settings\Bar.png",(9, 10), -5, 495)
                grupo_xp.add(nuevo_xp)
                subir_nivel[0] = 0
                subir_nivel[1] += 1
        else:
            cargar_linea_objetos(Xp, r"Seraph´s_wrath\assets\GUI\Settings\Bar.png", 0, 495, 30, 10, 30, grupo_xp, {"x": 32, "y": 0})




    def update(self, pantalla, jugador, grupo_vidas):
        pass


# 905