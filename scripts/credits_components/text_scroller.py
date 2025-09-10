# scripts/credits_components/text_scroller.py

import pygame
from scripts.credits_components.constants import (
    BLANC, NOIR, CHEMIN_POLICE_CREDITS_DEFAULT, VITESSE_DEFILEMENT_CREDITS,
    CREDITS_CONTENT, LARGEUR_ECRAN_CREDITS, HAUTEUR_ECRAN_CREDITS
)
from scripts.credits_components.resources import get_credits_font # Pour charger les polices
import math # Pour le calcul des positions

class CreditsTextScroller:
    def __init__(self):
        self.largeur = LARGEUR_ECRAN_CREDITS
        self.hauteur = HAUTEUR_ECRAN_CREDITS
        self.credits_list_data = CREDITS_CONTENT # Utilise la structure des constantes
        self.credits_y = self.hauteur # Commence sous l'écran
        self.credits_vitesse = VITESSE_DEFILEMENT_CREDITS

        self.loaded_images = {} # Sera rempli par la classe principale
        self.total_content_height = self._calculate_total_content_height()


    def _calculate_total_content_height(self):
        """Calcule la hauteur totale nécessaire pour afficher tout le contenu des crédits."""
        total_height = 0
        for item in self.credits_list_data:
            if item['type'] == 'text':
                # On utilise une police temporaire pour estimer la hauteur de ligne
                # ou une estimation moyenne. Pour une vraie précision, il faudrait charger
                # chaque police et faire un render, mais c'est lourd.
                # Une estimation basée sur la taille de police et un facteur est souvent suffisante.
                estimated_line_height = item.get('font_size', 30) * 1.5 # Facteur pour l'interligne
                total_height += estimated_line_height
            elif item['type'] == 'image':
                # Pour les images, on a besoin de la hauteur réelle après mise à l'échelle.
                # Comme elles ne sont pas encore chargées ici, nous utiliserons une estimation
                # basée sur le facteur d'échelle et la hauteur de l'écran.
                # Une meilleure approche serait de passer les images chargées pour obtenir la hauteur réelle.
                # Pour l'instant, estimation:
                estimated_image_height = self.hauteur * item.get('image_scale_factor', 0.5)
                total_height += estimated_image_height
            elif item['type'] == 'spacer':
                total_height += item.get('height', 0)
        return total_height + self.hauteur # Ajoute une hauteur d'écran pour permettre le défilement complet

    def set_loaded_images(self, images_dict):
        """Passe le dictionnaire des images chargées à la classe de défilement."""
        self.loaded_images = images_dict

    def draw_and_scroll_credits(self, surface):
        """
        Dessine et fait défiler les lignes de crédits sur la surface donnée.
        """
        current_y_offset = self.credits_y # Position de départ pour le rendu

        for item in self.credits_list_data:
            if item['type'] == 'text':
                font_size = item.get('font_size', 32)
                text_color = item.get('color', BLANC)
                font = get_credits_font(CHEMIN_POLICE_CREDITS_DEFAULT, font_size)
                texte_surface = font.render(item['value'], True, text_color)
                texte_rect = texte_surface.get_rect(center=(self.largeur // 2, current_y_offset))
                surface.blit(texte_surface, texte_rect)
                current_y_offset += texte_surface.get_height() + (font_size * 0.5) # Espacement dynamique

            elif item['type'] == 'image':
                image_key = item['value']
                if image_key in self.loaded_images:
                    image_surface = self.loaded_images[image_key]
                    image_rect = image_surface.get_rect(center=(self.largeur // 2, current_y_offset))
                    surface.blit(image_surface, image_rect)
                    current_y_offset += image_surface.get_height() + 20 # Espacement après image
                else:
                    # Dessiner un placeholder ou un message d'erreur si l'image n'est pas trouvée
                    error_font = get_credits_font(None, 20)
                    error_text = error_font.render(f"Image '{image_key}' not found!", True, ROUGE)
                    error_rect = error_text.get_rect(center=(self.largeur // 2, current_y_offset))
                    surface.blit(error_text, error_rect)
                    current_y_offset += error_text.get_height() + 20 # Espacement
            elif item['type'] == 'spacer':
                current_y_offset += item.get('height', 0)

        self.credits_y -= self.credits_vitesse

        # Réinitialise la position si tous les crédits ont défilé
        # Le calcul de `total_content_height` est essentiel ici
        if self.credits_y < -self.total_content_height:
            self.credits_y = self.hauteur # Revient en bas de l'écran