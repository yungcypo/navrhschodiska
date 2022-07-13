import pygame, sys, math
from button import *
from getfont import *
from inputbox import *
from text import *

'''
TODO

Výška stupňa
Scroll

'''


pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60
SCREEN_W, SCREEN_H = 900, 600
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H)) # make pygame window
TITLE = pygame.display.set_caption("Návrh schodiska")
ICON = pygame.image.load("assets\images\icon.png")
pygame.display.set_icon(ICON)

colors = {
    "white" : (255, 255, 255),
    "gray" : (20, 20, 20),
    "lightgray" : (50, 50, 50),
    "lightergray" : (100, 100, 100),
    "lightestgray" : (150, 150, 150),
    "black" : (0, 0, 0),
    "red" : (255, 0, 0)}

R = None  # Počet ramien
KV = None  # Konštrukčná výška
N = None  # Počet stupňov
N1, N2 = None, None  # Pomocné premenné pri výpočte počtu stupňov
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

text_pocet_stupnov = Text("Počet stupňov ", int(fontsize*1.25), colors["white"], SCREEN,
    topleft = (fontsize*1.25, inputbox_konstrukcna_vyska.rect.bottom + fontsize))
text_pocet_stupnov_nevyhovuje_norme = Text("Hodnota označená červenou farbou nevyhovuje norme", int(fontsize*0.75), colors["lightestgray"], SCREEN,
    midleft = text_pocet_stupnov.rect.midright)
button_pocet_stupnov_1 = Button("0", fontsize, colors["white"], colors["gray"], colors["lightgray"], colors["lightergray"], SCREEN,
    topleft = (text_pocet_stupnov.rect.left + fontsize, text_pocet_stupnov.rect.bottom + fontsize))
button_pocet_stupnov_2 = Button("0", fontsize, colors["white"], colors["gray"], colors["lightgray"], colors["lightergray"], SCREEN,
    topleft = (button_pocet_stupnov_1.rect.right + fontsize, text_pocet_stupnov.rect.bottom + fontsize))
buttons_pocet_stupnov = [button_pocet_stupnov_1, button_pocet_stupnov_2]

text_vyska_stupna = Text("Výška stupňa", fontsize, colors["white"], SCREEN, 
    topleft = (fontsize * 1.25, button_pocet_stupnov_1.rect.bottom + fontsize))
button_vyska_stupna = Button(H, fontsize, colors["white"], colors["gray"], colors["lightgray"], colors["lightergray"], SCREEN,
    topleft = (text_vyska_stupna.rect.left + fontsize, text_vyska_stupna.rect.bottom + fontsize))


inputboxes = [inputbox_konstrukcna_vyska]

def update_values():
    global R, KV, N, N1, N2, H
    global nevyhovuje_norme
    nevyhovuje_norme = False
    if button_jednoramenne.active:
        R = 1
    elif button_dvojramenne.active:
        R = 2

    try:
        KV = int(inputbox_konstrukcna_vyska.get_value())
    except:
        KV = 0
    
    if inputbox_konstrukcna_vyska.disabled:
        try:
            N = KV/170
        except:
            N = None

    if N != None and N > 0:
        if R == 1:
            N1 = math.floor(N)
            N2 = math.ceil(N)
        if R == 2:
            N1 = round(N)
            if N1 % 2 == 0:
                if N1 >= N:
                    N2 = N1
                    N1 -= 2
            elif N1 % 2 == 1:
                N1 -= 1
                N2 = N1 + 1

        if KV / N1 > 180:
            button_pocet_stupnov_1.foreground = colors["red"]
            nevyhovuje_norme = True
        else:
            button_pocet_stupnov_1.foreground = colors["white"]
            nevyhovuje_norme = False

        if KV / N2 > 180:
            button_pocet_stupnov_2.foreground = colors["red"]
            nevyhovuje_norme = True
        else:
            button_pocet_stupnov_2.foreground = colors["white"]
            nevyhovuje_norme = False

    button_pocet_stupnov_1.text = str(N1)
    button_pocet_stupnov_2.text = str(N2)
    button_pocet_stupnov_1.update()
    button_pocet_stupnov_2.update()
    button_pocet_stupnov_2.text_surf = getfont(button_pocet_stupnov_2.textsize).render(button_pocet_stupnov_2.text, True, button_pocet_stupnov_2.foreground)
    button_pocet_stupnov_2.text_rect = button_pocet_stupnov_2.text_surf.get_rect(
        topleft = (button_pocet_stupnov_1.rect.right + fontsize, button_pocet_stupnov_1.rect.top + fontsize/2))
    button_pocet_stupnov_2.rect.center = button_pocet_stupnov_2.outline_rect.center = button_pocet_stupnov_2.text_rect.center

    if button_pocet_stupnov_1.active:
        N = N1
    elif button_pocet_stupnov_2.active:
        N = N2
    
    try:
        H = KV / N 
    except:
        H = None
    






def main():
    global R, KV, N, N1, N2, H, B, L, P, M, A, H1, H2
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
                        else:
                            if event.key == pygame.K_RETURN:
                                i.disabled = True
                            else:
                                i.value += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_jednoramenne.hover:
                    for i in buttons_typ_shodiska:
                        i.active = False
                    button_jednoramenne.active = True
                elif button_dvojramenne.hover:
                    for i in buttons_typ_shodiska:
                        i.active = False
                    button_dvojramenne.active = True
                if button_pocet_stupnov_1.hover:
                    for i in buttons_pocet_stupnov:
                        i.active = False
                    button_pocet_stupnov_1.active = True
                elif button_pocet_stupnov_2.hover:
                    for i in buttons_pocet_stupnov:
                        i.active = False
                    button_pocet_stupnov_2.active = True

        SCREEN.fill(colors["gray"])

        text_nadpis.draw()
        pygame.draw.aaline(SCREEN, colors["white"], (fontsize, text_nadpis.rect.bottom + fontsize/2), (SCREEN_W - fontsize, text_nadpis.rect.bottom + fontsize/2))
        text_typ_schodiska.draw()

        button_jednoramenne.draw()
        button_dvojramenne.draw()

        text_konstrukcna_vyska.draw()
        text_konstrukcna_vyska_mm.draw()
        inputbox_konstrukcna_vyska.draw()  

        if KV > 0 and inputbox_konstrukcna_vyska.disabled:
            text_pocet_stupnov.draw()
            text_pocet_stupnov_nevyhovuje_norme.draw()
            button_pocet_stupnov_1.draw()
            button_pocet_stupnov_2.draw()

            if button_pocet_stupnov_1.active or button_pocet_stupnov_2.active:
                text_vyska_stupna.draw()
                button_vyska_stupna.draw()












        for i in inputboxes:
            if not i.disabled and FPS_COUNT < int(FPS/2):
                i.draw_cursor()

        FPS_COUNT += 1
        if FPS_COUNT >= FPS:
            FPS_COUNT = 1

        CLOCK.tick(FPS)
        pygame.display.update()

main()
