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
GOLD = (255, 215, 0)

# Set the font
FONT = pygame.font.Font(None, 36)

# Set the game states
START_STATE = 0
GAME_STATE = 1
END_STATE = 2

# Set the initial game state
game_state = START_STATE

# Set the screen size
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600

# Set the window caption
pygame.display.set_caption("Random Punch Cue")

# Create the window
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
        squares.append(square)

next_square = random.randint(0,len(squares))
current_square = next_square

# Define the functions

def draw_start_screen():
    # Clear the screen
    window.fill(WHITE)

    # Draw the title
    title_text = FONT.render("Welcome to the Punch Block Cuer", True, BLACK)
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

def draw_game_screen():
    # Clear the screen
    window.fill(WHITE)

    # Draw the squares
    for i, square in enumerate(squares):
        if i == current_square:
            pygame.draw.rect(window, RED, square)
        elif (i+j) % 2 == 0:
            pygame.draw.rect(window, BLACK, square)
        else:
            pygame.draw.rect(window, GRAY, square)

def draw_end_screen():
    # Clear the screen
    window.fill(GOLD)

    # Draw the title
    title_text = FONT.render("Good Work!", True, BLACK)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
    window.blit(title_text, title_rect)

# Start the game loop
reps = 0

while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == START_STATE:
                reps = 0
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
    elif game_state == END_STATE :
        draw_end_screen()
    pygame.display.update()

    # state updates
    if game_state == GAME_STATE :
        # delay between reps 
        pygame.time.wait(3000)
        
        # different random square position
        while next_square == current_square :
            next_square = random.randint(0,len(squares)-1)
        current_square = next_square
        
        # move to end state after 10 reps
        reps += 1
        if reps == 10 :
            game_state = END_STATE   
    elif game_state == END_STATE :
        # move to start state immediately after showing end screen
        pygame.time.wait(3000)
        game_state = START_STATE
        
