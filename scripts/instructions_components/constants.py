# scripts/instructions_components/constants.py

import pygame
from scripts.paths import get_resource_path

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Dimensions de l'écran (réutilisées des autres modules pour cohérence)
LARGEUR_ECRAN_INSTRUCTIONS = 800
HAUTEUR_ECRAN_INSTRUCTIONS = 600
TITRE_FENETRE_INSTRUCTIONS = "HYPNOTICA - Instructions"

# Chemin de la police
CHEMIN_POLICE_INSTRUCTIONS = get_resource_path("assets/fonts/MINDCONTROL.ttf")

# Durée de pause entre chaque caractère "tapé" (en millisecondes)
# Ajuste cette valeur pour contrôler la vitesse de frappe.
DELAI_FRAPPE_MS = 30 # Par exemple, 30 ms par caractère

# Instructions du jeu
INSTRUCTIONS_TEXT_CONTENT = [
    "Welcome to HYPNOTICA",
    "",
    "Objective : Keep the player satiated by",
    "collecting phones.",
    "Use the LEFT and RIGHT arrows to move the player",
    "If satiety drops to zero, it's Game Over!",
    "",
    "Press SPACE to return to the main menu."
]

# Tailles de police spécifiques pour certaines lignes
# Clé: début de la ligne, Valeur: taille de police
FONT_SIZES_MAP = {
    "Welcome to HYPNOTICA": 32,
    "Objective :": 24, # Applique à "Objective : Keep the player satiated by"
    "Use the LEFT and RIGHT arrows to move the player": 20, # Explicit pour les flèches
    "If satiety drops to zero, it's Game Over!": 20, # Explicite pour le game over
    "Press SPACE to return to the main menu.": 20 # Explicite pour retour menu
}
# La taille par défaut sera 20 si non spécifiée
DEFAULT_FONT_SIZE = 20