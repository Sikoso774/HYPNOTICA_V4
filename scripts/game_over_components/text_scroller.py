# scripts/game_over_components/text_scroller.py

import pygame
from scripts.game_over_components.constants import BLANC, VERT, TAILLE_POLICE_GO, VITESSE_DEFILEMENT_GO, CHEMIN_POLICE_GO, LISTE_TEXTE_GO
#from scripts.paths import get_resource_path

class TextScroller:
    def __init__(self, screen_width, screen_height):
        self.largeur = screen_width
        self.hauteur = screen_height
        self.police_go = pygame.font.Font(CHEMIN_POLICE_GO, TAILLE_POLICE_GO)
        self.list_GO = LISTE_TEXTE_GO # Utilise la liste des constantes
        self.go_x = self.largeur # Commence hors de l'écran à droite
        self.go_vitesse = VITESSE_DEFILEMENT_GO

    def draw_and_scroll_text(self, surface):
        for i, go_text in enumerate(self.list_GO):
            texte_go = self.police_go.render(go_text, True, VERT) # Utilise la couleur VERTE des constantes
            texte_go_rect = texte_go.get_rect(y=self.hauteur // 9.5 + i * 30)
            texte_go_rect.x = self.go_x
            surface.blit(texte_go, texte_go_rect)

        self.go_x -= self.go_vitesse
        # Réinitialise la position si le texte est sorti de l'écran
        # On calcule la largeur du texte le plus long pour bien gérer le retour
        max_text_width = 0
        for text_line in self.list_GO:
            current_width = self.police_go.render(text_line, True, VERT).get_rect().width
            if current_width > max_text_width:
                max_text_width = current_width

        if self.go_x < -max_text_width: # Si le texte est complètement sorti
            self.go_x = self.largeur # Le ramène à droite de l'écran