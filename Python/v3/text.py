import pygame
from getfont import *

class Text:
    def __init__(self, text, size, color, surface, **kwargs):
        self.text = text
        self.size = size
        self.color = color
        self.surface = surface
        self.kwargs = kwargs
        self.surf = getfont(self.size).render(str(self.text), True, color)
        self.rect = self.surf.get_rect(**self.kwargs)
        
    def draw(self):
        self.surface.blit(self.surf, self.rect)
