# Utilisation du Code Python pour Manipuler les Images

Ce script Python propose plusieurs filtres et manipulations d'images, permettant de les modifier selon différents critères.

## Prérequis

Avant d'exécuter ce code, assurez-vous d'avoir les bibliothèques Python suivantes installées :
- Pillow (`pip install Pillow`)
- OpenCV (`pip install opencv-python`)
- art (`pip install art`)

### Instructions

1. **Exécution du Code :**

   Pour lancer le programme, exécutez le fichier `main.py`.

2. **Menu Principal :**

   Au démarrage, le programme affiche un menu avec différentes options :

   - `Gray`: Convertit l'image en noir et blanc.
   - `Blur`: Applique un effet de flou à l'image.
   - `Dilate`: Effectue une dilatation sur l'image.
   - `Rotate`: Permet de faire pivoter l'image.
   - `Resize`: Redimensionne l'image.
   - `Text`: Ajoute du texte personnalisé sur l'image.
   - `Leave`: Quitte le programme.

3. **Options du Menu :**

   - `Gray`: Convertit l'image en noir et blanc.
   - `Blur`: Propose différentes intensités de floutage.
   - `Dilate`: Applique une dilatation à l'image.
   - `Rotate`: Demande à l'utilisateur un angle de rotation pour l'image. Il suffit de mettre des Chiffres et de faire entrer
   - `Resize`: Redimensionne l'image selon les dimensions saisies par l'utilisateur. Il suffit de mettre des Chiffres.
   **`ATTENTION`** 
   si une valeurs négatif est rentré le code ne fonctionnera pas. `il faut que les valeurs soit positif.`
   - `Text`: Permet d'ajouter du texte personnalisé sur l'image.

4. **Enregistrement des Images :**

   Chaque opération effectuée sur l'image produit une nouvelle version de l'image traitée, enregistrée sous un nom spécifique (par exemple : `gray.jpeg`, `blur.jpeg`, etc.).

5. **Notes Additionnelles :**

   - Assurez-vous que les images d'origine sont dans le même répertoire que le script ou spécifiez le chemin correct vers ces images dans le code.
   - L'ajout de texte personnalisé nécessite une interaction utilisateur pour saisir le texte à insérer.

`N'oubliez pas d'avoir une copie de sauvegarde des images d'origine avant de les modifier avec ce programme. `