import pygame
from enum import Enum
import time
import random

class Game(Enum):
    RUNNING = 1
    QUIT = 2
    WIN = 3
    LOSE = 4

FULLSCREEN = (500, 400)
CENTER = (FULLSCREEN[0] // 2, FULLSCREEN[1] // 2)


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

    game = 1 # Game loop control variable
    xpos = CENTER[0]; # Initial X position
    ypos = CENTER[1]; # Initial Y position
    ms = 10; # Movement speed
    length = 1; # Length of the snake
    positions = [[xpos, ypos]] # List of positions of the snake

    # Points to collect to win the game
    points = 0
    xpos_food = random.randint(0, FULLSCREEN[0])
    ypos_food = random.randint(0, FULLSCREEN[1])

    # Game loop

    while game == Game.RUNNING.value:
        if positions[0][0] < 0 or positions[0][0] > FULLSCREEN[0] or positions[0][1] < 0 or positions[0][1] > FULLSCREEN[1]:
            game = Game.LOSE.value
        if positions[0][0] <= xpos_food + 10 and positions[0][0] >= xpos_food - 10 and positions[0][1] <= ypos_food + 10 and positions[0][1] >= ypos_food - 10:
            points += 1
            length += 1
            # Add a new position to the list
            positions.append([positions[length - 2][0] + 10, positions[length - 2][1] + 10])
            xpos_food = random.randint(0, FULLSCREEN[0])
            ypos_food = random.randint(0, FULLSCREEN[1])
            if points == 10:
                game = Game.WIN
        for event in pygame.event.get():
            # Check for quit event
            if event.type==pygame.QUIT:
                game = Game.QUIT.value
            # Check for key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for i in range(length):
                        positions[i][0] -= ms
                elif event.key == pygame.K_RIGHT:
                    for i in range(length):
                        positions[i][0] += ms
                elif event.key == pygame.K_UP:
                    for i in range(length):
                        positions[i][1] -= ms
                elif event.key == pygame.K_DOWN:
                    for i in range(length):
                        positions[i][1] += ms
        
        # Fill the screen with black color
        display.fill((0,0,0))
        # Draw the snake
        for position in positions:
            pygame.draw.rect(display, (0, 255, 0), [position[0], position[1], 10, 10])
        # Draw the food
        pygame.draw.rect(display, (255, 0, 0), [xpos_food, ypos_food, 10, 10])
        # Draw the score
        print_message(display, FONT_STYLE, "Score: " + str(points), (255, 255, 255), position=[0, 0])
        # Update the display
        pygame.display.update()

    if game == Game.LOSE.value:
        print("You lose!")
        print_message(display, FONT_STYLE, "You lose!", (255, 0, 0))
        time.sleep(5)

    if game == Game.WIN.value:
        print("You win!")
        print_message(display, FONT_STYLE, "You win!", (0, 255, 0))
        time.sleep(5)

    pygame.quit()
    quit()

main()