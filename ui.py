import pygame
import sys

def draw_button(win, rect, text, color_bg, color_text):
    pygame.draw.rect(win, color_bg, rect, border_radius=18)
    text_surf = pygame.font.SysFont("Comic Sans MS", 36).render(text, True, color_text)
    win.blit(text_surf, (rect.centerx - text_surf.get_width() // 2, rect.centery - text_surf.get_height() // 2))

def start_screen(window, WIDTH, HEIGHT, font_big, draw_button, BLUE, RED, WHITE, PURPLE, BACKGROUND):
    easy_btn = pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2, 100, 50)
    hard_btn = pygame.Rect(WIDTH // 2 + 20, HEIGHT // 2, 100, 50)
    impossible_btn = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 80, 200, 50)
    while True:
        window.fill(BACKGROUND)
        title = font_big.render("Flappy Bird", True, (0,0,0))
        window.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
        draw_button(window, easy_btn, "Easy", BLUE, WHITE)
        draw_button(window, hard_btn, "Hard", RED, WHITE)
        draw_button(window, impossible_btn, "Impossible", PURPLE, WHITE)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_btn.collidepoint(event.pos):
                    return "easy", 30, 150
                elif hard_btn.collidepoint(event.pos):
                    return "hard", 45, 150
                elif impossible_btn.collidepoint(event.pos):
                    return "impossible", 45, 100

def game_over_screen(win, WIDTH, HEIGHT, font_big, font_medium, draw_button, RED, BLUE, WHITE, BACKGROUND, score, load_high_score, save_high_score, game_mode):
    old_high_score = load_high_score(game_mode)
    is_new_high = score > old_high_score
    if is_new_high:
        save_high_score(game_mode, score)
    game_over_text = font_big.render("Game Over", True, (0,0,0))
    score_text = font_medium.render(f"Score: {score}", True, (0,0,0))
    if is_new_high:
        high_score_text = font_medium.render("New Best Score!", True, RED)
    else:
        high_score_text = font_medium.render(f"Best Score: {old_high_score}", True, (0,0,0))

    play_again_btn = pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 + 80, 120, 60)
    exit_btn = pygame.Rect(WIDTH // 2 + 20, HEIGHT // 2 + 80, 120, 60)

    while True:
        win.fill(BACKGROUND)
        win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4 - 40))
        win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 80))
        if high_score_text:
            win.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2))

        draw_button(win, play_again_btn, "Replay", BLUE, WHITE)
        draw_button(win, exit_btn, "Exit", RED, WHITE)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_btn.collidepoint(event.pos):
                    return "replay"
                elif exit_btn.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()