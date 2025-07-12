# scripts/game_elements/player.py

import pygame
from scripts.game_elements.constants import PLAYER_SIZE, PLAYER_SPEED, LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU
from scripts.game_elements.resources import load_player_sprite


class Player(pygame.sprite.Sprite):  # Hérite de pygame.sprite.Sprite
    def __init__(self, group):
        super().__init__(group)  # Appel au constructeur de la classe parente (Sprite)
        self.size = PLAYER_SIZE
        self.speed = PLAYER_SPEED
        self.image = load_player_sprite(self.size)  # Charge le sprite (ou placeholder)
        self.direction = pygame.math.Vector2()

        # Position initiale (centrée horizontalement, un peu au-dessus du bas)
        self.rect = self.image.get_rect(
            centerx=LARGEUR_ECRAN_JEU // 2,
            bottom=HAUTEUR_ECRAN_JEU - 20
        )

    def update(self, dt):

        keys = pygame.key.get_pressed()  # <---- pour vérifier si une touche est pressée
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])  # <---- bcp plus simple
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

    def draw(self, surface):
        """
        Dessine le joueur sur la surface donnée.
        """
        surface.blit(self.image, self.rect)



# --- Bloc de test pour l'exécution indépendante (optionnel) ---
if __name__ == "__main__":
    # general setup
    pygame.init()
    screen_test = pygame.display.set_mode((LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU))
    pygame.display.set_caption("Test Player")
    running = True
    clock = pygame.time.Clock()

    # elements
    all_sprites = pygame.sprite.Group()
    player = Player(all_sprites)

    # main loop
    while running:
        dt = clock.tick(60) / 1000
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update
        all_sprites.update(dt)

        # draw the game
        screen_test.fill('#093815')
        all_sprites.draw(screen_test)

        pygame.display.update()


    pygame.quit()