import pygame, os
from pygame import mixer

FPS = 30
reloj = pygame.time.Clock()
directorio = os.getcwd()   
tiempo_real = pygame.time.get_ticks()

try:
    pygame.mixer.init()
except pygame.error:
    print('No se pudo inicializar el módulo de sonido de Pygame')

grupo_enemigos = pygame.sprite.Group()
grupo_jugador = pygame.sprite.Group()
grupo_arboles = pygame.sprite.Group()
grupo_paredes = pygame.sprite.Group()
grupo_proyectiles = pygame.sprite.Group()
grupo_proyectiles_tp = pygame.sprite.Group()
grupo_proyectiles_enemigos = pygame.sprite.Group()
grupo_collecionables = pygame.sprite.Group()
grupo_vidas = pygame.sprite.Group()
grupo_xp = pygame.sprite.Group()


vuelta_slime = 0
offset_x = 0
offset_y = 0
scroll_area_height = 300
scroll_area_width = 300
ultimo_arbol = 0
anchura = 900
altura = 500
anchura_prota = 50
altura_prota = 80
ultima_bala = 0
cooldown_bala = 3000
vidas = 3
nivel_anterior = 0
ultimo_mute = 0
cooldown_mute = 500
ultima_bala_fuego = 0
ultimo_cuchillo = 0
cooldown_bala_fuego = 1500
cooldown_cuchillo = 2000
ultimo_slime = 0
cooldown_slime = 2700

jugador_colision = False
carta_nivel = None
bandera_telepatia = True
bandera_veinte_veinte = True
mute = False
inmortalidad = False

subir_nivel = [0, 0]
lista_grupos = []
lista_al = []
que_hace = ["nada", "derecha"]

movimiento_prota = {"derecha": False, "arriba": False, "abajo": False, "izquierda": False}

cargar_cartas = {"veinte_veinte": r"Seraph´s_wrath\assets\cartas\veinte_veinte.jpg", "abel": r"Seraph´s_wrath\assets\cartas\abel.jpg", "biblia": r"Seraph´s_wrath\assets\cartas\biblia.jpg", 
                "cerebro": r"Seraph´s_wrath\assets\cartas\cerebro.jpg", "cuchillo": r"Seraph´s_wrath\assets\cartas\cuchillo.jpg", "glass_cannon": r"Seraph´s_wrath\assets\cartas\glass_cannon.jpg",
                "lucky_foot": r"Seraph´s_wrath\assets\cartas\lucky_foot.jpg", "midas": r"Seraph´s_wrath\assets\cartas\midas.jpg", "penny": r"Seraph´s_wrath\assets\cartas\penny.jpg", "sacrificial_dagger": r"Seraph´s_wrath\assets\cartas\sacrificial_dagger.jpg",
                "steam_final": r"Seraph´s_wrath\assets\cartas\steam_final.jpg", "suicide_king": r"Seraph´s_wrath\assets\cartas\suicide_king.jpg", "telepatia": r"Seraph´s_wrath\assets\cartas\telepatia.jpg", "xray": r"Seraph´s_wrath\assets\cartas\xray.jpg"}

diccionario_cartas = {"carta_0": [], "carta_1": [], "carta_2": []}

dicc_cartas = {"telepatia": False, "veinte_veinte": False, "abel": False,
                "biblia": False, "cerebro": False, "cuchillo": False,
                "glass_cannon": False, "lucky_foot": False, "midas": False,
                "penny": False, "sacrificial_dagger": False, "steam_final": False,
                "suicide_king": False, "xray": False}

lista_grupos.append(grupo_paredes)


