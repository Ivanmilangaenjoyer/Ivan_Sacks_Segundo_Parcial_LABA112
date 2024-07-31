from config import *
from typing import Any
import pygame, os
from pygame.sprite import *
from modulo_funciones import *
import math, random
from pygame import mixer
from armas import *

directorio = os.getcwd()   

class Jugador(pygame.sprite.Sprite):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad):
        super().__init__()
        self.image = pygame.image.load(dir_imagen)
        self.rect = self.image.get_rect(centerx = pos_x, centery = pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.diccionario_rectangulos = {}
        self.diccionario_mascaras = {}
        self.velocidad_x = velocidad
        self.velocidad_y = velocidad
        self.cooldown_animacion = 100
        self.cooldown_animacion_salto = 50
        self.ultima_animacion = 0
        self.indice = 0
        self.tiempo_actual = 0
        self.indice_ataque = 0
        self.salto_actual = 0
        self.colision_piso = False
        self.colision_dercha = False
        self.colision_izquierda = False
        self.colision_arriba = False
        self.cargar_partes_rectangulos()
        self.vidas = 3
        self.bandera_suicide_king = True

    def cargar_partes_rectangulos(self):
        self.diccionario_rectangulos["main"] = self.rect

        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left + 50, self.rect.top +5, self.rect.width - 110 , 13)

        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right - 65, self.rect.top + 15, 10, self.rect.height -20)

        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left + 50, self.rect.top + 13, 15, self.rect.height - 28)

        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left + 55, self.rect.bottom - 10, self.rect.width -115, 13)

    def cargar_sprites(self, lista_sprites, que_hace):
        if self.indice < len(lista_sprites[que_hace[0]]) -1:
            if self.tiempo_actual - self.ultima_animacion > self.cooldown_animacion:
                self.indice += 1
                self.ultima_animacion = self.tiempo_actual
                self.image = lista_sprites[que_hace[0]][self.indice]
                self.mask = pygame.mask.from_surface(self.image)
        else:
            self.indice = 0


    def movimiento(self, movimiento_prota):
        if not self.colision_arriba:
            if movimiento_prota["arriba"]:
                self.velocidad_y = -4
                self.rect.y += self.velocidad_y

        if not self.colision_dercha:
            if movimiento_prota["derecha"]:
                self.velocidad_x = 4
                self.rect.x += self.velocidad_x

        if not self.colision_izquierda:
            if movimiento_prota["izquierda"]:
                self.velocidad_x = -4
                self.rect.x += self.velocidad_x

        if not self.colision_piso:
            if movimiento_prota["abajo"]:
                self.velocidad_y = 4
                self.rect.y += self.velocidad_y


    def colisiones(self, grupo_objetos, lados_colisionar):
        for objeto in grupo_objetos:
            if self.diccionario_rectangulos[lados_colisionar[0]].colliderect(objeto.diccionario_rectangulos[lados_colisionar[1]]):
                    offset = (objeto.rect.x - self.rect.x, objeto.rect.y - self.rect.y)
                    if self.mask.overlap(objeto.mask, offset):
                        if lados_colisionar[0] == "bottom":
                            self.colision_piso = True
                        elif lados_colisionar[0] == "top":
                            self.colision_arriba = True
                        elif lados_colisionar[0] == "right":
                            self.colision_dercha = True
                        elif lados_colisionar[0] == "left":
                            self.colision_izquierda = True

    def update(self, lista_sprites, pantalla, que_hace, lista_colisiones_impasables, movimiento_prota, dicc_cartas):
        self.colision_piso = False
        self.colision_dercha = False
        self.colision_izquierda = False
        self.colision_arriba = False

        if dicc_cartas["suicide_king"] and self.bandera_suicide_king:
            self.bandera_suicide_king = False
            self.vidas = 1
        
        for grupo in lista_colisiones_impasables:
            self.colisiones(grupo, (("bottom", "top")))
            self.colisiones(grupo, (("top", "bottom")))
            self.colisiones(grupo, (("right", "left")))
            self.colisiones(grupo, (("left", "right")))

        self.cargar_partes_rectangulos()
        self.movimiento(movimiento_prota) 
        self.cargar_sprites(lista_sprites, que_hace)
        self.tiempo_actual = pygame.time.get_ticks()
        


