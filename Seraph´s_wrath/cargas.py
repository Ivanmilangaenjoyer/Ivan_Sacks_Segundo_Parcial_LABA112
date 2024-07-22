import pygame
from config import *
from modulo_funciones import *

fondo = pygame.image.load(r"Seraph´s_wrath\assets\fondos\veerde.jpg")
icono = pygame.image.load(r'Seraph´s_wrath\assets\items\muertos\Transperent\Icon29.png')
bloque = pygame.image.load(r"Seraph´s_wrath\assets\fondos\veerde.jpg")

personaje_quieto = [pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Quieto\Idle_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Quieto\Idle_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Quieto\Idle_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Quieto\Idle_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Quieto\Idle_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Quieto\Idle_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Quieto\Idle_6.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Quieto\Idle_7.png"), ((130, 70))),
                    ]

personaje_derecha = [pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Derecha\derecha_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Derecha\derecha_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Derecha\derecha_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Derecha\derecha_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Derecha\derecha_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Derecha\derecha_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Derecha\derecha_6.png"), ((130, 70))),
                    ]

personaje_izquierda = [pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Izquierda\izquierda_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Izquierda\izquierda_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Izquierda\izquierda_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Izquierda\izquierda_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Izquierda\izquierda_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Izquierda\izquierda_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\prota\Izquierda\izquierda_6.png"), ((130, 70))),
                    ]

explosion = [pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_0.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_1.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_2.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_3.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_4.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_5.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_6.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_7.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_8.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_9.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_10.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\animaciones\Explosion_11.png"), ((96, 96))),
            ]

slime_derecha = [
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_0.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_1.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_2.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_3.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_4.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_5.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_6.png"), ((128, 40))),
            ]

diccionario_slime = {"derecha": slime_derecha}
lista_sprites = {"nada": personaje_quieto, "derecha": personaje_derecha, "izquierda": personaje_izquierda,
                "arriba": personaje_derecha, "abajo": personaje_derecha}


pygame.mixer.music.load(r"Seraph´s_wrath\assets\sonidos\vampire_ost.mp3")
pygame.mixer.music.set_volume(0.2)

explosion_sonido = pygame.mixer.Sound(r"Seraph´s_wrath\assets\sonidos\explosion.mp3")
cuchillo_sonido = pygame.mixer.Sound(r"Seraph´s_wrath\assets\sonidos\cuchillo.mp3")
muerte_sonido = pygame.mixer.Sound(r"Seraph´s_wrath\assets\sonidos\recibir_daño.mp3")
level_sonido = pygame.mixer.Sound(r"Seraph´s_wrath\assets\sonidos\victoria.mp3")

cuchillo_sonido.set_volume(0.1)
explosion_sonido.set_volume(0.1)
muerte_sonido.set_volume(0.1)



imagen_fama, rect_fama = crear_rectango_imagen(r"Seraph´s_wrath\assets\fondos\Salon_fama.jpg", anchura // 2, altura // 2, ((anchura, altura)))

imagen_muerte, rect_muerte = crear_rectango_imagen(r"Seraph´s_wrath\assets\fondos\muerte.png", anchura // 2, altura // 2, ((anchura, altura)))

imagen_reintentar, rect_reintentar = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\reintentar.png", anchura // 2, 200, ((300, 60)))
rect_reintentar = imagen_reintentar.get_rect(centerx = (anchura // 2), centery = (310))

imagen_atras, rect_atras = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\atras.png", 50, 50, ((100, 100)))

imagen_musica_on, rect_musica_on = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\musica_on.png", anchura // 2, 100, ((400, 100)))
imagen_musica_off, rect_musica_off = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\musica_off.png", anchura // 2, 100, ((400, 85)))


imagen_inmortalidad_on, rect_inmortalidad_on = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\inmortalidad_on.png", anchura // 2, 250, ((400, 100)))
imagen_inmortalidad_off, rect_inmortalidad_off = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\inmortalidad_off.png", anchura // 2, 250, ((400, 85)))

imagen_efectos_off, rect_efectos_off = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\efectos_off.png", anchura // 2, 400, ((400, 85)))
imagen_efectos_on, rect_efectos_on = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\efectos_on.png", anchura // 2, 400, ((400, 100)))

imagen_fondo_opciones, rect_fondo_opciones = crear_rectango_imagen(r"Seraph´s_wrath\assets\fondos\templo.jpg", anchura // 2, altura // 2, ((anchura, altura)))

imagen_mute = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\mute.png"), ((50, 50)))
rect_mute = imagen_mute.get_rect(centerx = (60), centery = (470))

abel_imagen = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\armas\Objeto_Abel.png"), ((30, 30)))

imagen_muerte_menu = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\menu.png"), ((300, 60)))
rect_muerte_menu = imagen_muerte_menu.get_rect(centerx = (anchura // 2), centery = (210))

imagen_pausa = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\GUI\Pause menu\pausa.png"), ((300, 300)))
rect_pausa = imagen_pausa.get_rect(centerx = (anchura // 2), centery = (altura // 2))

imagen_empezar = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\empezar.png"), ((300, 60)))
rect_empezar = imagen_empezar.get_rect(centerx = (anchura // 2), centery = (110))

imagen_opciones = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\opciones.png"), ((300, 60)))
rect_opciones = imagen_opciones.get_rect(centerx = (anchura // 2), centery = (210))

imagen_ranking = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\ranking.png"), ((300, 60)))
rect_ranking = imagen_ranking.get_rect(centerx = (anchura // 2), centery = (310))

imagen_salir = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\salir.png"), ((300, 60)))
rect_salir = imagen_salir.get_rect(centerx = (anchura // 2), centery = (410))

imagen_jungla = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\fondos\jungla.jpg"), ((900, 600)))
rect_jungla = imagen_jungla.get_rect(centerx = (anchura // 2), centery = (altura // 2))

imagen_menu = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\menu_interfaz.png"), ((600, 540)))
rect_menu = imagen_jungla.get_rect(centerx = (anchura // 2 + 155), centery = (altura // 2 + 30))


dicc_rect_img = {"jungla":[imagen_jungla, rect_jungla], "fama":[imagen_fama, rect_fama], "muerte":[imagen_muerte, rect_muerte],
                "reintentar":[imagen_reintentar, rect_reintentar], "atras":[imagen_atras, rect_atras], 
                "musica":{"on":[imagen_musica_on, rect_musica_on], "off":[imagen_musica_off, rect_musica_off]},
                "inmortalidad":{"on":[imagen_inmortalidad_on, rect_inmortalidad_on], "off":[imagen_inmortalidad_off, rect_inmortalidad_off]},
                "efectos":{"on": [imagen_efectos_on, rect_efectos_on], "off":[imagen_efectos_off, rect_efectos_off]},
                "fondo_opciones": [imagen_fondo_opciones, rect_fondo_opciones], "mute":[imagen_mute, rect_mute],
                "abel":[abel_imagen], "pausa": [imagen_pausa, rect_pausa], "empezar": [imagen_empezar, rect_empezar],
                "opciones":[imagen_opciones, rect_opciones], "ranking":[imagen_ranking, rect_ranking], "salir":[imagen_salir, rect_salir],
                "menu": [imagen_menu, rect_menu], "menu_muerte": [imagen_muerte_menu, rect_muerte_menu]}
dicc_sonidos = {"explosion": explosion_sonido, "cuchillo": cuchillo_sonido, "muerte": muerte_sonido, "level": level_sonido}

