import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from random import choice

def resize_image(image_path, new_width, new_height):
    image = Image.open(image_path)
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

def get_computer_choice():
    return choice(["pierre", "papier", "ciseaux"])

def determine_winner(user_choice):
    computer_choice = get_computer_choice()
    computer_choice_text.set(f"Ordinateur a choisi : {computer_choice}")
    update_choices_display(user_choice, computer_choice)
    
    if user_choice == computer_choice:
        scores["egalites"] += 1
        winner_text.set("Égalité !")
        result_frame.configure(bg='light gray')
    elif (user_choice == "pierre" and computer_choice == "ciseaux") or \
         (user_choice == "papier" and computer_choice == "pierre") or \
         (user_choice == "ciseaux" and computer_choice == "papier"):
        scores["joueur"] += 1
        winner_text.set("Vous avez gagné !")
        result_frame.configure(bg='light green')
    else:
        scores["ordinateur"] += 1
        winner_text.set("L'ordinateur a gagné.")
        result_frame.configure(bg='salmon')

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
window.configure(bg='light blue')

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
choice_frame = tk.Frame(window, bg='light blue')
choice_frame.pack(pady=10)

result_frame = tk.Frame(window, bg='light blue')
result_frame.pack(pady=10)

# Boutons pour les choix
tk.Button(choice_frame, image=pierre_image, command=lambda: determine_winner("pierre"), bg='light blue').pack(side=tk.LEFT, padx=5)
tk.Button(choice_frame, image=papier_image, command=lambda: determine_winner("papier"), bg='light blue').pack(side=tk.LEFT, padx=5)
tk.Button(choice_frame, image=ciseaux_image, command=lambda: determine_winner("ciseaux"), bg='light blue').pack(side=tk.LEFT, padx=5)

# Labels pour afficher les choix et les résultats
user_choice_image_label = tk.Label(result_frame, bg='light blue')
user_choice_image_label.pack(side=tk.LEFT, padx=10)
computer_choice_image_label = tk.Label(result_frame, bg='light blue')
computer_choice_image_label.pack(side=tk.RIGHT, padx=10)

# Labels pour afficher le score, le gagnant et le choix de l'ordinateur
tk.Label(window, textvariable=computer_choice_text, bg='light blue', font=("Helvetica", 12)).pack()
tk.Label(result_frame, textvariable=winner_text, bg='light blue', font=("Helvetica", 14)).pack()
tk.Label(window, textvariable=score_text, bg='light blue', font=("Helvetica", 14)).pack()

# Bouton Quitter
tk.Button(window, text="Quitter", command=quitter, bg='light grey').pack(pady=10)

update_scores()  # Initialiser l'affichage des scores
window.mainloop()
