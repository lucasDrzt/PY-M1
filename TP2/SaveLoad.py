import json

def save_data(data, file_name):
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"✅ Données sauvegardées dans '{file_name}'.")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")


def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        print(f"✅ Données chargées depuis '{file_name}'.")
        return data
    except FileNotFoundError:
        print(f"❌ Fichier '{file_name}' introuvable.")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Erreur de format JSON : {e}")
        return None
    except Exception as e:
        print(f"❌ Erreur lors du chargement : {e}")
        return None
