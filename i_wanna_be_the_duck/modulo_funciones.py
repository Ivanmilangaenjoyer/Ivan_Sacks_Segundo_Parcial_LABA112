import pygame, sys
from math import sqrt
from diferentes_colores import *
import random
pygame.init()
pygame.font.init()

width = 600
height = 700

def crear_imagen(img: str, left: float, top: float, width: float, height: float, speed: tuple)-> dict:
    """Crea un diccionario con un rectangulo, imagen, velocidad, etc.

    Args:
        img (str): La direccion de memoria de una imagen
        left (float): Coordenada x de un rectangulo
        top (float): Coordenada y de un rectangulo
        width (float): Ancho de la imagen
        height (float): Altura de la imagen
        speed (tuple): Velocidad en x e y

    Returns:
        dict: Un diccionario para manejar un rectangulo
    """
    img = pygame.image.load(img)
    img = escalar_imagen(img, width, height)
    rect = pygame.Rect(left, top, width, height)

    return {"rect": rect, "speed_x": speed[0], 
                "speed_y": speed[1], "bajando": False, "derecha": False, 
                "arriba": False, "izquierda": False, "img": img}


def escalar_imagen(imagen: str, width: float, height: float) -> pygame.surface:
    """Mediante una direccion de imagen, crea una surface

    Args:
        imagen (str): Transforma en una surface
        width (float): Ancho de una imagen
        height (float): Altura de una imagen

    Returns:
        surface: Surface de la imagen
    """
    return pygame.transform.scale(imagen, (width, height))


def movimiento(pato: dict, width: float, height: float):
    """Mediante un diccionario mueve un rectangulo en x e y.
    Limita el movimiento de un rectangulo mediante el ancho
    y el alto de la pantalla.

    Args:
        pato (dict): Diccionario con un rectangulo
        width (float): Ancho de la pantalla
        height (float): Alto de la pantalla
    """
    if pato["derecha"]:
        if pato["rect"].right < (width - pato["speed_x"]):
            pato["rect"].left += pato["speed_x"]

    if pato["izquierda"]:
        if pato["rect"].left > (0 + pato["speed_x"]):
            pato["rect"].left -= pato["speed_x"]

    if pato["arriba"]:
        if pato["rect"].top > (0 + pato["speed_y"]):
            pato["rect"].top -= pato["speed_y"]

    if pato["bajando"]:
        if pato["rect"].bottom < (height - pato["speed_y"]):
            pato["rect"].bottom += pato["speed_y"]
    
def mostrar_texto(screen: pygame.surface, tam: float, texto: str, 
                coordenadas: tuple, color = Colores.BLANCO, color_fondo = None):
    """Muestra texto en pantalla

    Args:
        screen (surface): La pantalla del juego
        tam (float): Tamaño del texto
        texto (str): Texto a mostrar
        coordenadas (tuple): Coordenadas en x e y
        color (tuple, optional): El color del texto. Defaults to Colores.BLANCO.
        color_fondo (tuple, optional): El color de fondo del texto. Defaults to None.
    """
    fuente = pygame.font.SysFont(None, tam)
    texto_mostrar = fuente.render(f"{texto}", True, color, color_fondo)
    rect_texto_mostrar = texto_mostrar.get_rect()
    rect_texto_mostrar.center = (coordenadas)

    screen.blit(texto_mostrar, rect_texto_mostrar)

def texto_rectangulo(ventana, texto, rectangulo, colores = ((Colores.BLANCO, Colores.ROJO)), tamaño = 30):
    pos_mouse = pygame.mouse.get_pos()
    fuente = pygame.font.SysFont("AniME Matrix - MB_EN", tamaño)

    if rectangulo.collidepoint(pos_mouse):
        renderizado = fuente.render(texto, False, colores[1])
    else:
        renderizado = fuente.render(texto, False, colores[0])

    rectangulo = renderizado.get_rect(center = ((rectangulo.centerx, rectangulo.centery)))

    ventana.blit(renderizado, rectangulo)


