# scripts/credits_components/constants.py

import pygame
from scripts.paths import get_resource_path

# Couleurs (réutilisées des autres modules pour cohérence)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (96, 96, 96)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
VIOLET = (127, 0, 255)

# Dimensions de l'écran
LARGEUR_ECRAN_CREDITS = 800
HAUTEUR_ECRAN_CREDITS = 600
TITRE_FENETRE_CREDITS = "HYPNOTICA"

# Chemins des ressources
CHEMIN_POLICE_CREDITS_DEFAULT = get_resource_path("assets/fonts/MINDCONTROL.ttf")
CHEMIN_IMAGE_CREDITS = get_resource_path("assets/images/Zoléni_Cyberpunk.jpg")
CHEMIN_MUSIQUE_CREDITS = get_resource_path("assets/musics/waera - harinezumi [NCS Release].mp3")

# Propriétés de défilement
VITESSE_DEFILEMENT_CREDITS = 2 # Ajuster selon le besoin (plus petit pour plus lent)

# Structure des crédits : Chaque entrée est un dictionnaire pour flexibilité
# 'type': 'text' ou 'image'
# 'value': le texte de la ligne ou l'image_key (pour référence si l'image est chargée séparément)
# 'font_size': taille de la police (uniquement pour 'text')
# 'color': couleur du texte (uniquement pour 'text')
# 'spacer_height': hauteur d'espacement (pour 'spacer' ou après une ligne)
# 'image_scale_factor': facteur d'échelle pour l'image (si 'image')

CREDITS_CONTENT = [
    {'type': 'text', 'value': "Credits", 'font_size': 60, 'color': VERT},
    {'type': 'spacer', 'height': 80}, # Espacement
    {'type': 'text', 'value': "Developer : Sikoso 774", 'font_size': 32, 'color': BLANC},
    {'type': 'spacer', 'height': 150},
    {'type': 'image', 'value': "developer_image", 'image_path': CHEMIN_IMAGE_CREDITS, 'image_scale_factor': 0.5}, # chemin direct pour l'image
    {'type': 'spacer', 'height': 50},
    {'type': 'text', 'value': "Musics :", 'font_size': 30, 'color': BLANC},
    {'type': 'text', 'value': "waera - harinezumi [NCS Release]", 'font_size': 24, 'color': GRIS},
    {'type': 'text', 'value': "Licensed under Creative Commons", 'font_size': 20, 'color': GRIS},
    {'type': 'spacer', 'height': 30},
    {'type': 'text', 'value': "Max Brhon - AI [NCS Release]", 'font_size': 24, 'color': GRIS},
    {'type': 'text', 'value': "Licensed under Creative Commons", 'font_size': 20, 'color': GRIS},
    {'type': 'spacer', 'height': 30},

    {'type': 'text', 'value': "Game Concept : HYPNOTICA", 'font_size': 28, 'color': VIOLET},
    {'type': 'spacer', 'height': 50},
    {'type': 'text', 'value': "Special Thanks :", 'font_size': 30, 'color': BLANC},
    {'type': 'text', 'value': "- My family and friends", 'font_size': 24, 'color': BLANC},
    {'type': 'text', 'value': "- Pygame Community", 'font_size': 24, 'color': BLANC},
    {'type': 'text', 'value': "- Google Gemini (for refactoring tips!)", 'font_size': 24, 'color': BLANC},
    {'type': 'spacer', 'height': 80},
    {'type': 'text', 'value': "Thank You For Playing!", 'font_size': 40, 'color': VERT},
    {'type': 'spacer', 'height': 150}, # Grand espacement pour la fin
    {'type': 'text', 'value': "Press Q to Quit", 'font_size': 24, 'color': ROUGE},
    {'type': 'text', 'value': "Press M to Main Menu", 'font_size': 24, 'color': BLEU},
]