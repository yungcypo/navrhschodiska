import pygame 
from getfont import *

class Inputbox:
    def __init__(self, value, textsize, foreground, background, inactive, surface, **kwargs):
        self.value = value
        self.textsize = textsize
        self.foreground = foreground
        self.background = background
        self.inactive = inactive
        self.surface = surface
        self.kwargs = kwargs

        self.surf = getfont(self.textsize).render(self.value, True, self.foreground)
        self.rect = self.surf.get_rect(**self.kwargs)
        self.rect.width = self.textsize * 20

        self.padding = self.textsize/2
        self.outline_width = 2
        self.outline_surf = pygame.surface.Surface((self.rect.width + self.padding * 2 + self.outline_width, self.rect.height + self.padding * 2 + self.outline_width))
        self.outline_rect = self.outline_surf.get_rect(center = self.rect.center)
        self.inline_surf = pygame.surface.Surface((self.rect.width + self.padding * 2, self.rect.height + self.padding * 2))
        self.inline_rect = self.inline_surf.get_rect(center = self.rect.center)
        self.border_radius = int(self.textsize/7)
        self.disabled = True
    
    def get_value(self):
        return self.value

    def check(self): 
        if pygame.mouse.get_pressed()[0]:
            if self.inline_rect.collidepoint(pygame.mouse.get_pos()):
                self.disabled = False
            else:
                self.disabled = True

        if self.disabled:
            self.outline_color = self.inactive
        else:
            self.outline_color = self.foreground

    def draw_cursor(self):
        pygame.draw.aaline(self.surface, self.foreground, self.rect.topright, self.rect.bottomright)

    def draw(self):
        self.check()

        self.surf = getfont(self.textsize).render(self.value, True, self.foreground)
        self.rect = self.surf.get_rect(**self.kwargs)
        
        pygame.draw.rect(self.surface, self.outline_color, self.outline_rect, border_radius = self.border_radius)
        pygame.draw.rect(self.surface, self.background, self.inline_rect, border_radius = self.border_radius)
        self.surface.blit(self.surf, self.rect)

    