from PIL import Image, ImageFilter 
from art import tprint

def print_menu(img_path):
    tprint("Menu")
    print("1. Gray")
    print("2. Leave\n")

    
def gray_filter(img_path) :
    # Importer l'image à convertir
    image = Image.open(img_path)

    # Conversion image en noir et blanc (gray)
    gray_img = image.convert("L")

    # Enregistrement de l'image 
    new_img_path = "gray.jpeg"
    gray_img.save(new_img_path)
    
    
    