import pygame

class Button:
    def __init__(self, x, y, width, height, text, text_color, button_color):
        self._rect = pygame.Rect(x, y ,width ,height)
        self._text = text
        self._text_color = text_color
        self._button_color = button_color
        self.font = pygame.font.Font(None, 36)
    
    def draw(self, WINDOW):
        pygame.draw.rect(WINDOW, self._button_color, self._rect)
        text_surface = self.font.render(self._text, True, self._text_color)
        text_rect = text_surface.get_rect(center=self._rect.center)
        WINDOW.blit(text_surface, text_rect)
        