import pygame
import random

class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/GorilaRed.png")
        self.image = pygame.transform.scale(self.image, [10, 10])
        self.rect = self.image.get_rect()

        #Velocidade do Tiro
        self.speed = 4

    def update(self, *args, **kwargs):
        #LOGICA do TIRO
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()

