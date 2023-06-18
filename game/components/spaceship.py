import pygame

from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet

from game.utils.constants import SCREEN_HEIGHT, SPACESHIP, SCREEN_WIDTH

class Spaceship(Sprite):
    # declaramos constantes, estas siempre estaran escritas en mallusculas 
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEINGH = 40
    HALL_SCREEM_HEIGHT = SCREEN_HEIGHT // 2
    X_POS = (SCREEN_WIDTH // 2) - SPACESHIP_WIDTH
    Y_POS = 500 

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP,(40,60))
        self.rect = self.image.get_rect() 
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
  
    
   
    def update(self, game):
        # Obtener el estado actual de las teclas
        keys = pygame.key.get_pressed()
        
        # Comprobar las teclas de movimiento horizontal
        if keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_RIGHT]:
            self.move_right()

        # Comprobar las teclas de movimiento vertical
        if keys[pygame.K_UP]:
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.move_down()

        # Comprobar disparo
        if keys[pygame.K_e]:
            self.shoot(game.bullet_manager)
        

    
    #movimiento de jugador
    def move_left(self):

        self.rect.x -= 10
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.SPACESHIP_WIDTH

    def move_right(self):
        self.rect.x += 10

        if self.rect.left > SCREEN_WIDTH - self.SPACESHIP_WIDTH:
            self.rect.x = 0
    
    def move_up(self):
        if self.rect.y > self.HALL_SCREEM_HEIGHT:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEINGH:
            self.rect.y += 10

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))

    def shoot(self, bullet_manager):

        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)
            