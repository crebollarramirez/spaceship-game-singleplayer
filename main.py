import pygame, os
from Spaceship import Spaceship, AI, Game
pygame.font.init()
pygame.mixer.init()

def main():
    game = Game("Singleplayer", 900, 500)

    image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
    Player = Spaceship(image, game, 55, 40, 5)

    image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
    NPC = AI(image, game, 55, 40, 5)

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(Player.bullets) < Player.MAX_BULLETS:
                    bullet = pygame.Rect(Player.ship.x + Player.ship_width, Player.ship.y + Player.ship_height//2 - 2, 10, 5) 
                    Player.bullets.append(bullet)
                    game.BULLET_FIRE_SOUND.play()

            if event.type == Player.HIT:
                Player.health -= 1
                game.BULLET_HIT_SOUND.play()

            if event.type == NPC.HIT:
                NPC.health -= 1
                game.BULLET_HIT_SOUND.play()

        winner_text = ""
        if NPC.health <= 0:
            winner_text = "YOU WIN!"
        
        if Player.health <= 0:
            winner_text = "YOU LOST!"

        if winner_text != "":
            game.draw_winner(winner_text)
            break
        
        keys_pressed = pygame.key.get_pressed()
        Player.handle_movements(keys_pressed)
        Player.handle_bullets(NPC)

        game.draw_window(NPC, Player, NPC.bullets, Player.bullets, Player.health, NPC.health)
    main()
if __name__ == "__main__":
    main()
