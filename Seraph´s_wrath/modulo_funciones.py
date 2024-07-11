
from config import *
import random, math
import sys
from pygame import mixer

def mostrar_texto(screen: pygame.surface, tam: float, texto: str, 
                coordenadas: tuple, color = ((255,255,255)), color_fondo = ((0,0,0))):
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

def obtener_fondo(tile: str, offset_x: float, offset_y: float):
    """Crea coordenadas de filas y columnas,
    tamaños y alturas de una imagen,
    mueve las coordenadas con el jugador

    Args:
        offset_x (float): El desfasaje del jugador en x
        offset_y (float): El desfasaje del jugador en y

    Returns:
        tiles: Una lista con coordenas y tamaños
        imagen: Una imagen
    """
    imagen = tile
    _, _, width, height = imagen.get_rect()
    tiles = []
    for i in range((anchura + 500) // width + 1):
        for j in range((altura + 500) // height + 1):
            pos = (i * width - offset_x, j * height - offset_y)
            tiles.append(pos)

    return tiles, imagen

def draw(pantalla, bg, bg_image)-> None:
    """Imprime imagenes en pantalla,
        no retorna nada.
    Args:
        pantalla (_type_): El lugar donde se imprimen las imagenes
        bg (list): Un conjunto de coordenadas
        bg_image (_type_): La imagen a imprimirse
    """
    for tile in bg:
        pantalla.blit(bg_image, tile)


def cargar_linea_objetos(clase, dir_imagen: str, x: int, y: int, width: float, height: float, vueltas: int, grupo_objetos, incremento: dict)-> None:
    """Crea y carga objetos a un grupo de objetos,
    utiliza valores incrementales para crear filas y columnas de objetos,
    no retorna nada.

    Args:
        dir_imagen (str): Una dirreción de imagen
        x (int): Una coordenada x
        y (int): Una coordenada de Y
        width (float): El tamaño del objeto
        height (float): La altura del objeto
        vueltas (int): La cantidad de objetos a crear
        grupo_objetos (Group): El grupo de objetos a añadirse
        incremento (dict): Valores para incrementar en x e y
    """
    for vuelta in range(vueltas):
        objeto = clase(dir_imagen, (width, height), x, y, 3)
        grupo_objetos.add(objeto)
        x += incremento["x"] 
        y += incremento["y"] 


def cargar_carta(dir_memoria, lista, coordenadas):
    carta = pygame.image.load(dir_memoria)
    carta = pygame.transform.scale(carta, (250, 350))
    carta_rect = carta.get_rect()

    # Posición inicial de la imagen
    carta_rect.centerx = coordenadas[0]
    carta_rect.centery = coordenadas[1]

    lista.append(carta)
    lista.append(carta_rect)

def cartas_usuario(ventana, lista_al, diccionario_cartas): 
    func = True
    diccionario_cartas = {"carta_0": [], "carta_1": [], "carta_2": []}
    lista_al = []
    cartas_random(lista_al, diccionario_cartas)

    while func:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                click_pos = pygame.mouse.get_pos()
                if diccionario_cartas["carta_0"][1].collidepoint(click_pos):
                    carta_elegida = lista_al[0]
                    cargar_cartas.pop(lista_al[0], None)
                    func = False

                    
                elif diccionario_cartas["carta_1"][1].collidepoint(click_pos):
                    carta_elegida = lista_al[1]
                    cargar_cartas.pop(lista_al[1], None)
                    func = False

                elif diccionario_cartas["carta_2"][1].collidepoint(click_pos):
                    carta_elegida = lista_al[2]
                    cargar_cartas.pop(lista_al[2], None)
                    func = False


        dibujar_rectangulo(ventana, diccionario_cartas["carta_0"][0], diccionario_cartas["carta_0"][1])
        dibujar_rectangulo(ventana, diccionario_cartas["carta_1"][0], diccionario_cartas["carta_1"][1])
        dibujar_rectangulo(ventana, diccionario_cartas["carta_2"][0], diccionario_cartas["carta_2"][1])
        pygame.display.update()

    return carta_elegida

def cartas_random(lista_al, diccionario_cartas):
    numeros_posibles = []

    claves = list(cargar_cartas.keys())
    valor_max = len(claves)

    for numero in range(len(claves)):
        numero += 1
        numeros_posibles.append(numero)
    
    for i in range(3):
        numero_aleatorio = random.choice(numeros_posibles)
        numeros_posibles.remove(numero_aleatorio)
        match numero_aleatorio:
            case 1:
                carta_elegida = claves[0]
            case 2:
                carta_elegida = claves[1]
            case 3:
                carta_elegida = claves[2]
            case 4:
                carta_elegida = claves[3]
            case 5:
                carta_elegida = claves[4]
            case 6:
                carta_elegida = claves[5]
            case 7:
                carta_elegida = claves[6]
            case 8:
                carta_elegida = claves[7]
            case 9:
                carta_elegida = claves[8]
            case 10:
                carta_elegida = claves[9]
            case 11:
                carta_elegida = claves[10]
            case 12:
                carta_elegida = claves[11]
            case 13:
                carta_elegida = claves[12]
            case 14:
                carta_elegida = claves[13]

        lista_al.append(carta_elegida)

    cargar_carta(cargar_cartas[lista_al[0]], diccionario_cartas["carta_0"], [150, altura // 2])
    cargar_carta(cargar_cartas[lista_al[1]], diccionario_cartas["carta_1"], [anchura // 2, altura // 2])
    cargar_carta(cargar_cartas[lista_al[2]], diccionario_cartas["carta_2"], [anchura - 150, altura // 2])



# Función para dibujar la imagen en la pantalla
def dibujar_rectangulo(ventana, imagen, rectangulo):
    ventana.blit(imagen, rectangulo)


def crear_bala_fuego(tiempo_actual, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles, grupo_enemigos):
        if tiempo_actual - ultima_bala_fuego > cooldown_bala_fuego:
            ultima_bala_fuego = tiempo_actual
            if dicc_cartas["telepatia"] and len(grupo_enemigos) != 0:
                print("hola")
                bala = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_media.png",(40, 40),jugador.rect.centerx, jugador.rect.centery, 3, 3)
            else:
                if que_hace[1] == "derecha":
                    bala = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_derecha.png",(30, 30),jugador.rect.centerx + 30, jugador.rect.centery, 5, 0)
                elif que_hace[1] == "izquierda":
                    bala = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_izq.png",(30, 30),jugador.rect.centerx - 30, jugador.rect.centery, -5, 0)
                elif que_hace[1] == "arriba":
                    bala = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_arriba.png",(30, 30),jugador.rect.centerx, jugador.rect.centery -30, 0, -5)
                elif que_hace[1] == "abajo":
                    bala = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_abajo.png",(30, 30),jugador.rect.centerx, jugador.rect.centery +30, 0, +5)
            
            grupo_proyectiles.add(bala)
        return ultima_bala_fuego

def crear_bala_fuego_inversa(tiempo_actual, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles, grupo_enemigos):
        if tiempo_actual - ultima_bala_fuego > cooldown_bala_fuego:
            ultima_bala_fuego = tiempo_actual
            if dicc_cartas["telepatia"] and len(grupo_enemigos) != 0:
                bala = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_media.png",(40, 40),jugador.rect.centerx - 10, jugador.rect.centery + 10, 3, 3)
            else:
                if que_hace[1] == "izquierda":
                    bala = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_derecha.png",(30, 30),jugador.rect.centerx + 30, jugador.rect.centery, 5, 0)
                elif que_hace[1] == "derecha":
                    bala = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_izq.png",(30, 30),jugador.rect.centerx - 30, jugador.rect.centery, -5, 0)
                elif que_hace[1] == "abajo":
                    bala = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_arriba.png",(30, 30),jugador.rect.centerx, jugador.rect.centery -30, 0, -5)
                elif que_hace[1] == "arriba":
                    bala = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_abajo.png",(30, 30),jugador.rect.centerx, jugador.rect.centery +30, 0, +5)
            
            grupo_proyectiles.add(bala)

def crear_bala_fuego_inversa_2(tiempo_actual, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles, grupo_enemigos):
        if tiempo_actual - ultima_bala_fuego > cooldown_bala_fuego:
            ultima_bala_fuego = tiempo_actual
            if dicc_cartas["telepatia"] and len(grupo_enemigos) != 0:
                bala1 = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_media.png",(40, 40),jugador.rect.centerx + 10, jugador.rect.centery + 10, 3, 3)
                bala2 = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_media.png",(40, 40),jugador.rect.centerx - 10, jugador.rect.centery - 10, 3, 3)

            else:
                if que_hace[1] == "izquierda" or que_hace[1] == "derecha":
                    bala1 = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_arriba.png",(30, 30),jugador.rect.centerx, jugador.rect.centery -30, 0, -5)
                    bala2 = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_abajo.png",(30, 30),jugador.rect.centerx, jugador.rect.centery +30, 0, +5)
                elif que_hace[1] == "abajo" or que_hace[1] == "arriba":
                    bala1 = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_derecha.png",(30, 30),jugador.rect.centerx + 30, jugador.rect.centery, 5, 0)
                    bala2 = Bala(r"Seraph´s_wrath\assets\armas\bola_fuego_izq.png",(30, 30),jugador.rect.centerx - 30, jugador.rect.centery, -5, 0)

            grupo_proyectiles.add(bala1)
            grupo_proyectiles.add(bala2)


def crear_cuchillo(tiempo_actual, ultimo_cuchillo, cooldown_cuchillo, jugador, Cuchillo, grupo_proyectiles):
        if tiempo_actual - ultimo_cuchillo > cooldown_cuchillo:
            ultimo_cuchillo = tiempo_actual
            cuchillo = Cuchillo(r"Seraph´s_wrath\assets\armas\tramontina_abajo.png", (60, 90), jugador.rect.centerx, jugador.rect.top, 1, 4)
            grupo_proyectiles.add(cuchillo)
            cuchillo_sonido.play()
        return ultimo_cuchillo

def crear_cuchillo_2(tiempo_actual, ultimo_cuchillo, cooldown_cuchillo, jugador, Cuchillo, grupo_proyectiles):
        if tiempo_actual - ultimo_cuchillo > cooldown_cuchillo:
            ultimo_cuchillo = tiempo_actual
            cuchillo = Cuchillo(r"Seraph´s_wrath\assets\armas\tramontina_abajo.png", (60, 90), jugador.rect.centerx + 20, jugador.rect.top, 1, 4)
            grupo_proyectiles.add(cuchillo)

def rango_jugador(jugador):
    """Calcula un rango en base al jugador en donde no pueden aparecer enemigos,
    y devuelve dos posiciones que no estén en ese rango
    Args:
        jugador (class): El jugador al cúal se le va a calcular el rengo

    Returns:
        int: Posición en x 
        int: Posición en y
    """
    bloque_izquierda = jugador.rect.centerx - 500
    bloque_derecha = jugador.rect.centerx + 500
    bloque_arriba = jugador.rect.centery - 500
    bloque_abajo = jugador.rect.centery + 500

    pos_x = random.randint(150, 1400)
    pos_y = random.randint(150, 1100)


    while pos_x > bloque_izquierda and pos_x < bloque_derecha:
        pos_x = random.randint(150, 1400)

    while pos_y < bloque_arriba and pos_y > bloque_abajo:
        pos_y = random.randint(150, 1100)


    return pos_x, pos_y

def rango_minimo_enemigos(grupo_enemigos, jugador):
    distancia_minima =  1000 
    enemigo_mas_cercano = None

    for enemigo in grupo_enemigos:
        distancia = ((jugador.rect.centerx - enemigo.rect.centerx) ** 2 + (jugador.rect.centery - enemigo.rect.centery) ** 2) ** 0.5

        if distancia < distancia_minima:
            distancia_minima = distancia
            enemigo_mas_cercano = enemigo

    return enemigo_mas_cercano



def crear_slime(pos_x, pos_y, Enemigo, grupo_enemigos, ultimo_slime, cooldown_slime, tiempo_actual):
    if tiempo_actual - ultimo_slime > cooldown_slime:
        ultimo_slime = tiempo_actual
        slime = Enemigo(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_0.png", (128, 40), pos_x, pos_y, 5)
        grupo_enemigos.add(slime)
        
    return ultimo_slime



def pausa(ventana, rect_pausa, offset_x, offset_y):
    func = True
    while func:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.KEYDOWN:
                func = False

        ventana.blit(imagen_pausa, (rect_pausa.x, rect_pausa.y))
        pygame.display.update()

def menu_principal(ventana, inmortalidad, contenido_actual):
    func = True
    y = 100
    vueltas = len(contenido_actual)
    while func:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                click_pos = pygame.mouse.get_pos()
                if rect_empezar.collidepoint(click_pos):
                    func = False
                elif rect_opciones.collidepoint(click_pos):
                    inmortalidad = opciones(ventana, inmortalidad)
                elif rect_ranking.collidepoint(click_pos):
                    ranking(ventana, contenido_actual)
                elif rect_salir.collidepoint(click_pos):
                    pygame.quit()
                    sys.exit()

        ventana.blit(imagen_jungla, (rect_jungla.x, rect_jungla.y))
        ventana.blit(imagen_empezar, (rect_empezar.x, rect_empezar.y))
        ventana.blit(imagen_opciones, (rect_opciones.x, rect_opciones.y))
        ventana.blit(imagen_ranking, (rect_ranking.x, rect_ranking.y))
        ventana.blit(imagen_salir, (rect_salir.x, rect_salir.y))
        pygame.display.update()
    return inmortalidad

def ranking(ventana, contenido_actual):
    func = True
    contenido_actual = sorted(contenido_actual, reverse =True)
    while func:
        y = 20

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                click_pos = pygame.mouse.get_pos()

                if rect_atras.collidepoint(click_pos):
                        func = False

        ventana.blit(imagen_fama, (rect_fama.x, rect_fama.y))
        ventana.blit(imagen_atras, (rect_atras.x, rect_atras.y))

        for nivel in contenido_actual:
            mostrar_texto(ventana, 50, f"Nivel alcanzado: = {nivel}", ((anchura // 2, y)))
            y += 50

        pygame.display.flip()


def opciones(ventana, inmortalidad):
    tiempo_actual = pygame.time.get_ticks()
    imagen_musica, rect_musica = imagen_musica_on, rect_musica_on 
    imagen_efectos, rect_efectos = imagen_efectos_on, rect_efectos_on
    imagen_inmortalidad, rect_inmortalidad = imagen_inmortalidad_off, rect_inmortalidad_off
    func = True
    musica = True
    efectos = True
    inmortalidad = False
    ultimo_click = 0
    cooldown_click = 300
    while func:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and tiempo_actual - ultimo_click > cooldown_click:
                ultimo_click = tiempo_actual
                click_pos = pygame.mouse.get_pos()

                if rect_musica_on.collidepoint(click_pos) and musica == True:
                    imagen_musica = imagen_musica_off
                    rect_musica = rect_musica_off
                    musica = False
                    pygame.mixer.music.pause()
                elif rect_musica_off.collidepoint(click_pos) and musica == False:
                    imagen_musica = imagen_musica_on
                    rect_musica = rect_musica_on
                    musica = True
                    pygame.mixer.music.unpause()    


                if rect_efectos_on.collidepoint(click_pos) and efectos == True:
                    imagen_efectos = imagen_efectos_off
                    rect_efectos = rect_efectos_off
                    efectos = False
                    cuchillo_sonido.set_volume(0)
                    explosion_sonido.set_volume(0)
                    muerte_sonido.set_volume(0)
                elif rect_efectos_off.collidepoint(click_pos) and efectos == False:
                    imagen_efectos = imagen_efectos_on
                    rect_efectos = rect_efectos_on
                    efectos = True
                    cuchillo_sonido.set_volume(0.1)
                    explosion_sonido.set_volume(0.1)
                    muerte_sonido.set_volume(0.1)

                if rect_inmortalidad_off.collidepoint(click_pos) and inmortalidad == False:
                    imagen_inmortalidad = imagen_inmortalidad_on
                    rect_inmortalidad = rect_inmortalidad_on
                    inmortalidad = True
                elif rect_inmortalidad_on.collidepoint(click_pos) and inmortalidad == True:
                    imagen_inmortalidad = imagen_inmortalidad_off
                    rect_inmortalidad = rect_inmortalidad_off
                    inmortalidad = False

                if rect_atras.collidepoint(click_pos):
                    func = False

        tiempo_actual = pygame.time.get_ticks()
        ventana.blit(imagen_fondo_opciones, (rect_fondo_opciones.x, rect_fondo_opciones.y))
        ventana.blit(imagen_efectos, (rect_efectos.x, rect_efectos.y))
        ventana.blit(imagen_inmortalidad, (rect_inmortalidad.x, rect_inmortalidad.y))
        ventana.blit(imagen_musica, (rect_musica.x, rect_musica.y))
        ventana.blit(imagen_atras, (rect_atras.x, rect_atras.y))
        pygame.display.update()

    return inmortalidad


def func_mute(mute, tiempo_real, ultimo_mute, cooldown_mute):
        if tiempo_real - ultimo_mute > cooldown_mute:
            ultimo_mute = tiempo_real
            if mute:
                pygame.mixer.music.unpause()    
                cuchillo_sonido.set_volume(0.1)
                explosion_sonido.set_volume(0.1)
                muerte_sonido.set_volume(0.1)
                mute = False
            else:
                mute = True
                pygame.mixer.music.pause()
                cuchillo_sonido.set_volume(0)
                explosion_sonido.set_volume(0)
                muerte_sonido.set_volume(0)
        return ultimo_mute, mute

def menu_muerte(ventana, jugador, Vidas):
    func = True
    inmortalidad = False
    pygame.mixer.music.pause()
    muerte_sonido.play()

    while func:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                click_pos = pygame.mouse.get_pos()
                if rect_salir.collidepoint(click_pos):
                    pygame.quit()
                    sys.exit()

        ventana.blit(imagen_muerte, (rect_muerte.x, rect_muerte.y))
        ventana.blit(imagen_salir, (rect_salir.x, rect_salir.y))
        mostrar_texto(ventana, 400, "Puntaje", ((200,200)))

        pygame.display.update()

