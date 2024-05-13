import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Nave.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(40, 180, 100, 100)

        self.speedY = 0
        self.speedX = 0
        self.acceleration = 0.1

    def update(self, *args, **kwargs):
        #LOGICA do JOGO
        keys = pygame.key.get_pressed()

        #movimentos eixo X
        if keys[pygame.K_d]:
            self.speedX += self.acceleration
        elif keys[pygame.K_a]:
            self.speedX -= self.acceleration
        else:
            self.speedX *= 0.95
        self.rect.x += self.speedX

        #Movimentos no Eixo Y
        if keys[pygame.K_s]:
            self.speedY += self.acceleration
        elif keys[pygame.K_w]:
            self.speedY -= self.acceleration
        else:
            self.speedY *= 0.95
        self.rect.y += self.speedY


        #Limites de extremidades
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedY = 0

        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speedY = 0

        elif self.rect.right > 840:
            self.rect.right = 840
            self.speedX = 0

        elif self.rect.left < 0:
            self.rect.left = 0
            self.speedX = 0



