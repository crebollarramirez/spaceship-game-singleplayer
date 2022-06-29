import pygame, os
pygame.font.init()
pygame.mixer.init()

class Game():
    FPS = 60

    # Winning Text 
    HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
    WINNER_FONT = pygame.font.SysFont('comicsans', 100)

    # Sounds
    BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'AH_SHIT.mp3'))
    BULLET_HIT_SOUND.set_volume(0.2)
    BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'PEW.mp3'))
    BULLET_FIRE_SOUND.set_volume(0.2)

    GAMEOVER = pygame.mixer.Sound(os.path.join('Assets', 'GAMEOVER.mp3'))

    # Colors
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    
    def __init__(self, name, width, height):
        self.WIDTH = width
        self.HEIGHT = height
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

        red_health_text = self.HEALTH_FONT.render("HEALTH: " + str(bot.health), 1, self.WHITE)
        yellow_health_text = self.HEALTH_FONT.render("HEALTH: " + str(player.health), 1, self.WHITE)
        self.WIN.blit(red_health_text, (self.WIDTH - red_health_text.get_width() - 10, 10))
        self.WIN.blit(yellow_health_text, (10, 10))


        self.WIN.blit(player.image, (player.ship.x, player.ship.y))
        self.WIN.blit(bot.image, (bot.ship.x, bot.ship.y))


        for bullet in bot_bullets:
            pygame.draw.rect(self.WIN, self.RED, bullet)

        for bullet in player_bullets:
            pygame.draw.rect(self.WIN, self.YELLOW, bullet)
        
        pygame.display.update()   

    def endGame(self, NPC, Player):
        winner_text = ""

        if NPC.health <= 0:
            winner_text = "YOU WIN!"
        
        if Player.health <= 0:
            winner_text = "YOU LOST!"

        if winner_text != "":
            self.GAMEOVER.play()
            self.draw_winner(winner_text)
            return 1

class Spaceship():
    MAX_BULLETS = 3
    health = 10
    BULLET_VEL = 7
    HIT = pygame.USEREVENT + 1
    
    def __init__(self, image, game, ship_width, ship_height, velocity):
        self.game = game
        self.image = image
        self.ship_width = ship_width
        self.ship_height = ship_height
        self.VEL = velocity
        self.bullets = []

        self.ship = pygame.Rect(0,0, ship_width, ship_height) # x,y,WIDTH,HEIGHT
        self.image =  pygame.transform.rotate(pygame.transform.scale(image, (self.ship_width,self.ship_height)),90)

        # Start Location
        self.ship.x = 0
        self.ship.y = self.game.HEIGHT//2 - self.ship.height

    def handle_movements(self,keys_pressed):
        if keys_pressed[pygame.K_a] and self.ship.x - self.VEL > 0:    # left
            self.ship.x -= self.VEL
        if keys_pressed[pygame.K_d] and self.ship.x + self.VEL + self.ship.width - 20 < self.game.BORDER.x : # right
            self.ship.x += self.VEL
        if keys_pressed[pygame.K_w] and self.ship.y - self.VEL > 0: # up
            self.ship.y -= self.VEL
        if keys_pressed[pygame.K_s] and self.ship.y + self.VEL + self.ship.height < self.game.HEIGHT - 15: # down
            self.ship.y += self.VEL
    
    def handle_bullets(self, bot):
     for bullet in self.bullets:
        bullet.x += self.BULLET_VEL
        if bot.ship.colliderect(bullet):
            pygame.event.post(pygame.event.Event(bot.HIT))
            self.bullets.remove(bullet)
        elif bullet.x > self.game.WIDTH:
            self.bullets.remove(bullet)

class AI(Spaceship):
    def __init__(self, image, game, ship_width, ship_height, velocity):
        super().__init__(image, game, ship_width, ship_height, velocity)
        self.image = pygame.transform.rotate(pygame.transform.scale(image, (self.ship_width,self.ship_height)),270)
        self.HIT = pygame.USEREVENT + 2

        # Starting Location
        self.ship.x = self.game.WIDTH - self.ship.width
        self.ship.y = self.game.HEIGHT//2 - self.ship.height

    def handle_bullets(self, Player):
     for bullet in self.bullets:
        bullet.x -= self.BULLET_VEL
        if Player.ship.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Player.HIT))
            self.bullets.remove(bullet)
        elif bullet.x > self.game.WIDTH:
            self.bullets.remove(bullet)

    def handle_movements(self):
        if self.ship.y > 0:
            self.VEL = self.VEL * -1
        if self.ship.y < self.game.HEIGHT - 15:
            self.VEL = self.VEL * -1
        
        self.ship.y += self.VEL 

