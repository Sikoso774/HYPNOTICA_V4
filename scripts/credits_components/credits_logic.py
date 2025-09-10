# scripts/credits_components/credits_logic.py

import pygame
import sys
from scripts.credits_components.constants import (
    LARGEUR_ECRAN_CREDITS, HAUTEUR_ECRAN_CREDITS, TITRE_FENETRE_CREDITS, NOIR
)
from scripts.credits_components.resources import load_credits_resources
from scripts.credits_components.text_scroller import CreditsTextScroller

class CreditsScreen:
    _is_pygame_initialized_by_us = False

    def __init__(self):
        # Initialisation de Pygame (si pas déjà fait)
        if not pygame.get_init():
            pygame.init()
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            CreditsScreen._is_pygame_initialized_by_us = True

        self.largeur = LARGEUR_ECRAN_CREDITS
        self.hauteur = HAUTEUR_ECRAN_CREDITS
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(TITRE_FENETRE_CREDITS)

        self.noir = NOIR

        # Charger les ressources (images et musique)
        self.loaded_images, self.music_path = load_credits_resources()

        # Initialisation du scroller de texte et passage des images chargées
        self.credits_scroller = CreditsTextScroller()
        self.credits_scroller.set_loaded_images(self.loaded_images)

        # Gestion de la musique
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play(-1) # Joue en boucle
        except pygame.error as e:
            print(f"Erreur de chargement ou de lecture de la musique des crédits: {e}")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    if CreditsScreen._is_pygame_initialized_by_us:
                        pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: # Quitter
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.stop()
                        if CreditsScreen._is_pygame_initialized_by_us:
                            pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_m: # Retour au menu principal
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.stop()
                        return "menu" # Indique à main.py de retourner au menu

            self.ecran.fill(self.noir)
            self.credits_scroller.draw_and_scroll_credits(self.ecran) # Appelle le scroller

            pygame.display.flip()
            pygame.time.delay(30) # Vitesse de rafraîchissement

        return None # Ne devrait pas être atteint si une action de sortie est prise

if __name__ == "__main__":
    # Bloc de test pour l'écran Crédits seul
    try:
        credits_test_screen = CreditsScreen()
        action = credits_test_screen.run()
        print(f"Action choisie : {action}")
    except Exception as e:
        print(f"Erreur lors du test de CreditsScreen : {e}")
    finally:
        if pygame.get_init():
            pygame.quit()
        sys.exit()