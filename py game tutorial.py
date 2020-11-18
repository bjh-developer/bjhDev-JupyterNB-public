#pygame tutorial by freeCodeCampus.org, built in Visual Studio Code with Python 3 + pygame
import pygame

#initialise pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800, 600))

#title & icon




#game loop  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False