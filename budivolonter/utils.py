#Kosta Novokmet
#uzima trenutnog korisnika koji je logovan na sistem
def getCurrentUser():
    from .model_funcs import getUsers
    #ovo je samo za testiranje ovako napisano, inace treba stvarno da se vidi ko je logovan
    return getUsers()[0]


#Kosta Novokmet
#vraca na kom kontinentu je neka drzava 
def getContinent(country):
    from .locations import countries,continents
    for contient,countries in continents.items():
        if country in countries: return contient
    return None


#vraca listu svih drzava na svetu
#za potrebe biranja drzava kada se pravi aktivnost
def getCountries():
    from .locations import countries
    return countries
