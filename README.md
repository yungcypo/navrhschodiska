# navrhschodiska

**Obsah:**  

[Čo program ponúka](#%C4%8Do-program-pon%C3%BAka)  
[Ako použiť program](#ako-pou%C5%BEi%C5%A5-program)  
[Niečo o programe](#nie%C4%8Do-o-programe)  
[Kontakt](#kontakt)  

> Program nie je určený na profesionálne použitie. Autor nenesie zodpovednosť za prípadné problémy.  
> Verzia *v2* je zatiaľ vo vývoji. Zistite viac na konci odseku [Niečo o programe](#nie%C4%8Do-o-programe)  
> Zložku *Python* môžete pokojne ignorovať. Slúži vývojárom na lepšie pochopenie prípadných chýb v programe.  

## Čo program ponúka
Tento program Vám po zadaní údajov vypočíta potrebné údaje ku schodisku v stavebnom výkrese:
- ideálna výška stupňa, šírka stupňa a počet stupňov
- sklon ramena  
- podchodná a priechodná výška
- nárys, ako bude schodisko skutočne vyzerať (nepodporované vo verzií *v1*)

## Ako použiť program  
> Odporúčam používať [najnovšiu dostupnú verziu](navrhschodiska-v2.zip)

**Postup inštalácie programu:**
- Kliknete na súbor s označením verzie, ktorú ste si vybrali
- Kliknete na tlačidlo *download* nachádzajúce sa približne v strede obrazovky napravo. Súbor sa začne sťahovať
- Pri súboroch formátu *.zip* treba súbor najprv rozbaliť
- Po stiahnutí stačí otvoriť súbor *.exe* a riadiť sa pokynmi, ktoré bude program potrebovať

V **samotnom programe** bude potrebné zadať [konštrukčnú výšku](https://beliana.sav.sk/heslo/konstrukcna-vyska), počet stupňov schodiska, šírku ramena, šírku podesty a medzipodesty, vo verzií *v2* aj šírku zrkadla.  
Ak sú pre vás tieto pojmy neznáme, odporúčam Vám vyhľadať si [názvoslovie častí schodiska](https://www.novodrevis.sk/encyklopedia/nazvoslovie-technicke-poziadavky/)

## Niečo o programe
Ako som už spomínal - Tento program nie je určený na profesionálne použitie. Autor nenesie zodpovednosť za prípadné problémy.  
Program vznikol ako školská pomôcka na výpočet schodiska podľa [noriem](https://stavbadomu.sk/staviame-rodinny-dom/vypocet-schodiska-podla-stn-73-4130/).  

**Program z 'technického' hľadiska**  
Program je vytvorený v programovacom jazyku [Python](https://www.python.org/) s pomocou nasledovných modulov:  
- math - pri výpočte sklonu ramena, vo verzií *v1* aj na zaokrúhlovanie niektorých hodnôt  
- time - vo verzií *v1* na vytvorenie akejsi animácie  
- [colorama](https://pypi.org/project/colorama/) - vo verzií *v1* na zvýraznenie dôležitých informácií  
- [pygame](https://www.pygame.org/news) - vo verzií *v2* na zobrazenie nárysu schodiska a vypočítaných hodnôt  
- sys, os - v spojení s modulom pygame, pre právne fungovanie  

Verzia *v1* funguje výhradne pomocou konzoly. Nie je veľmi estetická, ale na výpočty poslúži dostatočne.  
Verzia *v2* funguje pomocou konzoly na zadanie potrebných údajov, potom sa objaví nové okno, v ktorom je možno vidieť výsledky výpočtov a samotné schodisko.  
Verzia *v3 (vo vývoji)* funguje výhradne pomocou okna.  

**Verzia *v2* je zatiaľ vo vývoji**  
Vo verzií *v2* bola zistená chyba. Po jej opravení bude sprístupnený nový súbor .exe    
Verzia sa dá použiť aj napriek chybe, program ale neukazuje všetky výsledky výpočtu 

# Kontakt
Niečo nefunguje správne?  
Našli ste chybu?  
Máte nejaké otázky?  
**Prosím neváhajte ma kontaktovať na cypooriginal@gmail.com**  

V prípade záujmu si môžte pozrieť aj moje [ďalšie projekty](https://github.com/yungcypo?tab=repositories)
