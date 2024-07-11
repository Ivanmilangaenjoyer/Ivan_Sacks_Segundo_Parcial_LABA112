import pygame, os
from pygame import mixer
FPS = 30
reloj = pygame.time.Clock()
directorio = os.getcwd()   
offset_x = 0
offset_y = 0
scroll_area_height = 300
scroll_area_width = 300
ultimo_arbol = 0
anchura = 900
altura = 500
anchura_prota = 50
altura_prota = 80
que_hace = ["nada", "derecha"]
jugador_colision = False
movimiento_prota = {"derecha": False, "arriba": False, "abajo": False, "izquierda": False}
lista_grupos = []
lista_al = []
fondo = pygame.image.load(r"Seraph´s_wrath\assets\fondos\veerde.jpg")
ultima_bala = 0
tiempo_real = pygame.time.get_ticks()
cooldown_bala = 3000
bloque = pygame.image.load(r"Seraph´s_wrath\assets\fondos\veerde.jpg")
vidas = 3
nivel_anterior = 0
subir_nivel = [0, 0]
carta_nivel = None
ultima_bala_fuego = 0
ultimo_cuchillo = 0
cooldown_bala_fuego = 1500
cooldown_cuchillo = 2000
ultimo_slime = 0
cooldown_slime = 2700
bandera_veinte_veinte = True
mute = False
ultimo_mute = 0
cooldown_mute = 500
inmortalidad = False

def crear_rectango_imagen(dir_imagen, pos_x, pos_y, medidas ):
    imagen = pygame.transform.scale(pygame.image.load(dir_imagen), medidas)
    rect = imagen.get_rect(centerx = (pos_x), centery = (pos_y))
    return imagen, rect

imagen_fama, rect_fama = crear_rectango_imagen(r"Seraph´s_wrath\assets\fondos\Salon_fama.jpg", anchura // 2, altura // 2, ((anchura, altura)))

imagen_muerte, rect_muerte = crear_rectango_imagen(r"Seraph´s_wrath\assets\fondos\muerte.png", anchura // 2, altura // 2, ((anchura, altura)))


imagen_reintentar, rect_reintentar = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\reintentar.png", anchura // 2, 200, ((400, 100)))


imagen_atras, rect_atras = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\atras.png", 50, 50, ((100, 100)))

imagen_musica_on, rect_musica_on = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\musica_on.png", anchura // 2, 100, ((400, 100)))
imagen_musica_off, rect_musica_off = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\musica_off.png", anchura // 2, 100, ((400, 100)))


imagen_inmortalidad_on, rect_inmortalidad_on = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\inmortalidad_on.png", anchura // 2, 250, ((400, 100)))
imagen_inmortalidad_off, rect_inmortalidad_off = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\inmortalidad_off.png", anchura // 2, 250, ((400, 100)))

imagen_efectos_off, rect_efectos_off = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\efectos_off.png", anchura // 2, 400, ((400, 100)))
imagen_efectos_on, rect_efectos_on = crear_rectango_imagen(r"Seraph´s_wrath\assets\botones\efectos_on.png", anchura // 2, 400, ((400, 100)))

imagen_fondo_opciones, rect_fondo_opciones = crear_rectango_imagen(r"Seraph´s_wrath\assets\fondos\templo.jpg", anchura // 2, altura // 2, ((anchura, altura)))

imagen_mute = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\mute.png"), ((50, 50)))
rect_mute = imagen_mute.get_rect(centerx = (60), centery = (470))

abel_imagen = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\armas\Objeto_Abel.png"), ((30, 30)))
imagen_pausa = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\GUI\Pause menu\pausa.png"), ((400, 300)))
rect_pausa = imagen_pausa.get_rect(centerx = (anchura // 2), centery = (altura // 2))

imagen_empezar = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\empezar.png"), ((400, 100)))
rect_empezar = imagen_empezar.get_rect(centerx = (anchura // 2), centery = (80))

imagen_opciones = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\opciones.png"), ((400, 100)))
rect_opciones = imagen_opciones.get_rect(centerx = (anchura // 2), centery = (200))

imagen_ranking = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\ranking.png"), ((400, 100)))
rect_ranking = imagen_ranking.get_rect(centerx = (anchura // 2), centery = (320))

imagen_salir = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\botones\salir.png"), ((400, 100)))
rect_salir = imagen_salir.get_rect(centerx = (anchura // 2), centery = (430))

imagen_jungla = pygame.transform.scale(pygame.image.load(r"Seraph´s_wrath\assets\fondos\jungla.jpg"), ((900, 500)))
rect_jungla = imagen_jungla.get_rect(centerx = (anchura // 2), centery = (altura // 2))

cargar_cartas = {"veinte_veinte": r"Seraph´s_wrath\assets\cartas\veinte_veinte.jpg", "abel": r"Seraph´s_wrath\assets\cartas\abel.jpg", "biblia": r"Seraph´s_wrath\assets\cartas\biblia.jpg", 
                "cerebro": r"Seraph´s_wrath\assets\cartas\cerebro.jpg", "cuchillo": r"Seraph´s_wrath\assets\cartas\cuchillo.jpg", "glass_cannon": r"Seraph´s_wrath\assets\cartas\glass_cannon.jpg",
                "lucky_foot": r"Seraph´s_wrath\assets\cartas\lucky_foot.jpg", "midas": r"Seraph´s_wrath\assets\cartas\midas.jpg", "penny": r"Seraph´s_wrath\assets\cartas\penny.jpg", "sacrificial_dagger": r"Seraph´s_wrath\assets\cartas\sacrificial_dagger.jpg",
                "steam_final": r"Seraph´s_wrath\assets\cartas\steam_final.jpg", "suicide_king": r"Seraph´s_wrath\assets\cartas\suicide_king.jpg", "telepatia": r"Seraph´s_wrath\assets\cartas\telepatia.jpg", "xray": r"Seraph´s_wrath\assets\cartas\xray.jpg"}

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

grupo_enemigos = pygame.sprite.Group()
grupo_jugador = pygame.sprite.Group()
grupo_arboles = pygame.sprite.Group()
grupo_paredes = pygame.sprite.Group()
grupo_proyectiles = pygame.sprite.Group()
grupo_collecionables = pygame.sprite.Group()
grupo_vidas = pygame.sprite.Group()
grupo_xp = pygame.sprite.Group()
lista_grupos.append(grupo_paredes)
diccionario_cartas = {"carta_0": [], "carta_1": [], "carta_2": []}

dicc_cartas = {"telepatia": False, "veinte_veinte": False, "abel": False,
                "biblia": False, "cerebro": False, "cuchillo": False,
                "glass_cannon": False, "lucky_foot": False, "midas": False,
                "penny": False, "sacrificial_dagger": False, "steam_final": False,
                "suicide_king": False, "xray": False}

try:
    pygame.mixer.init()
except pygame.error:
    print('No se pudo inicializar el módulo de sonido de Pygame')

pygame.mixer.music.load(r"Seraph´s_wrath\assets\sonidos\vampire_ost.mp3")
pygame.mixer.music.set_volume(0.3)

explosion_sonido = pygame.mixer.Sound(r"Seraph´s_wrath\assets\sonidos\explosion.mp3")
cuchillo_sonido = pygame.mixer.Sound(r"Seraph´s_wrath\assets\sonidos\cuchillo.mp3")
muerte_sonido = pygame.mixer.Sound(r"Seraph´s_wrath\assets\sonidos\recibir_daño.mp3")

cuchillo_sonido.set_volume(0.1)
explosion_sonido.set_volume(0.1)
muerte_sonido.set_volume(0.1)