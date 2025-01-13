import json
from Person import Person
from Mentalist import Mentalist
from Operator import Operator


class Fleet:
    def __init__(self, name):
        self.__name = name
        self.__spaceships = []

    def get_name(self):
        return self.__name

    def get_spaceships(self):
        return self.__spaceships

    def set_name(self, name):
        self.__name = name

    def add_spaceship(self, spaceship):
        if len(self.__spaceships) < 15:
            self.__spaceships.append(spaceship)
        else:
            print("La capacité maximale de la flotte est atteinte.")

    def statistics(self):
        if not self.__spaceships:
            print(f"La flotte {self.__name} ne contient aucun vaisseau.")
            return

        total_crew = sum(len(ship.get_crew()) for ship in self.__spaceships)
        roles = {}
        for ship in self.__spaceships:
            for crew_member in ship.get_crew():
                role = crew_member.get_role() if hasattr(crew_member, 'get_role') else "Inconnu"
                roles[role] = roles.get(role, 0) + 1

        print(f"Statistiques de la flotte {self.__name} :")
        print(f"- Nombre total de membres d'équipage : {total_crew}")
        print(f"- Répartition des rôles : {roles}")


        
    def statistics_from_file(self, file_name="data.json"):
        try:
            # Charger les données depuis le fichier JSON
            with open(file_name, "r") as file:
                data = json.load(file)

            # Trouver la flotte par son nom
            fleet_data = next((fleet for fleet in data["fleets"] if fleet["name"] == self.__name), None)
            if not fleet_data:
                print(f"❌ Flotte '{self.__name}' non trouvée dans le fichier JSON.")
                return

            # Calcul des statistiques
            total_spaceships = len(fleet_data["spaceships"])
            total_crew = 0
            role_count = {}
            operational_count = 0
            damaged_count = 0

            for ship in fleet_data["spaceships"]:
                total_crew += len(ship["crew"])
                # Vérifier l'état du vaisseau
                if ship["condition"].lower() == "operational":
                    operational_count += 1
                else:
                    damaged_count += 1

                # Compter les rôles des membres d'équipage
                for member in ship["crew"]:
                    role = member["role"].lower()
                    role_count[role] = role_count.get(role, 0) + 1

            # Afficher les statistiques
            print(f"Statistiques de la flotte '{self.__name}' :")
            print(f"- Nombre total de vaisseaux : {total_spaceships}")
            print(f"- Nombre total de membres d'équipage : {total_crew}")
            print(f"- Répartition des rôles : {role_count}")
            print(f"- Vaisseaux opérationnels : {operational_count}")
            print(f"- Vaisseaux endommagés : {damaged_count}")

        except FileNotFoundError:
            print(f"❌ Fichier '{file_name}' introuvable.")
        except json.JSONDecodeError as e:
            print(f"❌ Erreur de format JSON : {e}")
        except Exception as e:
            print(f"❌ Une erreur est survenue : {e}")
