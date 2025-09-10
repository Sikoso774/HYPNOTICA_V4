# scripts/schargement.py

import pygame
import sys # Pour sys.exit() si nécessaire
from scripts.chargement_components.constants import LARGEUR_ECRAN_CHARGEMENT, HAUTEUR_ECRAN_CHARGEMENT, TITRE_FENETRE_CHARGEMENT
from scripts.chargement_components.resources import load_chargement_resources
from scripts.chargement_components.animation_logic import run_spiral_transition

class Chargement:
    # Variables de classe pour stocker les images une fois chargées
    # Cela évite de les recharger si plusieurs instances de Chargement sont créées
    _gif_images_cache = []
    _image_fin_cache = None
    _is_pygame_initialized_by_us = False # Pour savoir si Pygame a été initialisé par cette classe

    def __init__(self):
        # Initialisation de Pygame (si pas déjà fait par main.py ou un autre écran)
        if not pygame.get_init():
            pygame.init()
            if not pygame.mixer.get_init(): # Initialise le mixer si ce n'est pas fait
                pygame.mixer.init()
            Chargement._is_pygame_initialized_by_us = True

        self.largeur = LARGEUR_ECRAN_CHARGEMENT
        self.hauteur = HAUTEUR_ECRAN_CHARGEMENT
        # L'écran doit être passé ou créé de manière cohérente dans le main.py.
        # Ici, on suppose que `main.py` a déjà configuré la fenêtre.
        # Pour les tests unitaires de ce module, il peut être nécessaire de le définir.
        self.screen = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(TITRE_FENETRE_CHARGEMENT)

        # Chargement des ressources une seule fois pour la classe (met en cache)
        if not Chargement._gif_images_cache or not Chargement._image_fin_cache:
            Chargement._gif_images_cache, Chargement._image_fin_cache = load_chargement_resources()

        self.gif_images = Chargement._gif_images_cache
        self.image_fin = Chargement._image_fin_cache

    def loading(self):
        """
        Exécute la transition de l'écran de chargement.
        """
        # La logique de la spirale est maintenant dans une fonction séparée
        run_spiral_transition(self.screen, self.image_fin, self.gif_images)

        # Après la transition, le contrôle est censé revenir au main.py.
        # Ne pas appeler pygame.quit() ou sys.exit() ici, sauf si c'est pour un test unitaire
        # et que tu veux que le programme se termine après ce seul écran.

# --- Bloc de test pour l'exécution indépendante (inchangé) ---
if __name__ == "__main__":
    try:
        # S'assurer que Pygame est bien initialisé pour le test indépendant
        if not pygame.get_init():
            pygame.init()
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        chargement_test = Chargement() # Initialise Pygame et charge les ressources
        print("Chargement des ressources terminé.")
        chargement_test.loading() # Appelle la fonction de transition
        print("Transition terminée. Le programme va se fermer.")

    except Exception as e:
        print(f"Une erreur s'est produite lors du test de chargement: {e}")
    finally:
        # S'assure que Pygame est quitté en cas d'erreur ou de fin de test
        if pygame.get_init():
            pygame.quit()
        sys.exit()