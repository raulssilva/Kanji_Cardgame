import pygame

pygame.init()
screen = pygame.display.set_mode((795, 415))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()