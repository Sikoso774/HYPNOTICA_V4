# scripts/game/game.py

import pygame
import sys  # Pour quitter proprement

# Importe les constantes et les classes des éléments de jeu
from scripts.game_elements.constants import (
    LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU, TITRE_FENETRE_JEU,
    FPS, NOIR
)
from scripts.game_elements.player import Player
from scripts.game_elements.phone import Phone
from scripts.game_elements.satiety import Satiety
from scripts.game_elements.background import Background


class Game:
    _is_pygame_initialized_by_us = False

    def __init__(self):
        # Initialisation de Pygame (si pas déjà fait par main.py)
        if not pygame.get_init():
            pygame.init()
            if not pygame.mixer.get_init():  # Initialise le mixer si nécessaire
                pygame.mixer.init()
            Game._is_pygame_initialized_by_us = True

        self.screen = pygame.display.set_mode((LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU))
        pygame.display.set_caption(TITRE_FENETRE_JEU)

        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(FPS) / 1000
        self.running = False  # État de la boucle de jeu

        # Initialisation des éléments du jeu

        self.phone = Phone()
        self.satiety_bar = Satiety()
        self.background = Background()

        # Groupes de sprites (optionnel mais très utile pour les collisions)
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self.all_sprites)

    def run(self):
        """
        Démarre et gère la boucle de jeu principale.
        Retourne True si le jeu doit être relancé, False sinon.
        """
        self.running = True
        while self.running:
            self._handle_events()
            self._update_game_state()
            self._draw_elements()

            pygame.display.flip()
            self.clock.tick(FPS)

        # Si la boucle se termine (satiété à zéro ou quit), retourne l'état de fin
        if self.satiety_bar.is_empty():
            return "game_over"  # Indique à main.py que c'est un game over

        # Si on a quitté le jeu via la croix
        return "quit"

    def _handle_events(self):
        """
        Gère les événements Pygame (clavier, souris, etc.).
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                # Quitte pygame et le système si ce module l'a initialisé
                if Game._is_pygame_initialized_by_us:
                    pygame.quit()
                sys.exit()  # Quitte l'application

            elif event.type == pygame.KEYDOWN:
                # La gestion continue du mouvement est faite dans _update_game_state avec pygame.key.get_pressed()
                pass

    def _update_game_state(self):
        """
        Met à jour la logique du jeu (mouvement, collisions, satiété).
        """
        # Mouvement du joueur basé sur les touches pressées
        self.all_sprites.update(self.dt)
        self.all_sprites.draw(self.screen)

        # Mise à jour du téléphone
        self.phone.update()

        # Diminution de la satiété
        self.satiety_bar.decrease()

        # Vérification des collisions
        # rect.colliderect est suffisant si nous n'avons qu'un joueur et un téléphone
        if self.player.rect.colliderect(self.phone.rect):
            self.satiety_bar.increase()
            self.phone.reset_position()  # Réinitialise la position du téléphone après la collecte

        # Vérification de la condition de fin de jeu
        if self.satiety_bar.is_empty():
            self.running = False  # Arrête la boucle de jeu

        # Mise à jour de l'arrière-plan animé
        self.background.update()

    def _draw_elements(self):
        """
        Dessine tous les éléments du jeu sur l'écran.
        """
        # Dessine l'arrière-plan en premier
        self.background.draw(self.screen)

        # Dessine le joueur et le téléphone
        self.player.draw(self.screen)
        self.phone.draw(self.screen)

        # Dessine la barre de satiété
        self.satiety_bar.draw(self.screen)

        # Optionnel: Dessiner les rects pour le débogage
        # pygame.draw.rect(self.screen, (255, 0, 0), self.player.rect, 2) # Rouge pour le joueur
        # pygame.draw.rect(self.screen, (0, 0, 255), self.phone.rect, 2)   # Bleu pour le téléphone


# --- Bloc de test pour l'exécution indépendante (optionnel) ---
if __name__ == "__main__":
    game_instance = Game()
    result = game_instance.run()
    if result == "game_over":
        print("Game Over! Satiété à zéro.")
    elif result == "quit":
        print("Jeu quitté par l'utilisateur.")
    pygame.quit()  # S'assure que Pygame est quitté après le test