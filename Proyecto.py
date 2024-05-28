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

# Definir colores en RGB
negro = (0, 0, 0)
rojo = (255, 0, 0)
naranja = (255, 165, 0)
amarillo = (255, 255, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
indigo = (75, 0, 130)
violeta = (238, 130, 238)
blanco = (255, 255, 255)

# Clase para manejar el Píxel Art
class PixelArt:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.asciiart = [[9 for _ in range(columnas)] for _ in range(filas)]
        self.matriz = [[COLOR_FONDO for _ in range(columnas)] for _ in range(filas)]

    def dibujar(self, pantalla):
        #lee la matris asciiart y asigna los colores en la matriz normal
        for fila in range(self.filas):
            for columna in range(self.columnas):
                match self.asciiart[fila][columna]:
                    case 1:
                        self.matriz[fila][columna] = negro
                    case 2:
                        self.matriz[fila][columna] = rojo
                    case 3:
                        self.matriz[fila][columna] = naranja
                    case 4:
                        self.matriz[fila][columna] = amarillo
                    case 5:
                        self.matriz[fila][columna] = verde
                    case 6:
                        self.matriz[fila][columna] = azul
                    case 7:
                        self.matriz[fila][columna] = indigo
                    case 8:
                        self.matriz[fila][columna] = violeta
                    case 9:
                        self.matriz[fila][columna] = blanco
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
            if color == negro:
                self.asciiart[fila][columna] = 1
            elif color == rojo:
                self.asciiart[fila][columna] = 2
            elif color == naranja:
                self.asciiart[fila][columna] = 3
            elif color == amarillo:
                self.asciiart[fila][columna] = 4
            elif color == verde:
                self.asciiart[fila][columna] = 5
            elif color == azul:
                self.asciiart[fila][columna] = 6
            elif color == indigo:
                self.asciiart[fila][columna] = 7
            elif color == violeta:
                self.asciiart[fila][columna] = 8
            elif color == blanco:
                self.asciiart[fila][columna] = 9

    def borrar_todo(self):
        self.matriz = [[blanco for _ in range(self.columnas)] for _ in range(self.filas)]
        self.asciiart = [[9 for _ in range(columnas)] for _ in range(filas)]
    
    def rotar_izquierda(self):
        tamaño = len(pixel_art.asciiart)
        nueva_matriz = [[0] * tamaño for _ in range(tamaño)]
        for columna in range(columnas):
            for fila in range(filas):
                nueva_matriz[tamaño - 1 - fila][columna] = pixel_art.asciiart[columna][fila]
        pixel_art.asciiart = nueva_matriz
        pixel_art.dibujar(ventana)
    
    def rotar_derecha(self):
        matriz_aux = list(zip(*self.asciiart))
        self.asciiart = [list(fila)[::-1] for fila in matriz_aux]
        pixel_art.dibujar(ventana)


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
columnas = (ANCHO_VENTANA - 400) // TAMAÑO_PIXEL  # Deja espacio para los botones
pixel_art = PixelArt(filas, columnas)

# Definimos los botones
boton_color_negro = pygame.Rect(850, 50, 50, 50)
boton_color_rojo = pygame.Rect(910, 50, 50, 50)
boton_color_naranja = pygame.Rect(850, 120, 50, 50)
boton_color_amarillo = pygame.Rect(910, 120, 50, 50)
boton_color_verde = pygame.Rect(850, 190, 50, 50)
boton_color_azul = pygame.Rect(910, 190, 50, 50)
boton_color_indigo = pygame.Rect(850, 260, 50, 50)
boton_color_violeta = pygame.Rect(910, 260, 50, 50)
boton_color_blanco = pygame.Rect(850, 330, 50, 50)
boton_borrar = pygame.Rect(850, 400, 50, 50)
boton_borrar_todo = pygame.Rect(910, 400, 50, 50)
boton_rotar_izquierda = pygame.Rect(850, 470, 50, 50)
boton_rotar_derecha = pygame.Rect(910, 470, 50, 50)

# Cargamos imagenes
imagen_borrar = pygame.image.load("borrar_icono.png")
imagen_cargar = pygame.image.load("cargar_icono.png")
imagen_guardar = pygame.image.load("guardar_icono.png")
imagen_restablecer = pygame.image.load("restablecer_icono.png")
imagen_rotar_derecha = pygame.image.load("rotar_derecha_icono.png")
imagen_rotar_izquierda = pygame.image.load("rotar_izquierda_icono.png")


# Bucle principal del juego
corriendo = True
color_actual = negro
print((filas, columnas))
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Boton izquierdo del raton
                x, y = evento.pos
                if boton_color_negro.collidepoint(x, y):
                    color_actual = negro
                if boton_color_rojo.collidepoint(x, y):
                    color_actual = rojo
                if boton_color_naranja.collidepoint(x, y):
                    color_actual = naranja
                if boton_color_amarillo.collidepoint(x, y):
                    color_actual = amarillo
                if boton_color_verde.collidepoint(x, y):
                    color_actual = verde
                if boton_color_azul.collidepoint(x, y):
                    color_actual = azul
                if boton_color_indigo.collidepoint(x, y):
                    color_actual = indigo
                if boton_color_violeta.collidepoint(x, y):
                    color_actual = violeta
                if boton_color_blanco.collidepoint(x, y):
                    color_actual = blanco
                elif boton_borrar.collidepoint(x, y):
                    color_actual = blanco
                elif boton_borrar_todo.collidepoint(x, y):
                    pixel_art.borrar_todo()
                elif boton_rotar_izquierda.collidepoint(x, y):
                    pixel_art.rotar_izquierda()
                elif boton_rotar_derecha.collidepoint(x, y):
                    pixel_art.rotar_derecha()
                else:
                    if x < ANCHO_VENTANA - 200:  # Asegura que el clic esté dentro de la cuadrícula
                        pixel_art.cambiar_color_pixel(x, y, color_actual)

    # Limpiamos la ventana
    ventana.fill(COLOR_FONDO)

    # Dibujamos el arte de píxeles con la cuadrícula
    pixel_art.dibujar(ventana)

    # Dibujamos los botones
    dibujar_boton(ventana, boton_color_negro, negro, "")
    dibujar_boton(ventana, boton_color_rojo, rojo, "")
    dibujar_boton(ventana, boton_color_naranja, naranja, "")
    dibujar_boton(ventana, boton_color_amarillo, amarillo, "")
    dibujar_boton(ventana, boton_color_verde, verde, "")
    dibujar_boton(ventana, boton_color_azul, azul, "")
    dibujar_boton(ventana, boton_color_indigo, indigo, "")
    dibujar_boton(ventana, boton_color_violeta, violeta, "")
    dibujar_boton(ventana, boton_color_blanco, (240, 240, 240), "")

    dibujar_boton_con_boton(ventana, boton_borrar, COLOR_BOTON, imagen_borrar)
    dibujar_boton_con_boton(ventana, boton_borrar_todo, COLOR_BOTON, imagen_restablecer)
    dibujar_boton_con_boton(ventana, boton_rotar_izquierda, COLOR_BOTON, imagen_rotar_izquierda)
    dibujar_boton_con_boton(ventana, boton_rotar_derecha, COLOR_BOTON, imagen_rotar_derecha)

    # Actualizamos la pantalla
    pygame.display.flip()

# Salimos de Pygame
pygame.quit()
sys.exit()
