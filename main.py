import tkinter as tk
from random import choice
from tkinter import messagebox
from tkinter import ttk


def resize_image(image_path, width, height):
    image = tk.PhotoImage(file=image_path)
    image = image.subsample(2)
    return image
def get_computer_choice():
    return choice(["pierre", "papier", "ciseaux"])

def determine_winner(user_choice):
    computer_choice = get_computer_choice()
    computer_choice_text.set(f"Ordinateur a choisi : {computer_choice}")
    update_choices_display(user_choice, computer_choice)
    
    if user_choice == computer_choice:
        scores["egalites"] += 1
        winner_text.set("Égalité !")
    elif (user_choice == "pierre" and computer_choice == "ciseaux") or \
         (user_choice == "papier" and computer_choice == "pierre") or \
         (user_choice == "ciseaux" and computer_choice == "papier"):
        scores["joueur"] += 1
        winner_text.set("Vous avez gagné !")
    else:
        scores["ordinateur"] += 1
        winner_text.set("L'ordinateur a gagné.")

    update_scores()

def update_scores():
    score_text.set(f"Scores - Joueur: {scores['joueur']}, Ordinateur: {scores['ordinateur']}, Égalités: {scores['egalites']}")

def update_choices_display(user_choice, computer_choice):
    user_choice_image_label.config(image=choice_images[user_choice])
    computer_choice_image_label.config(image=choice_images[computer_choice])

def quitter():
    window.destroy()

# Initialisation de Tkinter
window = tk.Tk()
window.title("Pierre-Papier-Ciseaux")
window.configure(bg='white')

# Chargement et redimensionnement des images
pierre_image = resize_image("./picture/pierre.png", 80, 80)
papier_image = resize_image("./picture/papier.png", 80, 80)
ciseaux_image = resize_image("./picture/ciseaux.png", 80, 80)

# Dictionnaire des images
choice_images = {"pierre": pierre_image, "papier": papier_image, "ciseaux": ciseaux_image}

# Variables globales
scores = {"joueur": 0, "ordinateur": 0, "egalites": 0}
winner_text = tk.StringVar()
score_text = tk.StringVar()
computer_choice_text = tk.StringVar()

# Création de l'interface
frame_choix = tk.Frame(window, bg='white')
frame_choix.pack(pady=10)

frame_resultat = tk.Frame(window, bg='white')
frame_resultat.pack(pady=10)

# Boutons pour les choix
tk.Button(frame_choix, image=pierre_image, command=lambda: determine_winner("pierre")).pack(side=tk.LEFT)
tk.Button(frame_choix, image=papier_image, command=lambda: determine_winner("papier")).pack(side=tk.LEFT)
tk.Button(frame_choix, image=ciseaux_image, command=lambda: determine_winner("ciseaux")).pack(side=tk.LEFT)

# Labels pour afficher les choix et les résultats
user_choice_image_label = tk.Label(frame_resultat, bg='white')
user_choice_image_label.pack(side=tk.LEFT)
computer_choice_image_label = tk.Label(frame_resultat, bg='white')
computer_choice_image_label.pack(side=tk.RIGHT)

# Labels pour afficher le score, le gagnant et le choix de l'ordinateur
tk.Label(window, textvariable=computer_choice_text, bg='white', font=("Helvetica", 12)).pack()
tk.Label(window, textvariable=winner_text, bg='white', font=("Helvetica", 14)).pack()
tk.Label(window, textvariable=score_text, bg='white', font=("Helvetica", 14)).pack()

# Bouton Quitter
tk.Button(window, text="Quitter", command=quitter, bg='light grey').pack(pady=10)

update_scores()  # Initialiser l'affichage des scores
window.mainloop()
