import pygame
import sys
from constants import *
from player import Player
from asteroid import *
from asteroidfield import AsteroidField

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable) 
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    main_player = Player(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)) 

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(main_player):
                print("Game Over!")
                sys.exit()
        
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    

            
        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = fps.tick(60)/1000

if __name__ == "__main__":
    main()