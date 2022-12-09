import pygame

from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                #game.playing = False
                #break
                pygame.time.delay(70)
                self.obstacles = []

                game.player_heart_manager.reduce_heart()

                if game.player_heart_manager.heart_count > 0:
                    game.player.shield = True
                    game.player.show_text = False
                    star_time = pygame.time.get_ticks()
                    game.player.shield_time_up = star_time + 1000
                else:
                    pygame.time.delay(50)
                    game.playing = False
                    game.death_count += 1

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self, self1):
        self.obstacles = []
        