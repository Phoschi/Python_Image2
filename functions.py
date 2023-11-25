from PIL import Image, ImageFilter, ImageOps
from art import tprint
import cv2
import numpy as np
from logger import log
import os


def is_valid_image_path(img_path):
    # Liste des extensions courantes de fichiers image
    extensions_valides = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    # Vérifie si le chemin est un fichier et a une extension d'image valide
    return os.path.isfile(img_path) and any(img_path.lower().endswith(ext) for ext in extensions_valides)



def image_import():
    while True:
        img_path = input("\n\nEntrez le chemin de l'image que vous souhaitez modifier : ")

        if is_valid_image_path(img_path):
            try:
                image = Image.open(img_path)
                return image
            except Exception as e:
                print(f"Erreur lors de l'ouverture de l'image : {e}")
        else:
            print("\nLe chemin d'image n'est pas valide. Veuillez entrer un chemin d'image correct.")





def print_menu(image):
    log("Affichage du menu")
    tprint("Menu")

    if image:
        print_second_menu()
    else:
        print("Veuillez charger une image avant d'afficher le menu.")




def print_second_menu():
    print("1. Noir et Blanc")
    print("2. Flou")
    print("3. Dilatation")
    print("4. Rotation")
    print("5. Redimensionnement")
    print("6. Texte")
    print("7. Aquarelle")
    print("8. Tous les filtres")
    print("9. GIF")
    print("0. Quitter\n")











def gray_filter(image, save_result=True):
    log("Conversion en Noir et Blanc")

    gray_img = image.convert("L")

    if save_result:
        new_img_path = "/Users/coding/Python_Image2/Images_finales/gray.jpg"
        new_img_name = "gray.jpg"
        
        gray_img.save(new_img_path)

        # Affiche un message indiquant que la conversion a été appliquée et où le nouveau fichier est enregistré
        print("\nConversion en Noir et Blanc appliquée.\n\nEnregistré sous le nom de : ", new_img_name, "\nSon chemin est :", new_img_path)
    else:
        # Si save_result est False, la fonction retourne simplement l'image en noir et blanc sans l'enregistrer
        return gray_img













def blur_filter(img, blur_choice, save_result=True):
    while True:
        try:

            if blur_choice == 0:
                print("\nOpération annulée.")
                return
            elif 1 <= blur_choice <= 4:
                break
            else:
                print("\nChoix invalide. Veuillez entrer une option valide.")
        except ValueError:
            print("\nEntrée invalide. Veuillez entrer un nombre entier.")
    
    log("Filtrage en flou")

    # Conversion image en flou
    if blur_choice == 1:
        blur_img = img.filter(ImageFilter.BoxBlur(2))
    elif blur_choice == 2:
        blur_img = img.filter(ImageFilter.BoxBlur(5))
    elif blur_choice == 3:
        blur_img = img.filter(ImageFilter.BoxBlur(8))
    elif blur_choice == 4:
        blur_img = img.filter(ImageFilter.BoxBlur(10))

    if save_result:
        new_img_path = "/Users/coding/Python_Image2/Images_finales/blur.jpeg"
        new_img_name = "blur.jpg"
        blur_img.save(new_img_path)
        print("\nFiltre Flou appliqué.\n\nEnregistré sous le nom de : " , new_img_name, "\nSon chemin est : ", new_img_path)
    else:
        return blur_img











def dilate_filter(img, save_result=True):
    log("Filtrage par dilation")

    # Convertir l'objet Image en tableau NumPy
    image_array = np.array(img)

    # Appliquer la dilation
    kernel = np.ones((5, 5), np.uint8)
    dilated_image = cv2.dilate(image_array, kernel, iterations=1)

    if save_result:
        new_img_path = "/Users/coding/Python_Image2/Images_finales/dilate.jpeg"
        new_img_name ="dilate.jpg"
        cv2.imwrite(new_img_path, dilated_image)
        print("\nFiltre de Dilatation appliqué.\n\nEnregistré sous le nom de : ",new_img_name, "\nSon chemin est :", new_img_path)
    else:
        return Image.fromarray(dilated_image)










