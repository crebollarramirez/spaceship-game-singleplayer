import pygame
import os
from Spaceship import Spaceship, AI, Game


def main():
    game = Game("Singleplayer", 900, 500)

    image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
    Player = Spaceship(image, 55, 40, 5)

    image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
    NPC = AI(image, 55, 40, 5)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        game.draw_window()

