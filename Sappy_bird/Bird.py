import pygame
class Bird(pygame.sprite.Sprite):


    def __init__ (self):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill([0,0,0])
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 350
        #self.pos = [50,350]
        self.cycle = 0
        self.accel = 0

    def up(self):
        self.accel = -10

    def update(self):
        if self.cycle%2 == 0:
            self.rect.y += self.accel
        if self.accel <= 5:
            self.accel += 1
        self.cycle = self.cycle % 2 + 1