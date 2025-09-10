# scripts/game_over_components/constants.py

import pygame
from scripts.paths import get_resource_path

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (96, 96, 96)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

# Dimensions de l'écran (doivent être cohérentes avec les autres écrans)
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600
TITRE_FENETRE = "HYPNOTICA_V3" # Ou autre titre si spécifique à cet écran

# Chemins des ressources
CHEMIN_POLICE_GO = get_resource_path("assets/fonts/MINDCONTROL.ttf")
CHEMIN_IMAGE_ARRIERE_PLAN_GO = get_resource_path("assets/images/Game-Over-Wallpaper-48909.jpg")
CHEMIN_MUSIQUE_GO = get_resource_path("assets/musics/More Plastic - Rewind [NCS Release].mp3")

# Propriétés du texte Game Over
TAILLE_POLICE_GO = 24
VITESSE_DEFILEMENT_GO = 0.95 # Ajuster selon le besoin

# Liste du texte à afficher (peut être déplacé si le texte est dynamique)
LISTE_TEXTE_GO = [
    "GAME OVER",
    "",
    "Press R to Replay",
    "",
    "Press A for Credits",
    "",
    "Press Q to Quit",
]