#import pygame #do I need this in a class? I don't think so
from Bird import Bird
from Pipe import Pipe
import pygame
class Game(object):
    def __init__(self):
        pygame.init()
        self.bird = Bird()
        self.sw = 700
        self.sh = 500
        #maybe need to make a loop to add all the pipes into a list or someting kewl
        self.pipes = pygame.sprite.Group()
        self.birds = pygame.sprite.Group()
        self.birds.add(self.bird)
        self.screen = pygame.display.set_mode([self.sw, self.sh])
        pygame.display.set_caption("Sappy Bird Nerd")
        self.clock = pygame.time.Clock()

        for i in range(8):
            self.pipe = Pipe()
            self.pipe.rect.x = i*self.pipe.spacing
            if i%2==0:
                #bottom
                self.pipe.rect.y = 500-self.pipe.h
            else: self.pipe.rect.y = 0
            self.pipes.add(self.pipe)

        self.score = 0
        self.game_over = False
        self.start = False

    def Process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if not self.start:
                    self.start = True
                if event.key == pygame.K_UP and self.start:
                    self.bird.up()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
                self.__init__()
        return False

    def Run_logic(self):
        if self.start and not self.game_over:
            #check collision
            if len(pygame.sprite.spritecollide(self.bird,self.pipes,False))>0 or self.bird.rect.y >= (self.sh - 20) or self.bird.rect.y<0:
                self.game_over = True
                self.start = False
            #count pipes passed
            for pipe in self.pipes:
                if pipe.rect.x == self.bird.rect.x:
                    self.score+=1
            #update all locations
            self.bird.update()
            self.pipes.update()

        self.clock.tick(60)

    def Display_frame(self):
        self.screen.fill([255,255,255])
        font = pygame.font.SysFont("serif", 25)
        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            self.screen.fill([0, 0, 0])
            text = font.render("Game Over, click to restart", True, [255,255,255])
            center_x = (self.sw// 2) - (text.get_width() // 2)
            center_y = (self.sh // 2) - (text.get_height() // 2)
            self.screen.blit(text, [center_x, center_y])
        else:
            score_text = font.render("Score: "+str(self.score),True,[0,0,0])
            self.pipes.draw(self.screen)
            self.birds.draw(self.screen)
            center_sx = (self.sw//2)- (score_text.get_width()//2)
            self.screen.blit(score_text,[center_sx,5])
        pygame.display.flip()
