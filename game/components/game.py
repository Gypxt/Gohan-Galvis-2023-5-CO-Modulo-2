import pygame


from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.enemies.enemy import Enemy
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.points_manager import PointManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu( self.screen)
        self.running = False
        self.points = PointManager()
        
        

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()
    
      
    def run(self):
        # Game loop: events - update - draw
        self.game_reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.player.update(self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.points.draw_score(self.screen)
        pygame.display.update()
        # pygame.display.flip()
        

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset(self.screen)
        
        half_screen_whidth = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        if self.points.death_count == 0:
            self.menu.draw(self.screen, 'Press Any KeyTo Star....')    
        else:
            self.menu.draw(self.screen, 'Press Any KeyTo Star....')    
            self.menu.draw(self.screen, f'Score: {self.points.point}', half_screen_whidth, 350)    
            self.menu.draw(self.screen, f'Deaths: {self.points.death_count}', half_screen_whidth, 400)    
            self.menu.draw(self.screen, f'Highest Score: {self.points.highest_score}', half_screen_whidth, 450)    
            pass
        icon = pygame.transform.scale(ICON,(80, 120))
        self.screen.blit(icon, (half_screen_whidth - 50, half_screen_height - 150))

        self.menu.update(self)

    def game_reset(self):
        self.player.reset()
        self.enemy_manager.reset()
        self.points.reset()
        self.bullet_manager.reset()

    