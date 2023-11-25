from functions import *
from logger import log
import os 

print("\nLa CLI doit être rédigé sous la forme suivante :\n\nfileText.py --filters “filter_name&filter_name:filter_value” --i img_source_folder --o img_destination_folder/\n\nVoici la liste des fonctions que vous pouvez utiliser :\n\ngray_filter : appliquer un filtre noir et blanc \nblur_filter : appliquer un effet de flou \ndilate_filter : permet de dilater l'image \nrotation : appliquer une rotation selon le degré souhaité \nrezise_image : permet de redimentionner l'image \nmessage : afficher un message sur l'image \nwatercolor_filter : appliquer un filtre aquarelle \ncreate_gif : transformer l'image en GIF")

    

if __name__ == "__main__":
    while True:
        print("")

        image = image_import()
        print_menu(image)

        choice = input("Entrez le numéro de votre choix : ")

        if choice == "1":
            gray_filter(image)
        elif choice == "2":
            blur_choice = int(input("\nQuelle puissance de floutage voulez-vous ?\n"
                                "1. floutage faible\n"
                                "2. floutage moyen\n"
                                "3. floutage fort\n"
                                "4. floutage très fort\n"
                                "\nEntrez le numéro de votre choix : "))
            blur_filter(image, blur_choice)
        elif choice == "3":
            dilate_filter(image)

        elif choice == "4":
            rotation(image)

        elif choice == "5":
            resize_image(image)

        elif choice == "6":
            message(image)

        elif choice == "7":
            watercolor_filter(image)

        elif choice == "8":
            all_filters(image)

        elif choice == "9":
            num_images = int(input("\nEntrez le nombre d'images à utiliser pour le GIF : "))
            gif_images = []
            for i in range(num_images):
                img_choice = input(f"Entrez le chemin de l'image {i + 1} : ")

                while not is_valid_image_path(img_choice):
                    img_choice = input(f"Entrez le chemin de l'image {i + 1} : ")

                gif_images.append(Image.open(img_choice))

            gif_output_path = input("\nEntrez le nom du fichier GIF de sortie : ")
            create_gif(gif_images, gif_output_path)

        elif choice == "0":
            print("\nAu revoir!")
            break

        else:
            print("\nChoix invalide. Veuillez entrer une option valide.")
            
            