# scripts/demarrage_components/demarrage_logic.py

import pygame
import sys
from scripts.demarrage_components.constants import (
    LARGEUR_ECRAN_DEMARRAGE, HAUTEUR_ECRAN_DEMARRAGE, TITRE_FENETRE_DEMARRAGE,
    DUREE_AFFICHAGE_PAR_IMAGE, NOIR, IMAGE_SIZES_FACTORS # IMPORTATION DU NOUVEAU CONSTANT
)
from scripts.demarrage_components.resources import load_demarrage_music
from scripts.demarrage_components.animation_logic import draw_demarrage_frame
from scripts.paths import get_resource_path


class Démarrage:
    _is_pygame_initialized_by_us = False

    def __init__(self):
        if not pygame.get_init():
            pygame.init()
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            Démarrage._is_pygame_initialized_by_us = True

        self.largeur = LARGEUR_ECRAN_DEMARRAGE
        self.hauteur = HAUTEUR_ECRAN_DEMARRAGE
        self.screen = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(TITRE_FENETRE_DEMARRAGE)

        self.music_path = load_demarrage_music()

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play(-1) # Joue en boucle
        except pygame.error as e:
            print(f"Erreur de chargement ou de lecture de la musique de démarrage: {e}")

    def run(self, image_paths):
        """
        Exécute la séquence d'images de démarrage.
        :param image_paths: Liste des chemins d'accès aux images à afficher en séquence.
        """
        loaded_images = []
        for i, path in enumerate(image_paths):
            try:
                original_img = pygame.image.load(path).convert_alpha()

                # Récupère les facteurs de taille pour cette image
                # Utilise une valeur par défaut de (1.0, 1.0) si IMAGE_SIZES_FACTORS n'a pas assez d'entrées
                if i < len(IMAGE_SIZES_FACTORS):
                    factor_width, factor_height = IMAGE_SIZES_FACTORS[i]
                else:
                    factor_width, factor_height = 1.0, 1.0 # Pleine taille par défaut

                # Calcul des nouvelles dimensions basées sur le facteur souhaité
                # et les dimensions de l'écran
                target_width = int(self.largeur * factor_width)
                target_height = int(self.hauteur * factor_height)

                # Redimensionnement proportionnel pour s'adapter DANS le rectangle cible
                img_width, img_height = original_img.get_size()
                scale_factor = min(target_width / img_width, target_height / img_height)

                new_width = int(img_width * scale_factor)
                new_height = int(img_height * scale_factor)

                img = pygame.transform.scale(original_img, (new_width, new_height))
                loaded_images.append(img)
            except pygame.error as e:
                print(f"Erreur de chargement de l'image de démarrage ({path}): {e}")
                loaded_images.append(pygame.Surface((self.largeur, self.hauteur), pygame.SRCALPHA)) # Surface vide

        # ... (rest of the run method, unchanged) ...
        for i, image in enumerate(loaded_images):
            temps_debut_phase = pygame.time.get_ticks()
            running_phase = True
            while running_phase:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.stop()
                        if Démarrage._is_pygame_initialized_by_us:
                            pygame.quit()
                        sys.exit()

                current_time_in_phase = pygame.time.get_ticks() - temps_debut_phase

                if current_time_in_phase < DUREE_AFFICHAGE_PAR_IMAGE:
                    draw_demarrage_frame(self.screen, image, current_time_in_phase, DUREE_AFFICHAGE_PAR_IMAGE)
                else:
                    running_phase = False

                pygame.display.flip()
                pygame.time.delay(10)

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

# --- Bloc de test pour l'exécution indépendante ---
if __name__ == "__main__":
    try:
        # Assure-toi que Pygame est bien initialisé pour le test indépendant
        if not pygame.get_init():
            pygame.init()
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # Exemple d'images à tester
        test_image_paths = [
            get_resource_path("assets/images/Zoléni_Cyberpunk.jpg"),
            get_resource_path("assets/images/PP_Sikoso_77.jpg"),
            get_resource_path("assets/images/pygame_logo.png")
        ]

        demarrage_test = Démarrage()
        print("Démarrage de la séquence d'introduction...")
        demarrage_test.run(test_image_paths)
        print("Séquence de démarrage terminée. Le programme va se fermer.")

    except Exception as e:
        print(f"Une erreur s'est produite lors du test de Démarrage : {e}")