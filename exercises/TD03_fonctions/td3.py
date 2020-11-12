def tempsEnSeconde(jours, heures, minutes, secondes):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    temps=(jours*86400+heures*3600+minutes*60+secondes)
    return temps

jours=3
heures=23
minutes=1
secondes=34
print(type(jours))
print(type(heures))
print(type(minutes))
print(type(secondes))
print(tempsEnSeconde(jours, heures, minutes, secondes))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    secondes=seconde
    minutes=secondes//60
    reste_sans_minutes=seconde%60
    heures=reste_sans_minutes//60
    reste_sans_heures=reste_sans_minutes%60
    jours=reste_sans_heures
    return (jours, heures, minutes, secondes)
    
temps = secondeEnTemps(100000)
print(temps)

#fonction auxiliaire ici

j=""
h=""
m=""
s=""


def afficheTemps(jours, heures, minutes, secondes):
    global j
    global h
    global m
    global s
    if jours>1:
        j=str(jours)+"jours,"
    elif jours==1:
        j="un jour,"
    else:
        j=""
    if heures>1:
        h=str(heures)+"heures,"
    elif heures==1:
        h="une heure,"
    else:
        h=""
    if minutes>1:
        m=str(minutes)+"minutes,"
    elif minutes==1:
        m="une minute,"
    else:
        m=""
    if secondes>1:
        s=str(secondes)+"secondes."
    elif secondes==1:
        s="une seconde."
    else:
        s=""
    print("Il y a", j, h, m, s)

def demandeTemps(jours, heures, minutes, secondes):
    jours = int(input("Combien de jours"))
    heures = int(input("Combien d'heures"))
    minutes = int(input("Combien de minutes"))
    secondes = int(input("Combien de seconde"))
    if (secondes > 59 or minutes > 59 or heures > 23):
      print("Entrée mal formée, ce n'est pas une date.")
      return (0,0,0,0)
    return (jours, heures, minutes, secondes)



def sommeTemps(jours1, heures1, minutes1, secondes1, jours2, heures2, minutes2, secondes2):
    secondes=secondes1+secondes2
    minutes=minutes1+minutes2
    heures=heures1+heures2
    jours=jours1+jours2
    if secondes>=60:
        minutes+=1
        secondes=secondes-60
    if minutes>=60:
        heures+=1
        minutes=minutes-60
    if heures>=24:
        jours+=1
        heures=heures-24
    demandeTemps(jours, heures, minutes, secondes)
    
sommeTemps(2,3,4,25, 5,22,57,1)

def proportionTemps(jours, heures, minutes, secondes, proportion):
    temps = tempsEnSeconde(jours, heures, minutes, secondes)
    prop_temps = temps*proportion
    return (demandeTemps(0, 0, 0, int(prop_temps)))

proportionTemps(2, 0, 36, 0, 0.2)

def tempsEnDate(année, jour, heure, minute, seconde):
    pass

def afficheDate(date = -1):
    pass

temps = secondeEnTemps(1000000000)
print(temps)
#afficheTemps(temps)
#afficheDate(tempsEnDate(temps))
#afficheDate()

def bisextile(jour):
    sec = jour * 86400
    #afficheDate(tempsEnDate(sec))
    an=année-1970
    if an//4 !=0:
        print("il n'y a aucune année bissextile")
    else:
        n=an//4
        L=[]
        for i in range(n):
            L.append(1972+i*4)
        return L

bisextile(20000)