def colision_proyectiles(score, enemigo, explosion_img, enemigos, jugador_proyectil, explosiones, explosion_escudo = ((0,0)), vidas = None, lista_colisiones = None, es_enemigo = False, explosion_dimensiones = ((70, 70)), proyectiles = None, escudo = False, sonido_explosion = None):
    try:
        enemigo_mask = pygame.mask.from_surface(enemigo["img"])
        jugador_proyectil_mask = pygame.mask.from_surface(jugador_proyectil["img"])

        offset = (enemigo["rect"].x - jugador_proyectil["rect"].x, enemigo["rect"].y - jugador_proyectil["rect"].y)
    
        if jugador_proyectil_mask.overlap(enemigo_mask, offset):
            enemigos.remove(enemigo)
            if proyectiles != None:
                proyectiles.remove(jugador_proyectil)
        
            if es_enemigo:
                explosiones.append(crear_imagen(explosion_img, enemigo["rect"].x + explosion_escudo[0], enemigo["rect"].centery + explosion_escudo[1], explosion_dimensiones[0], explosion_dimensiones[1], (5,5)))
                score[0] += 1
            else:
                explosiones.append(crear_imagen(explosion_img, enemigo["rect"].x + explosion_escudo[0], enemigo["rect"].bottom + explosion_escudo[1], explosion_dimensiones[0], explosion_dimensiones[1], (5,5)))

            lista_colisiones.append("Colision")
            sonido_explosion.play()

            if vidas and escudo == False and es_enemigo == False:
                vidas[0] -= 1
    except:
        pass

def colision_melee(score, enemigo, explosion_img, enemigos, jugador, escudo, explosiones, explosion_dimensiones, lista_colisiones, vidas, explosion_sonido):
        jugador_mask = pygame.mask.from_surface(jugador["img"])
        enemigo_mask = pygame.mask.from_surface(enemigo["img"])

        offset = jugador["rect"].x - enemigo["rect"].x, jugador["rect"].y - enemigo["rect"].y
    
        if enemigo_mask.overlap(jugador_mask, offset):
            enemigos.remove(enemigo)
            explosiones.append(crear_imagen(explosion_img, enemigo["rect"].x, enemigo["rect"].centery, explosion_dimensiones[0], explosion_dimensiones[1], (5,5)))
            lista_colisiones.append("EXPLOSIÓN")
            explosion_sonido.play()
            if escudo:
                score[0] += 1
            else:
                vidas[0] -= 1


def bala_rastreadora(balas, objetivo, projectile_speed):
    for bala in balas[:]:
        if bala["rect"].centerx == objetivo["rect"].centerx:
            bala["rect"].centerx = objetivo["rect"].centerx
        elif bala["rect"].centerx > objetivo["rect"].centerx:
            bala["rect"].centerx -= (projectile_speed[0])
        elif bala["rect"].centerx < objetivo["rect"].centerx:
            bala["rect"].centerx += projectile_speed[0]

        if bala["rect"].centery == objetivo["rect"].centery:
            bala["rect"].centery = objetivo["rect"].centery
        elif bala["rect"].centery > objetivo["rect"].centery:
            bala["rect"].centery -= (projectile_speed[1])
        elif bala["rect"].centery < objetivo["rect"].centery:
            bala["rect"].centery += projectile_speed[1]

        
def comportamiento_baby_dragons(enemigos, dimensiones, cooldown_movimiento_enemigo):
    for enemigo in enemigos[:]:
        if enemigo["rect"].top > dimensiones[1]:
            enemigos.remove(enemigo)

        if (cooldown_movimiento_enemigo[0]) > 1.2:
            for enemigo in enemigos[:]:
                enemigo["speed_x"] *= -1
            cooldown_movimiento_enemigo[0] = 0


        enemigo["rect"].x += enemigo["speed_x"]
        if enemigo["rect"].top < 50:
            enemigo["rect"].y += enemigo["speed_y"]


def comportamiento_aliens(enemigos, dimensiones):
    for enemigo in enemigos[:]:
        if enemigo["rect"].right > dimensiones[0]:
            enemigo["speed_x"] *= -1
        elif enemigo["rect"].left < 0:
            enemigo["speed_x"] *= -1
        if enemigo["rect"].top > dimensiones[1]:
            enemigos.remove(enemigo)

        enemigo["rect"].x += enemigo["speed_x"]

        enemigo["rect"].y += enemigo["speed_y"]

