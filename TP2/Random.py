import random

class Vaisseau:
    def __init__(self, nom, vie, attaque):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque

    def attaquer(self, ennemi):
        degats = random.randint(0, self.attaque)
        ennemi.vie -= degats
        print(f"{self.nom} attaque {ennemi.nom} et inflige {degats} dégâts!")

    def est_vivant(self):
        return self.vie > 0

vaisseau1 = Vaisseau("Étoile Noire", 100, 20)
vaisseau2 = Vaisseau("Millenium Falcon", 80, 25)

# Boucle de combat
while vaisseau1.est_vivant() and vaisseau2.est_vivant():
    vaisseau1.attaquer(vaisseau2)
    if vaisseau2.est_vivant():
        vaisseau2.attaquer(vaisseau1)

if vaisseau1.est_vivant():
    print(f"{vaisseau1.nom} remporte la bataille!")
else:
    print(f"{vaisseau2.nom} remporte la bataille!")
