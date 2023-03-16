import json

# POO
class soldat:
    def __init__(self):

        # Soldat et attribution des ses caractéristiques
        self._fiche_soldat = {
            "prenom": "John",
            "age": 49,
            "genre": "homme alpha/ sigma",
            "ID": "SERIA 117"
        }

    # Conversion de la fiche du major en Json
    def to_json(self):
        return json.dumps(self._fiche_soldat)

    #Getter et Setter
    def get_fiche_soldat(self):
        return self._fiche_soldat

    def set_fiche_soldat(self, fiche_soldat):
        self._fiche_soldat = fiche_soldat

# Affichage de l'objet JSON correspondant au dictionnaire
soldat = soldat()
print("Fiche du major : ", soldat.to_json())
