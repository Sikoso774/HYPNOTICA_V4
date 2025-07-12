# scripts/game_elements/constants.py

import pygame
from scripts.paths import get_resource_path # Renommé de utils_paths

# --- Dimensions de l'écran (Réutilisées des autres modules pour cohérence) ---
LARGEUR_ECRAN_JEU = 800
HAUTEUR_ECRAN_JEU = 600
TITRE_FENETRE_JEU = "HYPNOTICA"

# --- Couleurs ---
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (96, 96, 96)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
JAUNE = (255, 255, 0)
ORANGE = (255, 165, 0)
VIOLET = (127, 0, 255)

# --- Police ---
CHEMIN_POLICE_JEU = get_resource_path("assets/fonts/MINDCONTROL.ttf")
TAILLE_POLICE_JEU = 35

# --- Paramètres du Joueur ---
PLAYER_SIZE = 50 # Taille du carré temporaire du joueur
PLAYER_SPEED = 15 # Vitesse de déplacement du joueur

# --- Paramètres du Téléphone ---
PHONE_SIZE = 30 # Taille du cercle temporaire du téléphone
PHONE_SPEED = 3 # Vitesse de chute du téléphone

# --- Paramètres de Satiété ---
SATIETY_START = 100.0 # Satiété initiale
SATIETY_DECREASE_RATE = 0.05 # Taux de diminution par frame (ajusté pour être plus lent)
SATIETY_INCREASE_AMOUNT = 15 # Quantité de satiété ajoutée lors de la collecte

# --- Paramètres du jeu global ---
FPS = 60 # Images par seconde

# --- Chemins des ressources pour le jeu ---
# Note : Pour les sprites, tu remplaceras ces placeholders par les chemins réels quand tu les auras.
PLAYER_SPRITE_PATH = None # Placeholder, par exemple "assets/images/player_sprite.png"
PHONE_SPRITE_PATH = None  # Placeholder, par exemple "assets/images/phone_sprite.png"
GIF_FOLDER_PATH = get_resource_path("assets/images/hyphose_frames") # Chemin du dossier GIF pour le background

# --- Sons (si tu en as pour le gameplay) ---
# SOUND_COLLECT_PHONE = get_resource_path("assets/sounds/collect_phone.mp3")
# SOUND_GAME_OVER = get_resource_path("assets/sounds/game_over.mp3")