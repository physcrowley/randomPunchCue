import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

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
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Define the functions

def draw_start_screen():
    # Clear the screen
    window.fill(WHITE)

    # Draw the title
    title_text = FONT.render("Welcome to Pygame Example", True, BLACK)
    title_rect = title_text.get_rect(center=(WINDOW_WIDTH/2, 100))
    window.blit(title_text, title_rect)

    # Draw the start button
    start_button = pygame.Rect(150, 200, 100, 50)
    pygame.draw.rect(window, GREEN, start_button)
    start_text = FONT.render("Start", True, WHITE)
    start_rect = start_text.get_rect(center=start_button.center)
    window.blit(start_text, start_rect)

    # Draw the quit button
    quit_button = pygame.Rect(350, 200, 100, 50)
    pygame.draw.rect(window, RED, quit_button)
    quit_text = FONT.render("Quit", True, WHITE)
    quit_rect = quit_text.get_rect(center=quit_button.center)
    window.blit(quit_text, quit_rect)

def draw_game_screen():
    # Clear the screen
    window.fill(WHITE)

    # Draw the squares
    square_width = WINDOW_WIDTH/2
    square_height = WINDOW_HEIGHT/3

    for i in range(2):
        for j in range(3):
            square = pygame.Rect(i*square_width, j*square_height, square_width, square_height)
            if (i+j) % 2 == 0:
                pygame.draw.rect(window, BLACK, square)
            else:
                pygame.draw.rect(window, GRAY, square)

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
        draw_start_screen()
    elif game_state == GAME_STATE:
        draw_game_screen()

    # Update the display
    pygame.display.update()
