from functions import *
from logger import log
import os

while True:
    print("")
    img_path = input("\n\nEntrez le chemin de l'image que vous souhaitez modifier : ")

    while not is_valid_image_path(img_path):
        img_path = input("\n\nEntrez le chemin de l'image que vous souhaitez modifier : ")

    img_path_list = [img_path]

    print_menu(img_path_list)

    choice = input("Entrez le numéro de votre choix : ")

    if choice == "1":
        gray_filter(img_path)
    elif choice == "2":
        blur_choice = input("\nQuelle puissance de floutage voulez-vous ?\n"
                            "1. floutage faible\n"
                            "2. floutage moyen\n"
                            "3. floutage fort\n"
                            "4. floutage très fort\n"
                            "Entrez le numéro de votre choix : ")
        if blur_choice == "1":
            blur_filter(img_path, 1)
        elif blur_choice == "2":
            blur_filter(img_path, 2)
        elif blur_choice == "3":
            blur_filter(img_path, 3)
        elif blur_choice == "4":
            blur_filter(img_path, 4)
        else:
            print("Choix invalide. Veuillez entrer une option valide.")
    elif choice == "3":
        dilate_filter(img_path)
    elif choice == "4":
        rotation(img_path)
    elif choice == "5":
        resize_image(img_path)
    elif choice == "6":
        message(img_path)
    elif choice == "7":
        watercolor_filter(img_path)
    elif choice == "8":
        num_images = int(input("\nEntrez le nombre d'images à utiliser pour le GIF : "))
        gif_images = []
        for i in range(num_images):
            img_choice = input(f"Entrez le chemin de l'image {i + 1} : ")

            while not is_valid_image_path(img_choice):
                img_choice = input(f"Entrez le chemin de l'image {i + 1} : ")

            gif_images.append(Image.open(img_choice))

        gif_output_path = input("\nEntrez le nom du fichier GIF de sortie : ")
        create_gif(gif_images, gif_output_path)

    elif choice == "9":
        print("\nAu revoir!")
        break

    else:
        print("Choix invalide. Veuillez entrer une option valide.")
