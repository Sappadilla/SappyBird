import pygame
from Game import Game

#screen_w = 700
#screen_h = 500

def main():

    done = False
    game = Game()

    while not done:
        done = game.Process_events()
        game.Run_logic()
        game.Display_frame()
    pygame.quit()

if __name__ == "__main__":
    main()
