import pygame
import random

# Dimensiones de la ventana
WIDTH = 600
HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Inicializar pygame
pygame.init()

# Crear la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Proyecto Final Progra 1")

# Fuente de texto
font = pygame.font.Font(None, 30)

def generate_matrix(n):
    matrix = []
    for _ in range(n):
        row = [random.randint(1, 11) for _ in range(n)]
        matrix.append(row)
    return matrix

def draw_board(matrix, revealed, selected_x, selected_y, player1, player2, score1, score2):
    screen.fill(WHITE)
    n = len(matrix)
    cell_size = WIDTH // n
    margin = 10

    # Dibujar nombres de los jugadores y su puntaje
    text_player1 = font.render(f"{player1}: {score1}", True, BLACK)
    text_player2 = font.render(f"{player2}: {score2}", True, BLACK)
    screen.blit(text_player1, (margin, margin))
    screen.blit(text_player2, (margin, margin + 30))

    for y in range(n):
        for x in range(n):
            rect = pygame.Rect(x * cell_size + margin, y * cell_size + margin, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, rect, 1)

            if revealed[y][x]:
                number = matrix[y][x]
                text_color = BLUE
                if x == selected_x and y == selected_y:
                    text_color = RED
                text = font.render(str(number), True, text_color)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

    pygame.display.flip()

def reveal_cells(matrix, revealed, x, y):
    n = len(matrix)

    for i in range(max(y - 1, 0), min(y + 2, n)):
        for j in range(max(x - 1, 0), min(x + 2, n)):
            revealed[i][j] = True

def calculate_sum(matrix, x, y):
    n = len(matrix)
    total_sum = 0

    for i in range(max(y - 1, 0), min(y + 2, n)):
        for j in range(max(x - 1, 0), min(x + 2, n)):
            total_sum += matrix[i][j]

    selected_number = matrix[y][x]
    total_sum -= selected_number
    total_sum *= selected_number

    return total_sum

import random

def play_game():
    # Pedir nombres de los jugadores
    player1 = input("Nombre del Jugador 1: ")
    player2 = input("Nombre del Jugador 2: ")

    # Pedir número de turnos
    num_turns = int(input("Número de turnos: "))

    # Pedir tamaño de la matriz
    n = int(input("Tamaño de la matriz (N x N): "))

    # Crear matriz y matriz de reveladas
    matrix = generate_matrix(n)
    revealed = [[False] * n for _ in range(n)]

    # Variables de puntuación
    score1 = 0
    score2 = 0

    for _ in range(num_turns):
        # Turno del Jugador 1
        selected_x = -1
        selected_y = -1
        draw_board(matrix, revealed, selected_x, selected_y, player1, player2, score1, score2)
        print(f"\nTurno de {player1}")
        x, y = play_turn(matrix, revealed)
        selected_x = x
        selected_y = y
        reveal_cells(matrix, revealed, x, y)
        
        
        # Lógica para validar la opción seleccionada y actualizar puntaje si es correcta
        
        # Turno del Jugador 2
        selected_x = -1
        selected_y = -1
        draw_board(matrix, revealed, selected_x, selected_y, player1, player2, score1, score2)
        print("1. [" +str(calculate_sum(matrix,x,y))+ "]")
        print(f"2. {random.sample(range(1, calculate_sum(matrix,x,y)),1)}")
        print(f"3. {random.sample(range(1, calculate_sum(matrix,x,y)),1)}")
        print(f"4. {random.sample(range(1, calculate_sum(matrix,x,y)),1)}")
        option = int(input("Selecciona una opción (1, 2 o 3): "))
        if option == calculate_sum(matrix,x,y):
            score1 +=3

        print(f"\nTurno de {player2}")
        x, y = play_turn(matrix, revealed)
        selected_x = x
        selected_y = y
        reveal_cells(matrix, revealed, x, y)
        
        selected_x = -1
        selected_y = -1
        draw_board(matrix, revealed, selected_x, selected_y, player1, player2, score1, score2)
        print("1. [" +str(calculate_sum(matrix,x,y))+ "]")
        print(f"2. {random.sample(range(1, calculate_sum(matrix,x,y)),1)}")
        print(f"3. {random.sample(range(1, calculate_sum(matrix,x,y)),1)}")
        print(f"4. {random.sample(range(1, calculate_sum(matrix,x,y)),1)}")
        option = int(input("Selecciona una opción (1, 2 o 3): "))
        if option == calculate_sum(matrix,x,y):
            score2 +=3
        # Lógica para validar la opción seleccionada y actualizar puntaje si es correcta

    # Mostrar resultado final
    print("\nFin del juego")
    print(f"Puntuación de {player1}: {score1}")
    print(f"Puntuación de {player2}: {score2}")

def play_turn(matrix, revealed):
    n = len(matrix)
    cell_size = WIDTH // n
    margin = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = (pos[0] - margin) // cell_size
                y = (pos[1] - margin) // cell_size

                if 0 <= x < n and 0 <= y < n and not revealed[y][x]:
                    return x, y

# Ejecutar el juego
play_game()
