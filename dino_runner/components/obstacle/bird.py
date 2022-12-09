from dino_runner.components.obstacle.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.fly_steps = 0

    def fly (self, screen):
        if self.fly_steps >= 0:
            self.fly_steps = 0
        screen.blit(self.image[self.fly_steps // 5], self.rect)
        self.fly_steps += 1