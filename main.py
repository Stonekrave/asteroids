import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  clock = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Asteroids")
 

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable )
  asteroid_field = AsteroidField()
  player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)


  run = True
  while run: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    for object in updatable:
      object.update(dt)
    pygame.Surface.fill(screen, ("black"))
    for object in drawable:
      object.draw(screen)
    for asteroid in asteroids:
      if player.check_collision(asteroid):
        print("Game Over!")
        run = False
        break
      for shot in shots:
        if shot.check_collision(asteroid):
          shot.kill()
          asteroid.split()
    pygame.display.flip()
    #Limit the framerate to 60 FPS
    dt = (clock.tick(60)) / 1000
    

    

    




if __name__ == "__main__":
  main()