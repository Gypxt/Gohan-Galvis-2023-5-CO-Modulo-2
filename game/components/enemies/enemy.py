import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT, ENEMY_1, ENEMY_2, SCREEN_WIDTH

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEINGH = 40
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
    Y_POS = 40
    SPEED_X = 5
    SPEED_Y = 5
    mov_x = {0:'left', 1:'right'}
    TYPE = {0:pygame.transform.scale(ENEMY_1,(40,60)), 1:pygame.transform.scale(ENEMY_2,(40,60))}

    def __init__(self):
        self.image = self.TYPE[random.randint(0, 1)]
        self.rect = self.image.get_rect() 
        self.rect.x = self.X_POS_LIST[random.randint(0, 14)]
        self.rect.y = self.Y_POS 
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.mov_x[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0

        if self.image == self.TYPE[1]:  # Si la imagen es "enemy_2"
            self.speed_x += 5  # Aumentar la velocidad en 5 unidades



    def update(self, ships):

        self.rect.y += self.speed_y

        if self.movement_x == 'left' :
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT :
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))

    def change_movement_x(self):
        self.index += 1 
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH) :
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10 ):
            self.movement_x = 'right'
            self.index = 0