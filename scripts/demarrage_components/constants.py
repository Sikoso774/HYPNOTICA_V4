# scripts/demarrage_components/constants.py

import pygame
from scripts.paths import get_resource_path

# Couleurs (réutilisées des autres modules pour cohérence)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Dimensions de l'écran
LARGEUR_ECRAN_DEMARRAGE = 800
HAUTEUR_ECRAN_DEMARRAGE = 600
TITRE_FENETRE_DEMARRAGE = "HYPNOTICA_V4"

# Chemins des ressources
CHEMIN_POLICE_DEMARRAGE = get_resource_path("assets/fonts/MINDCONTROL.ttf")
CHEMIN_MUSIQUE_DEMARRAGE = get_resource_path("assets/musics/Max Brhon - AI [NCS Release].mp3")

# Durées des phases d'affichage (en millisecondes)
# Exemple: image_1 s'affiche pendant 3000ms, puis image_2 pendant 3000ms, etc.
DUREE_AFFICHAGE_PAR_IMAGE = 3000 # Durée pour une image + texte principal
DUREE_TRANSITION_ALPHA_MS = 1000 # Durée de la phase d'apparition/disparition
ALPHA_VITESSE = 255 / DUREE_TRANSITION_ALPHA_MS # Vitesse d'augmentation de l'alpha (pour 1000ms)

# Textes à afficher avec les images (tu peux les modifier ici)
TEXTE_LOGO_JEU = "HYPNOTICA"
TEXTE_DEVELOPPEUR = "Sikoso774"
# Ajoute d'autres textes si tu as plus de phases (ex: "Projet ENSEA")

# Facteurs de taille pour chaque image dans la séquence (largeur et hauteur max en proportion de l'écran)
# Si tu as 3 images, tu devras avoir 3 tuples (facteur_largeur, facteur_hauteur)
# (1.0, 1.0) signifie pleine taille (remplir l'écran en conservant les proportions)
# (0.7, 0.7) signifie 70% de la taille de l'écran
# Tu peux ajuster ces valeurs pour chaque image.
# Exemple si tu veux une image plus petite, sauf la première (logo Pygame) qui serait pleine taille :
IMAGE_SIZES_FACTORS = [
    (0.5, 0.5),  # Pour Zoléni_Cyberpunk.jpg (si tu veux qu'il soit un peu plus petit que l'écran)
    (0.5, 0.5),  # Pour PP_Sikoso_77.jpg (plus petit)
    (0.8, 0.8)   # Pour pygame_logo.png (un peu plus grand que le précédent)
]
# Assure-toi que la longueur de cette liste correspond au nombre d'images dans ton appel à Démarrage().run()