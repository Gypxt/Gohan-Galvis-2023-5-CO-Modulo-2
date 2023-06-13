import pygame

from pygame.sprite import Sprite
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
    
   
    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
    
    #movimiento de jugador
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10

    def move_up(self):
        if self.rect.y > self.HALL_SCREEM_HEIGHT:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.SPACESHIP_HEINGH:
            self.rect.y += 10

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