def rotation(img, save_result=True):
    log("Rotation de l'image")

    # Demande à l'utilisateur du choix de l'angle de rotation
    value = int(input("\nEntrez un angle de rotation : "))

    # Insertion de la valeur de l'utilisateur en paramètre de la fonction de rotation "rotate()"
    img_rot = img.rotate(value, expand=True)

    if save_result:
        new_img_path = "/Users/coding/Python_Image2/Images_finales/rotate.jpg"
        new_img_name = "rotate.jpg"
        img_rot.save(new_img_path)
        print("\nFiltre de Rotation appliqué.\n\nEnregistré sous le nom de : ",new_img_name, "\nSon chemin est :", new_img_path)
    else:
        return img_rot
    










def resize_image(img, save_result=True):
    log("Redimension de l'image")

    # Utilisation d'une boucle pour garantir que les dimensions entrées sont valides
    while True:
        try:
            # Demander à l'utilisateur la nouvelle largeur et hauteur
            new_width = int(input("\nEntrer la nouvelle largeur : "))
            new_height = int(input("Entrer la nouvelle hauteur : "))

            # Vérifier si les dimensions sont positives
            if new_width <= 0 or new_height <= 0:
                raise ValueError("Les dimensions doivent être des valeurs positives.")

            # Redimensionner l'image avec les nouvelles dimensions
            resized_img = img.resize((new_width, new_height))

            if save_result:
                # Enregistrer la nouvelle image avec un nouveau chemin
                new_img_path = "/Users/coding/Python_Image2/Images_finales/resized.jpg"
                new_img_name = "resized.jpg"
                resized_img.save(new_img_path)
                print("\nFiltre de Redimension appliqué.\n\nEnregistré sous le nom de : ",new_img_name, "\nSon chemin est :", new_img_path)

            # Sortir de la boucle si les dimensions sont valides
            break

        # Capturer une exception en cas d'erreur de conversion des dimensions en entiers
        except ValueError as e:
            print("Dimensions impossibles. Veuillez recommencer.")

    if not save_result:
        return resized_img













def message(img, save_result=True):
    log("Ajout d'un message sur l'image")

    # Demande à l'utilisateur du champ personnalisé
    user_text = input("\nTapez le texte à afficher sur l'image : ")

    # Convertir l'objet Image en tableau NumPy
    img_array = np.array(img)

    # Calculer la position au centre de l'image pour le texte
    text_size = cv2.getTextSize(user_text, cv2.FONT_HERSHEY_DUPLEX, 3.0, 3)[0]
    text_x = (img_array.shape[1] - text_size[0]) // 2
    text_y = (img_array.shape[0] + text_size[1]) // 2

    # Ajout du texte personnalisé sur l'image
    written = cv2.putText(
        img=img_array,
        text=user_text,
        org=(text_x, text_y),
        fontFace=cv2.FONT_HERSHEY_DUPLEX,
        fontScale=3.0,
        color=(255, 0, 0),
        thickness=3
        )

    if save_result:
        # Enregistrement de l'image avec le texte personnalisé
        new_img_path = "/Users/coding/Python_Image2/Images_finales/message.jpg"
        new_img_name = "message.jpg"
        cv2.imwrite(new_img_path, written)
        print("\nFiltre de Texte appliqué.\n\nEnregistré sous le nom de : ",new_img_name, "\nSon chemin est :", new_img_path)
    else:
        return Image.fromarray(written)
    
    
    
    
    
    
    
def watercolor_filter(img, save_result=True):
    log("Filtre aquarelle appliqué")

    # Convertir l'objet Image en format flottant
    float_img = np.float32(np.array(img))

    # Appliquer un filtre bilatéral pour simuler un effet aquarelle
    watercolor_img = cv2.bilateralFilter(float_img, 9, 75, 75)

    # Convertir le résultat en format 8 bits
    watercolor_img = np.uint8(watercolor_img)

    if save_result:
        # Enregistrer la nouvelle image
        new_img_path = "/Users/coding/Python_Image2/Images_finales/watercolor.jpg"
        new_img_name = "watercolor.jpg"
        cv2.imwrite(new_img_path, watercolor_img)
        print("\nFiltre Aquarelle appliqué.\n\nEnregistré sous le nom de : ",new_img_name, "\nSon chemin est :", new_img_path)
    else:
        return Image.fromarray(watercolor_img)









