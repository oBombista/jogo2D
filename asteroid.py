import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/GorilaRed.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(380, 180, 100, 100)

        #Surgimento dos asteroides
        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)
        self.speed = 1 + random.random() * 2


    def update(self, *args, **kwargs):
        #LOGICA dos ASTEROIDES
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
            print("morri!")
