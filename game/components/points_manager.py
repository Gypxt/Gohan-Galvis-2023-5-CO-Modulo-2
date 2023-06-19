import pygame

from game.utils.constants import FONT_STYLE

class PointManager:
    def __init__(self):
        self.point = 0
        self.death_count = 0
        self.highest_score = 0

    def update(self):
        self.point += 1
        if self.point > self.highest_score:
            self.highest_score = self.point

    def reset(self):
        self.point = 0

    def draw_score(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text_1 = font.render(f'Score: {self.point}', True, (255, 255,255))
        text_rect_1= text_1.get_rect()
        text_rect_1.center = (1000, 50)
        screen.blit(text_1, text_rect_1)
     
    
    def have_point(self, ponit_have):
        self.point = ponit_have