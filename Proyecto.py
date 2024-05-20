import pygame
import sys

# Inicializamos Pygame
pygame.init()

# Definimos algunas constantes
ANCHO_VENTANA = 1000
ALTO_VENTANA = 600
TAMAÑO_PIXEL = 20
COLOR_FONDO = (255, 255, 255)
COLOR_CUADRICULA = (200, 200, 200)
COLOR_BOTON = (180, 180, 180)
COLOR_TEXTO = (0, 0, 0)
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)
COLOR_ROJO = (192, 57, 43)
COLOR_AMARILLO = (247, 220, 111)
COLOR_AZUL = (41, 128, 185)

# Clase para manejar el Píxel Art
class PixelArt:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[COLOR_FONDO for _ in range(columnas)] for _ in range(filas)]

    def dibujar(self, pantalla):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                color = self.matriz[fila][columna]
                pygame.draw.rect(pantalla, color, (columna * TAMAÑO_PIXEL, fila * TAMAÑO_PIXEL, TAMAÑO_PIXEL, TAMAÑO_PIXEL))
                pygame.draw.rect(pantalla, COLOR_CUADRICULA, (columna * TAMAÑO_PIXEL, fila * TAMAÑO_PIXEL, TAMAÑO_PIXEL, TAMAÑO_PIXEL), 1)

    def cambiar_color_pixel(self, x, y, color):
        columna = x // TAMAÑO_PIXEL
        fila = y // TAMAÑO_PIXEL
        if 0 <= columna < self.columnas and 0 <= fila < self.filas:
            self.matriz[fila][columna] = color

# Función para dibujar botones
def dibujar_boton(pantalla, rect, color, texto):
    pygame.draw.rect(pantalla, color, rect)
    fuente = pygame.font.Font(None, 20)
    texto_renderizado = fuente.render(texto, True, COLOR_TEXTO)
    pantalla.blit(texto_renderizado, (rect.x + 10, rect.y + 10))

# Inicializamos la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Editor de Pixel Art')

# Creamos una instancia de PixelArt
filas = ALTO_VENTANA // TAMAÑO_PIXEL
columnas = (ANCHO_VENTANA - 150) // TAMAÑO_PIXEL  # Deja espacio para los botones
pixel_art = PixelArt(filas, columnas)

# Definimos los botones
boton_color_negro = pygame.Rect(850, 50, 110, 50)
boton_color_blanco = pygame.Rect(850, 120, 110, 50)
boton_color_rojo = pygame.Rect(850, 190, 110, 50)
boton_color_amarillo = pygame.Rect(850, 260, 110, 50)
boton_color_azul = pygame.Rect(850, 330, 110, 50)

# Bucle principal del juego
corriendo = True
color_actual = COLOR_NEGRO

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Boton izquierdo del raton
                x, y = evento.pos
                if boton_color_negro.collidepoint(x, y):
                    color_actual = COLOR_NEGRO
                elif boton_color_blanco.collidepoint(x, y):
                    color_actual = COLOR_BLANCO
                elif boton_color_rojo.collidepoint(x, y):
                    color_actual = COLOR_ROJO
                elif boton_color_amarillo.collidepoint(x, y):
                    color_actual = COLOR_AMARILLO
                elif boton_color_azul.collidepoint(x, y):
                    color_actual = COLOR_AZUL
                else:
                    if x < ANCHO_VENTANA - 200:  # Asegura que el clic esté dentro de la cuadrícula
                        pixel_art.cambiar_color_pixel(x, y, color_actual)

    # Limpiamos la ventana
    ventana.fill(COLOR_FONDO)

    # Dibujamos el arte de píxeles con la cuadrícula
    pixel_art.dibujar(ventana)

    # Dibujamos los botones
    dibujar_boton(ventana, boton_color_negro, COLOR_BOTON, "Color Negro")
    dibujar_boton(ventana, boton_color_blanco, COLOR_BOTON, "Color Blanco")
    dibujar_boton(ventana, boton_color_rojo, COLOR_BOTON, "Color Rojo")
    dibujar_boton(ventana, boton_color_amarillo, COLOR_BOTON, "Color Amarillo")
    dibujar_boton(ventana, boton_color_azul, COLOR_BOTON, "Color azul")


    # Actualizamos la pantalla
    pygame.display.flip()

# Salimos de Pygame
pygame.quit()
sys.exit()
