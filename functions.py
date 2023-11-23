from PIL import Image, ImageFilter 
from art import tprint
import cv2
import numpy as np

def print_menu(img_path):
    tprint("Menu")
    print("1. Gray")
    print("2. Blur")
    print("3. Dilate")
    print("4. Leave\n")

    
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
    

    
