import pygame
import random
from game.components.power_ups.auto_fire import AutoFire
from game.components.power_ups.shied import Shield

from game.utils.constants import SPACESHIP_SHIELD, TAKE_POWER_UP

class PowerUpManager:
    MIN_TIME_POWER_UP = 5000
    MAX_TIME_POWER_UP = 10000
    POWER_UP_TYPES = [Shield, AutoFire]
    
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.duration = random.randint(3, 5)
        self.powerup_sound_played = False

    def generate_power_up(self):
        power_up_type = random.choice(self.POWER_UP_TYPES)
        power_up = power_up_type()  # Crea una instancia del power-up seleccionado
        self.when_appears += random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.power_ups.append(power_up)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):

                if not self.powerup_sound_played:
                    TAKE_POWER_UP.play()
                    self.powerup_sound_played = True

                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_powe_up = True
                game.player.powe_time_up = power_up.start_time + (self.duration * 1000)

                if power_up.type == Shield.TYPE:
                    game.player.set_image((67, 75), SPACESHIP_SHIELD)
                    
                self.power_ups.remove(power_up)
                self.powerup_sound_played = False


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + self.MIN_TIME_POWER_UP, now + self.MAX_TIME_POWER_UP)
        self.powerup_sound_played = False