import pygame
from enum import Enum
import time
import random

class Game(Enum):
    RUNNING = 1
    QUIT = 2
    WIN = 3
    LOSE = 4

FULLSCREEN = (1000, 700)
CENTER = (FULLSCREEN[0] // 2, FULLSCREEN[1] // 2)

background = pygame.image.load('background.png')


def print_message(display, FONT_STYLE, message, color, background_color=(0,0,0), position=[CENTER[0] - 50, CENTER[1] - 50], size=None):
    message_display = FONT_STYLE.render(message, True, color, background_color)
    display.blit(message_display, position)
    pygame.display.update()


def main():
    #initialize pygame
    pygame.init()
    FONT_STYLE = pygame.font.SysFont(None, 50)
    display = pygame.display.set_mode(FULLSCREEN)
    pygame.display.set_caption('Snake game by Edureka')

    clock = time.perf_counter()  # Start the clock

    game = 1 # Game loop control variable
    xpos = CENTER[0]; # Initial X position
    ypos = CENTER[1]; # Initial Y position
    snakeblock = 50; # Size of the snake
    ms = 50; # Movement speed
    length = 1; # Length of the snake
    positions = [[xpos, ypos]] # List of positions of the snake

    # Points to collect to win the game
    points = 0
    xpos_food = random.randint(100, FULLSCREEN[0] - 100)
    ypos_food = random.randint(100, FULLSCREEN[1] - 100)

    # Game loop

    while game == Game.RUNNING.value:
        #update the clock
        clock = time.process_time()
        # Check if the snake is out of the screen
        if positions[0][0] < 0 or positions[0][0] > FULLSCREEN[0] or positions[0][1] < 0 or positions[0][1] > FULLSCREEN[1]:
            game = Game.LOSE.value
        for i in range(1, length):
            if positions[0][0] == positions[i][0] and positions[0][1] == positions[i][1]:
                game = Game.LOSE.value
        if positions[0][0] <= xpos_food + snakeblock and positions[0][0] >= xpos_food - snakeblock and positions[0][1] <= ypos_food + snakeblock and positions[0][1] >= ypos_food - snakeblock:
            points += 1
            length += 1
            # Add a new position to the list
            positions.append([-100, -100])
            xpos_food = random.randint(100, FULLSCREEN[0] - 100)
            ypos_food = random.randint(100, FULLSCREEN[1] - 100)
            if points == 10:
                game = Game.WIN.value
        for event in pygame.event.get():
            # Check for quit event
            if event.type==pygame.QUIT:
                game = Game.QUIT.value
            # Check for key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for i in range(length - 1, 0, -1):
                        positions[i][0] = positions[i - 1][0]
                        positions[i][1] = positions[i - 1][1]
                    positions[0][0] -= ms
                elif event.key == pygame.K_RIGHT:
                    for i in range(length - 1, 0, -1):
                        positions[i][0] = positions[i - 1][0]
                        positions[i][1] = positions[i - 1][1]
                    positions[0][0] += ms
                elif event.key == pygame.K_UP:
                    for i in range(length - 1, 0, -1):
                        positions[i][0] = positions[i - 1][0]
                        positions[i][1] = positions[i - 1][1]
                    positions[0][1] -= ms
                elif event.key == pygame.K_DOWN:
                    for i in range(length - 1, 0, -1):
                        positions[i][0] = positions[i - 1][0]
                        positions[i][1] = positions[i - 1][1]
                    positions[0][1] += ms
        
        # Fill the screen with black color
        display.fill((0,0,0))  
        # Draw the background
        display.blit(background, (0, 0))
        # Draw the snake
        pygame.draw.rect(display, (0, 0, 255), [positions[0][0], positions[0][1], snakeblock, snakeblock])
        for i in range(1, length):
            pygame.draw.rect(display, (0, 127, 127), [positions[i][0], positions[i][1], snakeblock, snakeblock])
        # Draw the food
        pygame.draw.rect(display, (255, 0, 0), [xpos_food, ypos_food, snakeblock, snakeblock])
        # Draw the score
        print_message(display, FONT_STYLE, "Score: " + str(points), (255, 255, 255), background_color=(181,230,29),position=[0, 0])
        # Draw the clock
        print_message(display, FONT_STYLE, "Time: " + str(int(clock)), (255, 255, 255), background_color=(181,230,29), position=[0, 50])
        # Update the display
        pygame.display.update()

    if game == Game.LOSE.value:
        print("You lose!")
        print_message(display, FONT_STYLE, "You lose!", (255, 0, 0), background_color=(181,230,29), size=200)
        time.sleep(5)

    if game == Game.WIN.value:
        print("You win!")
        print_message(display, FONT_STYLE, "You win!", (255, 0, 0), background_color=(181,230,29), size=200)
        time.sleep(5)

    pygame.quit()
    quit()

main()