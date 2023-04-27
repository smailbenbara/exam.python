class Vehicule:
    def __init__(self, marque, modele, annee, couleur):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee}) - {self.couleur}"


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, couleur, nb_portes):
        super().__init__(marque, modele, annee, couleur)
        self.nb_portes = nb_portes


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, couleur, cylindree):
        super().__init__(marque, modele, annee, couleur)
        self.cylindree = cylindree


class Autobus(Vehicule):
    def __init__(self, marque, modele, annee, couleur, nb_passagers):
        super().__init__(marque, modele, annee, couleur)
        self.nb_passagers = nb_passagers


class Metro(Vehicule):
    def __init__(self, marque, modele, annee, couleur, nb_wagons):
        super().__init__(marque, modele, annee, couleur)
        self.nb_wagons = nb_wagons


class GestionnaireVehicules:
    def __init__(self):
        self.vehicules = []

    def ajouter_vehicule(self, vehicule):
        self.vehicules.append(vehicule)

    def supprimer_vehicule(self, vehicule):
        self.vehicules.remove(vehicule)

    def modifier_vehicule(self, vehicule, nouvelle_marque, nouveau_modele, nouvelle_annee, nouvelle_couleur):
        vehicule.marque = nouvelle_marque
        vehicule.modele = nouveau_modele
        vehicule.annee = nouvelle_annee
        vehicule.couleur = nouvelle_couleur

    def afficher_vehicules(self):
        for vehicule in self.vehicules:
            print(vehicule)

    def stats_par_type(self):
        types = {}
        for vehicule in self.vehicules:
            if type(vehicule).__name__ in types:
                types[type(vehicule).__name__] += 1
            else:
                types[type(vehicule).__name__] = 1
        for vehicule_type, nb_vehicules in types.items():
            print(f"{vehicule_type}: {nb_vehicules}")

    def stats_par_prop(self, propriete):
        stats = {}
        for vehicule in self.vehicules:
            valeur = getattr(vehicule, propriete)
            if valeur in stats:
                stats[valeur] += 1
            else:
                stats[valeur] = 1
        for valeur, nb_vehicules in stats.items():
            print(f"{valeur}: {nb_vehicules}")


