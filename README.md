# navrhschodiska

Návrh schodiska  
[Čo program ponúka](#%C4%8Do-program-pon%C3%BAka)  
[Ako použiť program](#ako-pou%C5%BEi%C5%A5-program)  
[Niečo o programe](#nie%C4%8Do-o-programe)  
[Kontakt](#kontakt)  


> Program nie je určený na profesionálne použitie. Autor nenesie zodpovednosť za prípadné problémy.


## Čo program ponúka
Tento program Vám po zadaní údajov vypočíta potrebné údaje ku schodisku v stavebnom výkrese:
- ideálna výška stupňa, šírka stupňa a počet stupňov
- podchodná a priechodná výška
- sklon ramena  

Program tiež narysuje, ako bude schodisko vyzerať (nepodporované vo verzií v1)

## Ako použiť program  
**Odporúčam používať [najnovšiu verziu](https://github.com/yungcypo/navrhschodiska/tree/main/navrhschodiska-v2)**  
> *0* je označenie pre verziu, ktorú ste si vybrali
- Zo zložky s vybranou verziou si stiahnete súbor *vypocetschodiska-v0.zip*
- Po stiahnutí tento súbor rozbalíte, a spustíte *vypocetschodiska-v0.exe*
- Ďalej sa už len stačí riadiť pokynmi, ktoré bude program žiadať

## Niečo o programe
Ako som už spomínal, tento program nie je určený na profesionálne použitie. Autor nenesie zodpovednosť za prípadné problémy.  
Program vznikol ako školská pomôcka na výpočet schodiska podľa [noriem](https://stavbadomu.sk/staviame-rodinny-dom/vypocet-schodiska-podla-stn-73-4130/)  

Program je vytvorený v programovacom jazyku [Python](https://www.python.org/) s pomocou nasledovných modulov:  
- math - pri výpočte sklonu ramena, vo verzií *v1* aj na zaokrúhlovanie niektorých hodnôt  
- time - vo verzií *v1* na vytvorenie akejsi animácie  
- [colorama](https://pypi.org/project/colorama/) - vo verzií *v1* na zvýraznenie dôležitých informácií
- [pygame](https://www.pygame.org/news) - vo verzií *v2* na zobrazenie nárysu schodiska a vypočítaných hodnôt
- sys, os - v spojení s modulom pygame, pre právne fungovanie

# Kontakt
Ak niečo nefunguje správne, našli ste chybu, alebo máte nejaké otázky, prosím neváhajte ma kontaktovať na cypooriginal@gmail.com  
V prípade záujmu si môžte pozrieť aj moje [ďalšie projekty](https://github.com/yungcypo?tab=repositories)
