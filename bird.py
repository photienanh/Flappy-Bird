import pygame

class Bird:
    def __init__(self, HEIGHT, JUMP, GRAVITY, bird_img):
        self.x = 100
        self.y = HEIGHT // 2
        self.vel = 0
        self.JUMP = JUMP
        self.GRAVITY = GRAVITY
        self.rect = pygame.Rect(self.x, self.y, 30, 30)
        self.bird_img = bird_img

    def update(self):
        self.vel += self.GRAVITY
        self.y += self.vel
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.vel = self.JUMP

    def draw(self, win):
        win.blit(self.bird_img, (self.x, self.y))