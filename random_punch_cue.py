import pygame
import random

# Initialize Pygame
pygame.init()

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the font
FONT = pygame.font.Font(None, 36)

# Set the game states
START_STATE = 0
GAME_STATE = 1

# Set the initial game state
game_state = START_STATE

# Set the window caption
pygame.display.set_caption("Pygame Example")

# Create the window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1800
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define the Rect objects for the buttons
start_button = pygame.Rect(SCREEN_WIDTH/4 - 50, SCREEN_HEIGHT/2, 100, 50)
quit_button = pygame.Rect(3*SCREEN_WIDTH/4 - 50, SCREEN_HEIGHT/2, 100, 50)

# Define the Rect objects for the squares
square_width = SCREEN_WIDTH/2
square_height = SCREEN_HEIGHT/3
squares = []

for i in range(2):
    for j in range(3):
        square = pygame.Rect(i*square_width, j*square_height, square_width, square_height)
        if (i+j) % 2 == 0:
            squares.append((square, GRAY))
        else:
            squares.append((square, BLACK))

# Define the function to randomly change the color of a square
def change_color():
    for i in range(8):
        square_index = random.randint(0, len(squares)-1)
        square, color = squares[square_index]
        squares[square_index] = (square, RED)
        pygame.time.wait(4000)
        squares[square_index] = (square, color)
        pygame.time.wait(4000)

    # Change the game state back to START_STATE
    global game_state
    game_state = START_STATE

# Start the game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == START_STATE:
                if start_button.collidepoint(event.pos):
                    game_state = GAME_STATE
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()

    # Draw the appropriate screen
    if game_state == START_STATE:
        # Clear the screen
        window.fill(WHITE)

        # Draw the title
        title_text = FONT.render("Welcome to Pygame Example", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
        window.blit(title_text, title_rect)

        # Draw the start button
        pygame.draw.rect(window, GREEN, start_button)
        start_text = FONT.render("Start", True, WHITE)
        start_rect = start_text.get_rect(center=start_button.center)
        window.blit(start_text, start_rect)

        # Draw the quit button
        pygame.draw.rect(window, RED, quit_button)
        quit_text = FONT.render("Quit", True, WHITE)
        quit_rect = quit_text.get_rect(center=quit_button.center)
        window.blit(quit_text, quit_rect)

    elif game_state == GAME_STATE:
        # Clear the screen
        window.fill(WHITE)

        # Draw the squares
        for square, color in squares:
