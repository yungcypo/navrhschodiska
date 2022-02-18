import math
import pygame, sys, os


# credits - cypo


'''
TODO
rezová rovina ://
'''


CLOCK = pygame.time.Clock()
FPS = 60
WIDTH, HEIGHT = 900, 600
TITLE = pygame.display.set_caption("Schodisko")
ICON = pygame.image.load("icon.png")
pygame.display.set_icon(ICON)



colors = {
    "white" : (255, 255, 255),
    "grey" : (50, 50, 50),
    "black" : (0, 0, 0),
    "pink" : (255, 0, 255),
    "brown": (222, 184, 135)}


'''
SKRATKY

kv = konštrukčná výška
n = počet stupňov
n1, n2 = pomocné premenné pri výpočte n
h = výška stupňa
b = šírka stupňa
l = dĺžka ramena
š = šírka ramena
p = šírka podesty
m = šírka medzipodesty
alfa = skon ramena
h1 = podchodná výška
h2 = priechodná výška
X0, Y0 - začiatočné body v náčte 
k = koeficient - udáva veľkosť obrázku
# forX = súradnica x vo for loope pri výpočte stupňov
'''




def main():
    pygame.init()
    global kv, n, h, b, l, š, umiestnenie, p, m, alfa, sklon, h1, h2, z, k, koef, X0, Y0, X1, Y1
    os.system('cls')
    print("VÝPOČET SCHODISKA")
    print("\nPri výpočtoch sa používajú hodnoty v milimetroch\n"
    "Pre správny výpočet prosím taktiež používajte hodnoty v milimetroch")
    print("Ľavotočivé dvojramenné schodisko")


    # konštrukčná výška kv 
    print("\nKONŠTRUKČNÁ VÝŠKA")
    while True:
        try:
            kv = int(input("  Zadajte konštrukčnú výšku: "))
        except(ValueError):
            print("  Pravdepodobne ste nezadali číslo...")
        except:
            print("  Niečo sa pokazilo...")
        else:
            break
    

    # počet stupňov n
    print("\nPOČET STUPŇOV")
    n = kv/170
    n1 = round(n)
    
    if n1 % 2 == 0:
        if n1 >= n:
            n2 = n1
            n1 -= 2
        elif n1 < n:
            n2 = n1 + 2
    elif n1 % 2 == 1:
        n1 -= 1
        n2 = n1 + 2

    print("  Počet stupňov by mal byť " + str(n1) + " stupňov, alebo " + str(n2) + " stupňov")
    if kv / n1 > 180:
        print("  POZOR! " + str(n1) + " stupňov nevyhovuje norme!")
    elif kv / n2 > 180:
        print("  POZOR! " + str(n2) + " stupňov nevyhovuje norme!")    
    while True:
        try:
            n = int(input("  Zadajte počet stupňov: "))
        except(ValueError):
            print("  Pravdepodobne ste nezadali číslo...")
        except:
            print("  Niečo sa pokazilo...")
        else:
            break
        
    

    # výška stupňa h 
    h = kv / n

    # šírka stupňa b
    b = round(630 - (2 * h))

    # dĺžka ramena l
    l = round((n/2 - 1) * b)


    # návrh šírky ramena:
    print("\nNÁVRH ŠÍRKY RAMENA")
    print("  V rodinných domoch min. 900")
    print("  V bytových domoch min. 1200")
    print("  V iných občianskych stavbách min. 1500")
    while True:
        try:
            š = int(input("  Zadajte šírku ramena: "))
        except(ValueError):
            print("  Pravdepodobne ste nezadali číslo...")
        except:
            print("  Niečo sa pokazilo...")
        else:
            break
    umiestnenie = ""
    if š in range(900, 1199):
        umiestnenie = "rodinnom dome"
    elif š in range(1200, 1499):
        umistnenie = "bytovom dome"
    elif š > 1500:
        umiestnenie = "v inej občianskej stavbe"
    

    # návrh šírky podesty p 
    print("\nNÁVRH ŠÍRKY PODESTY")
    print("  Min. " + str(š + 100))
    while True:
        try:
            p = int(input("  Zadajte šírku podesty: "))
        except(ValueError):
            print("  Pravdepodobne ste nezadali číslo...")
        except:
            print("  Niečo sa pokazilo...")
        else:
            break

    # návrh šírky medzipodesty m
    print("\nNÁVRH ŠÍRKY MEDZIPODESTY")
    print("  Min. " + str(š))
    while True:
        try:
            m = int(input("  Zadajte šírku medzipodesty: "))
        except(ValueError):
            print("  Pravdepodobne ste nezadali číslo...")
        except:
            print("  Niečo sa pokazilo...")
        else:
            break



    # sklon ramena alfa
    alfa = round(math.degrees(math.atan(h/b)), 1)
    sklon = ""
    if round(alfa) in range(10, 20):
        sklon = "rampové"
    elif round(alfa) in range(20, 25):
        sklon = "mierne"
    elif round(alfa) in range(25, 35):
        sklon = "bežné"
    elif round(alfa) in range(35, 45):
        sklon = "strmé"
    elif round(alfa) in range(45, 58):
        sklon = "rebríkové"





    # podchodná výška h1
    h1 = round(1500 + (750/math.cos(math.radians(alfa))))
    if h1 < 2100:
        print("\nPOZOR! Podchodná výška nevyhovuje norme!")



    # priechodná výška h2
    h2 = round(750 + 1500 * math.cos(math.radians(alfa)))
    if h2 < 1900:
        print("\nPOZOR! Priechodná výška nevyhovuje norme!")

    
    # z = zrkadlo
    print("\nNÁVRH ŠÍRKY ZRKADLA")
    while True:
        try:
            z = int(input("  Zadajte šírku zrkadla: "))
        except(ValueError):
            print("  Pravdepodobne ste nezadali číslo...")
        except:
            print("  Niečo sa pokazilo...")
        else:
            break

    # k, koef = koeficient - basically zmenšenie obrázku
    koef = 7
    k = 1/koef
    # X0, X1, Y0, Y1 - pomocné súradnice
    X0, Y0 = 50, 50
    

