# scripts/chargement_components/animation_logic.py

import pygame
import math
import sys # Pour sys.exit() en cas de QUIT pendant l'animation
from scripts.chargement_components.constants import DUREE_TRANSITION_CHARGEMENT, LARGEUR_ECRAN_CHARGEMENT, HAUTEUR_ECRAN_CHARGEMENT

def run_spiral_transition(surface, image_fin, gif_images):
    """
    Exécute l'animation de transition en spirale de l'image_fin sur un fond de GIF animé.
    :param surface: La surface Pygame sur laquelle dessiner.
    :param image_fin: L'image à faire spirale.
    :param gif_images: Liste des images GIF pour l'arrière-plan.
    """
    temps_debut = pygame.time.get_ticks()
    centre_x, centre_y = LARGEUR_ECRAN_CHARGEMENT // 2, HAUTEUR_ECRAN_CHARGEMENT // 2
    rayon_max = min(LARGEUR_ECRAN_CHARGEMENT, HAUTEUR_ECRAN_CHARGEMENT) // 2
    duree_transition = DUREE_TRANSITION_CHARGEMENT # Utilise la constante

    while pygame.time.get_ticks() - temps_debut < duree_transition:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() # Quitte proprement si l'utilisateur ferme la fenêtre pendant la transition

        temps_ecoule = pygame.time.get_ticks() - temps_debut
        pourcentage = temps_ecoule / duree_transition
        angle = pourcentage * 10 * math.pi  # Ajustez pour la vitesse de rotation
        rayon = rayon_max * pourcentage

        # Efface l'écran avec la nouvelle frame du GIF
        if gif_images: # S'assurer qu'il y a des images GIF pour le fond
            frame = int(pourcentage * len(gif_images)) % len(gif_images)
            surface.blit(gif_images[frame], (0, 0))
        else:
            surface.fill((0, 0, 0)) # Fond noir si pas de GIF

        # Calcul des coordonnées de la spirale pour l'image_fin
        x = centre_x + rayon * math.cos(angle)
        y = centre_y + rayon * math.sin(angle)

        # Redimensionnement et rotation de l'image_fin
        # La taille diminue à mesure que le pourcentage augmente
        taille = int((1 - pourcentage) * min(LARGEUR_ECRAN_CHARGEMENT, HAUTEUR_ECRAN_CHARGEMENT))
        if taille > 0: # Éviter les erreurs de taille zéro
            image_transformee = pygame.transform.scale(image_fin, (taille, taille))
            image_transformee = pygame.transform.rotate(image_transformee, angle * 180 / math.pi)
            rect_transforme = image_transformee.get_rect(center=(x, y))
            surface.blit(image_transformee, rect_transforme)

        pygame.display.flip()
        pygame.time.delay(10) # Contrôle la vitesse de rafraîchissement (environ 100 FPS)