import pygame, sys
from button import *
from getfont import *
from inputbox import *
from text import *

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60
W, H = 900, 600
SCREEN = pygame.display.set_mode((W, H)) # make pygame window
TITLE = pygame.display.set_caption("Návrh schodiska")
ICON = pygame.image.load("assets\images\icon.png")
pygame.display.set_icon(ICON)

colors = {
    "white" : (255, 255, 255),
    "gray" : (20, 20, 20),
    "lightgray" : (50, 50, 50),
    "lightergray" : (100, 100, 100),
    "lightestgray" : (150, 150, 150),
    "black" : (0, 0, 0)}

R = None  # Počet ramien
KV = None  # Konštrukčná výška
N = None  # Počet stupňov
H = None  # Výška stupňa
B = None  # Šírka stupňa
L = None  # Dĺžka ramena
P = None  # Podesta - šírka podesty
M = None  # Medzipodesta - šírka medzipodesty
A = None  # Alfa - sklon ramena
H1 = None  # Podchodná výška
H2 = None  # Priechodná výška



fontsize = 24

text_nadpis = Text("Návrh schodiska", int(fontsize*2) , colors["white"], SCREEN, topleft = (fontsize, fontsize))
text_typ_schodiska = Text("Typ schodiska", int(fontsize*1.25), colors["white"], SCREEN, 
    topleft = (fontsize*1.5, text_nadpis.rect.bottom + fontsize))

button_jednoramenne = Button("Jednoramenné", fontsize, colors["white"], colors["gray"], colors["lightgray"], colors["lightergray"], SCREEN,
    topleft = (text_typ_schodiska.rect.left + fontsize, text_typ_schodiska.rect.bottom + fontsize))
button_dvojramenne = Button("Dvojramenné", fontsize, colors["white"], colors["gray"], colors["lightgray"], colors["lightergray"], SCREEN,
    topleft = (button_jednoramenne.rect.right + fontsize, button_jednoramenne.rect.top + fontsize/2))
buttons_typ_shodiska = [button_jednoramenne, button_dvojramenne]

text_konstrukcna_vyska = Text("Konštrukčná výška ", int(fontsize*1.25), colors["white"], SCREEN,
    topleft = (fontsize*1.5, button_jednoramenne.rect.bottom + fontsize))
text_konstrukcna_vyska_mm = Text("[mm]", int(fontsize*1.25), colors["lightestgray"], SCREEN,
    bottomleft = text_konstrukcna_vyska.rect.bottomright)
inputbox_konstrukcna_vyska = Inputbox("", fontsize, colors["white"], colors["gray"], colors["lightgray"], SCREEN, 
    topleft = (text_konstrukcna_vyska.rect.left + fontsize, text_konstrukcna_vyska.rect.bottom + fontsize))

inputboxes = [inputbox_konstrukcna_vyska]

def update_values():
    global R, KV
    if button_jednoramenne.active:
        R = 1
    elif button_dvojramenne.active:
        R = 2

    try:
        KV = int(inputbox_konstrukcna_vyska.get_value())
    except:
        KV = 0

def main():
    global KV
    FPS_COUNT = 1

    for i in buttons_typ_shodiska:
        i.active = False
    button_jednoramenne.active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            update_values()
            if event.type == pygame.KEYDOWN:
                for i in inputboxes:
                    if not i.disabled:
                        if event.key == pygame.K_BACKSPACE:
                            i.value = i.value[:-1]
                        if event.key == pygame.K_RETURN:
                            i.disabled = True
                        else:
                            i.value += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_jednoramenne.hover:
                    for i in buttons_typ_shodiska:
                        i.active = False
                    button_jednoramenne.active = True
                if button_dvojramenne.hover:
                    for i in buttons_typ_shodiska:
                        i.active = False
                    button_dvojramenne.active = True

        SCREEN.fill(colors["gray"])

        text_nadpis.draw()
        pygame.draw.aaline(SCREEN, colors["white"], (fontsize, text_nadpis.rect.bottom + fontsize/2), (W - fontsize, text_nadpis.rect.bottom + fontsize/2))
        text_typ_schodiska.draw()

        button_jednoramenne.draw()
        button_dvojramenne.draw()

        text_konstrukcna_vyska.draw()
        text_konstrukcna_vyska_mm.draw()
        inputbox_konstrukcna_vyska.draw()  

        if KV > 0:
            N = round(KV/170)















        for i in inputboxes:
            if not i.disabled and FPS_COUNT < int(FPS/2):
                i.draw_cursor()

        FPS_COUNT += 1
        if FPS_COUNT >= FPS:
            FPS_COUNT = 1

        CLOCK.tick(FPS)
        pygame.display.update()

main()