def ciary():
        # náčrt schodiska
        # horizontálne čiary
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0, Y0), 
            (X0 + (p + l + m) * k, Y0)
        ) # 'horná' časť schodiska
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0 + p * k, Y0 + š * k), 
            (X0 + (p + l) * k, Y0 + š * k)
        ) # zrkadlo 1
        if z > 0:
            pygame.draw.aaline(
                SCREEN, colors["pink"],
                (X0 + p * k, Y0 + (š + z) * k), 
                (X0 + (p + l) * k, Y0 + (š + z) * k)
            ) # zrkadlo 2
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0, Y0 + (š * 2 + z) * k), 
            (X0 + (p + l + m) * k, Y0 + (š * 2 + z) * k)
        ) # 'dolná' čast schodiska
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0 + (p - 50) * k, Y0 + (š - 50) * k), 
            (X0 + (p + l + 50) * k, Y0 + (š - 50) * k)
        ) # zábradlie 1
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0 + (p - 50) * k, Y0 + (š + z + 50) * k), 
            (X0 + (p + l + 50) * k, Y0 + (š + z + 50) * k)
        ) # zábradlie 2
        



        # vertikálne čiary
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0, Y0), 
            (X0, Y0 + (š * 2 + z) * k)
        ) # podesta 1
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0 + p * k, Y0), 
            (X0 + p * k, Y0 + (š * 2 + z) * k)
        ) # podesta 2
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0 + (p + l) * k, Y0), 
            (X0 + (p + l) * k, Y0 + (š * 2 + z) * k)
        ) # medzipodesta 1
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0 + (p + l + m) * k, Y0), 
            (X0 + (p + l + m) * k, Y0 + (š * 2 + z) * k)
        ) # medzipodesta 2
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0 + (p - 50) * k, Y0 + (š - 50) * k), 
            (X0 + (p - 50) * k, Y0 + (š + z + 50) * k)
        ) # zrkadlo 1 
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            (X0 + (p + l + 50) * k, Y0 + (š - 50) * k), 
            (X0 + (p + l + 50) * k, Y0 + (š + z + 50) * k)
        ) # zrkadlo 2

        # forX = súradnica x vo for loope
        forX = b 
        # stupne + vnútorná kóta
        for i in range(int(n/2 - 2)):
            pygame.draw.aaline(
                SCREEN, colors["pink"],
                (X0 + (p + forX) * k, Y0),
                (X0 + (p + forX) * k, Y0 + š * k)
            ) # stupeň v 'hornom' ramene
            
            pygame.draw.aaline(
                SCREEN, colors["pink"],
                (X0 + (p + forX) * k, Y0 + (š + z) * k),
                (X0 + (p + forX) * k, Y0 + (š * 2 + z) * k)
            ) # stupeň v 'dolnom' ramene
            forX += b


        # výstupové čiary
        pygame.draw.circle(
            SCREEN, colors["pink"],
            ((X0 + (p + 6) * k), (Y0 + (š * 1.5 + z) * k)),
            100 * k, width = 1
        ) # prvý krúžok
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            ((X0 + (p + 100 + 6) * k), (Y0 + (š * 1.5 + z) * k)),
            ((X0 + (p + l) * k), (Y0 + (š * 1.5 + z) * k))
        ) # prvá actually čiara
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            ((X0 + (p + l - 90) * k), (Y0 + (š * 1.5 + z - 90) * k)),
            ((X0 + (p + l) * k), (Y0 + (š * 1.5 + z) * k))
        ) # prvá šipka horná časť
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            ((X0 + (p + l - 90) * k), (Y0 + (š * 1.5 + z + 90) * k)),
            ((X0 + (p + l) * k), (Y0 + (š * 1.5 + z) * k))
        ) # prvá šipka dolná časť
        pygame.draw.circle(
            SCREEN, colors["pink"],
            (X0 + (p + l + 6) * k, (Y0 + š / 2 * k)),
            100 * k, width = 1
        ) # druhý krúžok
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            ((X0 + (p + l - 100 + 6) * k), (Y0 + š / 2 * k)),
            ((X0 + p * k), (Y0 + (š / 2 * k)))
        ) # druhá actually čiara
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            ((X0 + (p + 90) * k), (Y0 + (š / 2 - 90) * k)),
            ((X0 + p * k), (Y0 + š / 2 * k))
        ) # druhá šípka horná časť
        pygame.draw.aaline(
            SCREEN, colors["pink"],
            ((X0 + (p + 90) * k), (Y0 + (š / 2 + 90) * k)),
            ((X0 + p * k), (Y0 + š / 2 * k))
        ) # druhá šípka dolná časť


def koty():
    # kóty
        # horizontálne kóty dĺžkové
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0, Y0 + (š * 2 + z + 500) * k), 
            (X0 + (p + l + m) * k, Y0 + (š * 2 + z + 500) * k)
        ) # actually kóta 1 
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0, Y0 + (š * 2 + z + 750) * k), 
            (X0 + (p + l + m) * k, Y0 + (š * 2 + z + 750) * k)
        ) # actually kóta 2
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0, Y0 + (š * 2 + z + 250) * k), 
            (X0, Y0 + (š * 2 + z + 850) * k)
        ) # vertikalna ciarka zaciatok
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p + l + m) * k, Y0 + (š * 2 + z + 250) * k), 
            (X0 + (p + l + m) * k, Y0 + (š * 2 + z + 850) * k)
        ) # vertikalna ciarka koniec
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + p * k, Y0 + (š * 2 + z + 250) * k), 
            (X0 + p * k, Y0 + (š * 2 + z + 575) * k)
        ) # vertikalna ciarka podesta
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p + l) * k, Y0 + (š * 2 + z + 250) * k), 
            (X0 + (p + l) * k, Y0 + (š * 2 + z + 575) * k)
        ) # vertikalna ciarka medzipodesta
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 - 45 * k, Y0 + (š * 2 + z + 500 + 45)* k), 
            (X0 + 45 * k, Y0 + (š * 2 + z + 500 - 45)* k)
        ) # diagonalna ciarka zaciatok 1
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 - 45 * k, Y0 + (š * 2 + z + 750 + 45)* k), 
            (X0 + 45 * k, Y0 + (š * 2 + z + 750 - 45)* k)
        ) # diagonalna ciarka zaciatok 2
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p - 45) * k, Y0 + (š * 2 + z + 500 + 45)* k), 
            (X0 + (p + 45) * k, Y0 + (š * 2 + z + 500 - 45)* k)
        ) # diagonalna ciarka podesta
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p + l - 45) * k, Y0 + (š * 2 + z + 500 + 45)* k), 
            (X0 + (p + l + 45) * k, Y0 + (š * 2 + z + 500 - 45)* k)
        ) # diagonalna ciarka medzipodesta
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p + l + m - 45) * k, Y0 + (š * 2 + z + 500 + 45)* k), 
            (X0 + (p + l + m + 45) * k, Y0 + (š * 2 + z + 500 - 45)* k)
        ) # diagonalna ciarka koniec 1 
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p + l + m - 45) * k, Y0 + (š * 2 + z + 750 + 45)* k), 
            (X0 + (p + l + m + 45) * k, Y0 + (š * 2 + z + 750 - 45)* k)
        ) # diagonalna ciarka koniec 2

        # verikálne kóty dĺžkové
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p + l + m + 500) * k, Y0), 
            (X0 + (p + l + m + 500) * k, Y0 + (š * 2 + z) * k)
        ) # actually kóta 1
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p + l + m + 750) * k, Y0), 
            (X0 + (p + l + m + 750) * k, Y0 + (š * 2 + z) * k)
        ) # actually kóta 2
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p + l + m + 250) * k, Y0),
            (X0 + (p + l + m + 850) * k, Y0)
        ) # horizontalna ciarka zaciatok
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p + l + m + 250) * k, Y0 + (š * 2 + z) * k),
            (X0 + (p + l + m + 850) * k, Y0 + (š * 2 + z) * k)
        ) # horizontalna ciarka koniec
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            (X0 + (p + l + m + 250) * k, Y0 + š * k),
            (X0 + (p + l + m + 575) * k, Y0 + š * k)
        ) # horizontalna ciarka rameno 1 
        if z > 0:
            pygame.draw.aaline(
                SCREEN, colors["brown"],
                (X0 + (p + l + m + 250) * k, Y0 + (š + z) * k),
                (X0 + (p + l + m + 575) * k, Y0 + (š + z) * k)
            ) # horizontalna ciarka rameno 2
        pygame.draw.aaline( 
            SCREEN, colors["brown"],
            (X0 + (p + l + m + 500 - 45) * k, Y0 - 45 * k),
            (X0 + (p + l + m + 500 + 45) * k, Y0 + 45 * k)
        ) # diagonalna ciarka zaciatok 1 
        pygame.draw.aaline( 
            SCREEN, colors["brown"],
            (X0 + (p + l + m + 750 - 45) * k, Y0 - 45 * k),
            (X0 + (p + l + m + 750 + 45) * k, Y0 + 45 * k)
        ) # diagonalna ciarka zaciatok 2
        pygame.draw.aaline( 
            SCREEN, colors["brown"],
            (X0 + (p + l + m + 500 - 45) * k, Y0 + (š - 45) * k),
            (X0 + (p + l + m + 500 + 45) * k, Y0 + (š + 45) * k)
        ) # diagonalna ciarka rameno 1 
        if z > 0:
            pygame.draw.aaline( 
                SCREEN, colors["brown"],
                (X0 + (p + l + m + 500 - 45) * k, Y0 + (š + z - 45) * k),
                (X0 + (p + l + m + 500 + 45) * k, Y0 + (š + z + 45) * k)
            ) # diagonalna ciarka rameno 2
        pygame.draw.aaline( 
            SCREEN, colors["brown"],
            (X0 + (p + l + m + 500 - 45) * k, Y0 + (š * 2 + z - 45) * k),
            (X0 + (p + l + m + 500 + 45) * k, Y0 + (š * 2 + z + 45) * k)
        ) # diagonalna ciarka koniec 1 
        pygame.draw.aaline( 
            SCREEN, colors["brown"],
            (X0 + (p + l + m + 750 - 45) * k, Y0 + (š * 2 + z - 45) * k),
            (X0 + (p + l + m + 750 + 45) * k, Y0 + (š * 2 + z + 45) * k)
        ) # diagonalna ciarka koniec 2


        # vnútorná kóta šírky stupňa
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            ((X0 + (p + b - 45) * k), (Y0 + (š * (4/3) + z) * k)),
            ((X0 + (p + b * 2 + 45) * k), (Y0 + (š * (4/3) + z) * k)),
        ) # actually kóta
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            ((X0 + (p + b - 45) * k), (Y0 + (š * (4/3) + z + 45) * k)),
            ((X0 + (p + b + 45) * k), (Y0 + (š * (4/3) + z - 45) * k))
        ) # šikmá čiarka 1
        pygame.draw.aaline(
            SCREEN, colors["brown"],
            ((X0 + (p + b * 2 - 45) * k), (Y0 + (š * (4/3) + z + 45) * k)),
            ((X0 + (p + b * 2 + 45) * k), (Y0 + (š * (4/3) + z - 45) * k))
        )



