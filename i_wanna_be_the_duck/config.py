import pygame
from modulo_funciones import *
import random, os, json

##Variables
victoria = False
andando = False
escudo = False
explotando = False
explosion_cooldown = None
generacion_enemigos = True
ronda1 = False
ronda2 = False
ronda3 = False
ronda4 = False
ronda5 = False
ronda = 0
mas_vidas = False
musica = True
usar_mouse = False
reintento = False
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
vidas = [5]
score = [0]
score2 = [0]
cooldown_disparo_enemigo = [0, 0]
ultimo_disparo_enemigo = [3, 1]
#Archivos
directorio = os.getcwd()     
#Tiempo
timer = 0
cooldown_escudo = 0
cooldown_disparo = 0
ultimo_escudo = 2
ultimo_disparo = 0.5
disparo_enemigo = random.randint(3, 10)
FPS = 30
clock = pygame.time.Clock()
#Dimensiones pantalla
width = 600
height = 700
buttom_width = 150
#Dimensiones imagenes
pato_ancho = 70
pato_altura = 70
#Cargar imagenes
imagen_completa = os.path.join(directorio, r"assets\sunset-7790625_1280.png")
fondo = pygame.image.load(r"assets\fondo1.png")
fondo2 = pygame.image.load(r"assets\sunset-7790625_1280.png")
fondo_victoria = pygame.image.load(r"assets\fondo_victoria.jpg")
fondo_victoria = escalar_imagen(fondo_victoria, width, height)
salon_fama = pygame.image.load(imagen_completa)
salon_fama = escalar_imagen(salon_fama, width, height)
flecha_atras = crear_imagen(r"assets\flecha_atras.png", 0, 0, 100, 100, ((5,5)))
tesoro = crear_imagen(r"assets\tesoro.png", 150, 300, 150, 150, ((5,5)))

pato = crear_imagen("assets\pato_empresario.png", width // 2, height - 75, pato_ancho, pato_altura, (7, 7))
pato["rect"].midtop = (width//2, height - 100)
baby_dragon_img = (r"assets\baby_dragon_final.png")
fernet_img = (r"assets\MOLOTOV.png")
bomba_img = (r"assets\bomba.png")
bala_murcielago_img = (r"assets\bala_murcielagos.png")
pato_img = (r"assets\pato_empresario.png")
pato_escudo_img = (r"assets\pato_escudo.png")
explosion_img = (r"assets\explosion.png")
murcielago_img = (r"assets\murcielago_final.png")
explosion_azul_img = (r"assets\Explosion_blue_circle7.png")
alien_img = (r"assets\alien.png")
explosion = crear_imagen(explosion_img, -100, -100, pato_ancho // 2, pato_altura // 2, (5, 5))
## speeed
projectile_speed_x = 20
projectile_speed_y = 15
#Rectangulos
rect_iniciar = pygame.Rect(width // 2 - buttom_width // 2, height - 450, buttom_width, 50)
rect_opciones = pygame.Rect(width // 2 - buttom_width // 2, height - 350, buttom_width, 50)
rect_puntuacion = pygame.Rect(width // 2 - buttom_width // 2, height - 250, buttom_width, 50)
rect_salir = pygame.Rect(width // 2 - buttom_width // 2, height - 150, buttom_width, 50)
rect_reintentar = pygame.Rect(width // 2 - buttom_width // 2, height - 450, buttom_width, 50)
rect_menu = pygame.Rect(width // 2 - buttom_width // 2, height - 350, buttom_width, 50)
rect_musica = pygame.Rect(width // 2 - buttom_width // 2, height - 450, buttom_width, 50)
rect_sonido = pygame.Rect(width // 2 - buttom_width // 2, height - 350, buttom_width, 50)
rect_vidas_infinitas = pygame.Rect(width // 2 - buttom_width // 2, height - 250, buttom_width, 50)
rect_mouse = pygame.Rect(width // 2 - buttom_width // 2, height - 150, buttom_width, 50)
#Musica/sonidos
color_musica = Colores.VERDE
color_sonido = Colores.VERDE
color_vidas = Colores.ROJO
color_mouse = Colores.ROJO


explosion_sonido = pygame.mixer.Sound(r"sonidos\explosion.mp3")
muerte_sonido = pygame.mixer.Sound(r"sonidos\Sonido de campana meme (1).mp3")
sonido_victoria = pygame.mixer.Sound(r"sonidos\Final Fantasy VII - Victory Fanfare [HD].mp3")
pygame.mixer.music.load(r"sonidos\Mega Man 2 Medley - Super Smash Bros. Ultimate (1).mp3")
pygame.mixer.music.set_volume(0.3)
disparo_sonido = pygame.mixer.Sound(r"sonidos\cuack sonido de pato .mp3 link descripcion (1).mp3")
escudo_roto_sonido = pygame.mixer.Sound(r"sonidos\Shield Break (Nr. 1 - Fortnite Sound) - Sound Effect for editing.mp3")
escudo_sonido = pygame.mixer.Sound(r"sonidos\Electricity Sound Effect (mp3cut.net) (1).mp3")
explosion_sonido_laser = pygame.mixer.Sound(r"sonidos\Laser and explosion (with sound) (mp3cut.net).mp3")
sonido_laser = pygame.mixer.Sound(r"sonidos\Sonido de Blaster-Star Wars para notificaciones (mp3cut.net) (1).mp3")
explosion_sonido_laser.set_volume(0.1)
escudo_sonido.set_volume(0.1)
escudo_roto_sonido.set_volume(0.1)
disparo_sonido.set_volume(0.1)
sonido_laser.set_volume(0.1)
sonido_victoria.set_volume(0.1)
muerte_sonido.set_volume(0.1)
explosion_sonido.set_volume(0.1)






