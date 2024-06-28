import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Crear la ventana
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Rectángulo con Máscara")

# Crear una superficie para el rectángulo
rect_surface = pygame.Surface((200, 100))
rect_surface.fill(WHITE)

# Crear una máscara
mask_surface = pygame.Surface((200, 100), pygame.SRCALPHA)
pygame.draw.rect(mask_surface, BLACK, (0, 0, 200, 100))

# Aplicar la máscara al rectángulo
rect_surface.blit(mask_surface, (0, 0), special_flags = pygame.BLEND_RGBA_MULT)

# Posición del rectángulo en la ventana
rect_x = 300
rect_y = 250

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el rectángulo en la ventana
    window.fill(WHITE)
    window.blit(rect_surface, (rect_x, rect_y))

    # Actualizar la pantalla
    pygame.display.flip()
