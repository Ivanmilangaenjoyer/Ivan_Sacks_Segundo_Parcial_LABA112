import os
import pygame

FPS = 30
pygame.display.set_caption("Mission deliverance")
reloj = pygame.time.Clock()
directorio = os.getcwd()   
offset_x = 0
scroll_area_width = 300
anchura = 900
altura = 500
anchura_prota = 50
altura_prota = 80
corriendo = True
que_hace = ["nada", "nada"]
jugador_colision = False
plataformas = []
ventana = pygame.display.set_mode((anchura, altura))
fondo_dir = os.path.join(directorio, r"assets\imagenes\fondos\fondo.jpg")
fondo = pygame.image.load(fondo_dir)
pygame.transform.scale(fondo, (anchura, altura))

personaje_quieto = [pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Quieto\Idle_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Quieto\Idle_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Quieto\Idle_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Quieto\Idle_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Quieto\Idle_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Quieto\Idle_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Quieto\Idle_6.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Quieto\Idle_7.png"), ((130, 70))),
                    ]

personaje_salto_derecha = [pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_derecha\salto_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_derecha\salto_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_derecha\salto_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_derecha\salto_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_derecha\salto_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_derecha\salto_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_derecha\salto_6.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_derecha\salto_7.png"), ((130, 70))),
                    ]

personaje_salto_izquierda = [pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_izquierda\salto_izquierda_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_izquierda\salto_izquierda_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_izquierda\salto_izquierda_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_izquierda\salto_izquierda_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_izquierda\salto_izquierda_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_izquierda\salto_izquierda_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_izquierda\salto_izquierda_6.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Salto_izquierda\salto_izquierda_7.png"), ((130, 70))),
                    ]

personaje_derecha = [pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Derecha\derecha_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Derecha\derecha_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Derecha\derecha_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Derecha\derecha_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Derecha\derecha_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Derecha\derecha_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Derecha\derecha_6.png"), ((130, 70))),
                    ]

personaje_izquierda = [pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Izquierda\izquierda_0.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Izquierda\izquierda_1.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Izquierda\izquierda_2.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Izquierda\izquierda_3.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Izquierda\izquierda_4.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Izquierda\izquierda_5.png"), ((130, 70))),
                    pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\Izquierda\izquierda_6.png"), ((130, 70))),
                    ]

personaje_ataque_derecha = [pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\ataque_derecha\anim_ataque_0.png"), ((130, 70))),
                            pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\ataque_derecha\anim_ataque_1.png"), ((130, 70))),
                            pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\ataque_derecha\anim_ataque_2.png"), ((130, 70))),
                            pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\ataque_derecha\anim_ataque_3.png"), ((130, 70))),
                            pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\ataque_derecha\anim_ataque_4.png"), ((130, 70))),
                            pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\ataque_derecha\anim_ataque_5.png"), ((130, 70))),
                            pygame.transform.scale(pygame.image.load(r"assets\imagenes\prota\ataque_derecha\anim_ataque_6.png"), ((130, 70)))
                            ]

lista_sprites = {"nada": personaje_quieto, "derecha": personaje_derecha, "izquierda": personaje_izquierda,
                "salto_derecha": personaje_salto_derecha, "salto_izquierda": personaje_salto_izquierda, "ataque_derecha": personaje_ataque_derecha}

plataforma_imagen = pygame.transform.scale(pygame.image.load(r"assets\imagenes\plataformas\Pad_3_3.png"), ((300, 70)))
piso_imagen = pygame.image.load(r"assets\imagenes\plataformas\piso_piedra.jpg")
tile = pygame.image.load(r"assets\imagenes\fondos\pixel art_def.jpg")