class Vidas(Jugador):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad):
        super().__init__(dir_imagen, medidas, pos_x, pos_y, velocidad)
        self.vidas = 3

    def update(self, grupo_vidas, jugador, dicc_cartas):
        v = 0
        for vida in grupo_vidas:
            v += 1
        self.vidas = v

        if jugador.vidas < self.vidas and jugador.vidas > 0:
            ultimo_sprite = grupo_vidas.sprites()[-1] 
            grupo_vidas.remove(ultimo_sprite)  


class Enemigo(Jugador):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad):
        super().__init__(dir_imagen, medidas, pos_x, pos_y, velocidad = 0)
        self.cooldown_animacion = 150
        self.tiempo_actual = (pygame.time.get_ticks())
        self.xp = 30
        self.crawling_peg = 0.8
        self.colision = True
        self.devaluacion_nivelar = 0
        self.lista_colisiones = ["top", "right", "left", "bottom"]
        self.velocidad_x = 2
        self.velocidad_y = 2
        self.vidas = 2
        self.daño = 1
        self.cooldown_ataque = 1000
        self.ultimo_ataque = 0
        self.bandera_cannon = True
        self.bandera_midas = True
        self.bandera_steam = True

    def cargar_sprites(self, diccionario_sprites, que_hace):
        if self.indice < len(diccionario_sprites[que_hace]) -1:
            if self.tiempo_actual - self.ultima_animacion > self.cooldown_animacion:
                self.indice += 1
                self.ultima_animacion = self.tiempo_actual
                self.image = diccionario_sprites[que_hace][self.indice]
                self.mask = pygame.mask.from_surface(self.image)
        else:
            self.indice = 0

    def inflacion_xp(self, nivel_actual):
        if nivel_actual > self.devaluacion_nivelar and nivel_actual <= 10:
            self.xp *= self.crawling_peg
            self.devaluacion_nivelar += 1
            self.bandera_steam = True

    def movimiento(self, jugador):
        if jugador.rect.centerx < self.rect.centerx and self.colision_izquierda == False:
            self.velocidad_x = 2
            self.rect.x -= self.velocidad_x
        if jugador.rect.centerx > self.rect.centerx and self.colision_derecha == False:
            self.velocidad_x = 2
            self.rect.x += self.velocidad_x

        if jugador.rect.centery < self.rect.centery and self.colision_arriba == False:
            self.velocidad_y = 2
            self.rect.y -= self.velocidad_y
        if jugador.rect.centery > self.rect.centery and self.colision_piso == False:
            self.velocidad_y = 2
            self.rect.y += self.velocidad_y


    def soltar_xp(self, grupo_xp, subir_nivel):
        ultimo_xp = grupo_xp.sprites()[-1]
        ultimo_xp.ganar_xp(grupo_xp, self.xp, subir_nivel)
    
    def cargar_partes_rectangulos(self):
        self.diccionario_rectangulos["main"] = self.rect

        self.diccionario_rectangulos["top"] = pygame.Rect(self.rect.left + 45, self.rect.top + 12, self.rect.width - 100, 10)

        self.diccionario_rectangulos["right"] = pygame.Rect(self.rect.right - 52, self.rect.top + 10, 10, self.rect.height - 10)

        self.diccionario_rectangulos["left"] = pygame.Rect(self.rect.left + 30, self.rect.top + 10, 12, self.rect.height - 10)

        self.diccionario_rectangulos["bottom"] = pygame.Rect(self.rect.left + 43, self.rect.bottom - 10, self.rect.width - 98, 10)

    def colisiones_jugador(self,  jugador, lados_colisionar, dicc_cartas):
        if self.diccionario_rectangulos[lados_colisionar[0]].colliderect(jugador.diccionario_rectangulos[lados_colisionar[1]]):
            offset = (jugador.rect.x - self.rect.x, jugador.rect.y - self.rect.y)
            if self.mask.overlap(jugador.mask, offset):
                if lados_colisionar[0] == "bottom" or lados_colisionar[0] == "top" or lados_colisionar[0] == "right" or lados_colisionar[0] == "left":
                    if self.tiempo_actual - self.ultimo_ataque > self.cooldown_ataque:
                        self.ultimo_ataque = self.tiempo_actual
                        if dicc_cartas["penny"]:
                            self.num_random = random.randint(1, 2)
                            if self.num_random == 1:
                                jugador.vidas -= self.daño * 2
                        else:
                            jugador.vidas -= self.daño

    def colisiones_enemigo(self, grupo_objetos, lados_colisionar):
        for objeto in grupo_objetos:
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

    
    def colisiones_proyectiles(self, grupo_proyectiles, lados_colisionar):
        for proyectil in grupo_proyectiles:
            if self.diccionario_rectangulos[lados_colisionar[0]].colliderect(proyectil.diccionario_rectangulos[lados_colisionar[1]]):
                offset = (proyectil.rect.x - self.rect.x, proyectil.rect.y - self.rect.y)
                if self.mask.overlap(proyectil.mask, offset):
                    if lados_colisionar[0] == "bottom" or lados_colisionar[0] == "top" or lados_colisionar[0] == "right" or lados_colisionar[0] == "left":
                        if proyectil.anim_muerte != True:
                            self.vidas -= proyectil.daño
                            proyectil.anim_muerte = True
                            if self.vidas <= 0:
                                self.soltar_xp(grupo_xp, subir_nivel)
                                self.kill()
                                self.colision = False

    def update(self, diccionarios_slimes, pantalla, grupo_proyectiles, grupo_proyectiles_tp, grupo_xp, subir_nivel, 
            jugador, grupo_enemigos, dicc_cartas, offset_x, offset_y, BalaSlimeVerde, grupo_proyectiles_enemigos):
        self.tiempo_actual = pygame.time.get_ticks() 
        self.colision_piso = False
        self.colision_arriba = False
        self.colision_derecha = False
        self.colision_izquierda = False

        self.cargar_partes_rectangulos()
        self.cargar_sprites(diccionarios_slimes, "azul")
        self.movimiento(jugador) 
        self.inflacion_xp(subir_nivel[1])

        self.colisiones_enemigo(grupo_enemigos, (("bottom", "top")))
        self.colisiones_enemigo(grupo_enemigos, (("top", "bottom")))
        self.colisiones_enemigo(grupo_enemigos, (("right", "left")))
        self.colisiones_enemigo(grupo_enemigos, (("left", "right")))

        if dicc_cartas["xray"] and self.vidas > 0:
            dire = r"Seraph´s_wrath\assets\GUI\Inventory and Stats\vida"
            vida_image = pygame.transform.scale(pygame.image.load(f"{dire}_{self.vidas}.png"), ((50, 50)))
            vida_rect = self.image.get_rect(centerx = self.rect.centerx + 30, centery = self.rect.centery - 45)
            pantalla.blit(vida_image, (vida_rect.x - offset_x, vida_rect.y - offset_y))

        if dicc_cartas["glass_cannon"] and self.bandera_cannon:
            self.daño = self.daño * 2
            self.bandera_cannon = False

        if dicc_cartas["midas"] and self.bandera_midas:
            self.crawling_peg += 0.1
            self.bandera_midas = False

        if dicc_cartas["steam_final"] and self.bandera_steam:
            self.bandera_steam = False
            self.xp = self.xp * 1.2

        for lado_0 in self.lista_colisiones:
            for lado_1 in self.lista_colisiones:
                if self.colision:
                    self.colisiones_proyectiles(grupo_proyectiles, ((lado_0, lado_1)))

        self.colision = True

        for lado_0 in self.lista_colisiones:
            for lado_1 in self.lista_colisiones:
                if self.colision:
                    self.colisiones_proyectiles(grupo_proyectiles_tp, ((lado_0, lado_1)))

        self.colision = True

        for lado_0 in self.lista_colisiones:
            for lado_1 in self.lista_colisiones:
                if self.colision:
                    self.colisiones_jugador(jugador, ((lado_0, lado_1)), dicc_cartas)

        self.colision = True

