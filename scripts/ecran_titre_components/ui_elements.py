# scripts/ecran_titre_components/ui_elements.py

import pygame
# Importe les couleurs depuis ton fichier de constantes
from scripts.ecran_titre_components.constants import BLANC, GRIS, NOIR
# from scripts.utils_paths import get_resource_path # Plus besoin ici directement si sfx_manager gère
from scripts.sfx_manager import play_sfx, load_sfx # Importe les fonctions de gestion des sons

class Bouton:
    # Définis ici les chemins des sons si tu veux qu'ils soient fixes pour tous les boutons
    # Ou les passer en paramètre si chaque bouton peut avoir un son différent
    SOUND_CLICK_PATH = "assets/sounds/yes_clicked.wav" # Assure-toi d'avoir ce fichier !
    SOUND_HOVER_PATH = "assets/sounds/hover_click.wav" # Assure-toi d'avoir ce fichier !

    def __init__(self, x, y, largeur, hauteur, texte, action_liee, police_font, color=NOIR):
        """
        Initialise un bouton cliquable.

        Args:
            x (int): Coordonnée X du coin supérieur gauche du bouton.
            y (int): Coordonnée Y du coin supérieur gauche du bouton.
            largeur (int): Largeur du bouton.
            hauteur (int): Hauteur du bouton.
            texte (str): Texte à afficher sur le bouton.
            action_liee (str): La valeur de retour quand le bouton est cliqué (ex: "démarrer", "crédits").
            police_font (pygame.font.Font): L'objet police Pygame à utiliser pour le texte du bouton.
            color (tuple, optional): La couleur du bouton quand il est actif. Par défaut NOIR.
        """
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.texte = texte
        self.action_liee = action_liee
        self.police = police_font # La police est maintenant passée en argument
        self.couleur_inactive = GRIS
        self.couleur_active = color # Utilise le paramètre color
        self.couleur = self.couleur_inactive
        self.est_survole = False # Pour détecter l'entrée de la souris

        # Charge les sons une seule fois par classe Bouton, ou directement via le sfx_manager
        # C'est mieux de charger les sons au niveau du module ou de la classe appelante (EcranTitre)
        # pour éviter que chaque instance de bouton ne recharge les mêmes sons.
        # Pour cet exemple, on va les charger ici si sfx_manager les met en cache, c'est OK.
        load_sfx(self.SOUND_CLICK_PATH)
        load_sfx(self.SOUND_HOVER_PATH)


    def dessiner(self, surface, gif_image): # Gardons gif_image au cas où tu en aurais besoin pour un effet visuel
        """
        Dessine le bouton sur la surface donnée.
        Le bouton change de couleur au survol de la souris et joue un son au survol.
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if not self.est_survole: # Si la souris vient d'entrer dans le bouton
                play_sfx(self.SOUND_HOVER_PATH, volume=0.3) # Joue le son de survol
                self.est_survole = True
            self.couleur = self.couleur_active
        else:
            if self.est_survole: # Si la souris vient de quitter le bouton
                self.est_survole = False
            self.couleur = self.couleur_inactive

        pygame.draw.rect(surface, self.couleur, self.rect)

        texte_surface = self.police.render(self.texte, True, BLANC)
        texte_rect = texte_surface.get_rect(center=self.rect.center)
        surface.blit(texte_surface, texte_rect)

    def gerer_evenement(self, event):
        """
        Gère les événements liés au bouton (clic de souris).
        Joue un son au clic.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Clic gauche de la souris
                if self.rect.collidepoint(event.pos):
                    play_sfx(self.SOUND_CLICK_PATH, volume=0.5) # Joue le son de clic
                    return self.action_liee
        return None