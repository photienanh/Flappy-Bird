import pygame
import random

class Pipe:
    def __init__(self, WIDTH, HEIGHT, PIPE_GAP, PIPE_WIDTH, pipe_body_img, pipe_cap_img, GROUND_HEIGHT):
        self.x = WIDTH
        self.PIPE_WIDTH = PIPE_WIDTH
        self.PIPE_GAP = PIPE_GAP
        self.HEIGHT = HEIGHT
        self.GROUND_HEIGHT = GROUND_HEIGHT
        self.pipe_body_img = pipe_body_img
        self.pipe_cap_img = pipe_cap_img
        self.cap_height = pipe_cap_img.get_height()

        min_top = 50
        max_top = HEIGHT - GROUND_HEIGHT - PIPE_GAP - 50
        self.top_pipe_bottom = random.randint(min_top, max_top)
        self.bottom_pipe_top = self.top_pipe_bottom + PIPE_GAP

        self.passed = False

        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.top_pipe_bottom)
        self.bottom_rect = pygame.Rect(self.x, self.bottom_pipe_top, PIPE_WIDTH, HEIGHT - self.bottom_pipe_top - GROUND_HEIGHT)

    def update(self):
        self.x -= 5
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, win):
        body_height = self.top_pipe_bottom - self.cap_height
        if body_height > 0:
            body_img = pygame.transform.scale(self.pipe_body_img, (self.PIPE_WIDTH, body_height))
            body_img_flipped = pygame.transform.flip(body_img, False, True)
            win.blit(body_img_flipped, (self.x, 0))  # <-- vẽ body sát mép trên
        cap_img_flipped = pygame.transform.flip(self.pipe_cap_img, False, True)
        win.blit(cap_img_flipped, (self.x, self.top_pipe_bottom - self.cap_height))

        bottom_height = self.HEIGHT - self.bottom_pipe_top - self.GROUND_HEIGHT - self.cap_height
        if bottom_height > 0:
            body_img = pygame.transform.scale(self.pipe_body_img, (self.PIPE_WIDTH, bottom_height))
            win.blit(body_img, (self.x, self.bottom_pipe_top + self.cap_height))
        win.blit(self.pipe_cap_img, (self.x, self.bottom_pipe_top))