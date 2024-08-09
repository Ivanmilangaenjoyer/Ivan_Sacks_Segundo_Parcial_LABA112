import pygame, time, sys, random
import json
from config import *
from modulo_funciones import *
from pygame.locals import *
from paredes import *
from jugador import *
from armas import *
from cargas import *

pygame.init()
pygame.font.init()

pygame.display.set_icon(icono)
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
slime_rojo = SlimeRojo(r"Seraph´s_wrath\assets\enemigos\Slimes\Red_Slime\derecha\Run_0.png", (128, 40), 100, 100, 5)
grupo_jugador.add(jugador)
grupo_enemigos.add(slime_rojo)

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
inmortalidad, musica, efectos = menu_principal(ventana, inmortalidad, contenido_actual, dicc_rect_img, anchura, altura, 
                                    dicc_sonidos, musica, efectos)

while True:
    reloj.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    movimiento_personaje(teclas, movimiento_prota, que_hace, lista_sprites)

    
    if teclas[K_COMMA]:
        ultimo_xp = grupo_xp.sprites()[-1]
        ultimo_xp.ganar_xp(grupo_xp, 10, subir_nivel)

    if teclas[K_p] and tiempo_real > 1000 and not teclas[K_m]:
        pausa(ventana, rect_pausa, imagen_pausa)

    if teclas[K_k]:
        jugador.vidas -= 1

    if teclas[K_m]:
        ultimo_mute, mute, musica, efectos = func_mute(mute, tiempo_real, ultimo_mute, cooldown_mute, dicc_sonidos, 
                                                    musica, efectos)

    if subir_nivel[1] > nivel_anterior:
        cooldown_slime_verde -= 100
        cooldown_slime_rojo -= 100
        cooldown_slime_azul -= 100

        carta_nivel = cartas_usuario(ventana, lista_al, diccionario_cartas, cargar_cartas, anchura, altura)
        ultima_bala_fuego = tiempo_real
        ultima_bala_fuego = tiempo_real
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
    
    ultimo_slime_azul = crear_slime_azul(rango_pos_x, rango_pos_y, Enemigo, grupo_enemigos, ultimo_slime_azul, 
                                        cooldown_slime_azul, tiempo_real)

    ultimo_slime_verde = crear_slime_verde(rango_pos_x, rango_pos_y, SlimeVerde, grupo_enemigos, ultimo_slime_verde, 
                                        cooldown_slime_verde, tiempo_real, nivel_anterior)
    
    ultimo_slime_rojo = crear_slime_rojo(rango_pos_x, rango_pos_y, SlimeRojo, grupo_enemigos, ultimo_slime_rojo, 
                                    cooldown_slime_rojo, tiempo_real, nivel_anterior)

    if dicc_cartas["veinte_veinte"] and bandera_veinte_veinte:
        cooldown_bala_fuego = cooldown_bala_fuego - 700
        bandera_veinte_veinte = False

    if dicc_cartas["telepatia"] and bandera_telepatia:
        cooldown_bala_fuego += 2700
        bandera_telepatia = False

    if dicc_cartas["cerebro"]:
        crear_bala_fuego_inversa_2(tiempo_real, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles,
                                dicc_cartas, que_hace, grupo_proyectiles_tp, Bala_guiada)

    if dicc_cartas["biblia"]:
        crear_bala_fuego_inversa(tiempo_real, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles, 
                                dicc_cartas, que_hace, grupo_proyectiles_tp, Bala_guiada)

    ultima_bala_fuego = crear_bala_fuego(tiempo_real, ultima_bala_fuego, cooldown_bala_fuego, jugador, Bala, grupo_proyectiles,
                                        dicc_cartas, que_hace, grupo_proyectiles_tp, Bala_guiada)
    
    if bandera_sacrificial_dagger == False:
        if dicc_cartas["sacrificial_dagger"] and dicc_cartas["cuchillo"]:
            crear_cuchillo_2(tiempo_real, ultimo_cuchillo, cooldown_cuchillo, jugador, Cuchillo, grupo_proyectiles,
                            dicc_sonidos)

    if dicc_cartas["cuchillo"]:
        ultimo_cuchillo = crear_cuchillo(tiempo_real, ultimo_cuchillo, cooldown_cuchillo, jugador, Cuchillo, 
                                        grupo_proyectiles, dicc_sonidos)
        
        if bandera_sacrificial_dagger:
            bandera_sacrificial_dagger = False
            cargar_cartas["sacrificial_dagger"] = r"Seraph´s_wrath\assets\cartas\sacrificial_dagger.jpg"

    if ((jugador.rect.right - offset_x >= anchura - scroll_area_width) and jugador.velocidad_x > 0) and offset_x < 640 or (
            (jugador.rect.left - offset_x <= scroll_area_width) and jugador.velocidad_x < 0) and offset_x > 0:
        offset_x += jugador.velocidad_x

    if ((jugador.rect.bottom - offset_y >= scroll_area_height) and jugador.velocidad_y > 0) and offset_y < 750 or (
            (jugador.rect.bottom - offset_y <= scroll_area_height) and jugador.velocidad_y < 0) and offset_y > 0:
        offset_y += jugador.velocidad_y

    bg, bg_image = obtener_fondo(bloque, offset_x, offset_y, anchura, altura)
    draw(ventana, bg, bg_image)

    if dicc_cartas["abel"]:
        abel_rect = abel_imagen.get_rect(centerx = jugador.rect.centerx - 50, centery = jugador.rect.centery)
        ventana.blit(abel_imagen, (abel_rect.x - offset_x, abel_rect.y - offset_y))

    blitear_grupo(ventana, grupo_proyectiles, ((offset_x, offset_y)))
    blitear_grupo(ventana, grupo_proyectiles_tp, ((offset_x, offset_y)))
    blitear_grupo(ventana, grupo_proyectiles_enemigos, ((offset_x, offset_y)))
    blitear_grupo(ventana, grupo_paredes, ((offset_x, offset_y)))
    blitear_grupo(ventana, grupo_collecionables, ((offset_x, offset_y)))
    blitear_grupo(ventana, grupo_enemigos, ((offset_x, offset_y)))
    blitear_grupo(ventana, grupo_jugador, ((offset_x, offset_y)))
    blitear_grupo(ventana, grupo_arboles, ((offset_x, offset_y)))
    blitear_grupo(ventana, grupo_vidas)
    blitear_grupo(ventana, grupo_xp)

    if mute and musica == False and efectos == False:
        ventana.blit(imagen_mute, (rect_mute.x, rect_mute.y))

    enemigo_cerca = rango_minimo_enemigos(grupo_enemigos, jugador)

    grupo_xp.update(ventana, jugador, grupo_vidas)
    grupo_vidas.update(grupo_vidas, jugador, dicc_cartas)
    grupo_collecionables.update(ventana, jugador, grupo_vidas, dicc_cartas)
    grupo_paredes.update(ventana, jugador, grupo_vidas)
    grupo_proyectiles.update(enemigo_cerca, dicc_cartas, grupo_enemigos, explosion, dicc_rect_img, dicc_sonidos)
    grupo_proyectiles_tp.update(enemigo_cerca, dicc_cartas, grupo_enemigos, explosion, dicc_rect_img, dicc_sonidos)
    grupo_proyectiles_enemigos.update(ventana, jugador, dicc_cartas)
    grupo_jugador.update(lista_sprites, ventana, que_hace,  lista_grupos, movimiento_prota, dicc_cartas)
    grupo_arboles.update(ventana, grupo_proyectiles, grupo_proyectiles_tp, grupo_collecionables, dicc_cartas)
    grupo_enemigos.update(diccionarios_slimes, ventana, grupo_proyectiles, grupo_proyectiles_tp, grupo_xp, subir_nivel, jugador, grupo_enemigos, 
                    dicc_cartas, offset_x, offset_y, BalaSlimeVerde, grupo_proyectiles_enemigos)

    movimiento_prota = {"derecha": False, "arriba": False, "abajo": False, "izquierda": False}
    tiempo_real = pygame.time.get_ticks()

    if jugador.vidas <= 0 and inmortalidad != True:
        print("muerte")
        with open(path_completo, "w") as file:   
            contenido_actual.append(subir_nivel[1])
            json.dump(contenido_actual, file)
            
        grupo_enemigos.empty()
        grupo_proyectiles.empty()
        grupo_proyectiles_enemigos.empty()
        grupo_proyectiles_tp.empty()
        grupo_collecionables.empty()
        
        inmortalidad, musica, efectos = menu_muerte(ventana, subir_nivel, dicc_rect_img, dicc_sonidos, inmortalidad, contenido_actual, 
                                anchura, altura, musica, efectos)
        cargar_linea_objetos(Xp, r"Seraph´s_wrath\assets\GUI\Settings\Bar BG.png", 15, 495, 30, 10, 30, grupo_xp, {"x": 30, "y": 0})
        diccionario_cartas = {"carta_0": [], "carta_1": [], "carta_2": []}

        dicc_cartas = {"telepatia": False, "veinte_veinte": False, "abel": False,
                        "biblia": False, "cerebro": False, "cuchillo": False,
                        "glass_cannon": False, "lucky_foot": False, "midas": False,
                        "penny": False, "sacrificial_dagger": False, "steam_final": False,
                        "suicide_king": False, "xray": False}
        
        cargar_cartas = {"veinte_veinte": r"Seraph´s_wrath\assets\cartas\veinte_veinte.jpg", "abel": r"Seraph´s_wrath\assets\cartas\abel.jpg", "biblia": r"Seraph´s_wrath\assets\cartas\biblia.jpg", 
                "cerebro": r"Seraph´s_wrath\assets\cartas\cerebro.jpg", "cuchillo": r"Seraph´s_wrath\assets\cartas\cuchillo.jpg", "glass_cannon": r"Seraph´s_wrath\assets\cartas\glass_cannon.jpg",
                "lucky_foot": r"Seraph´s_wrath\assets\cartas\lucky_foot.jpg", "midas": r"Seraph´s_wrath\assets\cartas\midas.jpg", "penny": r"Seraph´s_wrath\assets\cartas\penny.jpg",
                "steam_final": r"Seraph´s_wrath\assets\cartas\steam_final.jpg", "suicide_king": r"Seraph´s_wrath\assets\cartas\suicide_king.jpg", "telepatia": r"Seraph´s_wrath\assets\cartas\telepatia.jpg", "xray": r"Seraph´s_wrath\assets\cartas\xray.jpg"}

        jugador.rect.centerx = anchura // 2
        jugador.rect.centery = altura // 2 
        jugador_colision = False
        carta_nivel = None
        bandera_telepatia = True
        bandera_veinte_veinte = True
        bandera_sacrificial_dagger = True
        nivel_anterior = 0
        offset_x = 0
        offset_y = 0
        cooldown_bala_fuego = 1500 
        cantidad_xp = 5
        cooldown_slime = 2700
        cooldown_cuchillo = 2000
        ultima_bala_fuego = 0
        movimiento_prota = {"derecha": False, "arriba": False, "abajo": False, "izquierda": False}
        jugador.vidas = 4
        
        cargar_linea_objetos(Vidas, r"Seraph´s_wrath\assets\items\muertos\Transperent\Icon1.png",32, 20, 32, 32, 3, grupo_vidas, {"x": 50, "y": 0})

        with open(path_completo, 'r') as archivo:
            contenido_actual = json.load(archivo)

        slime = Enemigo(r"Seraph´s_wrath\assets\enemigos\Slimes\Blue_Slime\derecha\Run_0.png", (128, 40), 400, 100, 5)
        grupo_enemigos.add(slime)

        subir_nivel[0] = 0
        subir_nivel[1] = 0

        tiempo_real = pygame.time.get_ticks()

        if musica:
            pygame.mixer.music.unpause()  
        if efectos:
            dicc_sonidos["cuchillo"].set_volume(0.1)
            dicc_sonidos["explosion"].set_volume(0.1)
            dicc_sonidos["muerte"].set_volume(0.1)  


    pygame.display.flip()