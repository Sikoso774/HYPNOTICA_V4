# scripts/instructions_components/instructions_logic.py

import pygame
import sys
from scripts.instructions_components.constants import (
    BLANC, NOIR, LARGEUR_ECRAN_INSTRUCTIONS, HAUTEUR_ECRAN_INSTRUCTIONS,
    TITRE_FENETRE_INSTRUCTIONS, INSTRUCTIONS_TEXT_CONTENT, DELAI_FRAPPE_MS,
    FONT_SIZES_MAP, DEFAULT_FONT_SIZE, CHEMIN_POLICE_INSTRUCTIONS
)
from scripts.instructions_components.resources import get_instructions_font
# Utiliser la fonction afficher_texte_centre modifiée.
# Assure-toi que le chemin est correct. Si tu l'as mise dans un nouveau fichier utils, mets le bon import.
# Pour l'instant, je vais assumer qu'elle est dans scripts/ecran_titre_components/text_utils.py
from scripts.ecran_titre_components.text_utils import afficher_texte_centre


class InstructionsScreen:
    _is_pygame_initialized_by_us = False

    def __init__(self):
        if not pygame.get_init():
            pygame.init()
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            InstructionsScreen._is_pygame_initialized_by_us = True

        self.largeur = LARGEUR_ECRAN_INSTRUCTIONS
        self.hauteur = HAUTEUR_ECRAN_INSTRUCTIONS
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(TITRE_FENETRE_INSTRUCTIONS)

        self.texte_instructions = INSTRUCTIONS_TEXT_CONTENT
        self.current_char_index = 0 # Index du caractère actuellement affiché
        self.last_char_time = pygame.time.get_ticks() # Temps du dernier affichage de caractère

        # Offset vertical pour le texte, pour le centrer ou le positionner au début
        self.text_start_y = self.hauteur // 4

    def run(self):
        running = True
        while running:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    if InstructionsScreen._is_pygame_initialized_by_us:
                        pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Si SPACE est pressé, afficher tout le texte d'un coup
                        # Ou avancer très vite jusqu'à la fin de la frappe
                        if self.current_char_index < self._get_total_chars():
                            self.current_char_index = self._get_total_chars()
                        else:
                            # Si tout est déjà affiché, on peut retourner au menu
                            return "menu"
                    # Permettre de sauter l'animation en appuyant sur une touche
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        self.current_char_index = self._get_total_chars() # Affiche tout d'un coup

            # Mise à jour de l'index des caractères à afficher
            if self.current_char_index < self._get_total_chars():
                if current_time - self.last_char_time > DELAI_FRAPPE_MS:
                    self.current_char_index += 1
                    self.last_char_time = current_time

            self.ecran.fill(NOIR)
            self.draw_instructions()
            pygame.display.flip()
            pygame.time.delay(10) # Petit délai pour contrôler le framerate et la consommation CPU

        return None # Ne devrait pas être atteint dans un jeu bien structuré

    def _get_total_chars(self):
        """Calcule le nombre total de caractères de toutes les instructions."""
        return sum(len(line) for line in self.texte_instructions) + len(self.texte_instructions) * 2 # +2 pour simuler des pauses entre les lignes

    def draw_instructions(self):
        char_count = 0
        for i, ligne in enumerate(self.texte_instructions):
            y_position = self.text_start_y + i * 30 # Espace les lignes

            # Détermine la taille de police spécifique pour cette ligne
            font_size = DEFAULT_FONT_SIZE
            for key, size in FONT_SIZES_MAP.items():
                if ligne.startswith(key):
                    font_size = size
                    break

            # Calcule le nombre de caractères de cette ligne à afficher
            chars_on_this_line = min(len(ligne), self.current_char_index - char_count)

            if chars_on_this_line > 0:
                # Utilise afficher_texte_centre qui peut gérer les caractères limités
                afficher_texte_centre(
                    self.ecran,
                    ligne, # Passe la ligne entière, la fonction la tronquera
                    BLANC,
                    y_position,
                    font_path=CHEMIN_POLICE_INSTRUCTIONS, # Spécifie la police des instructions
                    font_size=font_size
                )
            char_count += len(ligne) + 2 # +2 pour le compte des caractères inter-lignes

        # Si toutes les lignes sont affichées, on peut ajouter une indication "Appuyez sur ESPACE"
        if self.current_char_index >= self._get_total_chars():
            # Ajoute un clignotement pour le texte "Appuyez sur ESPACE" si tu le souhaites
            blink_alpha = abs(255 - (pygame.time.get_ticks() // 5 % 510)) # Clignotement simple
            temp_surface = get_instructions_font(24).render("Press SPACE to return to menu", True, BLANC)
            temp_surface.set_alpha(blink_alpha)
            temp_rect = temp_surface.get_rect(center=(self.largeur // 2, self.hauteur - 50))
            self.ecran.blit(temp_surface, temp_rect)


# --- Bloc de test pour l'exécution indépendante ---
if __name__ == "__main__":
    try:
        # Assure-toi que Pygame est bien initialisé pour le test indépendant
        if not pygame.get_init():
            pygame.init()
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        instructions_test = InstructionsScreen()
        print("Démarrage de l'écran d'instructions...")
        result = instructions_test.run()
        print(f"Écran instructions terminé, résultat : {result}")

    except Exception as e:
        print(f"Une erreur s'est produite lors du test des Instructions : {e}")
    finally:
        if pygame.get_init():
            pygame.quit()
        sys.exit()