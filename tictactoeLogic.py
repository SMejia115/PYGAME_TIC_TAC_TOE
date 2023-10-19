import pygame
import sys
from button import Button



# Constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = SCREEN_WIDTH // BOARD_COLS
BOARD_SIZE = SCREEN_WIDTH - LINE_WIDTH

# Colores
BG_COLOR = (173, 216, 230)  # Light Blue
LINE_COLOR = (255, 255, 255)  # Black
PLAYER1_COLOR = (255, 255, 255)  # Red-Orange
PLAYER2_COLOR = (255, 255, 255)  # Navy Blue

RED = (255, 0, 0)

# Inicialización de Pygame
font_path = "C:/Windows/Fonts/Arial.ttf"
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.Font(font_path, 55)

# Inicialización del tablero
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

current_player = "X"

def draw_board():
    background_image = pygame.image.load("./images/tic-tac-toe-background.jpg")
    screen.blit(background_image, (0,0))
    for i in range(1, BOARD_ROWS):
        pygame.draw.rect(screen, LINE_COLOR, (20, i * SQUARE_SIZE - LINE_WIDTH / 2, (BOARD_SIZE-20), LINE_WIDTH))
        pygame.draw.rect(screen, LINE_COLOR, (i * SQUARE_SIZE - LINE_WIDTH / 2, 20, LINE_WIDTH, (BOARD_SIZE-20)))

def draw_symbols():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "X":
                x_pos = col * SQUARE_SIZE + SQUARE_SIZE // 4
                y_pos = row * SQUARE_SIZE + SQUARE_SIZE // 4
                pygame.draw.line(screen, PLAYER1_COLOR, (x_pos, y_pos), (x_pos + SQUARE_SIZE // 2, y_pos + SQUARE_SIZE // 2), LINE_WIDTH)
                pygame.draw.line(screen, PLAYER1_COLOR, (x_pos, y_pos + SQUARE_SIZE // 2), (x_pos + SQUARE_SIZE // 2, y_pos), LINE_WIDTH)
            elif board[row][col] == "O":
                x_pos = col * SQUARE_SIZE + SQUARE_SIZE // 4
                y_pos = row * SQUARE_SIZE + SQUARE_SIZE // 4
                pygame.draw.circle(screen, PLAYER2_COLOR, (x_pos + SQUARE_SIZE // 4, y_pos + SQUARE_SIZE // 4), SQUARE_SIZE // 4, LINE_WIDTH)


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def check_win_or_draw(board):
    # Verificar filas y columnas
    for i in range(BOARD_ROWS):
        if all(cell == "X" for cell in board[i]) or all(cell == "O" for cell in board[i]):
            return True
        if all(board[row][i] == "X" for row in range(BOARD_ROWS)) or all(board[row][i] == "O" for row in range(BOARD_ROWS)):
            return True

    # Verificar diagonales
    if all(board[i][i] == "X" for i in range(BOARD_ROWS)) or all(board[i][BOARD_COLS - 1 - i] == "X" for i in range(BOARD_ROWS)):
        return True
    if all(board[i][i] == "O" for i in range(BOARD_ROWS)) or all(board[i][BOARD_COLS - 1 - i] == "O" for i in range(BOARD_ROWS)):
        return True

    # Verificar empate
    if all(cell != "" for row in board for cell in row):
        return "Empate"  # Empate

    return False


# Bucle principal del juego

def run_tic_tac_toe():
  global current_player
  restart_button = Button(225, 400, 150, 50, pygame.image.load("./images/buttons/resetButton2.png"), pygame.image.load("./images/buttons/resetButton1.png"), run_tic_tac_toe)
  exit_button = Button(225, 400, 150, 50, pygame.image.load("./images/buttons/exitButton2.png"), pygame.image.load("./images/buttons/exitButton1.png"), lambda: print("Exit button clicked"))
  buttons = [restart_button, exit_button]
  game_over = False
  while not game_over:

    winner_text = ""  # Inicializamos winner_text como cadena vacía

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            if board[clicked_row][clicked_col] == "":
                board[clicked_row][clicked_col] = current_player
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"

    draw_board()
    draw_symbols()




    if check_result := check_win_or_draw(board):
        if check_result == "Empate":
            winner_text = font.render("Empate!", True, RED)
            screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 2 - winner_text.get_height() // 2))
            game_over = True
        else:
            if current_player == "X":
                winner_text = font.render("Jugador O gana!", True, RED)
                screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 2 - winner_text.get_height() // 2))
                exit_button.draw(screen)
                game_over = True
            else:
                winner_text = font.render("Jugador X gana!", True, RED)
                screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 2 - winner_text.get_height() // 2))
                exit_button.draw(screen)
                game_over = True

    pygame.display.flip()
