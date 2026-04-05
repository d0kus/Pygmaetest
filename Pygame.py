import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 180, 50)
BLUE = (50, 100, 220)
YELLOW = (240, 200, 50)
COLORS = [RED, GREEN, BLUE, YELLOW]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)


def create_obj():
    obj = {
        "x": random.randint(0, SCREEN_WIDTH - 30),
        "y": 0,
        "color": random.choice(COLORS),
        "size": 20
    }
    return obj


basket_width = 120
basket_height = 20
basket_y = SCREEN_HEIGHT - 50
basket_speed = 50

# ОСНОВНОЙ ЦИКЛ
while True:
    # Сброс для новой игры
    game_state = {
        "score": 0,
        "lives": 3,
        "level": 1,
        "game_over": False,
        "fall_speed": 1
    }
    basket_x = SCREEN_WIDTH // 2 - basket_width // 2
    falling_objects = []
    frame_count = 0
    spawn_rate = 180

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
            game_state["level"] = game_state["score"] // 5
            game_state["fall_speed"] = game_state["level"]

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
        screen.blit(lives_text, (10, 40))
        screen.blit(level_text, (10, 70))
        pygame.display.flip()

    # GAME OVER ЭКРАН (ПОСЛЕ ИГРЫ)
    game_over_screen = True
    restart_game = False

    while game_over_screen:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_screen = False
                restart_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over_screen = False
                    restart_game = True
                if event.key == pygame.K_q:
                    game_over_screen = False
                    restart_game = False

        screen.fill(WHITE)
        game_over_font = pygame.font.SysFont("Arial", 60)
        game_over_text = game_over_font.render("Game Over", True, RED)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 180, 150))

        final_score_text = font.render(f"Final Score: {game_state['score']}", True, BLACK)
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - 150, 280))

        restart_text = font.render("Press R to restart or Q to quit", True, BLACK)
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - 200, 380))

        pygame.display.flip()

    if not restart_game:
        break

pygame.quit()