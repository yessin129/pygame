import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("runner")

while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
           pygame.quit()
           exit()
    #draw all our elements test
    #update evereything
     pygame.display.update