class SlimeRojo(Enemigo):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad):
        super().__init__(dir_imagen, medidas, pos_x, pos_y, velocidad = 0)
        self.vidas = 2
        self.velocidad_x = 3
        self.velocidad_y = 3

    def movimiento(self, jugador):
        if jugador.rect.centerx < self.rect.centerx and self.colision_izquierda == False:
            self.velocidad_x = 3
            self.rect.x -= self.velocidad_x
        if jugador.rect.centerx > self.rect.centerx and self.colision_derecha == False:
            self.velocidad_x = 3
            self.rect.x += self.velocidad_x

        if jugador.rect.centery < self.rect.centery and self.colision_arriba == False:
            self.velocidad_y = 3
            self.rect.y -= self.velocidad_y
        if jugador.rect.centery > self.rect.centery and self.colision_piso == False:
            self.velocidad_y = 3
            self.rect.y += self.velocidad_y

    def update(self, diccionarios_slimes, pantalla, grupo_proyectiles, grupo_proyectiles_tp, grupo_xp, subir_nivel, 
        jugador, grupo_enemigos, dicc_cartas, offset_x, offset_y, BalaSlimeVerde, grupo_proyectiles_enemigos):
            self.velocidad_y = 0
            self.velocidad_x = 0

            self.tiempo_actual = pygame.time.get_ticks() 

            self.colision_piso = False
            self.colision_arriba = False
            self.colision_derecha = False
            self.colision_izquierda = False

            self.cargar_partes_rectangulos()
            self.cargar_sprites(diccionarios_slimes, "rojo")
            self.movimiento(jugador) 

            self.inflacion_xp(subir_nivel[1])
            
            self.colisiones_enemigo(grupo_enemigos, (("bottom", "top")))
            self.colisiones_enemigo(grupo_enemigos, (("top", "bottom")))
            self.colisiones_enemigo(grupo_enemigos, (("right", "left")))
            self.colisiones_enemigo(grupo_enemigos, (("left", "right")))

            if dicc_cartas["xray"] and self.vidas > 0:
                dire = r"Seraph´s_wrath\assets\GUI\Inventory and Stats\vida"
                vida_image = pygame.transform.scale(pygame.image.load(f"{dire}_{self.vidas}.png"), ((50, 50)))
                vida_rect = self.image.get_rect(centerx = self.rect.centerx + 30, centery = self.rect.centery - 45)
                pantalla.blit(vida_image, (vida_rect.x - offset_x, vida_rect.y - offset_y))

            if dicc_cartas["glass_cannon"] and self.bandera_cannon:
                self.daño = self.daño * 2
                self.bandera_cannon = False

            if dicc_cartas["midas"] and self.bandera_midas:
                self.crawling_peg += 0.1
                self.bandera_midas = False

            if dicc_cartas["steam_final"] and self.bandera_steam:
                self.bandera_steam = False
                self.xp = self.xp * 1.2

            for lado_0 in self.lista_colisiones:
                for lado_1 in self.lista_colisiones:
                    if self.colision:
                        self.colisiones_proyectiles(grupo_proyectiles, ((lado_0, lado_1)))

            self.colision = True

            for lado_0 in self.lista_colisiones:
                for lado_1 in self.lista_colisiones:
                    if self.colision:
                        self.colisiones_proyectiles(grupo_proyectiles_tp, ((lado_0, lado_1)))

            self.colision = True

            for lado_0 in self.lista_colisiones:
                for lado_1 in self.lista_colisiones:
                    if self.colision:
                        self.colisiones_jugador(jugador, ((lado_0, lado_1)), dicc_cartas)

            self.colision = True


