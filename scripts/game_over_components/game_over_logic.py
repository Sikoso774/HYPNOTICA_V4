# scripts/game_over_components/game_over_logic.py

import pygame
import sys
#from scripts.paths import get_resource_path
from scripts.sfx_manager import play_sfx, load_sfx # Pour d'éventuels sons de game over

from scripts.game_over_components.constants import (
    LARGEUR_ECRAN, HAUTEUR_ECRAN, TITRE_FENETRE, NOIR, CHEMIN_MUSIQUE_GO, CHEMIN_IMAGE_ARRIERE_PLAN_GO
)
from scripts.game_over_components.text_scroller import TextScroller # Importe le gestionnaire de texte

class GameOverScreen:
    _is_pygame_initialized_by_us = False # Pour savoir si Pygame a été initialisé ici

    def __init__(self):
        # Initialisation de Pygame (si pas déjà fait par main.py ou EcranTitre)
        if not pygame.get_init():
            pygame.init()
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            GameOverScreen._is_pygame_initialized_by_us = True

        self.largeur = LARGEUR_ECRAN
        self.hauteur = HAUTEUR_ECRAN
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(TITRE_FENETRE)

        # Charger l'arrière-plan
        try:
            self.arriere_plan_game_over = pygame.image.load(CHEMIN_IMAGE_ARRIERE_PLAN_GO).convert()
            self.arriere_plan_game_over = pygame.transform.scale(self.arriere_plan_game_over, (self.largeur, self.hauteur))
        except pygame.error as e:
            print(f"Erreur de chargement de l'arrière-plan Game Over: {e}")
            self.arriere_plan_game_over = pygame.Surface((self.largeur, self.hauteur))
            self.arriere_plan_game_over.fill(NOIR) # Fond noir si l'image ne charge pas

        # Gestion de la musique
        # Arrête la musique précédente si elle existe
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load(CHEMIN_MUSIQUE_GO)
            pygame.mixer.music.play(-1) # Joue en boucle
        except pygame.error as e:
            print(f"Erreur de chargement ou de lecture de la musique Game Over: {e}")

        # Initialisation du scroller de texte
        self.text_scroller = TextScroller(self.largeur, self.hauteur)

        # Tu peux charger un son spécifique pour le Game Over ici si tu veux
        # load_sfx("assets/sounds/game_over_jingle.wav") # Exemple

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    if GameOverScreen._is_pygame_initialized_by_us:
                        pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        #if pygame.mixer.music.get_busy():
                            #pygame.mixer.music.stop() # Arrête la musique de game over avant de relancer
                        # play_sfx("assets/sounds/menu_select.wav") # Exemple de son de sélection
                        return "relancer"
                    elif event.key == pygame.K_q:
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.stop()
                        if GameOverScreen._is_pygame_initialized_by_us:
                            pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_a:
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.stop() # Arrête la musique de game over avant d'aller aux crédits
                        # play_sfx("assets/sounds/menu_select.wav") # Exemple de son de sélection
                        return "crédits" # Retourne "credits" pour indiquer au main.py d'aller aux crédits

            self.ecran.blit(self.arriere_plan_game_over, (0, 0))
            self.text_scroller.draw_and_scroll_text(self.ecran) # Appelle la nouvelle méthode

            pygame.display.flip()
            pygame.time.delay(30)

        return None # Ne devrait pas être atteint

    @property
    def is_pygame_initialized_by_us(self):
        return self._is_pygame_initialized_by_us


if __name__ == "__main__":
    # Ceci est un bloc de test pour l'écran Game Over seul
    go_screen = GameOverScreen()
    action = go_screen.run()
    print(f"Action choisie : {action}")
    if GameOverScreen.is_pygame_initialized_by_us and pygame.get_init():
        pygame.quit()
    sys.exit()