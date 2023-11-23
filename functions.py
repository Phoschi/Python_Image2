from PIL import Image, ImageFilter 
from art import tprint
import cv2
import numpy as np
from logger import log

def print_menu(img_path):
    log("Affichage du menu")
    tprint("Menu")
    print("1. Gray")
    print("2. Blur")
    print("3. Dilate")
    print("4. Rotate")
    print("5. Resize")
    print("6. Text")
    print("7. Watercolor")
    print("8. Leave\n")

    
def gray_filter(img_path) :
    log("Filtrage en noir et blanc")
    
    # Importer l'image à convertir
    image = Image.open(img_path)

    # Conversion image en noir et blanc (gray)
    gray_img = image.convert("L")

    # Enregistrement de l'image 
    new_img_path = "gray.jpeg"
    gray_img.save(new_img_path)
    
    print("\nFiltre aquarelle appliqué. Enregistré sous le nom de", new_img_path)

    
    
def blur_filter(img_path, blur_choice):
    log("Filtrage en flou")
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
    
    print("\nFiltre aquarelle appliqué. Enregistré sous le nom de", new_img_path)

    

def dilate_filter(img_path):
    log("Filtrage par dilation")
    
    image = cv2.imread(img_path)
    kernel = np.ones((5, 5), np.uint8) 
    dilated_image = cv2.dilate(image, kernel, iterations=1)
    
    new_img_path = "dilate.jpeg"
    cv2.imwrite(new_img_path, dilated_image)
    
    print("\nFiltre aquarelle appliqué. Enregistré sous le nom de", new_img_path)

    

def rotation(img_path):
    log("Rotation de l'image")
    
    # Importer l'image à convertir
    image = Image.open(img_path)

    # Demande à l'utilisateur du choix de l'angle de rotation
    value = int(input("Entrez un angle de rotation : "))

    # Insertion de la valeur de l'utilisateur en paramètre de la fonction de rotation "rotate()"
    img_rot = image.rotate(value, expand=True)

    # Enregistrement de l'image
    new_img_path = "rotate.jpeg"
    img_rot.save(new_img_path)

    print("\nFiltre aquarelle appliqué. Enregistré sous le nom de", new_img_path)



# Cette fonction redimensionne une image et la sauvegarde avec de nouvelles dimensions.
def resize_image(img_path):
    log("Redimmension de l'image")
    
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
            
    print("\nFiltre aquarelle appliqué. Enregistré sous le nom de", new_img_path)

            

def message(img_path):
    log("Ajout d'un message sur l'image")
    
    # Importer l'image à convertir
    image = cv2.imread(img_path, 1)

    # Demande à l'utilisateur du champ personnalisé
    user_text = input("Tapez le texte à afficher sur l'image : ")

    # Affichage du champ personnalisé sur l'image
    written = cv2.putText(
        img = image,
        text = user_text,
        org = (50, 50),
        fontFace = cv2.FONT_HERSHEY_DUPLEX,
        fontScale = 3.0,
        color = (255, 0, 0),
        thickness = 3
    )

    # Lecture du champ personnalisé + enregistrement de l'image
    new_img_path = "message.jpeg"
    cv2.imwrite(new_img_path, written)
    
    print("\nFiltre aquarelle appliqué. Enregistré sous le nom de", new_img_path)

    
    
import cv2
import numpy as np

def watercolor_filter(img_path):
    log("Filtre aquarelle appliqu")

    image = cv2.imread(img_path)

    # Convertir l'image en format flottant
    float_img = np.float32(image)

    # Appliquer un filtre bilatéral pour simuler un effet aquarelle
    watercolor_img = cv2.bilateralFilter(float_img, 9, 75, 75)

    # Convertir le résultat en format 8 bits
    watercolor_img = np.uint8(watercolor_img)

    # Enregistrer la nouvelle image
    new_img_path = "aquarelle.jpeg"
    cv2.imwrite(new_img_path, watercolor_img)

    print("\nFiltre aquarelle appliqué. Enregistré sous le nom de", new_img_path)

