import pygame
import sys
import random

# === Initialisation de pygame ===
pygame.init()

# === Constantes ===
WIDTH, HEIGHT = 1000, 1000
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS
LINE_WIDTH = 15
# ==================================================
# === Couleurs ===
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
WHITE = (255, 255, 255)

# === Fenêtre ===
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# === Plateau ===
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# === Images ===
circle_img = pygame.image.load("emogieee.png").convert_alpha()
cross_img = pygame.image.load("singe.png").convert_alpha()

circle_img = pygame.transform.scale(
    circle_img,
    (SQUARE_SIZE - 40, SQUARE_SIZE - 40)
)

cross_img = pygame.transform.scale(
    cross_img,
    (SQUARE_SIZE - 40, SQUARE_SIZE - 40)
)


# GRAPHISMES
# ==================================================

def draw_lines():
    for i in range(1, ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )

        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )

def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):

            x = col * SQUARE_SIZE + 20
            y = row * SQUARE_SIZE + 20

            if board[row][col] == 1:
                screen.blit(circle_img, (x, y))

            elif board[row][col] == 2:
                screen.blit(cross_img, (x, y))


# LOGIQUE
# ==================================================

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    return all(cell != 0 for row in board for cell in row)

def check_win(player):

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(COLS):
        if all(board[row][col] == player for row in range(ROWS)):
            return True

    if all(board[i][i] == player for i in range(ROWS)):
        return True

    if all(board[i][COLS - i - 1] == player for i in range(ROWS)):
        return True

    return False


# ECRAN DE FIN
# ==================================================

def display_end_message(message):

    screen.fill(BG_COLOR)

    font = pygame.font.Font(None, 70)

    text = font.render(
        message,
        True,
        WHITE
    )

    rect = text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    screen.blit(text, rect)

    pygame.display.update()

# ==================================================
# IA ALEATOIRE
# ==================================================

def get_random_move():

    empty = []

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                empty.append((row, col))

    if empty:
        return random.choice(empty)

    return None

# ==================================================
# MINIMAX
# ==================================================

def check_winner_state(state, player):

    for row in state:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(state[row][col] == player for row in range(3)):
            return True

    if all(state[i][i] == player for i in range(3)):
        return True

    if all(state[i][2 - i] == 
    empty = []

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                empty.append((row, col))

    if empty:player for i in range(3)):
        return True

    return False

def is_full_state(state):
    return all(cell != 0 for row in state for cell in row)

def minimax(board_state, depth, is_maximizing):

    if check_winner_state(board_state, 2):
        return 1

    if check_winner_state(board_state, 1):
        return -1

    if is_full_state(board_state):
screen.fill(BG_COLOR)
        return 0

   if is_maximizing:

        best_score = -999

        for row in range(3):
            for col in range(3):

                if board_state[row][col] == 0:

                    board_state[row][col] = 2

                    score = minimax(
                        board_state,
                        depth + 1,
                        False
                    )

                    board_state[row][col] = 0

                    best_score = max(
                        score,
                        best_score
                    )

        return best_score

    else:

        best_score = 999

        for row in range(3):
            for col in range(3):

                if board_state[row][col] == 0:

                    board_state[row][col] = 1

                    score = minimax(
                        board_state,
                        depth + 1,
                        True
                    )

                    board_state[row][col] = 0

                    best_score = min(
                        score,
                        best_score
                    )

        return best_score

def best_move():

    best_score = -999
    move = None

    for row in range(3):
        for col in range(3):

            if board[row][col] == 0:

                board[row][col] = 2

                score = minimax(
                    board,
                    0,
                    False
                )

                board[row][col] = 0

                if score > best_score:

                    best_score = score
                    move = (row, col)

    return move

# ==================================================
# ALPHA BETA
# ==================================================

def minimax_ab(board_state, depth, alpha, beta, is_maximizing):

    if check_winner_state(board_state, 2):
        return 1

    if check_winner_state(board_state, 1):
        return -1

    if is_full_state(board_state):
        return 0

    if is_maximizing:

        best_score = -999

        for row in range(3):
            for col in range(3):

                if board_state[row][col] == 0:

                    board_state[row][col] = 2

                    score = minimax_ab(
                        board_state,
                        depth + 1,
                        alpha,
                        beta,
                        False
                    )

                    board_state[row][col] = 0

                    best_score = max(
                        best_score,
                        score
                    )

                    alpha = max(
                        alpha,
                        score
                    )

                    if beta <= alpha:
                        break

        return best_score

    else:

        best_score = 999

        for row in range(3):
            for col in range(3):

                if board_state[row][col] == 0:

                    board_state[row][col] = 1

                    score = minimax_ab(
                        board_state,
                        depth + 1,
                        alpha,
                        beta,
                        True
                    )

                    board_state[row][col] = 0

                    best_score = min(
                        best_score,
                        score
                    )

                    beta = min(
                        beta,
                        score
                    )

                    if beta <= alpha:
                        break

        return best_score

def best_move_ab():

    best_score = -999
    move = None

    for row in range(3):
        for col in range(3):

            if board[row][col] == 0:

                board[row][col] = 2

                score = minimax_ab(
                    board,
                    0,
                    -999,
                    999,
                    False
                )

                board[row][col] = 0

                if score > best_score:

                    best_score = score
                    move = (row, col)

    return move

# ==================================================
# RESTART
# ==================================================

def restart():

    screen.fill(BG_COLOR)

    draw_lines()

    for row in range(ROWS):
        for col in range(COLS):
            board[row][col] = 0

# ==================================================
# JEU
# ==================================================

draw_lines()

player = 1
game_over = False

# random / minimax / alphabeta
ai_mode = "alphabeta"

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:

                restart()
                game_over = False
                player = 1

        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and not game_over
        ):

            mouseX, mouseY = event.pos

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(
                clicked_row,
                clicked_col
            ):

                mark_square(
                    clicked_row,
                    clicked_col,
                    1
                )

                draw_figures()

                if check_win(1):

                    display_end_message(
                        "Ta gagner, t'es un tigre wallah, press R = Restart !"
                    )

                    game_over = True

                elif is_board_full():

                    display_end_message(
                        "Match nul, press R pour restart sale bot !"
                    )

                    game_over = True

                player = 2

    if player == 2 and not game_over:

        pygame.time.wait(0)

        if ai_mode == "random":
            move = get_random_move()

        elif ai_mode == "minimax":
            move = best_move()

        else:
            move = best_move_ab()

        if move:

            mark_square(
                move[0],
                move[1],
                2
            )

            draw_figures()

            if check_win(2):

                display_end_message(
                    "L'IA gagne ptit bot !"
                )

                game_over = True

            elif is_board_full():

                display_end_message(
                    "Match nul, restart -> press R!"
                    
                )

                game_over = True
            
            player = 1

            

    pygame.display.update()

