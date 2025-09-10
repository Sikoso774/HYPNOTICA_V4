# scripts/game_elements/satiety.py

import pygame
from scripts.game_elements.constants import (
    SATIETY_START, SATIETY_DECREASE_RATE, SATIETY_INCREASE_AMOUNT,
    ROUGE, VERT, BLANC, NOIR, LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU
)
from scripts.game_elements.resources import get_game_font

class Satiety:
    def __init__(self):
        self.value = SATIETY_START
        self.decrease_rate = SATIETY_DECREASE_RATE
        self.increase_amount = SATIETY_INCREASE_AMOUNT
        self.font = get_game_font(20) # Police pour afficher la valeur de satiété

    def decrease(self):
        """Diminue la valeur de satiété."""
        self.value -= self.decrease_rate
        if self.value < 0:
            self.value = 0 # La satiété ne descend pas en dessous de zéro

    def increase(self):
        """Augmente la valeur de satiété, plafonnée à 100."""
        self.value += self.increase_amount
        if self.value > 100:
            self.value = 100

    def is_empty(self):
        """Vérifie si la satiété est tombée à zéro."""
        return self.value <= 0

    def draw(self, surface):
        """
        Dessine la barre de satiété et sa valeur.
        """
        # Dimensions et position de la barre de satiété
        bar_x, bar_y = 10, 10
        bar_width = 200
        bar_height = 20

        # Fond de la barre (toujours rouge pour indiquer la "perte" ou le maximum)
        pygame.draw.rect(surface, ROUGE, (bar_x, bar_y, bar_width, bar_height))

        # Calcul de la largeur de la partie verte de la barre
        current_width = int(bar_width * (self.value / 100))
        pygame.draw.rect(surface, VERT, (bar_x, bar_y, current_width, bar_height))

        # Contour de la barre
        pygame.draw.rect(surface, BLANC, (bar_x, bar_y, bar_width, bar_height), 2) # épaisseur 2

        # Afficher la valeur numérique de la satiété
        satiety_text = f"Satiété: {int(self.value)}%"
        text_surface = self.font.render(satiety_text, True, BLANC)
        text_rect = text_surface.get_rect(topleft=(bar_x + bar_width + 10, bar_y))
        surface.blit(text_surface, text_rect)

# --- Bloc de test pour l'exécution indépendante (optionnel) ---
if __name__ == "__main__":
    pygame.init()
    screen_test = pygame.display.set_mode((LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU))
    pygame.display.set_caption("Test Satiety")

    satiety_bar = Satiety()
    running = True
    clock = pygame.time.Clock()

    print("Appuyez sur ESPACE pour augmenter la satiété. La satiété diminue automatiquement.")
    print("La barre doit devenir rouge si la satiété est trop faible.")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    satiety_bar.increase()
                    print(f"Satiété augmentée ! Nouvelle valeur: {int(satiety_bar.value)}%")

        satiety_bar.decrease()
        if satiety_bar.is_empty():
            print("Satiété tombée à zéro ! Game Over simulé.")
            running = False # Arrête le test

        screen_test.fill(NOIR) # Fond noir
        satiety_bar.draw(screen_test)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()