def comportamiento_murcielagos(enemigos, dimensiones, cooldown_movimiento_enemigo):
    for enemigo in enemigos[:]:
        if enemigo["rect"].top > dimensiones[1]:
            enemigos.remove(enemigo)

        if (cooldown_movimiento_enemigo[0]) > 0.6:
            for enemigo in enemigos[:]:
                enemigo["speed_x"] *= -1
            cooldown_movimiento_enemigo[0] = 0

        enemigo["rect"].x += enemigo["speed_x"]

        enemigo["rect"].y += enemigo["speed_y"]


def bala_estandar(balas, velocidad_bala):
    for bala in balas:
        bala["rect"] += velocidad_bala


def cooldowns_disparos_enemigos_solitario(enemigos, cooldown_bala, ultima_bala, bala, bala_img, dimensiones_bala, velocidades):
    tam = len(enemigos)
    if (cooldown_bala[0]) >= ultima_bala[0] and tam > 0:
        try:
            indice_enemigo = random.randint(0, tam -1)
        except: 
            indice_enemigo = 0

        bala.append(crear_imagen(bala_img, enemigos[indice_enemigo]["rect"].midbottom[0], enemigos[indice_enemigo]["rect"].midbottom[1], dimensiones_bala[0], dimensiones_bala[1], (velocidades[0], velocidades[1])))
        cooldown_bala[0] = 0

def esperar_usuario(): 
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE or evento.key == pygame.K_ESCAPE :
                    pygame.quit()
                    sys.exit()
                else:
                    return 
                
def menu_inicio(ventana, rect_inicio, rect_opciones, rect_puntaje, rect_salir): 
    while True:
        
        pygame.draw.rect(ventana, Colores.VERDE, rect_inicio)
        pygame.draw.rect(ventana, Colores.VERDE, rect_opciones)
        pygame.draw.rect(ventana, Colores.VERDE, rect_puntaje)
        pygame.draw.rect(ventana, Colores.VERDE, rect_salir)

        texto_rectangulo(ventana, "Comenzar", rect_inicio, ((Colores.NEGRO, Colores.BLANCO)), 20)
        texto_rectangulo(ventana, "Opciones", rect_opciones, ((Colores.NEGRO, Colores.BLANCO)), 20)
        texto_rectangulo(ventana, "Puntuaciones", rect_puntaje, ((Colores.NEGRO, Colores.BLANCO)), 14)
        texto_rectangulo(ventana, "Salir", rect_salir, ((Colores.NEGRO, Colores.BLANCO)), 20)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            mouse_keys = pygame.mouse.get_pressed()
            if mouse_keys[0]: 
                mouse = evento.pos

                if rect_inicio.collidepoint(mouse[0], mouse[1]):
                    return "Iniciar"
                elif rect_opciones.collidepoint(mouse[0], mouse[1]):
                    return "Opciones"
                elif rect_puntaje.collidepoint(mouse[0], mouse[1]):
                    return "Puntaje"
                elif rect_salir.collidepoint(mouse[0], mouse[1]):
                    pygame.quit()
                    sys.exit()
                        
                            
                
def pantalla_game_over(ventana, rect_menu, rect_reintentar, vidas, score2): 
    while True:
        
        pygame.draw.rect(ventana, Colores.VERDE, rect_reintentar)
        pygame.draw.rect(ventana, Colores.VERDE, rect_menu)


        texto_rectangulo(ventana, "Reintentar", rect_reintentar, ((Colores.NEGRO, Colores.BLANCO)), 17)
        texto_rectangulo(ventana, "Volver al menu", rect_menu, ((Colores.NEGRO, Colores.BLANCO)), 13)
        mostrar_texto(ventana, 35, f"Puntuacion final: {score2[0]}", ((width // 2, 500)))


        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            mouse_keys = pygame.mouse.get_pressed()
            if mouse_keys[0]: 
                mouse = evento.pos

                if rect_menu.collidepoint(mouse[0], mouse[1]):
                    return None

                elif rect_reintentar.collidepoint(mouse[0], mouse[1]):
                    vidas[0] = 3
                    return "Reintentar"


