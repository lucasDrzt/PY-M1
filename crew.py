import random 
import time
import string
import os
import shutil
import sys

FRAME_DELAY = 0.05
DURATION = 5
CHARS = ['1', '0', ' ']  
CSI = "\x1b["  

def matrix_effect(duration=DURATION):
    """Affiche un effet Matrix dans le terminal."""
    cols, lines = shutil.get_terminal_size()
    end_time = time.time() + duration

    sys.stdout.write(f"{CSI}?25l")
    sys.stdout.flush()

    matrix = [" " for _ in range(cols)]
    speed = [random.randint(1, 5) for _ in range(cols)]

    try:
        while time.time() < end_time:
            for i in range(cols):
                if random.random() > 0.5:
                    char = random.choice(CHARS)
                    matrix[i] = char
                    sys.stdout.write(f"{CSI}{random.randint(1, lines)};{i}f")
                    sys.stdout.write(f"{CSI}32m{char}\033[0m")  
                    sys.stdout.flush()

                
                if speed[i] > 0:
                    speed[i] -= 1
                else:
                    speed[i] = random.randint(1, 5)
                    sys.stdout.write(f"{CSI}{lines};{i}f")
                    sys.stdout.write(" ")  
                    sys.stdout.flush()

            time.sleep(FRAME_DELAY)

    finally:
        
        sys.stdout.write(f"{CSI}2J")  
        sys.stdout.write(f"{CSI}0m")
        sys.stdout.write(f"{CSI}?25h")
        sys.stdout.flush()
        print("\033[92m✅ Le système est stabilisé.\033[0m\n")

if __name__ == "__main__":
    matrix_effect()

crew = [
    {"first_name": "John", "last_name": "Doe", "gender": "M", "age": 32, "role": "Captain"},
    {"first_name": "Anna", "last_name": "Smith", "gender": "F", "age": 29, "role": "Engineer"},
    {"first_name": "Paul", "last_name": "Brown", "gender": "M", "age": 35, "role": "Pilote"},
    {"first_name": "Laura", "last_name": "Johnson", "gender": "F", "age": 27, "role": "Technicien"},
    {"first_name": "Mike", "last_name": "White", "gender": "M", "age": 40, "role": "Pilote"}
]

action_counter = 0

def add_member(crew):

    def get_non_empty_input(prompt):
        while True:
            value = input(prompt)
            if value.strip():
                return value
            print("Ce champ est obligatoire. Veuillez réessayer.")

    first_name = input("Quelle est le prénom du membre d'équipage : ")
    while len(first_name) < 3 or len(first_name) > 15:
        print ("prénom contiennent entre 3 et 15 caractères")
        first_name = input("Quelle est le prénom du membre d'équipage : ")

    last_name = input("Quelle est le nom du membre d'équipage : ")
    while len(last_name) < 3 or len(last_name) > 15:
        print ("prénom contiennent entre 3 et 15 caractères")
        last_name = input("Quelle est le nom du membre d'équipage : ")


    gender = input("Quel est le genre du membre d'équipage : ")
    while not gender.strip():
        print("Le genre est obligatoire.")
        gender = input("Quel est le genre du membre d'équipage : ")

    role = input("Quel est le rôle du membre d'équipage : ")
    while not role.strip():
        print("Le rôle est obligatoire.")
        role = input("Quel est le rôle du membre d'équipage : ")

    age = input("Quel est l'âge du membre d'équipage : ")
    while True:
        if age.strip() and age.isdigit():
            age = int(age)
            break
        print("L'âge doit être un nombre valide.")
        age = input("Quel est l'âge du membre d'équipage : ")

    if role == 'Pilote' and age < 25:
        print("\033[91m⛔ Un pilote doit avoir au moins 25 ans.\033[0m")
        return
    if role == 'Technicien' and age < 18:
        print("\033[91m⛔ Un technicien doit avoir au moins 18 ans.\033[0m")
        return
    if age > 65:
        print("\033[91m⛔ Aucun membre ne peut avoir plus de 65 ans.\033[0m")
        return

    new_member = {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "age": age,
        "role": role
    }

    crew.append(new_member)
    print("Nouveau membre ajouté avec succès !")
    print(new_member)

def rm_member(crew):
    last_name = input("Quel est le nom du membre d'équipage à supprimer ? ")
    
    initial_length = len(crew)
    
    crew = [member for member in crew if member['last_name'] != last_name]
    
    if len(crew) < initial_length:
        print(f"Le membre avec le nom de famille '{last_name}' a été supprimé.")
    else:
        print(f"Aucun membre avec le nom de famille '{last_name}' n'a été trouvé.")

    return crew

