import pygame, time, sys
from config import *
from modulo_funciones import *
from modulo_funciones_entrada import *
import random

pygame.init()
pygame.font.init()


ventana = pygame.display.set_mode((width, height))
pygame.display.set_caption("I wanna be the Duck")

while True:
    pygame.mouse.set_visible(True)
    pygame.mixer.music.pause()
    sonido_victoria.stop()
    actualizacion = False
    directorio = os.getcwd()     
    path_completo = os.path.join(directorio, "Score.json")

    try:
        with open(path_completo, 'r') as archivo:
            contenido_actual = json.load(archivo)
    except:
        with open(path_completo, "w") as file:   
            json.dump([], file)

        with open(path_completo, 'r') as archivo:
            contenido_actual = json.load(archivo)

    if score[0] > 0:
        actualizacion = True

    if actualizacion == True:
        contenido_actual += score

        score2 = score
        score = [0]

        with open(path_completo, "w") as file:   
            json.dump(contenido_actual, file)

    if andando == False:
        opcion_elegida = None
        reintento = None
        ventana.fill(Colores.NEGRO)
        if vidas[0] < 1 and not victoria and not opcion_elegida:
            reintento = pantalla_game_over(ventana, rect_menu, rect_reintentar, vidas, score2)
            pygame.display.flip()
            if reintento:
                opcion_elegida = "Iniciar"

        elif victoria:
            while victoria:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_BACKSPACE]:
                        victoria = False

                    mouse_keys = pygame.mouse.get_pressed()
                    if mouse_keys[0]: 
                        mouse = evento.pos

                        if flecha_atras["rect"].collidepoint(mouse[0], mouse[1]):
                            victoria = False
                                    
                if bandera_victoia == True:
                    sonido_victoria.play()
                    bandera_victoia = False
                
                ventana.blit(fondo_victoria, (0, 0))
                pato["rect"].center = ((300, 400))
                mostrar_texto(ventana, 40, "Felicidades", ((width // 2, 200)))
                mostrar_texto(ventana, 40, "Ganaste", ((width // 2, 300)))
                mostrar_texto(ventana, 35, f"Puntuacion final: {score2[0]}", ((width // 2, 500)))
                ventana.blit(pato["img"], pato["rect"])
                ventana.blit(tesoro["img"], tesoro["rect"])
                ventana.blit(flecha_atras["img"], flecha_atras["rect"])

                pygame.display.flip()

        if not opcion_elegida and not reintento:
            vidas[0] = 5
            sonido_victoria.stop()
            ventana.blit(fondo2, (- 400, - 100))
            pato["rect"].center = ((300, 200))
            ventana.blit(pato["img"], pato["rect"])
            mostrar_texto(ventana, 60, "I Wanna Be The Duck", ((300, 100)), Colores.BLANCO)
            mostrar_texto(ventana, 30, "Por Iván Sacks", ((300, 150)), Colores.BLANCO)
            opcion_elegida = menu_inicio(ventana, rect_iniciar, rect_opciones, rect_puntuacion, rect_salir)


            if opcion_elegida == "Opciones":
                opcion = True
                while opcion:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                                            
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_BACKSPACE]:
                            opcion = False


                        mouse_keys = pygame.mouse.get_pressed()
                        if mouse_keys[0]: 
                            mouse = evento.pos

                            if flecha_atras["rect"].collidepoint(mouse[0], mouse[1]):
                                opcion = False


                            if rect_mouse.collidepoint(mouse[0], mouse[1]):
                                if color_mouse == Colores.VERDE:
                                    color_mouse = Colores.ROJO
                                    usar_mouse = False
                                else:
                                    color_mouse = Colores.VERDE
                                    usar_mouse = True
                            elif rect_musica.collidepoint(mouse[0], mouse[1]):
                                if color_musica == Colores.VERDE:
                                    musica = False
                                    color_musica = Colores.ROJO
                                else:
                                    musica = True
                                    color_musica = Colores.VERDE
                            elif rect_sonido.collidepoint(mouse[0], mouse[1]):
                                if color_sonido == Colores.VERDE:
                                    explosion_sonido_laser.set_volume(0)
                                    escudo_sonido.set_volume(0)
                                    escudo_roto_sonido.set_volume(0)
                                    disparo_sonido.set_volume(0)
                                    sonido_laser.set_volume(0)
                                    sonido_victoria.set_volume(0)
                                    muerte_sonido.set_volume(0)
                                    explosion_sonido.set_volume(0)
                                    color_sonido = Colores.ROJO
                                else:
                                    explosion_sonido_laser.set_volume(0.1)
                                    escudo_sonido.set_volume(0.1)
                                    escudo_roto_sonido.set_volume(0.1)
                                    disparo_sonido.set_volume(0.1)
                                    sonido_laser.set_volume(0.1)
                                    sonido_victoria.set_volume(0.1)
                                    muerte_sonido.set_volume(0.1)
                                    explosion_sonido.set_volume(0.1)
                                    color_sonido = Colores.VERDE
                            elif rect_vidas_infinitas.collidepoint(mouse[0], mouse[1]):
                                if color_vidas == Colores.VERDE:
                                    color_vidas = Colores.ROJO
                                    mas_vidas = False
                                else:
                                    color_vidas = Colores.VERDE
                                    mas_vidas = True                               

                    ventana.fill(Colores.AZUL)
                    pygame.draw.rect(ventana, color_musica, rect_musica)
                    pygame.draw.rect(ventana, color_vidas, rect_vidas_infinitas)
                    pygame.draw.rect(ventana, color_mouse, rect_mouse)
                    pygame.draw.rect(ventana, color_sonido, rect_sonido)

                    texto_rectangulo(ventana, "Mouse", rect_mouse, ((Colores.NEGRO, Colores.BLANCO)), 20)
                    texto_rectangulo(ventana, "Musica", rect_musica, ((Colores.NEGRO, Colores.BLANCO)), 20)
                    texto_rectangulo(ventana, "Mas vidas", rect_vidas_infinitas, ((Colores.NEGRO, Colores.BLANCO)), 20)
                    texto_rectangulo(ventana, "Sonido", rect_sonido, ((Colores.NEGRO, Colores.BLANCO)), 20)

                    mostrar_texto(ventana, 40, "Opciones", ((width // 2, 100)))
                    ventana.blit(flecha_atras["img"], flecha_atras["rect"])
                    pygame.display.flip()


            if opcion_elegida == "Puntaje":
                puntuacion = True
                while puntuacion:
                    for evento in pygame.event.get():
                        if evento.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                                            
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_BACKSPACE]:
                            puntuacion = False

                        mouse_keys = pygame.mouse.get_pressed()
                        if mouse_keys[0]: 
                            mouse = evento.pos

                            if flecha_atras["rect"].collidepoint(mouse[0], mouse[1]):
                                puntuacion = False

                    ventana.blit(salon_fama, (0, 0))

                    with open(path_completo, "r") as file:   
                        puntajes = json.load(file)

                    puntajes.sort(reverse = True)

                    distancia_y = 0
                    num = 1
                    for puntaje in puntajes:
                        if num <= 10:
                            mostrar_texto(ventana, 30, f"Puesto N{num}", ((width // 2 - 50, 150 + distancia_y)), Colores.NEGRO)
                            mostrar_texto(ventana, 30, f"{puntaje}", ((width // 2 + 50, 150 + distancia_y)), Colores.NEGRO)
                            distancia_y += 50
                            num += 1
                    mostrar_texto(ventana, 50, "Puntajes", ((width // 2, 100)), Colores.VERDE)
                    ventana.blit(flecha_atras["img"], flecha_atras["rect"])

                    pygame.display.flip()

        if opcion_elegida == "Iniciar" and not victoria:
            if musica:
                pygame.mixer.music.play(-1)
            pato["rect"].midtop = (width//2, height - 100)
            #Resetear datos
            #Variables
            reintento = False
            andando = True
            escudo = False
            explotando = False
            explosion_cooldown = None
            generacion_enemigos = True
            bandera_victoia = True
            victoria = False
            ronda1 = False
            ronda2 = False
            ronda3 = False
            ronda4 = False
            ronda5 = False
            ronda = 0
            sonido_escudo = False
            #Listas
            fernets = []
            aliens = []
            baby_dragons = []
            murcielagos = []
            balas_murcielagos = []
            bombas = []
            explosiones = []
            explosiones_cooldown = []
            lista_colisiones = []
            cooldown_movimientos_murcielagos = []
            cooldown_movimientos_dragones = []
            score = [0]
            score2 = [0]
            cooldown_disparo_enemigo = [0, 0]
            ultimo_disparo_enemigo = [3, 1]
            if mas_vidas:
                vidas = [99]
            else:
                vidas = [5]


    while andando:
        clock.tick(FPS)
        cooldown_disparo += ((FPS * 0.001))
        cooldown_escudo += ((FPS * 0.001))
        timer += ((FPS * 0.001))
        for indice in range(len(cooldown_disparo_enemigo)):
            cooldown_disparo_enemigo[indice] += ((FPS * 0.001))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                                
            keys = pygame.key.get_pressed()
            entrada_teclas(pato, keys)

            if evento.type == pygame.MOUSEMOTION:
                if usar_mouse:
                    pygame.mouse.set_visible(False)
                    mouse = evento.pos
                    pato["rect"].centerx = mouse[0]
                    pato["rect"].centery = mouse[1]
            if keys[pygame.K_BACKSPACE]:
                andando = False
            if keys[pygame.K_SPACE]:
                if cooldown_disparo >= ultimo_disparo:
                    disparo_sonido.play()
                    cooldown_disparo = 0              
                    fernets.append(crear_imagen(fernet_img, pato["rect"].midtop[0] - pato_ancho // 8, pato["rect"].midtop[1] - pato_altura // 3, pato_altura // 2, pato_ancho // 2, (5, 5)))
            if keys[pygame.K_j]:
                if cooldown_escudo >= ultimo_escudo and escudo == False:
                    pato_escudo = crear_imagen(pato_escudo_img, pato["rect"].topleft[0], pato["rect"].topleft[1], pato_altura + 8, pato_ancho + 8, (7, 7))
                    pato["img"] = pato_escudo["img"]
                    pato["rect"] = pato_escudo["rect"]
                    cooldown_escudo = 0
                    escudo = True
            if keys[pygame.K_e]:
                murcielagos = []
                aliens = []
                baby_dragons = []

        ventana.blit(fondo, (0, -400))

        if victoria == True:
            andando = False

        if ronda == 0 and generacion_enemigos == True:
            mov = 0
            generacion_enemigos = False
            for i in range(5):
                aliens.append(crear_imagen(alien_img, width // 12 + mov , -(pato_altura), pato_altura, pato_ancho, (19, 4)))
                mov += 110
        
        comportamiento_baby_dragons(baby_dragons, ((width, height)), cooldown_movimientos_dragones)
        if not usar_mouse:
            movimiento(pato, width, height)

        if cooldown_escudo > 0.5 and escudo == True:
            escudo_sonido.play()
            pato_2 = crear_imagen(pato_img, pato_escudo["rect"].topleft[0], pato_escudo["rect"].topleft[1], pato_altura, pato_ancho, (7, 7))
            pato["img"] = pato_2["img"]
            pato["rect"] = pato_2["rect"]
            escudo = False
            sonido_escudo = True
        elif escudo == False and sonido_escudo == True:
            escudo_roto_sonido.play()
            sonido_escudo = False

        ventana.blit(pato["img"], pato["rect"])

        cooldowns_disparos_enemigos_solitario(baby_dragons, cooldown_disparo_enemigo, ultimo_disparo_enemigo, bombas, bomba_img, ((pato_ancho // 2, pato_altura // 2)), ((5, 10)))
        
        ## 1
        if ronda == 1 and ronda1 == True:        
            if (cooldown_disparo_enemigo[1]) >= ultimo_disparo_enemigo[1]:
                for murcielago in murcielagos:
                        balas_murcielagos.append(crear_imagen(bala_murcielago_img, murcielago["rect"].midbottom[0],  murcielago["rect"].midbottom[1], pato_ancho // 2, pato_altura // 2, ((5, 10))))
                cooldown_disparo_enemigo[1] = 0

            if (murcielagos + aliens + baby_dragons) == []:
                ronda += 1
            
        if ronda == 0 and (murcielagos + aliens + baby_dragons) == []:
            mov = 0
            ronda1 = True
            ronda += 1

            for i in range(5):
                aliens.append(crear_imagen(alien_img, width // 12 + mov , -(pato_altura), pato_altura, pato_ancho, (19, 4)))
                murcielagos.append(crear_imagen(murcielago_img, width // 16 - 50 + mov , -(pato_altura), pato_altura, pato_ancho, (7, 2)))
                mov += 110

            ## 2
        if ronda == 2 and ronda2 == True:
            if (murcielagos + aliens + baby_dragons) == []:
                ronda += 1

        if ronda == 2 and (murcielagos + aliens + baby_dragons) == []:
            mov = 0
            for i in range(5):
                murcielagos.append(crear_imagen(murcielago_img, width // 16 + mov , -(pato_altura), pato_altura, pato_ancho, (7, 2)))
                if i <= 2:
                    baby_dragons.append(crear_imagen(baby_dragon_img, 100 + mov , - 50, pato_altura, pato_ancho, (3, 1)))
                mov += 110
            ronda2 = True
        ## 3
        if ronda == 3 and ronda3 == True:
            if (murcielagos + aliens + baby_dragons) == []:
                ronda += 1

        if ronda == 3 and (murcielagos + aliens + baby_dragons) == []:
            mov_x_aliens = 0
            mov_x_baby_dragons = 0
            for i in range(5):
                aliens.append(crear_imagen(alien_img,  mov_x_aliens , -(pato_altura), pato_altura, pato_ancho, (19, 4)))
                baby_dragons.append(crear_imagen(baby_dragon_img, 60 + (mov_x_baby_dragons) , - 50, pato_altura, pato_ancho, (3, 1)))
                mov_x_aliens += 110
                mov_x_baby_dragons += 90

            mov_x_aliens = 0
            mov_y_aliens = 70
            for i in range(5):
                aliens.append(crear_imagen(alien_img, width // 12 + mov_x_aliens , -(pato_altura) - mov_y_aliens, pato_altura, pato_ancho, (19, 4)))
                mov_x_aliens += 110

            ronda3 = True
        ## 4
        if ronda == 4 and ronda4 == True:
            if (murcielagos + aliens + baby_dragons) == []:
                ronda += 1

        if ronda == 4 and (murcielagos + aliens + baby_dragons) == []:
            mov = 0
            for i in range(5):
                aliens.append(crear_imagen(alien_img, width // 12 + mov , -(pato_altura) - mov_y_aliens, pato_altura, pato_ancho, (19, 4)))
                murcielagos.append(crear_imagen(murcielago_img, width // 16 + mov , -(pato_altura * 2), pato_altura, pato_ancho, (7, 2)))
                if i <= 3:
                    baby_dragons.append(crear_imagen(baby_dragon_img, 100 + mov , - 50, pato_altura, pato_ancho, (3, 1)))
                mov += 110
            ronda4 = True

    ## 5
        if ronda == 5 and ronda5 == True:
            if (murcielagos + aliens + baby_dragons) == []:
                victoria = True

        if ronda == 5 and (murcielagos + aliens + baby_dragons) == []:
            mov = 0
            mov_y_aliens = 0
            for i in range(10):
                if i < 5:
                    murcielagos.append(crear_imagen(murcielago_img, width // 16 + mov , -(pato_altura * 2), pato_altura, pato_ancho, (7, 2)))
                aliens.append(crear_imagen(alien_img, width // 12 + mov , -(pato_altura) - mov_y_aliens, pato_altura, pato_ancho, (19, 4)))
                if i < 3:
                    baby_dragons.append(crear_imagen(baby_dragon_img, 150 + mov , - 50, pato_altura, pato_ancho, (3, 1)))
                mov += 110
                if i == 5: 
                    mov = 0
                    mov_y_aliens = 100
            ronda5 = True



        for alien in aliens:
            ventana.blit(alien["img"], alien["rect"])

        comportamiento_aliens(aliens, ((width, height)))

        for murcielago in murcielagos:
                ventana.blit(murcielago["img"], murcielago["rect"])


        for bala in balas_murcielagos:
            ventana.blit(bala["img"], bala["rect"])
            bala["rect"].y += bala["speed_y"]

        for fernet in fernets:
            fernet["rect"].top -= fernet["speed_y"]
            ventana.blit(fernet["img"], fernet["rect"])

        for dragon in baby_dragons:
            ventana.blit(dragon["img"], dragon["rect"])

        bala_rastreadora(bombas, pato, ((projectile_speed_x, projectile_speed_y)))

        if balas_murcielagos:
            for bala_murcielago in balas_murcielagos[:]:
                if escudo:
                    colision_proyectiles(score, bala_murcielago, explosion_azul_img, balas_murcielagos, pato_escudo, explosiones, ((- 25, -25)), vidas, lista_colisiones, False, ((35, 35)), None, True, explosion_sonido_laser)
                else:
                    colision_proyectiles(score, bala_murcielago, explosion_azul_img, balas_murcielagos, pato, explosiones, ((0, 0)), vidas, lista_colisiones, False, ((35, 35)), sonido_explosion = explosion_sonido_laser)


        for bomba in bombas[:]:
            if escudo:
                colision_proyectiles(score, bomba, explosion_img, bombas, pato_escudo, explosiones, ((- 25, - 25)), vidas, lista_colisiones, False, ((35, 35)), None, True, explosion_sonido)
            else:
                colision_proyectiles(score, bomba, explosion_img, bombas, pato, explosiones, ((- 5, - 5)), vidas, lista_colisiones, False, ((35, 35)), sonido_explosion = explosion_sonido)
            
            ventana.blit(bomba["img"], bomba["rect"])
            

        for baby_dragon in baby_dragons[:]:
            for fernet in fernets[:]:
                colision_proyectiles(score, baby_dragon, explosion_img, baby_dragons, fernet, explosiones, ((0, 0)), vidas, lista_colisiones, True, ((70, 70)), fernets, sonido_explosion = explosion_sonido)

        for murcielago in murcielagos[:]:
            for fernet in fernets[:]:
                colision_proyectiles(score, murcielago, explosion_img, murcielagos, fernet, explosiones, ((0, 0)), vidas, lista_colisiones, True, ((70, 70)), fernets, sonido_explosion = explosion_sonido)
        
        for alien in aliens[:]:
            for fernet in fernets[:]:
                colision_proyectiles(score, alien, explosion_img, aliens, fernet, explosiones, ((0, 0)), vidas, lista_colisiones, True, ((70, 70)), fernets, sonido_explosion = explosion_sonido)

        for alien in aliens[:]:
            colision_melee(score, alien, explosion_img, aliens, pato, escudo, explosiones, ((pato_ancho, pato_altura)), lista_colisiones, vidas, explosion_sonido)
        
        for murcielago in murcielagos[:]:
            colision_melee(score, murcielago, explosion_img, murcielagos, pato, escudo, explosiones, ((pato_ancho, pato_altura)), lista_colisiones, vidas, explosion_sonido)
        
        for baby_dragon in baby_dragons[:]:
            colision_melee(score, baby_dragon, explosion_img, baby_dragons, pato, escudo, explosiones, ((pato_ancho, pato_altura)), lista_colisiones, vidas, explosion_sonido)
        
        for explosion in explosiones:
            ventana.blit(explosion["img"], explosion["rect"])

        if murcielagos:
            comportamiento_murcielagos(murcielagos, ((width, height)), cooldown_movimientos_murcielagos)
            cooldown_movimientos_murcielagos[0] += ((FPS * 0.001))

            if (cooldown_disparo_enemigo[1]) >= ultimo_disparo_enemigo[1]:
                sonido_laser.play()

                for murcielago in murcielagos:
                        balas_murcielagos.append(crear_imagen(bala_murcielago_img, murcielago["rect"].midbottom[0],  murcielago["rect"].midbottom[1], pato_ancho // 2, pato_altura // 2, ((5, 10))))
                cooldown_disparo_enemigo[1] = 0
        else:
            cooldown_movimientos_murcielagos = [0]
            cooldown_disparo_enemigo[1] = 0

        if baby_dragons:
            cooldown_movimientos_dragones[0] += ((FPS * 0.001))
        else:
            cooldown_movimientos_dragones = [0]


        if lista_colisiones:
            for vuelta in range(len(lista_colisiones[:])):
                explosion_cooldown = 0
                explosiones_cooldown.append(explosion_cooldown)

            lista_colisiones = []

        if explosiones_cooldown:
            i = 0
            for vuelta in range(len(explosiones_cooldown[:])):
                explosiones_cooldown[i] += ((FPS * 0.001))
                
                if explosiones_cooldown[i] > 0.1:
                    explosiones.remove(explosiones[i])
                    explosiones_cooldown.remove(explosiones_cooldown[i])
                    i -= 1
                i += 1

        if vidas[0] <= 0:
            andando = False
            muerte_sonido.play()

        mostrar_texto(ventana, 30, f"Vidas: {vidas[0]}", (50, 20))
        mostrar_texto(ventana, 30, f"Ronda: {ronda}", (300, 20))
        mostrar_texto(ventana, 30, f"Score: {score[0]}", (500, 20))



        pygame.display.flip()



