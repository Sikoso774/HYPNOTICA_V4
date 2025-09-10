# scripts/chargement_components/constants.py

import pygame
from scripts.paths import get_resource_path

# Dimensions de l'écran (doivent être cohérentes avec les autres écrans si c'est la même fenêtre)
LARGEUR_ECRAN_CHARGEMENT = 800
HAUTEUR_ECRAN_CHARGEMENT = 600
TITRE_FENETRE_CHARGEMENT = "HYPNOTICA_V3" # Titre spécifique à l'écran de chargement

# Chemins des ressources (utilisés par resources.py)
CHEMIN_GIF_CHARGEMENT = get_resource_path("assets/images/hyphose_frames") # Dossier contenant les images GIF
CHEMIN_IMAGE_FIN_CHARGEMENT = get_resource_path("assets/images/pygame_logo.png") # Image à faire spirale

# Durée de la transition en millisecondes
DUREE_TRANSITION_CHARGEMENT = 2000 # 2 secondes