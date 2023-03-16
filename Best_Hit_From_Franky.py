import random

# POO
class TitreAleatoire:
    def __init__(self, musiques):
        self._musiques = musiques

    # Fonction random musique
    def generer_titre(self):
        musiques = random.choice(self._musiques)
        return f"{musiques}"

    # Getter et setter pour musiques
    def get_musiques(self):
        return self._musiques

    def set_musiques(self, musiques):
        self._musiques = musiques

# Liste des titres
musiques = ["Fruit de la passion",
          "Tu veux mon zizi ?",
          "Vas y Franky, c'est bon !",
          "La chatte à la voisine",
          "Alice ça glisse",
          "Tu pues du cul"]

phrase = TitreAleatoire(musiques)

# Génération une recommandation pour l'écoute d'une titre musical endiablé !
print("Titre à écouter ce soir : ", phrase.generer_titre())