def run():
    global SCREEN, X0, Y0, k, koef, sklon, kotoy0, koty0_trigger
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    
    X0_change, Y0_change = 0, 0
    koef_change = 0


    info = False
    koty0 = True
    koty0_trigger = koty0


    
        
    def texty():
        global vyhodnotenie_4_rect

        font = pygame.font.Font('consolas.ttf', int(125 * k))

        celkova_dlzka_surf = font.render(str(p + l + m), True, colors["white"])
        podesta_surf = font.render(str(p), True, colors["white"])
        dlzka_ramena_surf = font.render(str(l), True, colors["white"])
        medzipodesta_surf = font.render(str(m), True, colors["white"])
        celkova_sirka_surf = font.render(str(š * 2 + z), True, colors["white"])
        celkova_sirka_surf = pygame.transform.rotate(celkova_sirka_surf, 90)
        sirka_ramena_surf = font.render(str(š), True, colors["white"])
        sirka_ramena_surf = pygame.transform.rotate(sirka_ramena_surf, 90)
        zrkadlo_surf = font.render(str(z), True, colors["white"])
        zrkadlo_surf = pygame.transform.rotate(zrkadlo_surf, 90)
        vnutorna_kota_surf = font.render(str(b), True, colors["white"])
        oznacenie_stupnov_1_surf = font.render(str(1), True, colors["white"])
        oznacenie_stupnov_2_surf = font.render(str(round(n / 2)), True, colors["white"])
        oznacenie_stupnov_3_surf = font.render(str(round(n / 2 + 1)), True, colors["white"])
        oznacenie_stupnov_4_surf = font.render(str(n), True, colors["white"])
        vyskova_kota_text = [
            ("0,000"),
            (str(int(kv / 2 / 1000)) + "," + str(round(kv / 2))[(len(str(kv)) - 3):]) # napr [1:] - odstraňuje prvé písmeno
        ]
        vyskova_kota_1_surf = font.render(vyskova_kota_text[0], True, colors["white"])
        vyskova_kota_2_surf = font.render(vyskova_kota_text[1], True, colors["white"])
        if z == 0:
            vyhodnotenie_text = [
                ("Navrhli sme schodisko pre KV = " + str(kv) + ", priame, " + str(sklon) + ", "),
                ("2-ramenné, ľavotočivé v " + umiestnenie),
                ("V jednom ramene"),
                (str(round(n/2)) + " x " + str(round(h, 2)) + " x " + str(b))
            ]
        elif z > 0 :
            vyhodnotenie_text = [
            ("Navrhli sme schodisko pre KV = " + str(kv) + ", priame, " + str(sklon) + ", "),
            ("2-ramenné, ľavotočivé, so zrkadlom v " + umiestnenie),
            ("V jednom ramene"),
            (str(round(n/2)) + " x " + str(round(h, 2)) + " x " + str(b))
        ]
        vyhodnotenie_1_surf = font.render(vyhodnotenie_text[0], True, colors["white"])
        vyhodnotenie_2_surf = font.render(vyhodnotenie_text[1], True, colors["white"])
        vyhodnotenie_3_surf = font.render(vyhodnotenie_text[2], True, colors["white"])
        vyhodnotenie_4_surf = font.render(vyhodnotenie_text[3], True, colors["white"])
        if not info_trigger:
            info_surf = font.render("Pre viac informácií stlačte 'i' ", True, colors["grey"])
        if info_trigger:
            info_surf = font.render("Pre menej informácií stlačte 'i' ", True, colors["grey"])
        vysvetlivky_text = [
            ("↑ ↓ → ←   posúvanie obrazovky"),
            ("+ -       zväčšovanie, zmenšovanie obrazovky"),
            ("K         zapnúť/vypnúť kóty"),
            ("R         resetovanie pozície obrazu"),
            ("ESC       ukončenie programu")
        ]
        vysvetlivky_1_surf = font.render(vysvetlivky_text[0], True, colors["white"])
        vysvetlivky_2_surf = font.render(vysvetlivky_text[1], True, colors["white"])
        vysvetlivky_3_surf = font.render(vysvetlivky_text[2], True, colors["white"])
        vysvetlivky_4_surf = font.render(vysvetlivky_text[3], True, colors["white"])
        vysvetlivky_5_surf = font.render(vysvetlivky_text[4], True, colors["white"])


        celkova_dlzka_rect = celkova_dlzka_surf.get_rect(midbottom = ((X0 + ((p + l + m) / 2) * k),(Y0 + (š * 2 + z + 750) * k)))
        podesta_rect = podesta_surf.get_rect(midbottom = ((X0 + (p / 2 ) * k ), (Y0 + (š * 2 + z + 500) * k)))
        dlzka_ramena_rect = dlzka_ramena_surf.get_rect(midbottom = ((X0 + (p + l / 2) * k), (Y0 + (š * 2 + z + 500) * k)))
        medzipodesta_rect = medzipodesta_surf.get_rect(midbottom = ((X0 + (p + l + m / 2) * k), (Y0 + (š * 2 + z + 500) * k)))
        celkova_sirka_rect = celkova_sirka_surf.get_rect(midright = ((X0 + (p + l + m + 750) * k), (Y0 + ((š * 2 + z )/ 2) * k)))
        sirka_ramena_1_rect = sirka_ramena_surf.get_rect(midright = ((X0 + (p + l + m + 500) * k), (Y0 + (š / 2) * k)))
        sirka_ramena_2_rect = sirka_ramena_surf.get_rect(midright = ((X0 + (p + l + m + 500) * k), (Y0 + (š * 1.5 + z) * k)))
        zrkadlo_rect = zrkadlo_surf.get_rect(bottomleft = ((X0 + (p + l + m + 525) * k), (Y0 + š * k)))
        vnutorna_kota_rect = vnutorna_kota_surf.get_rect(midbottom = ((X0 + (p + b * 1.5) * k), (Y0 + (š * (4/3) + z) * k)))
        oznacenie_stupnov_1_rect = oznacenie_stupnov_1_surf.get_rect(bottomleft = ((X0 + (p + 40)* k), (Y0 + (š * 2 + z) * k)))
        oznacenie_stupnov_2_rect = oznacenie_stupnov_2_surf.get_rect(bottomleft = ((X0 + (p + l + 40) * k), (Y0 + (š * 2 + z) * k)))
        oznacenie_stupnov_3_rect = oznacenie_stupnov_3_surf.get_rect(bottomleft = ((X0 + (p + l + 40) * k), (Y0 + (š - 50) * k)))
        oznacenie_stupnov_4_rect = oznacenie_stupnov_4_surf.get_rect(bottomleft = ((X0 + (p + 40) * k), (Y0 + (š - 50) * k)))
        vyskova_kota_1_rect = vyskova_kota_1_surf.get_rect(topleft = ((X0 + 150 * k), (Y0 + 150 * k)))
        vyskova_kota_2_rect = vyskova_kota_2_surf.get_rect(topright = ((X0 + (p + l + m - 150) * k), (Y0 + 150 * k)))
        vyhodnotenie_1_rect = vyhodnotenie_1_surf.get_rect(topleft = (X1, Y1))
        vyhodnotenie_2_rect = vyhodnotenie_2_surf.get_rect(topleft = (vyhodnotenie_1_rect.left, vyhodnotenie_1_rect.bottom + 10 * k))
        vyhodnotenie_3_rect = vyhodnotenie_3_surf.get_rect(topleft = (vyhodnotenie_2_rect.left, vyhodnotenie_2_rect.bottom + 100 * k))
        vyhodnotenie_4_rect = vyhodnotenie_4_surf.get_rect(topleft = (vyhodnotenie_3_rect.right + 80 * k, vyhodnotenie_3_rect.top))
        info_rect = info_surf.get_rect(topleft = (vyhodnotenie_3_rect.left, vyhodnotenie_3_rect.bottom + 100 * k))
        vysvetlivky_1_rect = vysvetlivky_1_surf.get_rect(topleft = (info_rect.left, info_rect.bottom + 10 * k))
        vysvetlivky_2_rect = vysvetlivky_2_surf.get_rect(topleft = (vysvetlivky_1_rect.left, vysvetlivky_1_rect.bottom + 10 * k))
        vysvetlivky_3_rect = vysvetlivky_3_surf.get_rect(topleft = (vysvetlivky_2_rect.left, vysvetlivky_2_rect.bottom + 10 * k))
        vysvetlivky_4_rect = vysvetlivky_4_surf.get_rect(topleft = (vysvetlivky_3_rect.left, vysvetlivky_3_rect.bottom + 10 * k))
        vysvetlivky_5_rect = vysvetlivky_5_surf.get_rect(topleft = (vysvetlivky_4_rect.left, vysvetlivky_4_rect.bottom + 10 * k))

        if koty0_trigger:
            SCREEN.blit(celkova_dlzka_surf, celkova_dlzka_rect)
            SCREEN.blit(podesta_surf, podesta_rect)
            SCREEN.blit(dlzka_ramena_surf, dlzka_ramena_rect)
            SCREEN.blit(medzipodesta_surf, medzipodesta_rect)
            SCREEN.blit(celkova_sirka_surf, celkova_sirka_rect)
            SCREEN.blit(sirka_ramena_surf, sirka_ramena_1_rect)
            SCREEN.blit(sirka_ramena_surf, sirka_ramena_2_rect)
            if z > 0:
                SCREEN.blit(zrkadlo_surf, zrkadlo_rect)
            SCREEN.blit(vnutorna_kota_surf, vnutorna_kota_rect)
            SCREEN.blit(oznacenie_stupnov_1_surf, oznacenie_stupnov_1_rect)
            SCREEN.blit(oznacenie_stupnov_2_surf, oznacenie_stupnov_2_rect)
            SCREEN.blit(oznacenie_stupnov_3_surf, oznacenie_stupnov_3_rect)
            SCREEN.blit(oznacenie_stupnov_4_surf, oznacenie_stupnov_4_rect)
            SCREEN.blit(vyskova_kota_1_surf, vyskova_kota_1_rect)
            SCREEN.blit(vyskova_kota_2_surf, vyskova_kota_2_rect)
        SCREEN.blit(vyhodnotenie_1_surf, vyhodnotenie_1_rect)
        SCREEN.blit(vyhodnotenie_2_surf, vyhodnotenie_2_rect)
        SCREEN.blit(vyhodnotenie_3_surf, vyhodnotenie_3_rect)
        SCREEN.blit(vyhodnotenie_4_surf, vyhodnotenie_4_rect)


        SCREEN.blit(info_surf, info_rect)
        if info_trigger:
            SCREEN.blit(vysvetlivky_1_surf, vysvetlivky_1_rect)
            SCREEN.blit(vysvetlivky_2_surf, vysvetlivky_2_rect)
            SCREEN.blit(vysvetlivky_3_surf, vysvetlivky_3_rect)
            SCREEN.blit(vysvetlivky_4_surf, vysvetlivky_4_rect)
            SCREEN.blit(vysvetlivky_5_surf, vysvetlivky_5_rect)

        # rámik okolo 'vyhodnotenie_4' vo vyhodnotení
        pygame.draw.polygon(
            SCREEN, colors["brown"],
            [
                (vyhodnotenie_4_rect.left - 30 * k, vyhodnotenie_4_rect.top - 20 * k),
                (vyhodnotenie_4_rect.right + 30 * k, vyhodnotenie_4_rect.top - 20 * k),
                (vyhodnotenie_4_rect.right + 30 * k, vyhodnotenie_4_rect.bottom + 10 * k),
                (vyhodnotenie_4_rect.left - 30 * k, vyhodnotenie_4_rect.bottom + 10 * k)
            ],
            width = 1
        )
        # rámik okolo výškových kót
        if koty0_trigger:
            pygame.draw.polygon(
                SCREEN, colors["brown"],
                [
                    (vyskova_kota_1_rect.left - 45 * k, vyskova_kota_1_rect.top - 35 * k),
                    (vyskova_kota_1_rect.right + 45 * k, vyskova_kota_1_rect.top - 35 * k),
                    (vyskova_kota_1_rect.right + 45 * k, vyskova_kota_1_rect.bottom + 25 * k),
                    (vyskova_kota_1_rect.left - 45 * k, vyskova_kota_1_rect.bottom + 25 * k)
                ],
                width = 1
            ) # prvá kóta
            pygame.draw.polygon(
            SCREEN, colors["brown"],
            [
                (vyskova_kota_2_rect.left - 45 * k, vyskova_kota_2_rect.top - 35 * k),
                (vyskova_kota_2_rect.right + 45 * k, vyskova_kota_2_rect.top - 35 * k),
                (vyskova_kota_2_rect.right + 45 * k, vyskova_kota_2_rect.bottom + 25 * k),
                (vyskova_kota_2_rect.left - 45 * k, vyskova_kota_2_rect.bottom + 25 * k)
            ],
            width = 1
        ) # druhá kóta


    while True:
        info_trigger = info
        koty0_trigger = koty0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # ukončenie 
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # pohyb
                if event.key == pygame.K_RIGHT:
                    X0_change -= 5
                if event.key == pygame.K_LEFT:
                    X0_change += 5
                if event.key == pygame.K_UP:
                    Y0_change += 5
                if event.key == pygame.K_DOWN:
                    Y0_change -= 5
                # zväčšovanie, zmenšovanie
                if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    if koef >= 2:
                        koef_change -= 0.2
                if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    koef_change += 0.2
                # reset 
                if event.key == pygame.K_0 or event.key == pygame.K_KP0 or event.key == pygame.K_r:
                    X0, Y0 = 50, 50
                    X0_change, Y0_change = 0, 0

                # zobrazovanie info
                if event.key == pygame.K_i:
                    if info_trigger:
                        info = False
                    if not info_trigger:
                        info = True
                # zobrazovanie kót
                if event.key == pygame.K_k:
                    if koty0_trigger:
                        koty0 = False
                    if not koty0_trigger:
                        koty0 = True

            if event.type == pygame.KEYUP:
                # pohyb
                if event.key == pygame.K_RIGHT:
                    X0_change = 0
                if event.key == pygame.K_LEFT:
                    X0_change = 0
                if event.key == pygame.K_UP:
                    Y0_change = 0
                if event.key == pygame.K_DOWN:
                    Y0_change = 0
                # zväčšovanie, zmenšovanie
                if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    koef_change = 0
                if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    koef_change = 0


        SCREEN.fill(colors["black"])

        if koty0_trigger:
            X1, Y1 = X0, (Y0 + (š * 2 + z + 750 + 150 + 50) * k)
        if not koty0_trigger:
            X1, Y1 = X0, (Y0 + (š * 2 + z + 200) * k)

        X0 += X0_change
        Y0 += Y0_change


        



        koef += koef_change
        if koef <= 2:
            koef = 2
        k = 1/koef
        
        
        
        
        
        



        ciary()
        texty()
        if koty0_trigger:
            koty()


        CLOCK.tick(FPS)
        pygame.display.update()




main()
run()
