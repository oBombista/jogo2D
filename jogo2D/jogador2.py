import pygame
import math

class GorilaRed(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/GorilaRed.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(380, 180, 100, 100)

        self.timer = 0

    def update(self, *args, **kwargs):
        #LOGICA do JOGO
        self.timer += 0.001

        self.rect.x = 100 + math.sin(self.timer) * 200

