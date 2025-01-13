import sys
import os
from Fleet import Fleet
from Spaceship import Spaceship
from Operator import Operator
from Mentalist import Mentalist
from SaveLoad import save_data, load_data
from Matrix import matrix_effect


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title(title):
    print("\033[1;36m" + "═" * (len(title) + 4))
    print(f"| {title} |")
    print("═" * (len(title) + 4) + "\033[0m")

def main_menu():
    fleets = []
    file_name = "data.json"  

    while True:
        clear_terminal()
        print_title("🚀 MENU DE GESTION DES FLOTES")
        print("1️⃣ Ajouter une flotte")
        print("2️⃣ Ajouter un vaisseau à une flotte")
        print("3️⃣ Gérer un équipage")
        print("4️⃣ Afficher les statistiques d'une flotte")
        print("5️⃣ Sauvegarder la flotte")
        print("6️⃣ Charger une flotte")
        print("7️⃣ Quitter")

        choix = input("Choisissez une option : ")

        if not choix.isdigit():
            print("❌ Veuillez entrer un nombre valide.")
            input("\nAppuyez sur Entrée pour continuer...")
            continue

        choix = int(choix)

        if choix == 1:
            clear_terminal()
            fleet_name = input("✏️ Entrez le nom de la flotte : ")
            fleet = Fleet(fleet_name)
            fleets.append(fleet)
            print(f"✅ Flotte '{fleet_name}' ajoutée avec succès.")
            input("\nAppuyez sur Entrée pour continuer...")

        elif choix == 2:
            clear_terminal()
            if not fleets:
                print("❌ Aucune flotte disponible. Veuillez en créer une d'abord.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            print("🌌 Flottes disponibles :")
            for idx, fleet in enumerate(fleets):
                print(f"{idx + 1}. {fleet.get_name()}")

            fleet_idx = input("🔢 Choisissez une flotte (par numéro) : ")
            if not fleet_idx.isdigit():
                print("❌ Veuillez entrer un nombre valide.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            fleet_idx = int(fleet_idx) - 1

            if 0 <= fleet_idx < len(fleets):
                fleet = fleets[fleet_idx]
                ship_name = input("✏️ Entrez le nom du vaisseau : ")
                ship_type = input("✏️ Entrez le type de vaisseau : ")
                spaceship = Spaceship(ship_name, ship_type)
                fleet.add_spaceship(spaceship)
                print(f"✅ Vaisseau '{ship_name}' ajouté à la flotte.")
                input("\nAppuyez sur Entrée pour continuer...")
            else:
                print("❌ Flotte invalide.")
                input("\nAppuyez sur Entrée pour continuer...")

        elif choix == 3:
            clear_terminal()
            if not fleets:
                print("❌ Aucune flotte disponible. Veuillez en créer une d'abord.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            print("🌌 Flottes disponibles :")
            for idx, fleet in enumerate(fleets):
                print(f"{idx + 1}. {fleet.get_name()}")

            fleet_idx = input("🔢 Choisissez une flotte (par numéro) : ")
            if not fleet_idx.isdigit():
                print("❌ Veuillez entrer un nombre valide.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            fleet_idx = int(fleet_idx) - 1

            if 0 <= fleet_idx < len(fleets):
                fleet = fleets[fleet_idx]
                print("🚀 Vaisseaux dans la flotte :")
                for idx, spaceship in enumerate(fleet.get_spaceships()):
                    print(f"{idx + 1}. {spaceship.get_name()}")

                ship_idx = input("🔢 Choisissez un vaisseau (par numéro) : ")
                if not ship_idx.isdigit():
                    print("❌ Veuillez entrer un nombre valide.")
                    input("\nAppuyez sur Entrée pour continuer...")
                    continue

                ship_idx = int(ship_idx) - 1

                if 0 <= ship_idx < len(fleet.get_spaceships()):
                    spaceship = fleet.get_spaceships()[ship_idx]
                    manage_crew(spaceship)
                else:
                    print("❌ Vaisseau invalide.")
                    input("\nAppuyez sur Entrée pour continuer...")
            else:
                print("❌ Flotte invalide.")
                input("\nAppuyez sur Entrée pour continuer...")

        elif choix == 4:
            clear_terminal()
            if not fleets:
                print("❌ Aucune flotte disponible.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            print("🌌 Flottes disponibles :")
            for idx, fleet in enumerate(fleets):
                print(f"{idx + 1}. {fleet.get_name()}")

            fleet_idx = input("🔢 Choisissez une flotte (par numéro) : ")
            if not fleet_idx.isdigit():
                print("❌ Veuillez entrer un nombre valide.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            fleet_idx = int(fleet_idx) - 1

            if 0 <= fleet_idx < len(fleets):
                fleet = fleets[fleet_idx]
                fleet.statistics_from_file("data.json")
                input("\nAppuyez sur Entrée pour continuer...")
            else:
                print("❌ Flotte invalide.")
                input("\nAppuyez sur Entrée pour continuer...")


        elif choix == 5:
            clear_terminal()
            if not fleets:
                print("❌ Aucune flotte disponible à sauvegarder.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            fleet_data = {
                "fleets": [
                    {
                        "name": fleet.get_name(),
                        "spaceships": [
                            {
                                "name": ship.get_name(),
                                "type": ship.get_ship_type(),
                                "condition": ship.get_condition(),
                                "crew": [
                                    {
                                        "first_name": member.get_first_name(),
                                        "last_name": member.get_last_name(),
                                        "role": member.get_role() if isinstance(member, Operator) else "Mentalist",
                                        "age": member.get_age()
                                    }
                                    for member in ship.get_crew()
                                ]
                            }
                            for ship in fleet.get_spaceships()
                        ]
                    }
                    for fleet in fleets
                ]
            }

            save_data(fleet_data, file_name)
            print(f"✅ Données de la flotte sauvegardées dans '{file_name}'.")
            input("\nAppuyez sur Entrée pour continuer...")


        elif choix == 6:
            clear_terminal()
            loaded_data = load_data(file_name)
            if loaded_data and "fleets" in loaded_data:
                fleets.clear()
                try:
                    for fleet_info in loaded_data["fleets"]:
                        fleet = Fleet(fleet_info["name"])
                        for ship_info in fleet_info.get("spaceships", []):
                            spaceship = Spaceship(
                                ship_info["name"],
                                ship_info["type"],
                                ship_info.get("condition", "opérationnel")
                            )
                            for member_info in ship_info.get("crew", []):
                                if member_info["role"].lower() == "mentaliste":
                                    member = Mentalist(
                                        member_info["first_name"],
                                        member_info["last_name"],
                                        "Unknown",
                                        member_info["age"]
                                    )
                                else:
                                    member = Operator(
                                        member_info["first_name"],
                                        member_info["last_name"],
                                        "Unknown",
                                        member_info["age"],
                                        member_info["role"]
                                    )
                                spaceship.add_member(member)
                            fleet.add_spaceship(spaceship)
                        fleets.append(fleet)
                    print(f"✅ Flotte(s) chargée(s) depuis '{file_name}'.")
                    input("\nAppuyez sur Entrée pour continuer...")
                except KeyError as e:
                    print(f"❌ Données invalides ou manquantes dans le fichier JSON : {e}")
                    input("\nAppuyez sur Entrée pour continuer...")
            else:
                print("❌ Aucun fichier valide trouvé pour charger les données.")
                input("\nAppuyez sur Entrée pour continuer...")


        elif choix == 7:
            clear_terminal()
            print("👋 Au revoir !")
            sys.exit()

        else:
            print("❌ Option invalide. Veuillez réessayer.")
            input("\nAppuyez sur Entrée pour continuer...")

def manage_crew(spaceship):
    while True:
        clear_terminal()
        print_title("👨‍🚀 MENU DE L'ÉQUIPAGE")
        print("1️⃣ Ajouter un membre")
        print("2️⃣ Supprimer un membre")
        print("3️⃣ Afficher l'équipage")
        print("4️⃣ Vérifier l'équipage")
        print("5️⃣ Retour")

        choix = input("🌟 Choisissez une option : ")

        if not choix.isdigit():
            print("❌ Veuillez entrer un nombre valide.")
            input("\nAppuyez sur Entrée pour continuer...")
            continue

        choix = int(choix)

        if choix == 1:
            first_name = input("✏️ Prénom : ")
            last_name = input("✏️ Nom : ")
            gender = input("✏️ Genre : ")
            age = input("✏️ Âge : ")
            if not age.isdigit():
                print("❌ Veuillez entrer un âge valide.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            age = int(age)
            role = input("✏️ Rôle (Mentaliste ou rôle spécifique) : ")

            if role.lower() == "mentaliste":
                member = Mentalist(first_name, last_name, gender, age)
            else:
                experience = input("✏️ Expérience : ")
                if not experience.isdigit():
                    print("❌ Veuillez entrer un nombre valide pour l'expérience.")
                    input("\nAppuyez sur Entrée pour continuer...")
                    continue

                experience = int(experience)
                member = Operator(first_name, last_name, gender, age, role, experience)

            spaceship.add_member(member)

        elif choix == 2:
            crew = spaceship.get_crew()
            if not crew:
                print("❌ Équipage vide.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            print("🚀 Membres de l'équipage :")
            for idx, member in enumerate(crew):
                print(f"{idx + 1}. {member.get_first_name()} {member.get_last_name()}")

            member_idx = input("🔢 Choisissez un membre à supprimer (par numéro) : ")
            if not member_idx.isdigit():
                print("❌ Veuillez entrer un nombre valide.")
                input("\nAppuyez sur Entrée pour continuer...")
                continue

            member_idx = int(member_idx) - 1

            if 0 <= member_idx < len(crew):
                removed_member = crew.pop(member_idx)
                print(f"✅ {removed_member.get_first_name()} {removed_member.get_last_name()} a été supprimé de l'équipage.")
                input("\nAppuyez sur Entrée pour continuer...")
            else:
                print("❌ Membre invalide.")
                input("\nAppuyez sur Entrée pour continuer...")

        elif choix == 3:
            spaceship.list_crew()
            input("\nAppuyez sur Entrée pour continuer...")

        elif choix == 4:
            spaceship.check_preparation()
            input("\nAppuyez sur Entrée pour continuer...")

        elif choix == 5:
            break

        else:
            print("❌ Option invalide. Veuillez réessayer.")
            input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    try:
        clear_terminal()
        matrix_effect()
        main_menu()
    except Exception as e:
        print(f"❌ Une erreur inattendue est survenue : {e}")
