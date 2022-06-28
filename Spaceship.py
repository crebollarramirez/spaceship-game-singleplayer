import pygame
import os
pygame.font.init()
pygame.mixer.init()

class Game():
    FPS = 60

    # Winning Text 
    HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
    WINNER_FONT = pygame.font.SysFont('comicsans', 100)

    # Sounds
    BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'AH_SHIT.mp3'))
    BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'PEW.mp3'))

    # Colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    
    def __init__(self, name, width, height, velocity):
        self.WIDTH = width
        self.HEIGHT = height
        self.VEL = velocity
        self.BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (self.WIDTH, self.HEIGHT))
        
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.BORDER = pygame.Rect(self.WIDTH//2 - 5, 0, 10, self.HEIGHT)

        WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(name)

    def draw_winner(self, text):
        draw_text = self.WINNER_FONT.render(text, 1, self.WHITE)
        self.WIN.blit(draw_text, (self.WIDTH//2 - draw_text.get_width()//2, self.HEIGHT//2 - draw_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(5000)
    
    
    def draw_window(self, bot, player, bot_bullets, player_bullets, bot_health, player_health):
        self.WIN.blit(self.BACKGROUND, (0,0))
        pygame.draw.rect(self.WIN, self.BLACK, self.BORDER)

        red_health_text = self.HEALTH_FONT.render("HEALTH: " + str(red_health), 1, self.WHITE)
        yellow_health_text = self.HEALTH_FONT.render("HEALTH: " + str(yellow_health), 1, self.WHITE)
        self.WIN.blit(red_health_text, (self.WIDTH - red_health_text.get_width() - 10, 10))
        self.WIN.blit(yellow_health_text, (10, 10))


        # EDIT THIS ---------------------------
        self.WIN.blit(player, (player.x, player.y))
        self.WIN.blit(bot, (bot.x, bot.y))
        # _________________________________________________

        for bullet in bot_bullets:
            pygame.draw.rect(self.WIN, self.RED, bullet)

        for bullet in player_bullets:
            pygame.draw.rect(self.WIN, self.YELLOW, bullet)
        
        pygame.display.update()   


class Spaceship(Game):
    def __init__(self, image, ship_width, ship_height, velocity):
        self.image = image
        self.ship_width = ship_width
        self.ship_height = ship_height
        self.VEL = velocity

        self.ship = pygame.Rect(0,0, ship_width, ship_height) # x,y,WIDTH,HEIGHT

    def handle_movements(self,keys_pressed):
        if keys_pressed[pygame.K_a] and self.ship.x - super.VEL > 0:    #left
            self.ship.x -= super.VEL
        if keys_pressed[pygame.K_d] and self.ship.x + super.VEL + self.ship.width < BORDER.x:    #right
            self.ship.x += super.VEL
        if keys_pressed[pygame.K_w] and self.ship.y - super.VEL > 0:    #up
            self.ship.y -= super.VEL
        if keys_pressed[pygame.K_s] and self.ship.y + super.VEL + self.ship.height < HEIGHT - 15:    #down
            self.ship.y += super.VEL

    def shoot():
        pass
    
    def location(xcord, ycord):
        pass

class AI(Spaceship):
    def handle_movements(self, keys_pressed):
        pass

