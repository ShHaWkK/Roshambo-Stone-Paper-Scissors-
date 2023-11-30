from random import choice

def get_user_choice():
    user_choice = ""
    while user_choice not in ["pierre", "papier", "ciseaux", "quitter"]:
        user_choice = input("Pierre, Papier, Ciseaux ou Quitter ?").strip().lower()
        if user_choice not in ["pierre", "papier", "ciseaux", "quitter"]:
            print("Choix invalide. Veuillez choisir entre Pierre, Papier, Ciseaux ou Quitter.")
    return user_choice

def get_computer_choice()
    return choice(["pierre", "papier", "ciseaux"])

def determine_winner(user_choice, computer_choice):
    if user_choice == "quitter":
        return "Le jeu est terminé."
    elif user_choice == computer_choice:
        return "Egalité"
    elif (user_choice == "pierre" and computer_choice == "ciseaux") or (user_choice == "papier" and computer_choice == "pierre") or (user_choice == "ciseaux" and computer_choice == "papier"):
        return "Vous avez gagné !"
    else:
        return "L'ordinateur a gagné."

def main():
    user_choice = ""
    while user_choice != "quitter":
        user_choice = get_user_choice()
        if user_choice == "quitter":
            print("Le jeu est terminé.")
            break
        computer_choice = get_computer_choice()
        print(f"L'ordinateur a choisi : {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()


