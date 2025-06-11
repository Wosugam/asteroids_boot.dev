import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_player = Player(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        main_player.update(dt)
            
        screen.fill((0,0,0))
        main_player.draw(screen)
        pygame.display.flip()

        dt = fps.tick(60)/1000

if __name__ == "__main__":
    main()