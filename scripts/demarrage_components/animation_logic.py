# scripts/demarrage_components/animation_logic.py

import pygame
from scripts.demarrage_components.constants import (
    BLANC, NOIR, LARGEUR_ECRAN_DEMARRAGE, HAUTEUR_ECRAN_DEMARRAGE,
    DUREE_AFFICHAGE_PAR_IMAGE, ALPHA_VITESSE,
    TEXTE_LOGO_JEU, TEXTE_DEVELOPPEUR
)
from scripts.demarrage_components.resources import get_demarrage_font

def draw_demarrage_frame(screen, image, current_phase_time, total_duration_per_phase):
    """
    Dessine une frame de l'écran de démarrage avec l'image et les textes
    en gérant leurs alphas respectifs.
    :param screen: La surface Pygame sur laquelle dessiner.
    :param image: L'image actuelle à afficher.
    :param current_phase_time: Le temps écoulé dans la phase d'affichage actuelle (ms).
    :param total_duration_per_phase: La durée totale pour une phase d'affichage (ms).
    """
    screen.fill(NOIR)

    # Calcul de l'alpha pour l'image
    # L'image apparaît, reste visible, puis le texte apparaît
    alpha_image = 255
    if current_phase_time < total_duration_per_phase / 3:
        # Apparition de l'image
        alpha_image = int(current_phase_time * ALPHA_VITESSE)
    elif current_phase_time > 2 * total_duration_per_phase / 3:
        # L'image commence à disparaître pour la transition vers la prochaine
        alpha_image = 255 - int((current_phase_time - (2 * total_duration_per_phase / 3)) * ALPHA_VITESSE)

    alpha_image = max(0, min(255, alpha_image)) # Assure que l'alpha est entre 0 et 255

    # Application de l'alpha à une copie de l'image pour ne pas modifier l'originale
    # C'est important si l'image est utilisée ailleurs ou si elle est mise en cache
    image_to_blit = image.copy()
    image_to_blit.set_alpha(alpha_image)

    # Redimensionnement de l'image pour qu'elle s'adapte à l'écran
    # Gardons la proportion originale de l'image
    image_rect = image_to_blit.get_rect(center=(LARGEUR_ECRAN_DEMARRAGE // 2, HAUTEUR_ECRAN_DEMARRAGE // 2))

    screen.blit(image_to_blit, image_rect)

    # Texte 1 (Logo jeu / Nom du développeur) - Apparaît après 1/3 de la durée
    alpha_txt_1 = 0
    if current_phase_time > total_duration_per_phase / 3:
        alpha_txt_1 = int((current_phase_time - total_duration_per_phase / 3) * ALPHA_VITESSE)
    alpha_txt_1 = max(0, min(255, alpha_txt_1))

    police_txt_1 = get_demarrage_font(48) # Taille plus grande pour le logo
    txt_1_surface = police_txt_1.render(TEXTE_LOGO_JEU, True, BLANC)
    txt_1_surface.set_alpha(alpha_txt_1)
    txt_1_rect = txt_1_surface.get_rect(center=(LARGEUR_ECRAN_DEMARRAGE // 2, HAUTEUR_ECRAN_DEMARRAGE // 6))
    screen.blit(txt_1_surface, txt_1_rect)

    # Texte 2 (Sikoso774 / Projet Hypnotica) - Apparaît après 2/3 de la durée
    alpha_txt_2 = 0
    if current_phase_time > 2 * total_duration_per_phase / 3:
        alpha_txt_2 = int((current_phase_time - 2 * total_duration_per_phase / 3) * ALPHA_VITESSE)
    alpha_txt_2 = max(0, min(255, alpha_txt_2))

    police_txt_2 = get_demarrage_font(36)
    txt_2_surface = police_txt_2.render(TEXTE_DEVELOPPEUR, True, BLANC)
    txt_2_surface.set_alpha(alpha_txt_2)
    txt_2_rect = txt_2_surface.get_rect(center=(LARGEUR_ECRAN_DEMARRAGE // 2, HAUTEUR_ECRAN_DEMARRAGE - 100))
    screen.blit(txt_2_surface, txt_2_rect)