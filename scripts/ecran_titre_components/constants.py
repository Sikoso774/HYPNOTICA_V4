# scripts/ecran_titre_components/constants.py

import pygame
from scripts.paths import get_resource_path # Important pour les chemins de ressources

# --- COULEURS ---
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (96, 96, 96)
ROUGE = (145, 3, 3)
VERT = (13, 69, 28)
BLEU = (0, 0, 255)
VIOLET = (127, 0, 255)
ORANGE  = (212, 92, 6)

# --- DIMENSIONS DE L'ÉCRAN ---
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600
TITRE_FENETRE = "HYPNOTICA"

# --- CHEMINS ET RESSOURCES ---
# Utilise toujours get_resource_path pour que PyInstaller fonctionne
CHEMIN_POLICE = get_resource_path("assets/fonts/MINDCONTROL.ttf")
TAILLE_POLICE = 25 # Police principale de l'écran titre
CHEMIN_MUSIQUE = get_resource_path("assets/musics/Max Brhon - AI [NCS Release].mp3")
CHEMIN_IMAGES_GIF = get_resource_path("assets/images/hyphose_frames")
VITESSE_ANIMATION_GIF = 60 # Vitesse d'animation du GIF en FPS (images par seconde)