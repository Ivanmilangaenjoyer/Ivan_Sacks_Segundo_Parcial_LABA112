import pygame
from modulo_funciones import *
import sys, time
from diferentes_colores import *
import os
import json

scores = {"ivan": 5 ,"Juan": 7, "Pablo": 200}


    
directorio = os.getcwd()     
path_completo = os.path.join(directorio, "Score.json")   

with open(path_completo, "w") as file:   
    json.dump(scores, file)



with open(path_completo, "r") as file:   
        archivo = json.load(file)



print("Podio     Puntuaciones")
for clave, valor in archivo.items():
    print(f"{clave}              {valor:2d}")

















# directorio = os.getcwd()     
# path_completo = os.path.join(directorio, "Score.txt")   

# with open(path_completo, "w") as file:   
#     for score in scores:
#         str(score)
#         file.write(f"{score} \n")



# with open(path_completo, "r") as file:   
#         archivo = file.read()
#         print(archivo)


































# height = 500
# width = 500
# ventana = pygame.display.set_mode((width, height))
# buttom_width = 150

# rect_iniciar = pygame.Rect(width // 2 - buttom_width // 2, height - 450, buttom_width, 50)
# rect_opciones = pygame.Rect(width // 2 - buttom_width // 2, height - 350, buttom_width, 50)
# rect_puntuacion = pygame.Rect(width // 2 - buttom_width // 2, height - 250, buttom_width, 50)
# rect_salir = pygame.Rect(width // 2 - buttom_width // 2, height - 150, buttom_width, 50)

# pygame.init()

# FPS = 30
# reloj = pygame.time.Clock()
# while True:
#         reloj.tick(FPS)

#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             Keys = pygame.key.get_pressed()

#             if Keys[pygame.K_BACKSPACE]:
#                 pygame.quit()
#                 sys.exit()

#             mouse_keys = pygame.mouse.get_pressed()
#             if mouse_keys[0]: 
#                 mouse = evento.pos

#                 if rect_iniciar.collidepoint(mouse[0], mouse[1]):
#                     print("Inicio")
#                 elif rect_opciones.collidepoint(mouse[0], mouse[1]):
#                     print("Opciones")
#                 elif rect_puntuacion.collidepoint(mouse[0], mouse[1]):
#                     print("Puntuación")                               
#                 elif rect_salir.collidepoint(mouse[0], mouse[1]):
#                     pygame.quit()
#                     sys.exit()

#         ventana.fill(Colores.NEGRO)

#         pygame.draw.rect(ventana, Colores.VERDE, rect_iniciar)
#         pygame.draw.rect(ventana, Colores.VERDE, rect_opciones)
#         pygame.draw.rect(ventana, Colores.VERDE, rect_puntuacion)
#         pygame.draw.rect(ventana, Colores.VERDE, rect_salir)

#         texto_rectangulo(ventana, "Comenzar", rect_iniciar, ((Colores.NEGRO, Colores.BLANCO)), 20)
#         texto_rectangulo(ventana, "Opciones", rect_opciones, ((Colores.NEGRO, Colores.BLANCO)), 20)
#         texto_rectangulo(ventana, "Puntuaciones", rect_puntuacion, ((Colores.NEGRO, Colores.BLANCO)), 14)
#         texto_rectangulo(ventana, "Salir", rect_salir, ((Colores.NEGRO, Colores.BLANCO)), 20)




#         pygame.display.flip()


