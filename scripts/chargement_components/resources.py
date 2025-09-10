# scripts/chargement_components/resources.py

import pygame
import os
#from scripts.paths import get_resource_path
from scripts.chargement_components.constants import LARGEUR_ECRAN_CHARGEMENT, HAUTEUR_ECRAN_CHARGEMENT, CHEMIN_GIF_CHARGEMENT, CHEMIN_IMAGE_FIN_CHARGEMENT

def load_chargement_resources():
    """
    Charge les images GIF et l'image de fin pour l'écran de chargement.
    Retourne un tuple (gif_images, image_fin).
    """
    gif_images = []
    image_fin = None

    try:
        # Chargement des images GIF
        image_folder = CHEMIN_GIF_CHARGEMENT
        if not os.path.isdir(image_folder):
            print(f"Avertissement : Le dossier GIF n'existe pas : {image_folder}. L'animation GIF sera vide.")
            # Créer une surface vide pour éviter les erreurs de blit
            gif_images.append(pygame.Surface((LARGEUR_ECRAN_CHARGEMENT, HAUTEUR_ECRAN_CHARGEMENT), pygame.SRCALPHA))
        else:
            files_in_folder = [f for f in os.listdir(image_folder) if f.lower().endswith(".png")]
            if not files_in_folder:
                print(f"Avertissement : Aucun fichier PNG trouvé dans : {image_folder}. L'animation GIF sera vide.")
                gif_images.append(pygame.Surface((LARGEUR_ECRAN_CHARGEMENT, HAUTEUR_ECRAN_CHARGEMENT), pygame.SRCALPHA))
            else:
                for filename in sorted(files_in_folder):
                    image_path = os.path.join(image_folder, filename)
                    image = pygame.image.load(image_path).convert_alpha()
                    image = pygame.transform.scale(image, (LARGEUR_ECRAN_CHARGEMENT, HAUTEUR_ECRAN_CHARGEMENT))
                    gif_images.append(image)

        # Chargement de l'image de fin (pygame_logo.png)
        image_fin = pygame.image.load(CHEMIN_IMAGE_FIN_CHARGEMENT).convert_alpha()

    except (FileNotFoundError, ValueError) as e:
        print(f"Erreur de chargement des ressources de chargement : {e}")
        # En cas d'erreur, fournir des surfaces par défaut pour éviter les crashs
        gif_images = [pygame.Surface((LARGEUR_ECRAN_CHARGEMENT, HAUTEUR_ECRAN_CHARGEMENT), pygame.SRCALPHA)]
        image_fin = pygame.Surface((1, 1), pygame.SRCALPHA) # Petite surface vide
    except pygame.error as e:
        print(f"Erreur Pygame lors du chargement des ressources de chargement : {e}")
        gif_images = [pygame.Surface((LARGEUR_ECRAN_CHARGEMENT, HAUTEUR_ECRAN_CHARGEMENT), pygame.SRCALPHA)]
        image_fin = pygame.Surface((1, 1), pygame.SRCALPHA)

    return gif_images, image_fin