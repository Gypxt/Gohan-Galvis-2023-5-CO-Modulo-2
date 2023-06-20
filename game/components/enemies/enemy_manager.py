from game.components.enemies.enemy import Enemy

class EnemyManager:

    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy(game)

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            enemy.shoot(game.bullet_manager)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self, game):
        if game.points.point >= 5:
            if len(self.enemies) < 5:
                enemy = Enemy()
                self.enemies.append(enemy)
                enemy.shoot(game.bullet_manager)

        if len(self.enemies) < 1:
            enemy = Enemy()
            self.enemies.append(enemy)
            

    def reset(self):
        for enemy in self.enemies:
            self.enemies.remove(enemy)