def mijn_functie_2(x):
    mapping = {
        (12, 3): [15, 9, 36, 4],
        (12, 2): [14, 10, 24, 6],
        (110, 5): [15, 5, 50, 2],
        (100, 20): [120, 80, 2000, 5]
    }
    
    return mapping.get(x, "Ongeldig argument")

def aanbieding_1(smaak, prijs, korting):
    
    nieuwe_prijs = prijs * (1 - korting)
    
    originele_prijs = 4
    
    nieuwe_prijs = originele_prijs * (1 - korting)
    
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {originele_prijs:.2f} euro voor {nieuwe_prijs:.2f} euro."

def inkomsten_totaal(inkomsten):

    totaal = sum(inkomsten)
    
    return totaal

def inkomsten_totaal(inkomsten, btw):
    
    totaal = sum(inkomsten)
    
    btw_bedrag = totaal * btw
    
    return f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    
    return [laagste, hoogste]

def gemiddelde(mijn_lijst):
    
    totaal = sum(mijn_lijst)
    
    gemiddelde_waarde = totaal / len(mijn_lijst)
    
    return gemiddelde_waarde

def gemiddelde(mijn_lijst):
    
    totaal = sum(mijn_lijst)
    
    gemiddelde_waarde = totaal / len(mijn_lijst)
    
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_waarde:.2f} euro."

def hoog_en_laag(mijn_lijst):
    
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    
    return [hoogste, laagste]

def meervoudig(invoer_lijst):
    return hoog_en_laag(invoer_lijst)

def combinatie(invoer_lijst_2):
    resultaat = meervoudig(invoer_lijst_2)
    
    return resultaat

voorbeeld_lijst = [10, 5, 3, 2, 1, 2, 9]
resultaat = combinatie(voorbeeld_lijst)
print(resultaat)