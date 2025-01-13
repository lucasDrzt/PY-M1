from Person import Person

class Operator(Person):
    def __init__(self, first_name, last_name, gender, age, role, experience=0):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = experience

    def get_role(self):
        return self.__role

    def get_experience(self):
        return self.__experience

    def set_role(self, role):
        self.__role = role

    def set_experience(self, experience):
        if experience >= 0:
            self.__experience = experience
        else:
            raise ValueError("L'expérience doit être un entier positif.")

    def act(self):
        return f"{self.get_first_name()} {self.get_last_name()} {self.__role.lower()} exécute une action liée à son rôle."

    def gain_experience(self):
        self.__experience += 1
        return f"{self.get_first_name()} {self.get_last_name()} gagne de l'expérience ! Expérience actuelle : {self.__experience}"
