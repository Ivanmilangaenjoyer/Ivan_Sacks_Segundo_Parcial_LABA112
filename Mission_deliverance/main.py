import pygame, time, sys
from config import *
from clase_prota import *
from pygame.locals import *
from plataforma import *
from fondo import *
pygame.init()
pygame.font.init()
ventana = pygame.display.set_mode((anchura, altura))

jugador = Jugador(personaje_quieto[0], (anchura_prota, altura_prota), anchura // 2, altura // 2, 1)


plataforma = Plataforma(r"assets\imagenes\plataformas\Pad_3_3.png", (200, 50), 500, 380, 3, "no")


plataformas.append(plataforma)

y = 0
for i in range(10):
    pared = Plataforma(r"assets\imagenes\plataformas\Piso\Piedra_grande_derecha.png", (90, 80), 0, y, 3, "si")
    y += 70
    plataformas.append(pared)

x = 0
for i in range(5):
    piso = Plataforma(r"assets\imagenes\plataformas\piso_piedra.jpg", (anchura, 100), x, 500, 3, "si")
    plataformas.append(piso)
    x += anchura

grupo_jugador = pygame.sprite.Group()
grupo_plataformas = pygame.sprite.Group()

for plataforma in plataformas:
    grupo_plataformas.add(plataforma)

grupo_jugador.add(jugador)


while corriendo:
    reloj.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    if teclas[K_d] or teclas[K_a] or teclas[K_w] or teclas[K_s] or teclas[K_SPACE] or que_hace[1] == "salto":
        if  teclas[K_d]:
            que_hace[0] = "derecha"
            
        if teclas[K_a]:
            que_hace[0] = "izquierda"

        if teclas[K_SPACE]:
            que_hace[0] = "ataque_derecha"

        if teclas[K_w]:
            que_hace[1] = "salto"
    else:
        que_hace[0] = "nada"


    if  ((jugador.rect.right - offset_x >= anchura - scroll_area_width) and jugador.velocidad > 0) or (
            (jugador.rect.left - offset_x <= scroll_area_width) and jugador.velocidad < 0) and offset_x > 0:
        offset_x += jugador.velocidad

    bg, bg_image = obtener_fondo()
    draw(ventana, bg, bg_image)

    grupo_plataformas.update(ventana)
    grupo_jugador.update(lista_sprites, ventana, que_hace, grupo_plataformas)

    for jugador in grupo_jugador:
        ventana.blit(jugador.image, (jugador.rect.x - offset_x, jugador.rect.y))

    for plataforma in grupo_plataformas:
        ventana.blit(plataforma.image, (plataforma.rect.x - offset_x, plataforma.rect.y))


    pygame.display.flip()