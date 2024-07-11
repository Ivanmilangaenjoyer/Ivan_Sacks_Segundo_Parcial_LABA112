import pygame, time, sys
from config import *
from modulo_funciones import *
from pygame.locals import *
import random
from paredes import *
from jugador import *
from armas import *
import json

pygame.init()
pygame.font.init()

directorio = os.path.join(directorio, "Seraph´s_wrath")
path_completo = os.path.join(directorio, "Nivel.json")

try:
    with open(path_completo, 'r') as archivo:
        contenido_actual = json.load(archivo)
except:
    with open(path_completo, "w") as file:   
        json.dump([], file)

    with open(path_completo, 'r') as archivo:
        contenido_actual = json.load(archivo)
try:
    pygame.mixer.init()
except pygame.error:
    print('No se pudo inicializar el módulo de sonido de Pygame')

ventana = pygame.display.set_mode((anchura, altura))
pygame.display.set_caption("Seraph´s wrath")

jugador = Jugador(r"Seraph´s_wrath\assets\prota\Quieto\Idle_0.png", (anchura_prota, altura_prota), anchura // 2, altura // 2, 5)
slime = Enemigo(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_0.png", (128, 40), 400, 100, 5)

grupo_jugador.add(jugador)
grupo_enemigos.add(slime)

cargar_linea_objetos(Objetos, r"Seraph´s_wrath\assets\fondos\musgo.png",0, 0, 70, 50, 22, grupo_paredes, {"x": 70, "y": 0})
cargar_linea_objetos(Objetos, r"Seraph´s_wrath\assets\fondos\musgo.png",0, 0, 70, 50, 25, grupo_paredes, {"x": 0, "y": 50})
cargar_linea_objetos(Objetos, r"Seraph´s_wrath\assets\fondos\musgo.png",1540, 0, 70, 50, 26, grupo_paredes, {"x": 0, "y": 50})
cargar_linea_objetos(Objetos, r"Seraph´s_wrath\assets\fondos\musgo.png",0, 1250, 70, 50, 26, grupo_paredes, {"x": 70, "y": 0})

for vueltas in range(10):
    num_x = random.randrange(200, 1400)
    num_y = random.randrange(200, 1000)

    cargar_linea_objetos(Arbol, r"Seraph´s_wrath\assets\objetos_entorno\Arboles\fir_tree_4.png", num_x, num_y, 50, 150, 1, grupo_arboles, {"x": 0, "y": 0})

cargar_linea_objetos(Vidas, r"Seraph´s_wrath\assets\items\muertos\Transperent\Icon1.png",32, 20, 32, 32, 3, grupo_vidas, {"x": 50, "y": 0})

cargar_linea_objetos(Xp, r"Seraph´s_wrath\assets\GUI\Settings\Bar BG.png", 15, 495, 30, 10, 30, grupo_xp, {"x": 30, "y": 0})
cargar_linea_objetos(Xp, r"Seraph´s_wrath\assets\GUI\Settings\Bar.png", -5, 495, 9, 10, 1, grupo_xp, {"x": 0, "y": 0})

cantidad_xp = 5

pygame.mixer.music.play(-1)
inmortalidad = menu_principal(ventana, inmortalidad, contenido_actual)

while True:
    reloj.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[K_COMMA]:
        ultimo_xp = grupo_xp.sprites()[-1]
        ultimo_xp.ganar_xp(grupo_xp, 10, subir_nivel)

    if teclas[K_p] and tiempo_real > 2000:
        pausa(ventana, rect_pausa, offset_x, offset_y)

    if teclas[K_m]:
        ultimo_mute, mute = func_mute(mute, tiempo_real, ultimo_mute, cooldown_mute)

    if teclas[K_d] or teclas[K_a] or teclas[K_w] or teclas[K_s]:
        if teclas[K_d]:
            movimiento_prota["derecha"] = True
            que_hace[0] = "derecha"
        elif teclas[K_a]:
            movimiento_prota["izquierda"] = True
            que_hace[0] = "izquierda"

        if teclas[K_w] or teclas[K_s]:
            if teclas[K_w]:
                movimiento_prota["arriba"] = True
                que_hace[0] = "arriba"
            else:
                movimiento_prota["abajo"] = True
                que_hace[0] = "abajo"

        if movimiento_prota["derecha"] == True:
            lista_sprites["arriba"] = personaje_derecha
            lista_sprites["abajo"] = personaje_derecha
        elif movimiento_prota["izquierda"] == True:
            lista_sprites["arriba"] = personaje_izquierda
            lista_sprites["abajo"] = personaje_izquierda
    else:
        que_hace[0] = "nada"

    if que_hace[0] != "nada": 
        que_hace[1] = que_hace[0]

    if subir_nivel[1] > nivel_anterior:
        cooldown_slime -= 100
        carta_nivel = cartas_usuario(ventana, lista_al, diccionario_cartas)
        nivel_anterior += 1

    for clave in dicc_cartas:
        if carta_nivel == clave:
            dicc_cartas[clave] = True

    if tiempo_real - ultimo_arbol > 10000:
        ultimo_arbol = tiempo_real
        num_x = random.randrange(200, 1400)
        num_y = random.randrange(200, 1000)

        cargar_linea_objetos(Arbol, r"Seraph´s_wrath\assets\objetos_entorno\Arboles\fir_tree_4.png", num_x, num_y, 50, 150, 1, grupo_arboles, {"x": 0, "y": 0})

    rango_pos_x, rango_pos_y = rango_jugador(jugador)
    ultimo_slime = crear_slime(rango_pos_x, rango_pos_y, Enemigo, grupo_enemigos, ultimo_slime, cooldown_slime, tiempo_real)
    
    if dicc_cartas["veinte_veinte"] and bandera_veinte_veinte:
        cooldown_bala_fuego = cooldown_bala_fuego / 2
        bandera_veinte_veinte = False

    if dicc_cartas["cerebro"]:
        crear_bala_fuego_inversa_2(tiempo_real, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles, grupo_enemigos)

    if dicc_cartas["biblia"]:
        crear_bala_fuego_inversa(tiempo_real, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles, grupo_enemigos)

    ultima_bala_fuego = crear_bala_fuego(tiempo_real, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles, grupo_enemigos)
    
    if dicc_cartas["sacrificial_dagger"] and dicc_cartas["cuchillo"]:
        crear_cuchillo_2(tiempo_real, ultimo_cuchillo, cooldown_cuchillo, jugador, Cuchillo, grupo_proyectiles)

    if dicc_cartas["cuchillo"]:
        ultimo_cuchillo = crear_cuchillo(tiempo_real, ultimo_cuchillo, cooldown_cuchillo, jugador, Cuchillo, grupo_proyectiles)

    if ((jugador.rect.right - offset_x >= anchura - scroll_area_width) and jugador.velocidad_x > 0) and offset_x < 640 or (
            (jugador.rect.left - offset_x <= scroll_area_width) and jugador.velocidad_x < 0) and offset_x > 0:
        offset_x += jugador.velocidad_x

    if ((jugador.rect.bottom - offset_y >= scroll_area_height) and jugador.velocidad_y > 0) and offset_y < 750 or (
            (jugador.rect.bottom - offset_y <= scroll_area_height) and jugador.velocidad_y < 0) and offset_y > 0:
        offset_y += jugador.velocidad_y

    bg, bg_image = obtener_fondo(bloque, offset_x, offset_y)
    draw(ventana, bg, bg_image)

    if dicc_cartas["abel"]:
        abel_rect = abel_imagen.get_rect(centerx = jugador.rect.centerx - 50, centery = jugador.rect.centery)
        ventana.blit(abel_imagen, (abel_rect.x - offset_x, abel_rect.y - offset_y))

    if mute:
        ventana.blit(imagen_mute, (rect_mute.x, rect_mute.y))

    for proyectil in grupo_proyectiles:
        ventana.blit(proyectil.image, (proyectil.rect.x - offset_x, proyectil.rect.y - offset_y))

    for pared in grupo_paredes:
        ventana.blit(pared.image, (pared.rect.x - offset_x, pared.rect.y - offset_y))

    for collecionable in grupo_collecionables:
            ventana.blit(collecionable.image, (collecionable.rect.x - offset_x, collecionable.rect.y - offset_y))

    for vida in grupo_vidas:
        ventana.blit(vida.image, (vida.rect.x, vida.rect.y))

    for enemigo in grupo_enemigos:
        ventana.blit(enemigo.image, (enemigo.rect.x - offset_x, enemigo.rect.y - offset_y))

    for jugador in grupo_jugador:
        ventana.blit(jugador.image, (jugador.rect.x - offset_x, jugador.rect.y - offset_y))

    for arbol in grupo_arboles:
        ventana.blit(arbol.image, (arbol.rect.x - offset_x, arbol.rect.y - offset_y))

    for xp in grupo_xp:
        ventana.blit(xp.image, (xp.rect.x, xp.rect.y))

    enemigo_cerca = rango_minimo_enemigos(grupo_enemigos, jugador)

    grupo_xp.update(ventana, jugador, grupo_vidas)
    grupo_vidas.update(grupo_vidas, jugador, dicc_cartas)
    grupo_collecionables.update(ventana, jugador, grupo_vidas, dicc_cartas)
    grupo_paredes.update(ventana, jugador, grupo_vidas)
    grupo_proyectiles.update(ventana, jugador, grupo_proyectiles, que_hace, enemigo_cerca, dicc_cartas, grupo_enemigos)
    grupo_enemigos.update(diccionario_slime, ventana, grupo_proyectiles, grupo_xp, subir_nivel, jugador, grupo_enemigos, dicc_cartas, offset_x, offset_y)
    grupo_jugador.update(lista_sprites, ventana, que_hace,  lista_grupos, movimiento_prota, dicc_cartas)
    grupo_arboles.update(ventana, grupo_proyectiles, grupo_collecionables, dicc_cartas)


    movimiento_prota = {"derecha": False, "arriba": False, "abajo": False, "izquierda": False}
    tiempo_real = pygame.time.get_ticks()
    if jugador.vidas <= 0 and inmortalidad != True:
        with open(path_completo, "w") as file:   
            contenido_actual.append(subir_nivel[1])
            json.dump(contenido_actual, file)
        menu_muerte(ventana, subir_nivel)
        cargar_linea_objetos(Xp, r"Seraph´s_wrath\assets\GUI\Settings\Bar BG.png", 15, 495, 30, 10, 30, grupo_xp, {"x": 30, "y": 0})
        dicc_cartas = {"telepatia": False, "veinte_veinte": False, "abel": False,
                        "biblia": False, "cerebro": False, "cuchillo": False,
                        "glass_cannon": False, "lucky_foot": False, "midas": False,
                        "penny": False, "sacrificial_dagger": False, "steam_final": False,
                        "suicide_king": False, "xray": False}
        cargar_cartas = {"veinte_veinte": r"Seraph´s_wrath\assets\cartas\veinte_veinte.jpg", "abel": r"Seraph´s_wrath\assets\cartas\abel.jpg", "biblia": r"Seraph´s_wrath\assets\cartas\biblia.jpg", 
                "cerebro": r"Seraph´s_wrath\assets\cartas\cerebro.jpg", "cuchillo": r"Seraph´s_wrath\assets\cartas\cuchillo.jpg", "glass_cannon": r"Seraph´s_wrath\assets\cartas\glass_cannon.jpg",
                "lucky_foot": r"Seraph´s_wrath\assets\cartas\lucky_foot.jpg", "midas": r"Seraph´s_wrath\assets\cartas\midas.jpg", "penny": r"Seraph´s_wrath\assets\cartas\penny.jpg", "sacrificial_dagger": r"Seraph´s_wrath\assets\cartas\sacrificial_dagger.jpg",
                "steam_final": r"Seraph´s_wrath\assets\cartas\steam_final.jpg", "suicide_king": r"Seraph´s_wrath\assets\cartas\suicide_king.jpg", "telepatia": r"Seraph´s_wrath\assets\cartas\telepatia.jpg", "xray": r"Seraph´s_wrath\assets\cartas\xray.jpg"}

        jugador.rect.centerx = anchura // 2
        jugador.rect.centery = altura // 2
        carta_nivel = None
        nivel_anterior = 0
        offset_x = 0
        offset_y = 0
        cooldown_bala_fuego = 1500
        cooldown_cuchillo = 2000
        ultima_bala_fuego = 0
        que_hace = ["nada", "derecha"]
        movimiento_prota = {"derecha": False, "arriba": False, "abajo": False, "izquierda": False}
        jugador.vidas = 4
        cargar_linea_objetos(Vidas, r"Seraph´s_wrath\assets\items\muertos\Transperent\Icon1.png",32, 20, 32, 32, 3, grupo_vidas, {"x": 50, "y": 0})



        with open(path_completo, 'r') as archivo:
            contenido_actual = json.load(archivo)

        slime = Enemigo(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_0.png", (128, 40), 400, 100, 5)
        grupo_enemigos.add(slime)


        subir_nivel = [0, 0]

        tiempo_real = pygame.time.get_ticks()


    pygame.display.flip()