from PIL import Image, ImageFilter 
from art import tprint
import cv2
import numpy as np

def print_menu(img_path):
    tprint("Menu")
    print("1. Gray")
    print("2. Blur")
    print("3. Dilate")
    print("4. Rotate")
    print("5. Resize")
    print("6. Leave\n")

    
def gray_filter(img_path) :
    # Importer l'image à convertir
    image = Image.open(img_path)

    # Conversion image en noir et blanc (gray)
    gray_img = image.convert("L")

    # Enregistrement de l'image 
    new_img_path = "gray.jpeg"
    gray_img.save(new_img_path)
    
    
def blur_filter(img_path, blur_choice):
    
    image = Image.open(img_path)

    # Conversion image en flou
    if blur_choice == 1:
        blur_img = image.filter(ImageFilter.BoxBlur(2))
    elif blur_choice == 2:
        blur_img = image.filter(ImageFilter.BoxBlur(5))
    elif blur_choice == 3:
        blur_img = image.filter(ImageFilter.BoxBlur(8))
    elif blur_choice == 4:
        blur_img = image.filter(ImageFilter.BoxBlur(10))
    else:
        print("Choix invalide. Veuillez entrer une option valide.")
        return

    new_img_path = "blur.jpeg"
    blur_img.save(new_img_path)
    

def dilate_filter(img_path):
    
    image = cv2.imread(img_path)
    kernel = np.ones((5, 5), np.uint8) 
    dilated_image = cv2.dilate(image, kernel, iterations=1)
    cv2.imwrite("dilate.jpeg", dilated_image)
    

def rotation(img_path):
    # Importer l'image à convertir
    
    image = Image.open(img_path)

    # Demande à l'utilisateur du choix de l'angle de rotation
    value = int(input("Entrez un angle de rotation : "))

    # Insertion de la valeur de l'utilisateur en paramètre de la fonction de rotation "rotate()"
    img_rot = image.rotate(value, expand=True)

    # Enregistrement de l'image
    new_img_path = "rotate.jpeg"
    img_rot.save(new_img_path)



# Cette fonction redimensionne une image et la sauvegarde avec de nouvelles dimensions.
def resize_image(img_path):
    # Chemin de l'image à redimensionner
    image = Image.open(img_path)

    # Utilisation d'une boucle pour garantir que les dimensions entrées sont valides
    while True:
        try:
            # Demander à l'utilisateur la nouvelle largeur et hauteur
            new_width = int(input("Entrer la nouvelle largeur : "))
            new_height = int(input("Entrer la nouvelle hauteur : "))

            # Vérifier si les dimensions sont positives
            if new_width <= 0 or new_height <= 0:
                raise ValueError("Les dimensions doivent être des valeurs positives.")

            # Redimensionner l'image avec les nouvelles dimensions
            resized_img = image.resize((new_width, new_height))

            # Enregistrer la nouvelle image avec un nouveau chemin
            new_img_path = " resized.jpeg"
            resized_img.save(new_img_path)

            # Sortir de la boucle si les dimensions sont valides
            break

        # Capturer une exception en cas d'erreur de conversion des dimensions en entiers
        except ValueError as e:
            print(f"Erreur : {e}")
            print("Dimensions impossibles. Veuillez recommencer.")
            
