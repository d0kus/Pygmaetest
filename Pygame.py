import pygame
import random
# Initialize PyGame
pygame.init()
# --- Constants (use tuples for colors) ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 180, 50)
BLUE = (50, 100, 220)
YELLOW = (240, 200, 50)
COLORS = [RED, GREEN, BLUE, YELLOW]
# --- Game State (use a dictionary) ---
game_state = {
 "score": 0,
 "lives": 3,
 "level": 1,
 "game_over": False,
 "fall_speed": 3
}
# --- Player (basket) settings ---
basket_width = 120
basket_height = 20
basket_x = SCREEN_WIDTH // 2 - basket_width // 2
basket_y = SCREEN_HEIGHT - 50
basket_speed = 8
# --- Falling objects (use a list of dictionaries) ---
falling_objects = []
# --- Screen setup ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)
# TODO 1: Write a function to create a new falling object
# It should return a dictionary with keys: "x", "y",
# "color", "size"
# x = random position, y = 0 (top), color = random from COLORS

# TODO 2: Write the main game loop (while not game_over)
# Inside the loop:
# a) Handle events (QUIT, key presses for LEFT/RIGHT)
# b) Spawn new objects (e.g., every 30 frames)
# c) Move each object down using a for loop
# d) Check collision with basket (if/elif/else)
# e) Remove caught or missed objects from the list
# f) Update game_state dictionary (score, lives, level)
# g) Increase difficulty every 5 points
# h) Draw everything on the screen
# i) Display score and lives
# TODO 3: Write the Game Over screen
# Display "Game Over" and final score
# Allow R to restart, Q to quit
pygame.quit()
