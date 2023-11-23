from functions import *

while True:
    print("")
    img_path = input("Entrez le chemin de l'image que vous souhaitez modifier : ")

    print_menu(img_path)

    choice = input("Entrez le numéro de votre choix : ")

    if choice == "1":
        gray_filter(img_path)

    elif choice == "2":
        print("\nAu revoir!")
        break
    
    else : 
        print("Choix invalide. Veuillez entrer une option valide.") 