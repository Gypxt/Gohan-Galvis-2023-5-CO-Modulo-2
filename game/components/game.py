import pygame


from game.utils.constants import BG, FONT_STYLE, ICON, MUSIC_GAME, SCREEN_HEIGHT, SCREEN_WIDTH, SOUND_GAMEOVER, TITLE, FPS, DEFAULT_TYPE, TX_GAMEOVER_P1, TX_GAMEOVER_P2
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.enemies.enemy import Enemy
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.points_manager import PointManager
from game.components.power_ups.power_up_manager import PowerUpManager

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
        self.power_up_manager = PowerUpManager()
        self.game_over_sound_played = False
        
        

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
        MUSIC_GAME.play()
        self.playing = True
        self.game_over_sound_played = False
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
        self.power_up_manager.update(self)

        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.points.draw_score(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
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
            MUSIC_GAME.stop()
            if not self.game_over_sound_played:  # Verificar si el sonido ya ha sido reproducido
                SOUND_GAMEOVER.play()
                self.game_over_sound_played = True
            text_game_over = pygame.transform.scale(TX_GAMEOVER_P1,(400 , 117))
            self.screen.blit(text_game_over, (80, half_screen_height - 60))
            text_game_over = pygame.transform.scale(TX_GAMEOVER_P2,(400 , 117))
            self.screen.blit(text_game_over, (650 , half_screen_height - 55))
            self.menu.draw(self.screen, f'Score: {self.points.point}', half_screen_whidth, 260)    
            self.menu.draw(self.screen, f'Deaths: {self.points.death_count}', half_screen_whidth, 310)    
            self.menu.draw(self.screen, f'Highest Score: {self.points.highest_score}', half_screen_whidth, 360)    
        
        self.menu.update(self)

    def game_reset(self):
        self.player.reset()
        self.enemy_manager.reset()
        self.points.reset()
        self.bullet_manager.reset()
        self.power_up_manager.reset()
        

    def draw_power_up_time(self):
        if self.player.has_powe_up:
            time_to_show = round((self.player.powe_time_up - pygame.time.get_ticks())/ 1000, 2)

            if time_to_show >= 0:
                self.menu.draw(self.screen,f'{self.player.power_up_type.capitalize()} is enable for {time_to_show}', 540, 50, (255, 255, 255))
            else:
                self.player.has_powe_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()