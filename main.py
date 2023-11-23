from functions import *
from logger import log

while True:
    print("")
    img_path = input("Entrez le chemin de l'image que vous souhaitez modifier : ")

    print_menu(img_path)

    choice = input("Entrez le numéro de votre choix : ")

    if choice == "1":
        gray_filter(img_path)
        
    elif choice == "2":
        while True:
            blur_choice = input("\nQuelle puissance de floutage voulez-vous ?\n"
                                "1. floutage faible\n"
                                "2. floutage moyen\n"
                                "3. floutage fort\n"
                                "4. floutage très fort\n"
                                "5. Revenir au menu principal\n\n"
                                "Entrez le numéro de votre choix : ")

            if blur_choice == "1":
                blur_filter(img_path, 1)
            elif blur_choice == "2":
                blur_filter(img_path, 2)
            elif blur_choice == "3":
                blur_filter(img_path, 3)
            elif blur_choice == "4":
                blur_filter(img_path, 4)
            elif blur_choice == "5":
                break
            else:
                print("Choix invalide. Veuillez entrer une option valide.")
                
    elif choice == "3":
        dilate_filter(img_path)
    
    elif choice =="4" :
        rotation(img_path)
        
    elif choice == "5":
        resize_image(img_path)
        
    elif choice == "6":
        message(img_path)
        
    elif choice == "7":
        watercolor_filter(img_path)

    elif choice == "8":
        print("\nAu revoir!")
        break
    
    else : 
        print("Choix invalide. Veuillez entrer une option valide.") 