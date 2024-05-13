import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
####
import pygame
from jogador import Jogador
from asteroid import Asteroid
from shot import Shot
from score import Scoreboard
from level import LevelManager
import random

#iniciando o Game / Ajuste de Janela
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Game em 2D")

# Carregar a fonte
fonte = pygame.font.Font(None, 36)

#Grupo de Sprites
drawGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

#background
bg = pygame.sprite.Sprite(drawGroup)
bg.image = pygame.image.load("data/space4.png")
bg.image = pygame.transform.scale(bg.image,[840, 480])
bg.rect = bg.image.get_rect()

#Sprites
jogador = Jogador(drawGroup)
scoreboard = Scoreboard()
level_manager = LevelManager()

#Musicas do Game
pygame.mixer.music.load("data/music.wav")
pygame.mixer.music.play(-1)

#Sons do Game
shoot = pygame.mixer.Sound("data/shoot.wav")
jump = pygame.mixer.Sound("data/Jump.wav")

gameLoop = True
clock = pygame.time.Clock()
timer = 0

pontuacao_anterior = 0

#Aqui para baixo, somente as funcionalidades do game
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    shoot.play()
                    newShot = Shot(drawGroup, shotGroup)
                    newShot.rect.center = jogador.rect.center

                elif event.key == pygame.K_SPACE:
                    jump.play()

        # Verifica Colisao
        colisao = pygame.sprite.spritecollide(jogador, asteroidGroup, False, pygame.sprite.collide_mask)
        if colisao:
            print("Game Over!")
            gameLoop = False

        # Verifica Colisao de Tiros
        tiros = pygame.sprite.groupcollide(shotGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)
        for tiro in tiros:
            scoreboard.increase_score(10)

        # Renderizar o texto da pontuação e level
        texto_pontuacao = fonte.render(f"Score: {scoreboard.get_score()}", True, (255, 255, 255))
        texto_level = fonte.render(f"Level: {level_manager.get_level()}", True, (255, 255, 255))
        if level_manager.get_level() == 1 :
            texto_dificuldade = fonte.render(f"Dificuldade: {"Facil"}", True, ("green"))
        elif level_manager.get_level() == 5:
            texto_dificuldade = fonte.render(f"Dificuldade: {"Moderado"}", True, ("blue"))
        elif level_manager.get_level() == 10:
            texto_dificuldade = fonte.render(f"Dificuldade: {"Hard"}", True, ("red"))
        elif level_manager.get_level() == 20:
            texto_dificuldade = fonte.render(f"Dificuldade: {"Deus"}", True, ("yellow"))

        #controle de level
        if scoreboard.get_score() // 100 > pontuacao_anterior:
            level_manager.increase_level()
            pontuacao_anterior = scoreboard.get_score() // 100


        # Chance de Surgimento dos asteroides
        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < level_manager.get_enemy_spawn_rate():
                novoAsteroide = Asteroid(drawGroup, asteroidGroup)


        # Update da Lógica
        drawGroup.update()

        # Draw
        display.fill([3, 252, 181])
        drawGroup.draw(display)
        display.blit(texto_pontuacao, (680, 10))
        display.blit(texto_level, (680, 40))
        display.blit(texto_dificuldade, (10, 10))

        pygame.display.update()