def all_filters(image):
    # Filtre Noir et Blanc
    gray_choice = input("\nVoulez-vous appliquer le filtre Noir et Blanc (oui / non) : ").lower()
    if gray_choice == 'oui':
        image = gray_filter(image, save_result=False)
        print("Filtre Noir et Blanc appliqué")

    # Filtre Flou
    blur_choice_menu = input("\nVoulez-vous appliquer le filtre Flou (oui / non) : ").lower()
    if blur_choice_menu == 'oui':
        blur_choice = int(input("\nQuelle puissance de floutage voulez-vous ?\n"
                                "1. floutage faible\n"
                                "2. floutage moyen\n"
                                "3. floutage fort\n"
                                "4. floutage très fort\n"
                                "\nEntrez le numéro de votre choix : "))
        image = blur_filter(image, blur_choice, save_result=False)
        print("Filtre Flou appliqué")

    # Filtre Dilatation
    dilate_choice = input("\nVoulez-vous appliquer le filtre Dilatation (oui / non) : ").lower()
    if dilate_choice == 'oui':
        image = dilate_filter(image, save_result=False)
        print("Filtre Dilatation appliqué")

    # Filtre Rotation
    rotation_choice = input("\nVoulez-vous appliquer le filtre Rotation (oui / non) : ").lower()
    if rotation_choice == 'oui':
        image = rotation(image, save_result=False)
        print("Filtre Rotation appliqué")

    # Filtre Redimensionnement
    resize_choice = input("\nVoulez-vous appliquer le filtre Redimensionnement (oui / non) : ").lower()
    if resize_choice == 'oui':
        image = resize_image(image, save_result=False)
        print("Filtre Redimmension appliqué")

    # Filtre Texte
    message_choice = input("\nVoulez-vous appliquer le filtre Texte (oui / non) : ").lower()
    if message_choice == 'oui':
        image = message(image, save_result=False)
        print("Filtre Texte appliqué")

    # Filtre Aquarelle
    watercolor_choice = input("\nVoulez-vous appliquer le filtre Aquarelle (oui / non) : ").lower()
    if watercolor_choice == 'oui':
        image = watercolor_filter(image, save_result=False)
        print("Filtre Aquarelle appliqué")

    # Enregistrer l'image après avoir appliqué tous les filtres
    new_img_path = "/Users/coding/Python_Image2/Images_finales/tous_les_filtre.jpg"
    new_img_name = "tous_les_filtres.jpg"
    image.save(new_img_path)
    print("\nTous les filtres ont été appliqués avec succès.\n\nEnregistré sous le nom de : ", new_img_name,
          "\nSon chemin est :", new_img_path)




# Fonction pour créer un fichier GIF à partir d'une liste d'images
def create_gif(images, output_path):
    # Enregistre un message de journalisation indiquant le début de la création du GIF
    log("Création d'un GIF")

# Vérifie si l'extension du fichier de sortie n'est pas .gif
    if not output_path.lower().endswith('.gif'):
        output_path += '.gif'

    # Sauvegarde le GIF en utilisant la première image comme référence
    images[0].save(
        output_path,          # Chemin complet du fichier de sortie (GIF)
        save_all=True,        # Indique de sauvegarder toutes les images dans la liste
        append_images=images[1:],  # Liste des images à ajouter au GIF après la première
        duration=500,         # Durée d'affichage de chaque image en millisecondes
        loop=0                # Indique que le GIF doit boucler indéfiniment
    )

# Affiche un message indiquant que le GIF a été créé avec succès et enregistré sous le nom spécifié
    print(f"\nGIF créé avec succès. Enregistré sous le nom de {output_path}")
