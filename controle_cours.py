
def sup21(n):
    if n < 21:
        print("False")
    else:
        print("True")

def pairs(liste):
    return [x for x in liste if x % 2 == 0]

def ajout4(liste):
    return liste + [4]

def to_strings(dico):
    liste = []
    for k, v in dico.items():
        liste.append(str(k) + ":" + str(v))
    return liste

def extremites(liste):
    return liste[:2]  + liste[-2:]

class Mot():
    def __init__ (self, mot):
        self.mot = mot
        
    def mot(self, mot):
        self.mot = mot
    
    def comptelettre(self, letter):
        if letter.lower() in self.lower():
            print(self.count(letter.lower()))
       
def tri_et_inverse(liste):
    rev = []
    for element in reversed(liste):
        rev.append(element)
    return (sorted(liste), rev)
            
def aller_a_paris(input_call=input):
    # code a remplir
    while input_call != 'paris':
        saisie = input_call('Question ')
    return saisie.lower()
    # quelque part dans le code de cette fonction: saisie = input_call('Question ')
    # en fonction de saisie on continue a demander ou on renvoie 'Paris'
    # Au lieu d'utiliser input comme en cours vous appelez input_call
    # par dÃ©faut elle vaut input donc vous pouvez appeller
    # aller_a_paris() pour tester a la main
    while True:
        return 0, 'Nulle Part'
  
ville_nom_pays = {
        'Paris':'France',
        'Berlin':'Allemagne',
        'Madrid':'Espagne',
        'Moscou':'Russie'
        } 

class Pays():
    def __init__ (self, nom, visa):
        self.nom = nom
        self.visa = visa


ville_pays = {
        'Paris' : Pays('France', False),
        'Berlin' : Pays('Allemagne', False),
        'Madrid' : Pays('Espagne', False),
        'Moscou' : Pays('Russie', True)
}

    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)