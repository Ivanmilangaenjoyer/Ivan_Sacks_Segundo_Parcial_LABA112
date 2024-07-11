import pygame, os

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
fondo = pygame.image.load(r"assets\fondos\veerde.jpg")
ultima_bala = 0
tiempo_real = pygame.time.get_ticks()
cooldown_bala = 3000
bloque = pygame.image.load(r"assets\fondos\veerde.jpg")
vidas = 3
nivel_anterior = 0
subir_nivel = [0, 0]
carta_nivel = None
ultima_bala_fuego = 0
ultimo_cuchillo = 0
cooldown_bala_fuego = 1500
cooldown_cuchillo = 2000
ultimo_slime = 0
cooldown_slime = 3000
bandera_veinte_veinte = True
abel_imagen = pygame.transform.scale(pygame.image.load(r"assets\armas\Objeto_Abel.png"), ((30, 30)))
imagen_pausa = pygame.transform.scale(pygame.image.load(r"assets\GUI\Pause menu\pausa.png"), ((400, 300)))
rect_pausa = imagen_pausa.get_rect(centerx = (anchura // 2), centery = (altura // 2))



cargar_cartas = {"veinte_veinte": r"assets\cartas\veinte_veinte.jpg", "abel": r"assets\cartas\abel.jpg", "biblia": r"assets\cartas\biblia.jpg", 
                "cerebro": r"assets\cartas\cerebro.jpg", "cuchillo": r"assets\cartas\cuchillo.jpg", "glass_cannon": r"assets\cartas\glass_cannon.jpg",
                "lucky_foot": r"assets\cartas\lucky_foot.jpg", "midas": r"assets\cartas\midas.jpg", "penny": r"assets\cartas\penny.jpg", "sacrificial_dagger": r"assets\cartas\sacrificial_dagger.jpg",
                "steam_final": r"assets\cartas\steam_final.jpg", "suicide_king": r"assets\cartas\suicide_king.jpg", "telepatia": r"assets\cartas\telepatia.jpg", "xray": r"assets\cartas\xray.jpg"}

personaje_quieto = [pygame.transform.scale(pygame.image.load(r"assets\prota\Quieto\Idle_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Quieto\Idle_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Quieto\Idle_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Quieto\Idle_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Quieto\Idle_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Quieto\Idle_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Quieto\Idle_6.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Quieto\Idle_7.png"), ((130, 70))),
                    ]

personaje_derecha = [pygame.transform.scale(pygame.image.load(r"assets\prota\Derecha\derecha_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Derecha\derecha_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Derecha\derecha_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Derecha\derecha_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Derecha\derecha_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Derecha\derecha_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Derecha\derecha_6.png"), ((130, 70))),
                    ]

personaje_izquierda = [pygame.transform.scale(pygame.image.load(r"assets\prota\Izquierda\izquierda_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Izquierda\izquierda_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Izquierda\izquierda_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Izquierda\izquierda_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Izquierda\izquierda_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Izquierda\izquierda_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\prota\Izquierda\izquierda_6.png"), ((130, 70))),
                    ]

explosion = [pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_0.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_1.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_2.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_3.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_4.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_5.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_6.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_7.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_8.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_9.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_10.png"), ((96, 96))),
            pygame.transform.scale(pygame.image.load(r"assets\animaciones\Explosion_11.png"), ((96, 96))),
            ]

slime_derecha = [
            pygame.transform.scale(pygame.image.load(r"assets\enemigos\Slimes\Blue_Slime\derecha\Run_0.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"assets\enemigos\Slimes\Blue_Slime\derecha\Run_1.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"assets\enemigos\Slimes\Blue_Slime\derecha\Run_2.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"assets\enemigos\Slimes\Blue_Slime\derecha\Run_3.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"assets\enemigos\Slimes\Blue_Slime\derecha\Run_4.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"assets\enemigos\Slimes\Blue_Slime\derecha\Run_5.png"), ((128, 40))),
            pygame.transform.scale(pygame.image.load(r"assets\enemigos\Slimes\Blue_Slime\derecha\Run_6.png"), ((128, 40))),

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


