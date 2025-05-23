import pygame
import random

class Pipe:
    def __init__(self, WIDTH, HEIGHT, PIPE_GAP, PIPE_WIDTH, pipe_img, GROUND_HEIGHT):
        self.x = WIDTH
        self.PIPE_WIDTH = PIPE_WIDTH
        self.PIPE_GAP = PIPE_GAP
        self.HEIGHT = HEIGHT
        self.GROUND_HEIGHT = GROUND_HEIGHT
        self.pipe_img = pipe_img

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
        # Vẽ ống trên (crop từ trên xuống, rồi lật ngược)
        top_crop_height = min(self.top_pipe_bottom, self.pipe_img.get_height())
        if top_crop_height > 0:
            top_crop = self.pipe_img.subsurface((0, 0, self.PIPE_WIDTH, top_crop_height))
            top_img = pygame.transform.flip(top_crop, False, True)
            win.blit(top_img, (self.x, 0))

        # Vẽ ống dưới (crop từ trên cùng của ảnh)
        bottom_height = self.HEIGHT - self.bottom_pipe_top - self.GROUND_HEIGHT
        if bottom_height > 0:
            bottom_crop_height = min(bottom_height, self.pipe_img.get_height())
            bottom_crop = self.pipe_img.subsurface((0, 0, self.PIPE_WIDTH, bottom_crop_height))
            win.blit(bottom_crop, (self.x, self.bottom_pipe_top))