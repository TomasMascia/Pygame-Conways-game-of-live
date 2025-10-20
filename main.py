import pygame # importamos biblioteca
import sys # nos interesa para poder manejar la consola
import numpy as np # se utiliza para trabajar matrices de manera facil

# con esto inicializamod el pygame
pygame.init()

#_____________________________________________________________________
# DEFINIMOS TODO TIPO DE VARIABLE GLOBAL PARA PODER UTILIZAR LUEGO 

WIDTH, HEIGHT = 801, 601 # dimensiones de la ventana/screen
CELL_SIZE = 20 # tamaño de las celdas/celulas


# colores que voy a utilizar
BLACK = (0, 0, 0)
GRID_COLOR = (40, 40, 40)
ALIVE_COLOR = (0, 255, 0) # es verde
DEAD_COLOR = BLACK

# columns
columns = WIDTH // CELL_SIZE
rows = HEIGHT // CELL_SIZE
#_____________________________________________________________________

# creamos una matriz de ceros (todas las celdas estan muertas)
grid = np.zeros((rows, columns))

# ahora creo la ventana/screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# esto lo que hace es ponerle un titulo a la ventana
pygame.display.set_caption("Conway's Game of Life - Tomi Mascia")

# creo un reloj para poder temporizar el juego
clock = pygame.time.Clock()

# definimos paused
paused = True

#_____________________________________________________________________
# Funcion para dibujar la cuadrilla 
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0,y), (WIDTH, y))
#_____________________________________________________________________

#_____________________________________________________________________
def draw_cells():
    for y in range(rows):
        for x in range(columns):
            if grid[y][x] == 1: # si la celda esta viva
                rect = pygame.Rect(x* CELL_SIZE, y* CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
                pygame.draw.rect(screen, ALIVE_COLOR, rect) 
#_____________________________________________________________________

#_____________________________________________________________________
def update_grid(grid):
    new_grid = np.copy(grid)
    for y in range(rows):
        for x in range(columns):
            total = np.sum(grid[max(0,y-1):min(rows, y+2), max(0, x-1): min(columns, x+2)]) - grid[y][x]

            if grid[y][x] == 1: 
                if total < 2 or total > 3:
                    new_grid[y][x] = 0
            else:
                if total == 3:
                    new_grid[y][x] = 1
    
    return new_grid
#_____________________________________________________________________

# creamos el buble principal para que se ejecute hasta el final
while True:
    # Manejamos los eventos que necesitemos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # cerramos pygame
            sys.exit() # cerramos el programa

        # movimiento de barra espaciadora
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    # movimiento del mouse
    if pygame.mouse.get_pressed()[0]: # boton izquierdo
        mx, my = pygame.mouse.get_pos() # coordenadas del mouse
        x = mx // CELL_SIZE
        y = my // CELL_SIZE
        grid[y][x] = 1 # se convierte en celula viva
    elif pygame.mouse.get_pressed()[2]: # boton derecho
        mx, my = pygame.mouse.get_pos() # coordenadas del mouse
        x = mx // CELL_SIZE
        y = my // CELL_SIZE
        grid[y][x] = 0 # se muere la celula

    # pintamos el fondo de negro
    screen.fill(BLACK)
    draw_grid()
    draw_cells()
    
    # se actualiza si no esta en pausa
    if not paused:
        grid = update_grid(grid)
    
    pygame.display.flip() # esto actualiza, y muestra lo que dibujamos en pantalla
    clock.tick(10) # limitamos a 60 fotogramas por segundo
