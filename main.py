import tkinter as tk
from random import choice
from tkinter import PhotoImage
import sys
import os

# Function to determine the resource path where the images are located
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Function to resize the image (defined before use)
def resize_image(image_path, width, height):
    image = PhotoImage(file=resource_path(image_path))
    image = image.subsample(2)  # You might want to adjust subsampling based on the original image size
    return image

def get_computer_choice():
    return choice(["rock", "paper", "scissors"])

def determine_winner(user_choice):
    computer_choice = get_computer_choice()
    computer_choice_text.set(f"Computer chose: {computer_choice}")
    update_choices_display(user_choice, computer_choice)
    
    if user_choice == computer_choice:
        scores["ties"] += 1
        winner_text.set("Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        scores["player"] += 1
        winner_text.set("You won!")
    else:
        scores["computer"] += 1
        winner_text.set("Computer won.")

    update_scores()

def update_scores():
    score_text.set(f"Scores - Player: {scores['player']}, Computer: {scores['computer']}, Ties: {scores['ties']}")

def update_choices_display(user_choice, computer_choice):
    user_choice_image_label.config(image=choice_images[user_choice])
    computer_choice_image_label.config(image=choice_images[computer_choice])

def quit_game():
    window.destroy()

# Initialize the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.configure(bg='white')

# Use the resource_path function to specify the correct path for the images
rock_image = resize_image("picture/rock.png", 80, 80)
paper_image = resize_image("picture/paper.png", 80, 80)
scissors_image = resize_image("picture/scissors.png", 80, 80)

# Store the PhotoImage objects in a dictionary
choice_images = {"rock": rock_image, "paper": paper_image, "scissors": scissors_image}

# Initialize the scores and text variables
scores = {"player": 0, "computer": 0, "ties": 0}
winner_text = tk.StringVar()
score_text = tk.StringVar()
computer_choice_text = tk.StringVar()

# Create frames for choice and result display
choice_frame = tk.Frame(window, bg='white')
choice_frame.pack(pady=10)

result_frame = tk.Frame(window, bg='white')
result_frame.pack(pady=10)

# Create buttons for the choices
tk.Button(choice_frame, image=rock_image, command=lambda: determine_winner("rock")).pack(side=tk.LEFT)
tk.Button(choice_frame, image=paper_image, command=lambda: determine_winner("paper")).pack(side=tk.LEFT)
tk.Button(choice_frame, image=scissors_image, command=lambda: determine_winner("scissors")).pack(side=tk.LEFT)

# Labels for displaying the user and computer choices
user_choice_image_label = tk.Label(result_frame, bg='white')
user_choice_image_label.pack(side=tk.LEFT)
computer_choice_image_label = tk.Label(result_frame, bg='white')
computer_choice_image_label.pack(side=tk.RIGHT)

# Labels for displaying the score and results
tk.Label(window, textvariable=computer_choice_text, bg='white', font=("Helvetica", 12)).pack()
tk.Label(window, textvariable=winner_text, bg='white', font=("Helvetica", 14)).pack()
tk.Label(window, textvariable=score_text, bg='white', font=("Helvetica", 14)).pack()

tk.Button(window, text="Quit", command=quit_game, bg='light grey').pack(pady=10)

update_scores()


window.mainloop()
