import math
import time
from colorama import init, Fore, Style
init(convert=True)

def info():
    print("kv = konštrukčná výška")
    print("n = počet stupňov")    
    print("h = výška stupňa")
    print("b = šírka stupňa")
    print("L = dĺžka ramena")
    print("podesta = šírka podesty")
    print("medzipodesta = šírka medzipodesty")    
    print("alfa = sklon schodiska")
    print("V = podchodná výška \n    *tiež označovaná ako h1")
    print("D = priechodná výška \n    *tiež označovaná ako h2")
    print("")
def vyhodnotenie():   # Toto ukáže program
    time.sleep(0.5)
    print("")
    print("")
    print(Fore.GREEN + "VYHODNOTENIE:" + Style.RESET_ALL)
    time.sleep(1)
    print("1) Počet stupňov " + Fore.YELLOW + "n = " + str(n) + Style.RESET_ALL)
    time.sleep(0.1)
    if h <= 180:
        print("2) Výška stupňa " + Fore.YELLOW + "h = " + str(h) + Style.RESET_ALL)
    if h > 180:
        print("2) Výška stupňa " + Fore.RED + "h = " + str(h) + " - nevyhovuje" + Style.RESET_ALL)
    time.sleep(0.1)
    print("3) Šírka stupňa " + Fore.YELLOW + "b = " + str(b) + Style.RESET_ALL)
    time.sleep(0.1)
    print("4) Rozmery a počty stupňov v 1 ramene (n/2 ˣ h ˣ b)")
    print(Fore.GREEN + "   " + str(math.trunc(n/2)) + " ˣ " + str(h) + " ˣ " + str(b) + Style.RESET_ALL)
    time.sleep(0.1)
    print("5) Dĺžka ramena = " + Fore.YELLOW + str(L) + Style.RESET_ALL)
    time.sleep(0.1)
    print("6) Šírka ramena = " + Fore.YELLOW + str(rameno) + Style.RESET_ALL)
    time.sleep(0.1)
    print("7) " + Fore.YELLOW + "Šírka - podesty = " + str(sirka_podesty))
    print("         - medzipodesty = " + str(sirka_medzipodesty) + Style.RESET_ALL)
    time.sleep(0.1)
    print("8) Sklon ramena " + Fore.YELLOW + "α = " + str(alfa) + "°" + Style.RESET_ALL)
    time.sleep(0.1)
    if V >= 2100:
        print("9) Podchodná výška " + Fore.YELLOW + " V = " + str(V) + Fore.GREEN + " => vyhovuje" + Style.RESET_ALL)
    if V < 2100:
        print("9) Podchodná výška = " + str(V) + Fore.RED +" => nevyhovuje" + Style.RESET_ALL)
    time.sleep(0.1)
    if D >= 1900:
        print("10) Prechodná výška " + Fore.YELLOW + "D = " + str(D) + Fore.GREEN +" => vyhovuje" + Style.RESET_ALL)
    if D < 199:
        print("9) Podchodná výška " + Fore.RED + "D = " + str(D) +" => nevyhovuje" + Style.RESET_ALL)
    time.sleep(0.5)
    sklon = f_sklon()
    typ_stavby = f_typ_stavby()
    print("")
    print("Navrhli sme schodisko pre KV = " + str(kv) + "mm, priame, " + sklon + ", 2-ramenné, " + typ_stavby + ".")
    print("V 1 ramene " + Fore.GREEN + str(math.trunc(n/2)) + " ˣ " + str(h) + " ˣ " + str(b) + Style.RESET_ALL)
    print("")
def f_sklon():
    if alfa >= 10 and alfa < 20:
        return "rampové" 
    if alfa >= 20 and alfa < 25:
        return "mierne" 
    if alfa >= 25 and alfa < 35:
        return "bežné" 
    if alfa >= 35 and alfa < 45:
        return "strmé"
    if alfa >= 45 and alfa < 58:
        return "rebríkové" 
    if alfa < 10 or alfa >= 58:
        return "" 
def f_typ_stavby():
    if rameno >= 900 and rameno < 1200:
        return "rodinnom dome alebo bytovom dome alebo v inej občianskej stavbe"
    if rameno >= 1200 and rameno < 1500:
        return "bytovom dome alebo v inej občianskej stavbe"
    if rameno >= 1500:
        return "v občianskej stavbe"


print(Fore.GREEN + "NÁVRH SCHODISKA" + Style.RESET_ALL)
print("Vo výpočtoch sa používajú hodnoty v milimetroch")
time.sleep(0.5)
kv = int(input("Zadaj konštrukčnú výšku [mm]: "))


n = kv/170
n01 = math.floor(n)
if n01 % 2 == 1:
    n01 -= 1
n02 = math.ceil(n)
if n02 % 2 == 1:
    n02 += 1


h01 = round(kv/n01, 3) 
h02 = round(kv/n02, 3)
h001 = h01
h002 = h02
if h01 > 180:
    h001 = str(h01) + Fore.RED + " (nevyhovuje norme!)" + Style.RESET_ALL
if h02 > 180:
    h002 = str(h02) + Fore.RED + " (nevyhovuje norme!)" + Style.RESET_ALL


print("Počet stupňov môže byť " + Fore.YELLOW + str(n01) + Style.RESET_ALL + " (výška stupňa " + str(h001) + ") alebo " + Fore.YELLOW + str(n02) + Style.RESET_ALL + " (výška stupňa " + str(h002) + ").")
time.sleep(0.5)
n = int(input("Zadaj počet stupňov (" + str(n01) + " alebo " + str(n02) + "): "))
n = math.trunc(n)


h = round((kv / n), 3)


b = round(630 - (2*h))


L = (n/2 - 1) * b
L = math.trunc(L)


print("")
time.sleep(0.2)
print("Návrh šírky ramena:")
time.sleep(0.2)
print("    Rodinné domy - min. 900 mm")
time.sleep(0.2)
print("    Bytové domy - min. 1200 mm")
time.sleep(0.2)
print("    Iné občianske stavby - min. 1200 mm;")
time.sleep(0.2)
print("        Môže byť aj viac podľa prepokladaného počtu ľudí, podľa požiarnych predpisov,...")
print("        - 1500, 1800,...")
time.sleep(0.2)
rameno = int(input("Zadaj návrh šírky ramena [mm]: "))


print("")
time.sleep(0.2)
print("Návrh šírky podesty:")
time.sleep(0.2)
print("    min. šírka podesty = šírka ramena (" + str(rameno) + ") + 100 = " + str(rameno + 100))
time.sleep(0.2)
sirka_podesty = int(input("Zadaj šírku podesty [mm]: "))


print("")
time.sleep(0.2)
print("Návrh šírky medzipodesty:")
time.sleep(0.2)
print("    min. šírka medzipodesty = šírka ramena(" + str(rameno) + ").")
time.sleep(0.2)
sirka_medzipodesty = int(input("Zadaj šírku medzipodesty [mm]: "))


alfa = round(math.degrees(math.atan(h/b)), 1)


V = round(1500 + (750/math.cos(math.radians(alfa))))


D = round(750 + (1500*math.cos(math.radians(alfa))))


vyhodnotenie()
time.sleep(2)
input("Stlač enter pre ukončenie...")
