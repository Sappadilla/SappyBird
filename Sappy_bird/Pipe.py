import pygame, random
class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #add random here to randomize the height
        self.h = random.randrange(150,350)
        self.image = pygame.Surface((20,self.h))
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.spacing = 125

    def update(self):
        if self.rect.x <= 0:
            if self.rect.y == 0:
                self.__init__()
                self.rect.y = 0
            else:
                self.__init__()
                self.rect.y = 500 - self.h
            self.rect.x = 8 * self.spacing
            #self.image = pygame.Surface((20, self.h))
            #self.image.fill([0,255,0])
        self.rect.x+=-2
