import pygame
class Pill():
    def __init__(self, x, y, img):
        
        self.image = pygame.image.load(img).convert_alpha()
        
        self.rect = self.image.get_rect(topleft=(x,y))
    
    def draw_pill(self,WINDOW):
        WINDOW.blit(self.image, self.rect)
        