class SlimeVerde(Enemigo):
    def __init__(self, dir_imagen, medidas, pos_x, pos_y, velocidad):
        super().__init__(dir_imagen, medidas, pos_x, pos_y, velocidad = 0)
        self.velocidad_x = 1
        self.velocidad_y = 1
        self.cooldown_bala = random.randint(3000, 6000)
        self.ultima_bala = 0
        self.vidas = 1

    def crear_proyectil_slime(self, grupo_proyectiles_enemigos):
        if self.tiempo_actual - self.ultima_bala > self.cooldown_bala:
            self.ultima_bala = self.tiempo_actual
            if self.velocidad_x > 0 and self.velocidad_y == 0:
                velocidad_x = 5
                velocidad_y = 0
            elif self.velocidad_x > 0 and self.velocidad_y < 0:
                velocidad_x = 5
                velocidad_y = -5
            elif self.velocidad_x > 0 and self.velocidad_y > 0:
                velocidad_x = 5
                velocidad_y = 5
            elif self.velocidad_x == 0 and self.velocidad_y > 0:
                velocidad_y = 5
                velocidad_x = 0
            elif self.velocidad_x == 0 and self.velocidad_y < 0:
                velocidad_y = -5
                velocidad_x = 0
            elif self.velocidad_x < 0 and self.velocidad_y == 0:
                velocidad_x = -5
                velocidad_y = 0
            elif self.velocidad_x < 0 and self.velocidad_y < 0:
                velocidad_x = -5
                velocidad_y = -5
            elif self.velocidad_x < 0 and self.velocidad_y > 0:
                velocidad_x = -5
                velocidad_y = 5
            else:
                velocidad_x = 5
                velocidad_y = 0

            bala_slime = BalaSlimeVerde(r"Seraph´s_wrath\assets\armas\disparo_slime.png", (20, 20), self.rect.centerx, 
                                        self.rect.centery, velocidad_x, velocidad_y)
            
            grupo_proyectiles_enemigos.add(bala_slime)

    def movimiento(self, jugador):
        if jugador.rect.centerx < self.rect.centerx and self.colision_izquierda == False:
            self.velocidad_x = -1
            self.rect.x += self.velocidad_x
        if jugador.rect.centerx > self.rect.centerx and self.colision_derecha == False:
            self.velocidad_x = 1
            self.rect.x += self.velocidad_x

        if jugador.rect.centery < self.rect.centery and self.colision_arriba == False:
            self.velocidad_y = -1
            self.rect.y += self.velocidad_y
        if jugador.rect.centery > self.rect.centery and self.colision_piso == False:
            self.velocidad_y = 1
            self.rect.y += self.velocidad_y

    def update(self, diccionarios_slimes, pantalla, grupo_proyectiles, grupo_proyectiles_tp, grupo_xp, subir_nivel, 
        jugador, grupo_enemigos, dicc_cartas, offset_x, offset_y, BalaSlimeVerde, grupo_proyectiles_enemigos):

        self.velocidad_y = 0
        self.velocidad_x = 0
        self.tiempo_actual = pygame.time.get_ticks() 
        self.colision_piso = False
        self.colision_arriba = False
        self.colision_derecha = False
        self.colision_izquierda = False

        self.cargar_partes_rectangulos()
        self.cargar_sprites(diccionarios_slimes, "verde")
        self.movimiento(jugador) 

        self.crear_proyectil_slime(grupo_proyectiles_enemigos)

        self.inflacion_xp(subir_nivel[1])
        
        self.colisiones_enemigo(grupo_enemigos, (("bottom", "top")))
        self.colisiones_enemigo(grupo_enemigos, (("top", "bottom")))
        self.colisiones_enemigo(grupo_enemigos, (("right", "left")))
        self.colisiones_enemigo(grupo_enemigos, (("left", "right")))

        if dicc_cartas["xray"] and self.vidas > 0:
            dire = r"Seraph´s_wrath\assets\GUI\Inventory and Stats\vida"
            vida_image = pygame.transform.scale(pygame.image.load(f"{dire}_{self.vidas}.png"), ((50, 50)))
            vida_rect = self.image.get_rect(centerx = self.rect.centerx + 30, centery = self.rect.centery - 45)
            pantalla.blit(vida_image, (vida_rect.x - offset_x, vida_rect.y - offset_y))

        if dicc_cartas["glass_cannon"] and self.bandera_cannon:
            self.daño = self.daño * 2
            self.bandera_cannon = False

        if dicc_cartas["midas"] and self.bandera_midas:
            self.crawling_peg += 0.1
            self.bandera_midas = False

        if dicc_cartas["steam_final"] and self.bandera_steam:
            self.bandera_steam = False
            self.xp = self.xp * 1.2

        for lado_0 in self.lista_colisiones:
            for lado_1 in self.lista_colisiones:
                if self.colision:
                    self.colisiones_proyectiles(grupo_proyectiles, ((lado_0, lado_1)))

        self.colision = True

        for lado_0 in self.lista_colisiones:
            for lado_1 in self.lista_colisiones:
                if self.colision:
                    self.colisiones_proyectiles(grupo_proyectiles_tp, ((lado_0, lado_1)))

        self.colision = True

        for lado_0 in self.lista_colisiones:
            for lado_1 in self.lista_colisiones:
                if self.colision:
                    self.colisiones_jugador(jugador, ((lado_0, lado_1)), dicc_cartas)

        self.colision = True
