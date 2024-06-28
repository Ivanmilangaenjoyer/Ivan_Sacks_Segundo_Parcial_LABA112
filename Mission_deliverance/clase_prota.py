from typing import Any
import pygame, os
from pygame.sprite import *
from plataforma import *
directorio = os.getcwd()   

class Jugador(pygame.sprite.Sprite):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad):
        super().__init__()
        self.image = pygame.image.load(r"assets\imagenes\prota\Quieto\Idle_0.png")
        self.rect = self.image.get_rect(centerx = pos_x, centery = pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.diccionario_rectangulos = {}
        self.diccionario_mascaras = {}
        self.velocidad = velocidad
        self.cooldown_animacion = 100
        self.cooldown_animacion_salto = 50
        self.ultima_animacion = 0
        self.cooldown_salto = 100
        self.cooldown_animacion_ataque = 50
        self.ultimo_salto = 0
        self.indice = 0
        self.indice_salto = 0
        self.tiempo_actual = 0
        self.indice_ataque = 0
        self.velocidad = 3
        self.salto_actual = 0
        self.salto_bajando = False
        self.salto_subiendo = False
        self.colision_piso = False
        self.colision_dercha = False
        self.colision_izquierda = False
        self.colision_arriba = False
        self.cargar_partes_rectangulos()


    def cargar_partes_rectangulos(self):
        self.diccionario_rectangulos["main"] = self.rect

        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left + 45, self.rect.top +5, self.rect.width -100 , 13)

        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right - 62, self.rect.top, 13, self.rect.height -5)

        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left + 43, self.rect.top, 13, self.rect.height -5)

        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left + 45, self.rect.bottom - 10, self.rect.width -100, 15)

    def cargar_sprites(self, lista_sprites, que_hace):
        if que_hace[1] == "salto":
            if self.indice_salto < len(lista_sprites["salto_derecha"]) -1 and que_hace[0] != "izquierda":
                if self.tiempo_actual - self.ultima_animacion > self.cooldown_animacion_salto:
                    if self.indice_salto < 5:
                        self.indice_salto += 1
                    self.ultima_animacion = self.tiempo_actual
                    self.image = lista_sprites["salto_derecha"][self.indice_salto]
                    self.mask = pygame.mask.from_surface(self.image)
                    
            if self.indice_salto < len(lista_sprites["salto_izquierda"]) -1 and que_hace[0] == "izquierda":
                if self.tiempo_actual - self.ultima_animacion > self.cooldown_animacion_salto:
                    if self.indice_salto < 5:
                        self.indice_salto += 1
                    self.ultima_animacion = self.tiempo_actual
                    self.image = lista_sprites["salto_izquierda"][self.indice_salto]
                    self.mask = pygame.mask.from_surface(self.image)
        else:
            if que_hace[0] == "ataque_derecha":
                if self.indice < len(lista_sprites["ataque_derecha"]) -1:
                    if self.tiempo_actual - self.ultima_animacion > self.cooldown_animacion_ataque:
                        if self.indice_ataque < 6:
                            self.indice_ataque += 1

                        self.ultima_animacion = self.tiempo_actual
                        self.image = lista_sprites["ataque_derecha"][self.indice_ataque]
                        self.mask = pygame.mask.from_surface(self.image)
            else:
                if self.indice < len(lista_sprites[que_hace[0]]) -1:
                    if self.tiempo_actual - self.ultima_animacion > self.cooldown_animacion:
                        self.indice += 1
                        self.ultima_animacion = self.tiempo_actual
                        self.image = lista_sprites[que_hace[0]][self.indice]
                        self.mask = pygame.mask.from_surface(self.image)
                else:
                    self.indice = 0


    def movimiento(self, que_hace):
            if que_hace[0] != "ataque_derecha":
                self.indice_ataque = 0

                if not self.colision_piso:
                    if self.salto_bajando == False and self.salto_subiendo == False:
                        self.rect.y += self.velocidad

                if not self.colision_dercha and not self.colision_izquierda and not self.colision_arriba:
                    if que_hace[1] == "salto":
                            if self.tiempo_actual - self.ultimo_salto > self.cooldown_salto:
                                self.ultimo_salto = self.tiempo_actual

                                if self.salto_bajando == False:
                                    self.salto_subiendo = True

                if not self.colision_dercha:
                    if que_hace[0] == "derecha":
                        self.velocidad = 3
                        self.rect.x += self.velocidad

                if not self.colision_izquierda:
                    if que_hace[0] == "izquierda":
                        self.velocidad = -3
                        self.rect.x += self.velocidad


            self.gravedad(que_hace)


    def gravedad(self, que_hace):
        if self.salto_actual < 30 and self.salto_subiendo == True and not self.colision_arriba:
            self.salto_actual += 1
            self.rect.y -= 3
        elif not self.colision_piso:
            self.salto_subiendo = False
            self.salto_bajando = True
            self.rect.y += 3
            self.salto_actual -= 1
        else:
            self.salto_subiendo = False
            self.salto_bajando = False
            que_hace[1] = "nada"
            self.indice_salto = 0
            self.salto_actual = 0

    def colisiones(self, grupo_objetos, lados_colisionar):
        for objeto in grupo_objetos:
            if self.diccionario_rectangulos[lados_colisionar[0]].colliderect(objeto.diccionario_rectangulos[lados_colisionar[1]]):
                    offset = (objeto.rect.x - self.rect.x, objeto.rect.y - self.rect.y)
                    if self.mask.overlap(objeto.mask, offset):
                        if lados_colisionar[0] == "bottom":
                            self.colision_piso = True
                            self.salto_bajando = False
                        elif lados_colisionar[0] == "top":
                            self.colision_arriba = True

                        elif lados_colisionar[0] == "right":
                            if self.salto_actual != 0:
                                self.salto_subiendo = False
                                self.salto_bajando = True
                            self.colision_dercha = True
                        elif lados_colisionar[0] == "left":
                            if self.salto_actual != 0:
                                self.salto_subiendo = False
                                self.salto_bajando = True
                            self.colision_izquierda = True




    def update(self, lista_sprites, pantalla, que_hace, grupo_plataformas):

        self.colision_piso = False
        self.colision_dercha = False
        self.colision_izquierda = False
        self.colision_arriba = False


        self.colisiones(grupo_plataformas, (("bottom", "top")))
        self.colisiones(grupo_plataformas, (("top", "bottom")))
        self.colisiones(grupo_plataformas, (("right", "left")))
        self.colisiones(grupo_plataformas, (("left", "right")))

        self.cargar_partes_rectangulos()
        self.movimiento(que_hace) 
        self.cargar_sprites(lista_sprites, que_hace)
        self.tiempo_actual = pygame.time.get_ticks()

        print(self.indice_ataque, que_hace[0])


        # pygame.draw.rect(pantalla, (0,255,255), self.diccionario_rectangulos["right"])
        # pygame.draw.rect(pantalla, (255,255,255), self.diccionario_rectangulos["left"])
        # pygame.draw.rect(pantalla, (0,255,255), self.diccionario_rectangulos["bottom"])
        # pygame.draw.rect(pantalla, (0,0,255), self.diccionario_rectangulos["top"])







