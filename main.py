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


def print_message(display, FONT_STYLE, message, color):
    message_display = FONT_STYLE.render(message, True, color, (0, 0, 0))
    display.blit(message_display, [CENTER[0] - 50, CENTER[1] - 50])
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
    points = 10
    xpos_food = random.randint(0, FULLSCREEN[0])
    ypos_food = random.randint(0, FULLSCREEN[1])

    # Game loop

    while game == Game.RUNNING.value:
        print(positions)
        print(xpos_food, ypos_food)
        if xpos < 0 or xpos > FULLSCREEN[0] or ypos < 0 or ypos > FULLSCREEN[1]:
            game = Game.LOSE
        print(xpos <= xpos_food + 10)
        print(xpos >= xpos_food - 10)
        print(ypos <= ypos_food + 10)
        print(ypos >= ypos_food - 10)
        if xpos <= xpos_food + 10 and xpos >= xpos_food - 10 and ypos <= ypos_food + 10 and ypos >= ypos_food - 10:
            points -= 1
            length += 1
            positions.pop(0)
            positions.append([xpos, ypos])
            xpos_food = random.randint(0, FULLSCREEN[0])
            ypos_food = random.randint(0, FULLSCREEN[1])
            if points == 0:
                game = Game.WIN
        for event in pygame.event.get():
            # Check for quit event
            if event.type==pygame.QUIT:
                game = Game.Quit
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
        # Update the display
        pygame.display.update()

    if game == Game.LOSE:
        print("You lose!")
        print_message(display, FONT_STYLE, "You lose!", (255, 0, 0))
        time.sleep(5)

    if game == Game.WIN:
        print("You win!")
        print_message(display, FONT_STYLE, "You win!", (0, 255, 0))
        time.sleep(5)

    pygame.quit()
    quit()

main()