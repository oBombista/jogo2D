# level.py

class LevelManager:
    def __init__(self):
        self.level = 1
        self.enemy_spawn_rate = 0.3  # Taxa de surgimento inicial de inimigos

    def increase_level(self):
        self.level += 1
        self.enemy_spawn_rate += 0.1  # Aumenta a taxa de surgimento de inimigos a cada nível

    def get_level(self):
        return self.level

    def get_enemy_spawn_rate(self):
        return self.enemy_spawn_rate
