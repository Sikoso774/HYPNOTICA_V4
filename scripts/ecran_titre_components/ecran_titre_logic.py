# scripts/ecran_titre_components/ecran_titre_logic.py

import pygame
import os
import sys

from scripts.ecran_titre_components.constants import ORANGE
from scripts.paths import get_resource_path
from scripts.ecran_titre_components.constants import (
    BLANC, LARGEUR_ECRAN, HAUTEUR_ECRAN, TITRE_FENETRE, NOIR, ROUGE, VERT,  # Ajout de GRIS
    CHEMIN_POLICE, TAILLE_POLICE, CHEMIN_MUSIQUE, CHEMIN_IMAGES_GIF, VITESSE_ANIMATION_GIF
)
from scripts.ecran_titre_components.ui_elements import Bouton
from scripts.ecran_titre_components.text_utils import afficher_texte_centre
from scripts.sfx_manager import load_sfx # Importer pour précharger les sons des boutons


class EcranTitre:
    _gif_images_cache = []
    _is_pygame_initialized_by_us = False

    def __init__(self):
        if not pygame.get_init():
            pygame.init()
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            EcranTitre._is_pygame_initialized_by_us = True

        self.largeur = LARGEUR_ECRAN
        self.hauteur = HAUTEUR_ECRAN
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption(TITRE_FENETRE)

        # Chargement des ressources (images GIF et musique)
        if not EcranTitre._gif_images_cache:
            self._load_resources()
            EcranTitre._gif_images_cache = self._gif_images

        self.gif_images = EcranTitre._gif_images_cache

        try:
            self._bouton_police = pygame.font.Font(get_resource_path(CHEMIN_POLICE), TAILLE_POLICE)
        except Exception as e:
            print(f"Erreur de chargement de la police pour les boutons: {e}")
            self._bouton_police = pygame.font.SysFont(None, TAILLE_POLICE) # Fallback

        # Précharger les sons des boutons pour éviter les lags au premier survol/clic
        load_sfx(Bouton.SOUND_CLICK_PATH)
        load_sfx(Bouton.SOUND_HOVER_PATH)

        # Configuration des boutons avec la nouvelle couleur par défaut ou spécifique
        self.boutons = [
            Bouton(self.largeur // 2 - 100, self.hauteur // 2, 200, 50, "Démarrer", "démarrer", self._bouton_police, color=VERT), # Utilise la couleur VERTE pour "Démarrer"
            Bouton(self.largeur // 2 - 100, self.hauteur // 2 + 70, 200, 50, "Crédits", "crédits", self._bouton_police, color=ORANGE), # Exemple : Bouton "Crédits" en BLEU
            Bouton(self.largeur // 2 - 100, self.hauteur // 2 + 140, 200, 50, "Instructions", "instructions", self._bouton_police, color=ROUGE), # Exemple : Bouton "Instructions" en ROUGE
            Bouton(self.largeur // 2 - 100, self.hauteur // 2 + 210, 200, 50, "Quitter", "quitter", self._bouton_police, color=NOIR) # Exemple : Bouton "Quitter" en GRIS
        ]

        self.animation_frame = 0
        self.animation_speed = VITESSE_ANIMATION_GIF

        # Chargement de la musique
        pygame.mixer.music.load(get_resource_path("assets/musics/Max Brhon - AI [NCS Release].mp3"))

    def _load_resources(self):
        self._gif_images = []
        try:
            image_folder = CHEMIN_IMAGES_GIF
            if not os.path.isdir(image_folder):
                raise FileNotFoundError(f"Le dossier GIF n'existe pas : {image_folder}")

            files_in_folder = [f for f in os.listdir(image_folder) if f.lower().endswith(".png")]
            if not files_in_folder:
                raise ValueError(f"Aucun fichier PNG trouvé dans : {image_folder}")

            for filename in sorted(files_in_folder):
                image_path = get_resource_path(os.path.join("images_gif", filename))
                image = pygame.image.load(image_path).convert_alpha()
                image = pygame.transform.scale(image, (self.largeur, self.hauteur))
                self._gif_images.append(image)

            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(CHEMIN_MUSIQUE)
                pygame.mixer.music.play(-1)

        except (FileNotFoundError, ValueError) as e:
            print(f"Erreur critique lors du chargement des ressources de l'écran titre : {e}")
            if pygame.get_init():
                pygame.quit()
            sys.exit()
        except pygame.error as e:
            print(f"Erreur Pygame lors du chargement des ressources de l'écran titre : {e}")
            if pygame.get_init():
                pygame.quit()
            sys.exit()

    def run_Tscreen(self):
        pygame.mixer.music.play(-1)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    if EcranTitre._is_pygame_initialized_by_us:
                        pygame.quit()
                    sys.exit()

                action = self._gerer_interactions(event)
                if action:
                    if action == "crédits":
                        pygame.mixer.music.stop()
                    elif action == "quitter":
                        pygame.mixer.music.stop()
                        if EcranTitre._is_pygame_initialized_by_us:
                            pygame.quit()
                        sys.exit()
                    return action

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return "démarrer"
                    if event.key == pygame.K_c:
                        pygame.mixer.music.stop()
                        return "crédits"
                    if event.key == pygame.K_i:
                        return "instructions"
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        if EcranTitre._is_pygame_initialized_by_us:
                            pygame.quit()
                        sys.exit()

            self._dessiner()
            pygame.display.flip()
            self._animer_gif()
            pygame.time.delay(1000 // self.animation_speed)

        pygame.mixer.music.stop()
        if EcranTitre._is_pygame_initialized_by_us:
            pygame.quit()
        return None

    def _gerer_interactions(self, event):
        for bouton in self.boutons:
            action = bouton.gerer_evenement(event)
            if action:
                return action
        return None

    def _dessiner(self):
        self.ecran.blit(self.gif_images[self.animation_frame], (0, 0))
        afficher_texte_centre(self.ecran, "HYPNOTICA", BLANC, HAUTEUR_ECRAN // 4,
                              font_path=get_resource_path("assets/fonts/MINDCONTROL.ttf"))
        afficher_texte_centre(self.ecran, "Zoléni KOKOLO ZASSI - 2025", BLANC, HAUTEUR_ECRAN // 4 + 50, font_size=28)
        for bouton in self.boutons:
            bouton.dessiner(self.ecran, self.gif_images[self.animation_frame])

    def _animer_gif(self):
        self.animation_frame += 1
        if self.animation_frame >= len(self.gif_images):
            self.animation_frame = 0

    @property
    def is_pygame_initialized_by_us(self):
        return self._is_pygame_initialized_by_us


if __name__ == "__main__":
    try:
        ecran_titre_test = EcranTitre()
        print("Écran titre initialisé. Lancement de la boucle...")
        result = ecran_titre_test.run_Tscreen()
        print(f"Écran titre terminé, résultat : {result}")
    except Exception as e:
        print(f"Une erreur s'est produite lors du test de l'écran titre: {e}")
    finally:
        if EcranTitre.is_pygame_initialized_by_us and pygame.get_init():
            pygame.quit()
        sys.exit()