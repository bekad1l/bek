import pygame
import sys
import random
import time
import os

pygame.init()

# Screen dimensions
width = 800
height = 600

# Colors
white = (255, 255, 255)
red = (213, 50, 80)
black = (0, 0, 0)

# Block size
block_size = 20

# Initial speed and levels
speed = 10
current_level = 1
score = 0

# Initialize the display
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

# Font
font = pygame.font.SysFont("comicsansms", 35)

# Load fruit images
fruit_images_dir = "C:\\Users\\Admin\\OneDrive\\Рабочий стол\\games\\bek\\lab1\\lab9\\snake"
fruit_files = ['food1.png', 'food2.png', 'food3.png']  # File names of the fruit images

# Load fruit images into a dictionary
fruit_images = {}
for filename in fruit_files:
    fruit_images[filename] = pygame.image.load(os.path.join(fruit_images_dir, filename)).convert_alpha()

# Resize fruit images
fruit_width = 20
fruit_height = 20
for name, img in fruit_images.items():
    fruit_images[name] = pygame.transform.scale(img, (fruit_width, fruit_height))

# Function to display messages
def message(msg, color):
    mesg = font.render(msg, True, color)
    game_display.blit(mesg, [width / 2 - len(msg) * 10, height / 2])

# Function to display the current level
def display_level(level):
    level_text = font.render("Level: " + str(level), True, white)
    game_display.blit(level_text, [10, 10])

# Function to display the current score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    game_display.blit(score_text, [width - 150, 10])

# Main game loop
def gameLoop():
    global speed, current_level, score
    game_exit = False
    game_over = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Define positions where food can appear
    food_positions = [
        ((width // 2) - 20, (height // 2) - 20),  # Center position
        (100, 100),  # Custom position 1
        (600, 400),  # Custom position 2
        (300, 500)   # Custom position 3
        # Add more positions as needed
    ]

    # Define fruit images
    fruits = list(fruit_images.values())

    # Initially, there is no food on the screen
    food_x = -100
    food_y = -100
    current_fruit = None

    while not game_exit:
        while game_over == True:
            game_display.fill(black)
            message("Game Over! Press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        speed = 10
                        current_level = 1
                        score = 0
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)

        # If there is no food on the screen, generate a new one
        if food_x == -100 and food_y == -100:
            food_x, food_y = random.choice(food_positions)
            current_fruit = random.choice(fruits)

        game_display.blit(current_fruit, (food_x, food_y))

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        for segment in snake_list:
            pygame.draw.rect(game_display, white, [segment[0], segment[1], block_size, block_size])

        display_level(current_level)
        display_score(score)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            # Reset food position
            food_x = -100
            food_y = -100
            # Increase snake length and score
            length_of_snake += 1
            score += 10

            if score % 30 == 0:  # Increase level every 3 foods
                current_level += 1
                speed += 2  # Increase speed with each level

        pygame.time.Clock().tick(speed)

    pygame.quit()
    quit()

gameLoop()
