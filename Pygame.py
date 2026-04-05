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
def create_obj():
    obj = {
        "x": random.randint(0, SCREEN_WIDTH - 30),
        "y": 0,
        "color": random.choice(COLORS),
        "size": 20
    }
    return obj

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
frame_count = 0
spawn_rate = 30

while True:
    while not game_state["game_over"]:
        clock.tick(60)
        frame_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state["game_over"] = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    basket_x -= basket_speed
                if event.key == pygame.K_RIGHT:
                    basket_x += basket_speed
        if basket_x < 0:
            basket_x = 0
        if basket_x + basket_width > SCREEN_WIDTH:
            basket_x = SCREEN_WIDTH - basket_width

        if frame_count % spawn_rate == 0:
            falling_objects.append(create_obj())

        for obj in falling_objects:
            obj["y"] += game_state["fall_speed"]

        objects_keep = []
        for obj in falling_objects:
            if obj["y"] + obj["size"] >= basket_y and basket_x <= obj["x"] <= basket_x + basket_width:
                game_state["score"] += 1
            elif obj["y"] > SCREEN_HEIGHT:
                game_state["lives"] -= 1
            else:
                objects_keep.append(obj)
        falling_objects = objects_keep

        if game_state["score"] > 0 and game_state["score"] % 5 == 0:
            game_state["fall_speed"] += 1
            game_state["level"] = game_state["score"] // 5
            game_state["fall_speed"] = 3 + game_state["level"]

        if game_state["lives"] <= 0:
            game_state["game_over"] = True

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (basket_x, basket_y, basket_width, basket_height))

        for obj in falling_objects:
            pygame.draw.circle(screen, obj["color"], (obj["x"], obj["y"]), obj["size"])
        score_text = font.render(f"Score: {game_state['score']}", True, BLACK)
        lives_text = font.render(f"Lives: {game_state['lives']}", True, BLACK)
        level_text = font.render(f"Level: {game_state['level']}", True, BLACK)

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 30))
        screen.blit(level_text, (10, 50))
        pygame.display.flip()

    # TODO 3: Write the Game Over screen
    # Display "Game Over" and final score
    # Allow R to restart, Q to quit
    game_over_screen = True

    while game_over_screen:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_screen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state = {
                        "score": 0,
                        "lives": 3,
                        "level": 1,
                        "game_over": False,
                        "fall_speed": 3
                    }
                    basket_x = SCREEN_WIDTH // 2 - basket_width // 2
                    falling_objects = []
                    frame_count = 0
                    game_over_screen = False
                    break
                if event.key == pygame.K_q:
                    game_over_screen = False

        screen.fill(WHITE)
        game_over_font = pygame.font.SysFont("Arial", 60)
        game_over_text = game_over_font.render("Game Over", True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 250, 150))

        final_score_text = font.render(f"Final Score: {game_state['score']}", True, BLACK)
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 200, 280))

        restart_text = font.render("Press R to restart or Q to quit", True, BLACK)
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - 200, 380))

        pygame.display.flip()
    if not game_over_screen:
        if game_state["game_over"]:
            continue
        else:
            break
pygame.quit()
