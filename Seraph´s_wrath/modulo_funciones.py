
from config import *
import random, math
import sys

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
                bala = Bala(r"assets\armas\bola_fuego_media.png",(40, 40),jugador.rect.centerx, jugador.rect.centery, 3, 3)
            else:
                if que_hace[1] == "derecha":
                    bala = Bala(r"assets\armas\bola_fuego_derecha.png",(30, 30),jugador.rect.centerx + 30, jugador.rect.centery, 5, 0)
                elif que_hace[1] == "izquierda":
                    bala = Bala(r"assets\armas\bola_fuego_izq.png",(30, 30),jugador.rect.centerx - 30, jugador.rect.centery, -5, 0)
                elif que_hace[1] == "arriba":
                    bala = Bala(r"assets\armas\bola_fuego_arriba.png",(30, 30),jugador.rect.centerx, jugador.rect.centery -30, 0, -5)
                elif que_hace[1] == "abajo":
                    bala = Bala(r"assets\armas\bola_fuego_abajo.png",(30, 30),jugador.rect.centerx, jugador.rect.centery +30, 0, +5)
            
            grupo_proyectiles.add(bala)
        return ultima_bala_fuego

def crear_bala_fuego_inversa(tiempo_actual, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles, grupo_enemigos):
        if tiempo_actual - ultima_bala_fuego > cooldown_bala_fuego:
            ultima_bala_fuego = tiempo_actual
            if dicc_cartas["telepatia"] and len(grupo_enemigos) != 0:
                bala = Bala(r"assets\armas\bola_fuego_media.png",(40, 40),jugador.rect.centerx - 10, jugador.rect.centery + 10, 3, 3)
            else:
                if que_hace[1] == "izquierda":
                    bala = Bala(r"assets\armas\bola_fuego_derecha.png",(30, 30),jugador.rect.centerx + 30, jugador.rect.centery, 5, 0)
                elif que_hace[1] == "derecha":
                    bala = Bala(r"assets\armas\bola_fuego_izq.png",(30, 30),jugador.rect.centerx - 30, jugador.rect.centery, -5, 0)
                elif que_hace[1] == "abajo":
                    bala = Bala(r"assets\armas\bola_fuego_arriba.png",(30, 30),jugador.rect.centerx, jugador.rect.centery -30, 0, -5)
                elif que_hace[1] == "arriba":
                    bala = Bala(r"assets\armas\bola_fuego_abajo.png",(30, 30),jugador.rect.centerx, jugador.rect.centery +30, 0, +5)
            
            grupo_proyectiles.add(bala)

def crear_bala_fuego_inversa_2(tiempo_actual, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles, grupo_enemigos):
        if tiempo_actual - ultima_bala_fuego > cooldown_bala_fuego:
            ultima_bala_fuego = tiempo_actual
            if dicc_cartas["telepatia"] and len(grupo_enemigos) != 0:
                bala1 = Bala(r"assets\armas\bola_fuego_media.png",(40, 40),jugador.rect.centerx + 10, jugador.rect.centery + 10, 3, 3)
                bala2 = Bala(r"assets\armas\bola_fuego_media.png",(40, 40),jugador.rect.centerx - 10, jugador.rect.centery - 10, 3, 3)

            else:
                if que_hace[1] == "izquierda" or que_hace[1] == "derecha":
                    bala1 = Bala(r"assets\armas\bola_fuego_arriba.png",(30, 30),jugador.rect.centerx, jugador.rect.centery -30, 0, -5)
                    bala2 = Bala(r"assets\armas\bola_fuego_abajo.png",(30, 30),jugador.rect.centerx, jugador.rect.centery +30, 0, +5)
                elif que_hace[1] == "abajo" or que_hace[1] == "arriba":
                    bala1 = Bala(r"assets\armas\bola_fuego_derecha.png",(30, 30),jugador.rect.centerx + 30, jugador.rect.centery, 5, 0)
                    bala2 = Bala(r"assets\armas\bola_fuego_izq.png",(30, 30),jugador.rect.centerx - 30, jugador.rect.centery, -5, 0)

            grupo_proyectiles.add(bala1)
            grupo_proyectiles.add(bala2)


def crear_cuchillo(tiempo_actual, ultimo_cuchillo, cooldown_cuchillo, jugador, Cuchillo, grupo_proyectiles):
        if tiempo_actual - ultimo_cuchillo > cooldown_cuchillo:
            ultimo_cuchillo = tiempo_actual
            cuchillo = Cuchillo(r"assets\armas\tramontina_abajo.png", (60, 90), jugador.rect.centerx, jugador.rect.top, 1, 4)
            grupo_proyectiles.add(cuchillo)
        return ultimo_cuchillo

def crear_cuchillo_2(tiempo_actual, ultimo_cuchillo, cooldown_cuchillo, jugador, Cuchillo, grupo_proyectiles):
        if tiempo_actual - ultimo_cuchillo > cooldown_cuchillo:
            ultimo_cuchillo = tiempo_actual
            cuchillo = Cuchillo(r"assets\armas\tramontina_abajo.png", (60, 90), jugador.rect.centerx + 20, jugador.rect.top, 1, 4)
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


def crear_slime(pos_x, pos_y, Enemigo, grupo_enemigos, ultimo_slime, cooldown_slime, tiempo_actual):
    if tiempo_actual - ultimo_slime > cooldown_slime:
        ultimo_slime = tiempo_actual
        slime = Enemigo(r"assets\enemigos\Slimes\Blue_Slime\derecha\Run_0.png", (128, 40), pos_x, pos_y, 5)
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

def menu_principal(ventana):
    pass