def display_crew(crew):
    if not crew:
        print("\n\033[91m⚠️  L'équipage est vide pour le moment.\033[0m\n")  # Message en rouge
    else:
        print("\n\033[94m🚀 Liste des membres d'équipage :\033[0m\n")  # Titre en bleu
        for member in crew:
            print(f"\033[92m🌟 {member['first_name']} {member['last_name']}\033[0m")  # Prénom et nom en vert
            print(f"   \033[1m👤 Genre  :\033[0m {member['gender']}")
            print(f"   \033[1m🎂 Âge    :\033[0m {member['age']}")
            print(f"   \033[1m⚓ Rôle   :\033[0m {member['role']}")
            print("\033[90m" + "-" * 40 + "\033[0m")  # Séparateur gris

def check_crew(crew):
    if len(crew) < 2:
        print("\033[91m⛔ L'équipage doit contenir au moins 2 membres pour être prêt.\033[0m")
        return
    
    # Vérification des rôles
    has_pilot = any(member['role'].lower() == 'pilote' and member['age'] >= 25 for member in crew)
    has_technician = any(member['role'].lower() == 'technicien' and member['age'] >= 18 for member in crew)
    over_65 = any(member['age'] > 65 for member in crew)

    if over_65:
        print("\033[91m⛔ L'équipage contient un membre âgé de plus de 65 ans.\033[0m")
    elif has_pilot and has_technician:
        print("\033[92m✅ L'équipage est prêt pour la mission !\033[0m 🚀")
    else:
        print("\033[91m⛔ L'équipage doit contenir au moins un pilote de 25 ans et un technicien de 18 ans.\033[0m")

def clear_terminal():
    """Efface le terminal en fonction du système d'exploitation."""
    os.system('cls' if os.name == 'nt' else 'clear')

def user_do():
    global crew, action_counter  
    while True:  
        clear_terminal()  
        print("\n--- MENU DE L'ÉQUIPAGE ---")
        print("1. Ajouter un membre")
        print("2. Supprimer un membre")
        print("3. Afficher l'équipage")
        print("4. Vérifier l'équipage")
        print("5. Quitter")

        lunch_function = input("Entrez le numéro de l'action à effectuer : ")
        
        while lunch_function not in ["1", "2", "3", "4", "5"]:
            print("Entrez un nombre valide (1 à 5).")
            lunch_function = input("Entrez le numéro de l'action à effectuer : ")

        if lunch_function == "1":
            add_member(crew)
        elif lunch_function == "2":
            crew = rm_member(crew)
        elif lunch_function == "3":
            display_crew(crew)
        elif lunch_function == "4":
            check_crew(crew)
        elif lunch_function == "5":
            print("👋 Au revoir !")
            break  

        action_counter += 1

        if action_counter % 1 == 0:
            print("\n🎲 \033[94mUn événement aléatoire se produit...\033[0m\n")
            trigger_random_event(crew)

        input("\n\033[90m[Appuyez sur Entrée pour continuer...]\033[0m")

def matrix_effect(duration=5):
    columns = os.get_terminal_size().columns
    lines = os.get_terminal_size().lines   
    end_time = time.time() + duration
    
    while time.time() < end_time:
        matrix_line = ''.join(random.choices("01 ", k=columns))
        print(f"\033[92m{matrix_line}\033[0m")
        time.sleep(0.1)  

    print("\033[93m🛠️  Récupération du système en cours...\033[0m")
    time.sleep(1)
    print("\033[92m✅ Le système est stabilisé. Ouf !\033[0m\n")

def simulate_terminal_glitch():
    for _ in range(10):
        glitch_line = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*()', k=120))
        print(f"\033[91m{glitch_line}\033[0m")
        time.sleep(0.1)
    print("\033[93m🛠️  Réparation de la console en cours...\033[0m")
    time.sleep(1)
    print("\033[92m✅ Console restaurée avec succès !\033[0m\n")

def trigger_random_event(crew):
    if not crew:
        print("\033[93m⚠️  Aucun événement ne peut se produire, l'équipage est vide.\033[0m")
        return

    event = random.choice(['quit', 'promote', 'funny_event1', 'matrix_event'])
    selected_member = random.choice(crew)

    if event == 'quit':
        crew.remove(selected_member)
        print(f"\033[91m🚪 {selected_member['first_name']} {selected_member['last_name']} a quitté l'équipage.\033[0m")

    elif event == 'promote':
        old_role = selected_member['role']
        new_role = 'Pilote' if old_role == 'Technicien' else 'Technicien'
        selected_member['role'] = new_role
        print(f"\033[92m🎖️ {selected_member['first_name']} {selected_member['last_name']} a été promu(e) au poste de {new_role}.\033[0m")

    elif event == 'funny_event1':
        print(f"\033[96m😂 {selected_member['first_name']} {selected_member['last_name']} a renversé son café sur la console... 😱\033[0m")
        time.sleep(1)
        simulate_terminal_glitch()

    elif event == 'matrix_event':
        print(f"\033[95m🧑‍💻 {selected_member['first_name']} {selected_member['last_name']} a lancé une commande étrange... Que se passe-t-il ?\033[0m")
        time.sleep(1)
        matrix_effect()



user_do()
