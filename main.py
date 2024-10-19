import pygame
from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Asteroids")
  run = True
  while run:
    pygame.Surface.fill(screen, ("black"))
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
  main()