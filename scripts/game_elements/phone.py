# scripts/game_elements/phone.py

import pygame
import random
from scripts.game_elements.constants import PHONE_SIZE, PHONE_SPEED, LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU
from scripts.game_elements.resources import load_phone_sprite


class Phone(pygame.sprite.Sprite):  # Hérite de pygame.sprite.Sprite
    def __init__(self):
        super().__init__()  # Appel au constructeur de la classe parente (Sprite)
        self.size = PHONE_SIZE
        self.speed = PHONE_SPEED
        self.image = load_phone_sprite(self.size)  # Charge le sprite (ou placeholder)

        self.rect = self.image.get_rect()  # Initialise le rect à partir de l'image
        self.reset_position()  # Initialise la position aléatoirement

    def reset_position(self):
        """
        Réinitialise la position du téléphone en haut de l'écran à une position X aléatoire.
        """
        self.rect.x = random.randint(0, LARGEUR_ECRAN_JEU - self.size)
        self.rect.y = 0  # Commence en haut de l'écran

    def update(self):
        """
        Met à jour la position du téléphone (le fait tomber).
        """
        self.rect.y += self.speed

        # Si le téléphone sort de l'écran, le réinitialise
        if self.rect.top > HAUTEUR_ECRAN_JEU:
            self.reset_position()

    def draw(self, surface):
        """
        Dessine le téléphone sur la surface donnée.
        """
        surface.blit(self.image, self.rect)


# --- Bloc de test pour l'exécution indépendante (optionnel) ---
if __name__ == "__main__":
    pygame.init()
    screen_test = pygame.display.set_mode((LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU))
    pygame.display.set_caption("Test Phone")

    phone_test = Phone()
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        phone_test.update()

        screen_test.fill((0, 0, 0))  # Fond noir
        phone_test.draw(screen_test)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()