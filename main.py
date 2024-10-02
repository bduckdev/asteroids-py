import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player =  Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            asteroid_is_colliding = asteroid.check_collision(player)
            for shot in shots:
                shot_is_colliding = shot.check_collision(asteroid)
                if shot_is_colliding == True:
                    shot.kill()
                    asteroid.split()
            if asteroid_is_colliding == True:
                print("Game Over!")
                exit()

        pygame.display.flip()

        tick = clock.tick(60)
        dt = tick / 1000

if __name__ == "__main__":
    main()
