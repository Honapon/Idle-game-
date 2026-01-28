import pygame
class Pill():
    def __init__(self, x, y):
        
        self.image = pygame.image.load('sprites/pille.png').convert_alpha()
        
        self.rect = self.image.get_rect(topleft=(x,y))
    
    def draw_pill(self,WINDOW):
        WINDOW.blit(self.image, self.rect)
        