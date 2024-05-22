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
            
    def borrar_todo(self):
        self.matriz = [[COLOR_FONDO for _ in range(self.columnas)] for _ in range(self.filas)]


# Función para dibujar botones
def dibujar_boton(pantalla, rect, color, texto):
    pygame.draw.rect(pantalla, color, rect)
    fuente = pygame.font.Font(None, 24)
    texto_renderizado = fuente.render(texto, True, COLOR_TEXTO)
    pantalla.blit(texto_renderizado, (rect.x + 10, rect.y + 10))
    
def dibujar_boton_con_boton(pantalla, rect, color, imagen):
    pygame.draw.rect(pantalla, color, rect)
    pantalla.blit(imagen, (rect.x, rect.y))

# Inicializamos la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Editor de Pixel Art')

# Creamos una instancia de PixelArt
filas = ALTO_VENTANA // TAMAÑO_PIXEL
columnas = (ANCHO_VENTANA - 200) // TAMAÑO_PIXEL  # Deja espacio para los botones
pixel_art = PixelArt(filas, columnas)

# Definimos los botones
boton_color_negro = pygame.Rect(850, 50, 50, 50)
boton_color_verde = pygame.Rect(910, 50, 50, 50)
boton_color_rojo = pygame.Rect(850, 120, 50, 50)
boton_color_amarillo = pygame.Rect(910, 120, 50, 50)
boton_color_azul = pygame.Rect(850, 190, 50, 50)
boton_color_morado = pygame.Rect(910, 190, 50, 50)
boton_color_naranja = pygame.Rect(850, 260, 50, 50)
boton_color_gris = pygame.Rect(910, 260, 50, 50)
boton_color_celeste = pygame.Rect(850, 330, 50, 50)
boton_color_rosa = pygame.Rect(910, 330, 50, 50)
boton_borrar = pygame.Rect(850, 400, 50, 50)
boton_borrar_todo = pygame.Rect(850, 470, 50, 50)

# Cargamos imagenes
imagen_borrar = pygame.image.load("Imagenes/Borrar_icono.png")
imagen_cargar = pygame.image.load("Imagenes/Cargar_icono.png")
imagen_guardar = pygame.image.load("Imagenes/Guardar_icono.png")
imagen_restablecer = pygame.image.load("Imagenes/Restablecer_icono.png")
imagen_rotar_derecha = pygame.image.load("Imagenes/Rotar_icono_derecha.png")
imagen_rotar_izquierda = pygame.image.load("Imagenes/Rotar_icono_izquierda.png")


# Bucle principal del juego
corriendo = True
color_actual = (0, 0, 0)

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Boton izquierdo del raton
                x, y = evento.pos
                if boton_color_negro.collidepoint(x, y):
                    color_actual = (0, 0, 0)
                elif boton_color_verde.collidepoint(x, y):
                    color_actual = (25, 111, 61)
                elif boton_color_rojo.collidepoint(x, y):
                    color_actual = (192, 57, 43)
                elif boton_color_amarillo.collidepoint(x, y):
                    color_actual = (247, 220, 111)
                elif boton_color_azul.collidepoint(x, y):
                    color_actual = (41, 128, 185)
                elif boton_color_morado.collidepoint(x, y):
                    color_actual = (125, 60, 152)
                elif boton_color_naranja.collidepoint(x, y):
                    color_actual = (230, 126, 34)
                elif boton_color_gris.collidepoint(x, y):
                    color_actual = (86, 101, 115)
                elif boton_color_rosa.collidepoint(x, y):
                    color_actual = (217, 136, 128)
                elif boton_color_celeste.collidepoint(x, y):
                    color_actual = (174, 214, 241 )
                elif boton_borrar.collidepoint(x, y):
                    color_actual = (255, 255, 255)
                elif boton_borrar_todo.collidepoint(x, y):
                    pixel_art.borrar_todo()
                else:
                    if x < ANCHO_VENTANA - 200:  # Asegura que el clic esté dentro de la cuadrícula
                        pixel_art.cambiar_color_pixel(x, y, color_actual)

    # Limpiamos la ventana
    ventana.fill(COLOR_FONDO)

    # Dibujamos el arte de píxeles con la cuadrícula
    pixel_art.dibujar(ventana)

    # Dibujamos los botones
    dibujar_boton(ventana, boton_color_negro, (0, 0, 0), "")
    dibujar_boton(ventana, boton_color_verde, (25, 111, 61), "")
    dibujar_boton(ventana, boton_color_rojo, (192, 57, 43), "")
    dibujar_boton(ventana, boton_color_amarillo, (247, 220, 111), "")
    dibujar_boton(ventana, boton_color_azul, (41, 128, 185), "")
    dibujar_boton(ventana, boton_color_morado, (125, 60, 152), "")
    dibujar_boton(ventana, boton_color_naranja, (230, 126, 34), "")
    dibujar_boton(ventana, boton_color_gris, (86, 101, 115), "")
    dibujar_boton(ventana, boton_color_rosa, (217, 136, 128), "")
    dibujar_boton(ventana, boton_color_celeste, (174, 214, 241 ), "")
    dibujar_boton_con_boton(ventana, boton_borrar, COLOR_BOTON, imagen_borrar)
    dibujar_boton_con_boton(ventana, boton_borrar_todo, COLOR_BOTON, imagen_restablecer)

    # Actualizamos la pantalla
    pygame.display.flip()

# Salimos de Pygame
pygame.quit()
sys.exit()
