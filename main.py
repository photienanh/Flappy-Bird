import pygame
import os
import sys
from bird import Bird
from pipe import Pipe
from score import load_high_score, save_high_score
from ui import draw_button, start_screen, game_over_screen

pygame.init()
WIDTH, HEIGHT = 400, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (100, 149, 237)
PURPLE = (75, 0, 130)
GRAVITY = 1
JUMP = -10
PIPE_WIDTH = 70
PIPE_GAP = 150
BACKGROUND = (239, 230, 221)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

BIRD_IMG = pygame.image.load(resource_path("img/bird.png"))
BIRD_IMG = pygame.transform.scale(BIRD_IMG, (30, 30))

PIPE_IMG = pygame.image.load(resource_path("img/pipe.png"))
ORIGINAL_PIPE_WIDTH = PIPE_IMG.get_width()
ORIGINAL_PIPE_HEIGHT = PIPE_IMG.get_height()

# Tính tỉ lệ scale
scale_ratio = PIPE_WIDTH / ORIGINAL_PIPE_WIDTH
scaled_height = int(ORIGINAL_PIPE_HEIGHT * scale_ratio)

# Scale giữ nguyên tỉ lệ
PIPE_IMG = pygame.transform.smoothscale(PIPE_IMG, (PIPE_WIDTH, scaled_height))

GROUND_HEIGHT = 60
GROUND_IMG = pygame.image.load(resource_path("img/ground.png"))
GROUND_IMG = pygame.transform.scale(GROUND_IMG, (WIDTH, GROUND_HEIGHT))

BG_IMG = pygame.image.load(resource_path("img/background.png"))
BG_IMG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT - GROUND_HEIGHT))

font_big = pygame.font.SysFont("Comic Sans MS", 60)
font_medium = pygame.font.SysFont("Comic Sans MS", 36)
font_small = pygame.font.SysFont("Comic Sans MS", 24)

def main():
    while True:
        # Start screen
        game_mode, FPS , PIPE_GAP = start_screen(window, WIDTH, HEIGHT, font_big, draw_button, BLUE, RED, WHITE, PURPLE, BACKGROUND)
        clock = pygame.time.Clock()
        bird = Bird(HEIGHT, JUMP, GRAVITY, BIRD_IMG)
        pipes = [Pipe(WIDTH, HEIGHT, PIPE_GAP, PIPE_WIDTH, PIPE_IMG, GROUND_HEIGHT)]
        score = 0
        countdown_time = 3
        countdown_start = pygame.time.get_ticks()
        running = True
        game_started = False
        while running:
            clock.tick(FPS)
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - countdown_start) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird.jump()

            bird.update()
            if elapsed_time >= countdown_time:
                game_started = True
            if game_started:
                if pipes[-1].x < WIDTH // 2:
                    pipes.append(Pipe(WIDTH, HEIGHT, PIPE_GAP, PIPE_WIDTH, PIPE_IMG, GROUND_HEIGHT))
                for pipe in pipes[:]: 
                    pipe.update()
                    if pipe.x + PIPE_WIDTH < 0:
                        pipes.remove(pipe)
                    if not pipe.passed and bird.x > pipe.x + PIPE_WIDTH:
                        pipe.passed = True 
                        score += 1
                    if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                        running = False
            if bird.y < 0 or bird.y + BIRD_IMG.get_height() >= HEIGHT - GROUND_HEIGHT:
                    running = False

            window.blit(BG_IMG, (0, 0))
            bird.draw(window)
            for pipe in pipes:
                pipe.draw(window)
            window.blit(GROUND_IMG, (0, HEIGHT - GROUND_HEIGHT))
            score_text = font_small.render(f"Score: {score}", True, BLACK)
            window.blit(score_text, (10, 10))
            pygame.display.update()

        # Game over screen
        action = game_over_screen(window, WIDTH, HEIGHT, font_big, font_medium, draw_button, RED, BLUE, WHITE, BACKGROUND, score, load_high_score, save_high_score, game_mode)
        if action == "replay":
            continue  # Chơi lại
        else:
            break

if __name__ == "__main__":
    main()