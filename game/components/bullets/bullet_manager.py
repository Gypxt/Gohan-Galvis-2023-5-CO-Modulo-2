import random
import pygame
from game.components.bullets.bullet import Bullet

from game.utils.constants import AUTO_FIRE_TYPE, EXPLOSION, SHIELD_TYPE 

class BulletManager():
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)
            

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    EXPLOSION.play()
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.points.update()
                    
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.points.death_count += 1
                    game.playing = False
                    pygame.time.delay(500)
                    break

        for enemy in game.enemy_manager.enemies:
            if enemy.bullet_cooldown <= pygame.time.get_ticks():
                bullet = Bullet(enemy)
                self.enemy_bullets.append(bullet)
                enemy.bullet_cooldown = pygame.time.get_ticks() + random.randint(30, 50)

        if game.player.has_powe_up and game.player.power_up_type == AUTO_FIRE_TYPE:
            if len(self.bullets) < 10000:
                
                bullet = Bullet(game.player)
                self.bullets.append(bullet)


    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)

        if bullet.owner == 'player' and len(self.bullets) < 6:
            self.bullets.append(bullet)
    
    def reset(self):
        
        self.bullets = []
        self.enemy_bullets = []