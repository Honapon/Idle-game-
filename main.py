import pygame
import sys
from buttons_class import Button
#const
pygame.init()

WIDTH,HEIGHT = 960,540
WINDOW = pygame.display.set_mode([WIDTH,HEIGHT])
FONT = pygame.font.SysFont("Comic sans", 25)
#var
bg_color = (255,255,255)
bacteria = Button(400, 250, 150, 150, "bacteria", bg_color, (0,0,0))
running = True

#loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    WINDOW.fill(bg_color)
    
    bacteria.draw(WINDOW)
    
    
            
    pygame.display.update()
pygame.quit()