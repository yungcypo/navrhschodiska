import pygame
from getfont import *

class Button:
    def __init__(self, text, textsize, foreground, background, hovercolor, clickedcolor, surface, **kwargs):
        self.text = str(text)
        self.textsize = textsize
        self.foreground = foreground
        self.background = background
        self.hovercolor = hovercolor
        self.clickedcolor = clickedcolor
        self.surface = surface
        self.kwargs = kwargs

        self.padding = self.textsize/2

        self.update()

        self.border_radius = int(self.textsize/7)
        self.color = self.background
        self.outline_color = self.foreground
        self.disabled = False
        self.hover = False
        self.clicked = False
        self.active = False

    def update(self):
        self.text_surf = getfont(self.textsize).render(self.text, True, self.foreground)
        self.text_rect = self.text_surf.get_rect(**self.kwargs)
        self.surf = pygame.surface.Surface((self.text_rect.width + self.padding * 2, self.text_rect.height + self.padding * 2))
        self.rect = self.surf.get_rect(center = self.text_rect.center)
        self.outline_width = 2
        self.outline_surf = pygame.surface.Surface((self.text_rect.width + self.padding * 2 + self.outline_width, self.text_rect.height + self.padding * 2 + self.outline_width))
        self.outline_rect = self.outline_surf.get_rect(center = self.text_rect.center)

    def check(self):  # check hover and clicked
        if not self.disabled:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.hover = True
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    self.clicked = False
            else:
                self.hover = False

    def draw(self):
        self.check()
        if self.hover:
            self.color = self.hovercolor
            if not self.disabled and self.clicked:
                self.active = True
            else:
                self.outline_color = self.hovercolor
        else:
            self.color = self.background

        if self.active:
            self.outline_color = self.foreground
        else:
            self.outline_color = self.clickedcolor

        pygame.draw.rect(self.surface, self.outline_color, self.outline_rect, border_radius = self.border_radius)
        pygame.draw.rect(self.surface, self.color, self.rect, border_radius = self.border_radius)
        self.surface.blit(self.text_surf, self.text_rect)
