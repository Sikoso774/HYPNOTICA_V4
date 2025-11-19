# Fichier: game/core/game_over.py

import pygame
import sys
from ..config.settings import *
from ..config.support import get_resource_path
from ..components.elements.textscroller import TextScroller

class GameOver:
    def __init__(self):
        # Récupération de l'écran existant
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        
        # --- Chargement des ressources ---
        
        # 1. Arrière-plan
        bg_path = get_resource_path(join("assets", "images", "Game-Over-Wallpaper-48909.jpg"))
        try:
            self.background = pygame.image.load(bg_path).convert()
            self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        except pygame.error as e:
            print(f"Erreur chargement BG Game Over: {e}")
            self.background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            self.background.fill(COLORS['black'])

        # 2. Musique
        self.music_path = get_resource_path(join("assets", "audio", "More Plastic - Rewind [NCS Release].mp3"))

        # 3. Scroller
        self.scroller = TextScroller()

    def run(self):
        """
        Lance la boucle de l'écran Game Over.
        Retourne une string indiquant l'action choisie : 'restart', 'quit', 'credits'.
        """
        # Lancement de la musique
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            try:
                pygame.mixer.music.load(self.music_path)
                pygame.mixer.music.play(-1)
            except pygame.error as e:
                print(f"Erreur musique Game Over: {e}")

        running = True
        while running:
            # 1. Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pygame.mixer.music.stop()
                        return "restart" # Indique au main.py de relancer
                    
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                        
                    elif event.key == pygame.K_a:
                        pygame.mixer.music.stop()
                        return "credits" # Indique au main.py d'aller aux crédits

            # 2. Dessin
            # Afficher l'image de fond
            self.screen.blit(self.background, (0, 0))
            
            # Afficher le texte défilant
            self.scroller.draw_and_scroll(self.screen)

            # 3. Mise à jour écran
            pygame.display.flip()
            self.clock.tick(FPS)

# Bloc de test indépendant
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    game_over = GameOver()
    action = game_over.run()
    print(f"Action choisie : {action}")
    pygame.quit()