# scripts/game_elements/background.py

import pygame
from scripts.game_elements.constants import LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU, FPS
from scripts.game_elements.resources import load_gif_frames

class Background:
    def __init__(self):
        self.frames = load_gif_frames() # Charge toutes les images GIF au démarrage
        self.num_frames = len(self.frames)
        self.current_frame_index = 0
        self.last_frame_time = pygame.time.get_ticks()
        self.frame_duration = 1000 / FPS # Durée de chaque frame en ms (pour une animation fluide)

    def update(self):
        """
        Met à jour l'index de l'image GIF pour l'animation.
        """
        if self.num_frames == 0: # Si aucune image n'a été chargée
            return

        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time > self.frame_duration:
            self.current_frame_index = (self.current_frame_index + 1) % self.num_frames
            self.last_frame_time = current_time

    def draw(self, surface):
        """
        Dessine la frame actuelle de l'arrière-plan sur la surface.
        """
        if self.num_frames > 0:
            surface.blit(self.frames[self.current_frame_index], (0, 0))
        else:
            # Fallback si pas d'images GIF chargées
            surface.fill((0, 0, 50)) # Fond bleu très foncé

# --- Bloc de test pour l'exécution indépendante (optionnel) ---
if __name__ == "__main__":
    pygame.init()
    screen_test = pygame.display.set_mode((LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU))
    pygame.display.set_caption("Test Background GIF")

    background_test = Background()
    running = True
    clock = pygame.time.Clock()

    print("Vérifiez l'animation GIF en arrière-plan. Si rien n'apparaît, vérifiez le dossier 'hyphose_frames'.")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        background_test.update() # Met à jour la frame de l'animation
        background_test.draw(screen_test) # Dessine la frame
        pygame.display.flip()
        clock.tick(FPS) # Utilise le FPS défini dans constants pour la vitesse de l'animation

    pygame.quit()