class Person:
    def __init__(self, first_name, last_name, gender, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("L'âge doit être un entier positif.")

    def introduce_yourself(self):
        article = "un" if self.__gender.lower() == "homme" else "une"
        return f"Je m'appelle {self.__last_name} {self.__first_name}, je suis {article} {self.__gender} et j'ai {self.__age} ans."
