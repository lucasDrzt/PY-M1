from Person import Person

class Mentalist(Person):
    def __init__(self, first_name, last_name, gender, age, mana=100):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = mana

    def get_mana(self):
        return self.__mana

    def set_mana(self, mana):
        if mana >= 0:
            self.__mana = mana
        else:
            raise ValueError("Les points de mana doivent être positifs ou nuls.")

    def act(self, target):
        if self.__mana < 20:
            return f"{self.get_first_name()} {self.get_last_name()} n'a pas assez de mana pour agir."

        self.__mana -= 20

        if hasattr(target, "act") and callable(target.act):
            action_result = target.act()
            return (f"{self.get_first_name()} {self.get_last_name()} utilise ses pouvoirs mentaux "
                    f"pour influencer {target.get_first_name()} {target.get_last_name()}.\n"
                    f"Action réalisée : {action_result}")
        else:
            return (f"{self.get_first_name()} {self.get_last_name()} tente d'influencer la cible, "
                    f"mais celle-ci ne peut pas agir.")

    def recharge(self):
        if self.__mana < 100:
            self.__mana = min(self.__mana + 50, 100)
            return (f"{self.get_first_name()} {self.get_last_name()} se recharge en mana. "
                    f"Mana actuel : {self.__mana}")
        else:
            return (f"{self.get_first_name()} {self.get_last_name()} a déjà le mana au maximum (100).")
