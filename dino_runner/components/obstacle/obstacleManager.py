import pygame
import random

from dino_runner.components.obstacle.cactus import CactusSmall
from dino_runner.components.obstacle.cactus import CactusLarge
from dino_runner.components.obstacle.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, CLOUD

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        probability = random.randrange(1, 9)

        if len(self.obstacles) == 0 and probability < 4:
            self.obstacles.append(CactusSmall(SMALL_CACTUS))

        elif len(self.obstacles) == 0 and probability > 3 and probability < 6:
            self.obstacles.append(CactusLarge(LARGE_CACTUS))

        elif len(self.obstacles) == 0 and probability > 6 and probability < 9:
            self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                #game.playing = False
                #break
                if not game.player.shield:
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
                        break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self, self1):
        self.obstacles = []
        