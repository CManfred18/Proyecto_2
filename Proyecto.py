import pygame
import sys
import os

# Inicializamos Pygame
pygame.init()

# Definimos algunas constantes
ANCHO_VENTANA = 800
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
        
    def rotar_derecha(self):
        self.matriz = [list(filas) for filas in zip(*self.matriz[::-1])]
        self.filas, self.columnas = self.columnas, self.filas
        
    def rotar_izquierda(self):
        self.matriz = [list(filas) for filas in zip(*self.matriz)][::-1]
        self.filas, self.columnas = self.columnas, self.filas
        
    def reflejo_horizontal(self):
        self.matriz = [fila[::-1] for fila in self.matriz]
    
    def reflejo_vertical(self):
        self.matriz = self.matriz[::-1]
        
    def convertir_a_ascii_art(self):
        ascii_art = ""
        for fila in range(self.columnas):
            for columna in range(self.filas):
                color = self.matriz[fila][columna]
                if color == (0, 0, 0):
                    ascii_art += "."
                elif color == (25, 111, 61):
                    ascii_art += ":"
                elif color == (192, 57, 43):
                    ascii_art += "-"
                elif color == (247, 220, 111):
                    ascii_art += "="
                elif color == (41, 128, 185):
                    ascii_art += "¡"
                elif color == (125, 60, 152):
                    ascii_art += "&"
                elif color == (230, 126, 34):
                    ascii_art += "$"
                elif color == (86, 101, 115):
                    ascii_art += "%"
                elif color == (174, 214, 241 ):
                    ascii_art += "@"
                elif color == (217, 136, 128):
                    ascii_art += "?"
                else:
                    ascii_art += " "
            ascii_art += "\n"
        return ascii_art
    
    def mostrar_matriz_numerica(self):
        matriz_numerica = ""
        for fila in range(self.columnas):
            for columna in range(self.filas):
                color = self.matriz[fila][columna]
                if color == (0, 0, 0):
                    matriz_numerica += "0"
                elif color == (25, 111, 61):
                    matriz_numerica += "1"
                elif color == (192, 57, 43):
                    matriz_numerica += "2"
                elif color == (247, 220, 111):
                    matriz_numerica += "3"
                elif color == (41, 128, 185):
                    matriz_numerica += "4"
                elif color == (125, 60, 152):
                    matriz_numerica += "5"
                elif color == (230, 126, 34):
                    matriz_numerica += "6"
                elif color == (86, 101, 115):
                    matriz_numerica += "7"
                elif color == (174, 214, 241 ):
                    matriz_numerica += "8"
                elif color == (217, 136, 128):
                    matriz_numerica += "9"
                else:
                    matriz_numerica += "_"
            matriz_numerica += "\n"
        print(matriz_numerica)

    def negativo(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                color = self.matriz[fila][columna]
                if color == (0, 0, 0):  # 0
                    self.matriz[fila][columna] = (255, 255, 255)  # Color blanco
                elif color == (25, 111, 61):  # 1
                    self.matriz[fila][columna] = (217, 136, 128)  # 9
                elif color == (192, 57, 43):  # 2
                    self.matriz[fila][columna] = (174, 214, 241)  # 8
                elif color == (247, 220, 111):  # 3
                    self.matriz[fila][columna] = (86, 101, 115)  # 7
                elif color == (41, 128, 185):  # 4
                    self.matriz[fila][columna] = (230, 126, 34)  # 6
                elif color == (125, 60, 152):  # 5
                    self.matriz[fila][columna] = (125, 60, 152)  # 5 
                elif color == (230, 126, 34):  # 6
                    self.matriz[fila][columna] = (41, 128, 185)  # 4
                elif color == (86, 101, 115):  # 7
                    self.matriz[fila][columna] = (247, 220, 111)  # 3
                elif color == (174, 214, 241):  # 8
                    self.matriz[fila][columna] = (192, 57, 43)  # 2
                elif color == (217, 136, 128):  # 9
                    self.matriz[fila][columna] = (25, 111, 61)  # 1
                elif color == (255, 255, 255):  # Blanco
                    self.matriz[fila][columna] = (0, 0, 0)  # 0
    
    def alto_contraste(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                color = self.matriz[fila][columna]
                if color in [(0, 0, 0), (25, 111, 61), (192, 57, 43), (247, 220, 111), (41, 128, 185)]:  # Colores de 0 a 4
                    self.matriz[fila][columna] = (0, 0, 0)  # 0
                elif color in [(125, 60, 152), (230, 126, 34), (86, 101, 115), (174, 214, 241), (217, 136, 128)]:  # Colores de 5 a 9
                    self.matriz[fila][columna] = (217, 136, 128)  # 9
                    
    def guardar_matriz(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            for fila in self.matriz:
                for color in fila:
                    if color == (0, 0, 0):
                        archivo.write("0")
                    elif color == (25, 111, 61):
                        archivo.write("1")
                    elif color == (192, 57, 43):
                        archivo.write("2")
                    elif color == (247, 220, 111):
                        archivo.write("3")
                    elif color == (41, 128, 185):
                        archivo.write("4")
                    elif color == (125, 60, 152):
                        archivo.write("5")
                    elif color == (230, 126, 34):
                        archivo.write("6")
                    elif color == (86, 101, 115):
                        archivo.write("7")
                    elif color == (174, 214, 241):
                        archivo.write("8")
                    elif color == (217, 136, 128):
                        archivo.write("9")
                    else:
                        archivo.write("_")
                archivo.write("\n")
                
    def cargar_matriz(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            for fila, linea in enumerate(archivo):
                for columna, caracter in enumerate(linea.strip()):
                    if caracter == "0":
                        self.matriz[fila][columna] = (0, 0, 0)
                    elif caracter == "1":
                        self.matriz[fila][columna] = (25, 111, 61)
                    elif caracter == "2":
                        self.matriz[fila][columna] = (192, 57, 43)
                    elif caracter == "3":
                        self.matriz[fila][columna] = (247, 220, 111)
                    elif caracter == "4":
                        self.matriz[fila][columna] = (41, 128, 185)
                    elif caracter == "5":
                        self.matriz[fila][columna] = (125, 60, 152)
                    elif caracter == "6":
                        self.matriz[fila][columna] = (230, 126, 34)
                    elif caracter == "7":
                        self.matriz[fila][columna] = (86, 101, 115)
                    elif caracter == "8":
                        self.matriz[fila][columna] = (174, 214, 241)
                    elif caracter == "9":
                        self.matriz[fila][columna] = (217, 136, 128)
                    else:
                        self.matriz[fila][columna] = COLOR_FONDO
                        
    def entrada_texto(self, pantalla, mensaje):
        fuente = pygame.font.Font(None, 24)
        input_box = pygame.Rect(300, 268, 140, 32)
        color_inactivo = pygame.Color(217, 136, 128)
        color_activo = pygame.Color(169, 223, 191)
        color = color_inactivo
        activo = False
        texto = ''
        hecho = False

        while not hecho:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(evento.pos):
                        activo = not activo
                    else:
                        activo = False
                    color = color_activo if activo else color_inactivo
                elif evento.type == pygame.KEYDOWN:
                    if activo:
                        if evento.key == pygame.K_RETURN:
                            hecho = True
                        elif evento.key == pygame.K_BACKSPACE:
                            texto = texto[:-1]
                        else:
                            texto += evento.unicode

            pantalla.fill(COLOR_FONDO)
            txt_superficie = fuente.render(mensaje, True, color)
            pantalla.blit(txt_superficie, (input_box.x, input_box.y-20))
            nombre = fuente.render(texto, True, color)
            pantalla.blit(nombre, (input_box.x+6, input_box.y+8))
            pygame.draw.rect(pantalla, color, input_box, 2)
            pygame.display.flip()

        return texto

# Función para dibujar botones
def dibujar_boton(pantalla, rect, color, texto):
    pygame.draw.rect(pantalla, color, rect, 0, 10)
    fuente = pygame.font.Font(None, 24)
    texto_renderizado = fuente.render(texto, True, COLOR_TEXTO)
    pantalla.blit(texto_renderizado, (rect.x + 10, rect.y + 10))
    
def dibujar_boton_con_imagen(pantalla, rect, color, imagen):
    pygame.draw.rect(pantalla, color, rect, 0, 10)
    pantalla.blit(imagen, (rect.x, rect.y))

# Inicializamos la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Editor de Pixel Art')

# Creamos una instancia de PixelArt
filas = ALTO_VENTANA // TAMAÑO_PIXEL
columnas = (ANCHO_VENTANA - 200) // TAMAÑO_PIXEL  # Deja espacio para los botones
pixel_art = PixelArt(filas, columnas)

# Definimos los botones
boton_color_negro = pygame.Rect(610, 10, 50, 50)
boton_color_verde = pygame.Rect(610, 70, 50, 50)
boton_color_rojo = pygame.Rect(610, 130, 50, 50)
boton_color_amarillo = pygame.Rect(610, 190, 50, 50)
boton_color_azul = pygame.Rect(610, 250, 50, 50)
boton_color_morado = pygame.Rect(610, 310, 50, 50)
boton_color_naranja = pygame.Rect(610, 370, 50, 50)
boton_color_gris = pygame.Rect(610, 430, 50, 50)
boton_color_celeste = pygame.Rect(610, 490, 50, 50)
boton_color_rosa = pygame.Rect(610, 550, 50, 50)



boton_borrar = pygame.Rect(670, 10, 50, 50)
boton_borrar_todo = pygame.Rect(670, 70, 50, 50)
boton_rotar_derecha = pygame.Rect(670, 130, 50, 50)
boton_rotar_izquierda = pygame.Rect(670, 190, 50, 50)
boton_reflejo_horizontal = pygame.Rect(670, 250, 50, 50)
boton_reflejo_vertical = pygame.Rect(670, 310, 50, 50)
boton_mostrar_matriz = pygame.Rect(670, 370, 50, 50)
boton_negativo = pygame.Rect(670, 430, 50, 50)
boton_alto_contraste = pygame.Rect(670, 490, 50, 50)
boton_guardar = pygame.Rect(670, 550, 50, 50)
boton_cargar = pygame.Rect(730, 10, 50, 50)


# Cargamos imagenes
imagen_borrar = pygame.image.load("Imagenes/Borrar_icono.png")
imagen_restablecer = pygame.image.load("Imagenes/Restablecer_icono.png")
imagen_rotar_derecha = pygame.image.load("Imagenes/Rotar_icono_derecha.png")
imagen_rotar_izquierda = pygame.image.load("Imagenes/Rotar_icono_izquierda.png")
imagen_reflejo_horizontal = pygame.image.load("Imagenes/Reflejo_icono_horizontal.png")
imagen_reflejo_vertical = pygame.image.load("Imagenes/Reflejo_icono_vertical.png")
imagen_negativo = pygame.image.load("Imagenes/Negativo_icono.png")
imagen_alto_contraste = pygame.image.load("Imagenes/Contraste_icono.png")
imagen_matriz = pygame.image.load("Imagenes/Matriz_icono.png")
imagen_guardar = pygame.image.load("Imagenes/Guardar_icono.png")
imagen_cargar = pygame.image.load("Imagenes/Cargar_icono.png")

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
                elif boton_rotar_derecha.collidepoint(x, y):
                    pixel_art.rotar_derecha()
                elif boton_rotar_izquierda.collidepoint(x, y):
                    pixel_art.rotar_izquierda()
                elif boton_reflejo_horizontal.collidepoint(x, y):
                    pixel_art.reflejo_horizontal()
                elif boton_reflejo_vertical.collidepoint(x, y):
                    pixel_art.reflejo_vertical()
                elif boton_mostrar_matriz.collidepoint(x, y):
                    pixel_art.mostrar_matriz_numerica()
                elif boton_negativo.collidepoint(x, y):
                    pixel_art.negativo()
                elif boton_alto_contraste.collidepoint(x, y):
                    pixel_art.alto_contraste()
                elif boton_guardar.collidepoint(x, y):
                    nombre_archivo = pixel_art.entrada_texto(ventana, "Nombre del archivo: ")
                    pixel_art.guardar_matriz(nombre_archivo + ".txt")
                elif boton_cargar.collidepoint(x, y):
                    nombre_archivo = pixel_art.entrada_texto(ventana, "Nombre del archivo: ")
                    if os.path.exists(nombre_archivo + ".txt"):
                        pixel_art.cargar_matriz(nombre_archivo + ".txt")
                    else:
                        print(f"El archivo {nombre_archivo}.txt no existe.")
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
    dibujar_boton_con_imagen(ventana, boton_borrar, COLOR_BOTON, imagen_borrar)
    dibujar_boton_con_imagen(ventana, boton_borrar_todo, COLOR_BOTON, imagen_restablecer)
    dibujar_boton_con_imagen(ventana, boton_rotar_derecha, COLOR_BOTON, imagen_rotar_derecha)
    dibujar_boton_con_imagen(ventana, boton_rotar_izquierda, COLOR_BOTON, imagen_rotar_izquierda)
    dibujar_boton_con_imagen(ventana, boton_reflejo_horizontal, COLOR_BOTON, imagen_reflejo_horizontal)
    dibujar_boton_con_imagen(ventana, boton_reflejo_vertical, COLOR_BOTON, imagen_reflejo_vertical)
    dibujar_boton_con_imagen(ventana, boton_mostrar_matriz, COLOR_BOTON, imagen_matriz)
    dibujar_boton_con_imagen(ventana, boton_negativo, COLOR_BOTON, imagen_negativo)
    dibujar_boton_con_imagen(ventana, boton_alto_contraste, COLOR_BOTON, imagen_alto_contraste) 
    dibujar_boton_con_imagen(ventana, boton_guardar, COLOR_BOTON, imagen_guardar)
    dibujar_boton_con_imagen(ventana, boton_cargar, COLOR_BOTON, imagen_cargar)

    # Actualizamos la pantalla
    pygame.display.flip()

ascii_art = pixel_art.convertir_a_ascii_art()

# Imprimir en la consola
print(ascii_art)

# Salimos de Pygame
pygame.quit()
sys.exit()
