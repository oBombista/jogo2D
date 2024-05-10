
class LevelManager:
    def __init__(self):
        self.level = 1
        self.enemy_spawn_rate = 0.3

    def increase_level(self):
        self.level += 1
        self.enemy_spawn_rate += 0.1

    def get_level(self):
        return self.level

    def get_enemy_spawn_rate(self):
        return self.enemy_spawn_rate
