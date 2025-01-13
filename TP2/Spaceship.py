from Person import Person
from Mentalist import Mentalist
from Operator import Operator

class Spaceship:
    def __init__(self, name, ship_type, condition="opérationnel"):
        self.__name = name
        self.__ship_type = ship_type
        self.__crew = []
        self.__condition = condition

    def get_name(self):
        return self.__name

    def get_ship_type(self):
        return self.__ship_type

    def get_crew(self):
        return self.__crew

    def get_condition(self):
        return self.__condition

    def set_name(self, name):
        self.__name = name

    def set_ship_type(self, ship_type):
        self.__ship_type = ship_type

    def set_condition(self, condition):
        self.__condition = condition

    def add_member(self, member):
        if len(self.__crew) >= 10:
            print("Capacité maximale atteinte pour l'équipage.")
            return
        self.__crew.append(member)

    def list_crew(self):
        if not self.__crew:
            print("Aucun membre d'équipage à afficher.")
            return
        print(f"Équipage de {self.__name} :")
        for member in self.__crew:
            role = member.get_role() if hasattr(member, 'get_role') else "Inconnu"
            print(f"- {member.get_first_name()} {member.get_last_name()}, rôle : {role}")

    def check_preparation(self):
        if len(self.__crew) < 2:
            print("\033[91m⛔ L'équipage doit contenir au moins 2 membres pour être prêt.\033[0m")
            return

        has_pilot = any(isinstance(member, Operator) and member.get_role().lower() == 'pilote' and member.get_age() >= 25 for member in self.__crew)
        has_technician = any(isinstance(member, Operator) and member.get_role().lower() == 'technicien' and member.get_age() >= 18 for member in self.__crew)
        over_65 = any(member.get_age() > 65 for member in self.__crew)

        if over_65:
            print("\033[91m⛔ L'équipage contient un membre âgé de plus de 65 ans.\033[0m")
        elif has_pilot and has_technician:
            print("\033[92m✅ L'équipage est prêt pour la mission !\033[0m 🚀")
        else:
            print("\033[91m⛔ L'équipage doit contenir au moins un pilote de 25 ans et un technicien de 18 ans.\033[0m")

    def add_new_member(self):
        first_name = input("Quelle est le prénom du membre d'équipage : ")
        while len(first_name) < 3 or len(first_name) > 15:
            print("Le prénom doit contenir entre 3 et 15 caractères.")
            first_name = input("Quelle est le prénom du membre d'équipage : ")

        last_name = input("Quelle est le nom du membre d'équipage : ")
        while len(last_name) < 3 or len(last_name) > 15:
            print("Le nom doit contenir entre 3 et 15 caractères.")
            last_name = input("Quelle est le nom du membre d'équipage : ")

        gender = input("Quel est le genre du membre d'équipage : ")
        while not gender.strip():
            print("Le genre est obligatoire.")
            gender = input("Quel est le genre du membre d'équipage : ")

        role = input("Quel est le rôle du membre d'équipage (Mentaliste ou rôle spécifique) : ").capitalize()
        age = input("Quel est l'âge du membre d'équipage : ")
        while not age.isdigit():
            print("L'âge doit être un nombre valide.")
            age = input("Quel est l'âge du membre d'équipage : ")
        age = int(age)

        if role.lower() == 'mentaliste':
            member = Mentalist(first_name, last_name, gender, age)
        else:
            if role.lower() == 'pilote' and age < 25:
                print("\033[91m⛔ Un pilote doit avoir au moins 25 ans.\033[0m")
                return
            if role.lower() == 'technicien' and age < 18:
                print("\033[91m⛔ Un technicien doit avoir au moins 18 ans.\033[0m")
                return
            if age > 65:
                print("\033[91m⛔ Aucun membre ne peut avoir plus de 65 ans.\033[0m")
                return

            member = Operator(first_name, last_name, gender, age, role)

        self.__crew.append(member)
        print("✅ Nouveau membre ajouté avec succès !")
