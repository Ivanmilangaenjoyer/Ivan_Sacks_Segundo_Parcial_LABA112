from config import *

def obtener_fondo():
    imagen = tile
    _, _, width, height = imagen.get_rect()
    tiles = []

    for i in range(anchura // width + 1):
        for j in range(altura // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, imagen

def draw(pantalla, bg, bg_image):
    for tile in bg:
        pantalla.blit(bg_image, tile)






