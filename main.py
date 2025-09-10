# Zoléni KOKOLO ZASSI
# Hypnotica_V2

# -------------- Importations de Pygame et sys pour quitter proprement -------------------
import pygame
import sys

# -------------- Mes programmes (mise à jour des chemins) --------------------------------

from scripts.chargement_components.chargement import Chargement
from scripts.demarrage_components.demmarage_logic import Démarrage
from scripts.ecran_titre_components.ecran_titre_logic import EcranTitre
from scripts.game.game import Game
from scripts.credits_components.credits_logic import CreditsScreen
from scripts.game_over_components.game_over_logic import GameOverScreen
from scripts.instructions_components.instructions_logic import InstructionsScreen
from scripts.paths import get_resource_path

# --------------------------- Programme principal ------------------------------------------------------

if __name__ == '__main__':
    # Initialisation de Pygame et du mixer, une seule fois au début du programme.
    # Bien que d'autres modules l'initialisent aussi, le faire ici garantit
    # qu'il est prêt pour toutes les classes.
    if not pygame.get_init():
        pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Exécution de l'écran de démarrage
    game_demarrage = Démarrage()
    # Le chemin des images pour Démarrage.run() doit être correct
    game_demarrage.run([get_resource_path("assets/images/Zoléni_Cyberpunk.jpg"),
                        get_resource_path("assets/images/PP_Sikoso_77.jpg"),
                        get_resource_path("assets/images/pygame_logo.png")])

    # Exécution de la transition de chargement
    game_chargement = Chargement()
    # Correction ici: Appel de loading() sans arguments,
    # car Chargement.py charge ses propres images globalement.
    game_chargement.loading()

# --------------------------- Boucle principale du jeu ---------------------------------------------
    while True:
        # Écran titre
        ecran_titre_instance = EcranTitre()
        action_menu = ecran_titre_instance.run_Tscreen()  # Doit retourner "démarrer", "crédits", "instructions", ou "quit"

        if action_menu == "démarrer":
            # Instancie et lance le jeu principal
            game_instance = Game()  # Utilise la nouvelle classe Game
            game_result = game_instance.run()  # run() retourne "game_over" ou "quit"

            if game_result == "game_over":
                game_over_instance = GameOverScreen()
                action_apres_go = game_over_instance.run()

                if action_apres_go == "relancer":
                    continue  # Retourne au début de la boucle principale pour relancer le jeu
                elif action_apres_go == "crédits":
                    credits_instance = CreditsScreen()
                    action_apres_credits = credits_instance.run()
                    if action_apres_credits == "menu":  # Si les crédits retournent au menu
                        continue
                    elif action_apres_credits == "quit":  # Si l'utilisateur quitte depuis les crédits
                        break
                elif action_apres_go == "quit":
                    break  # Quitte la boucle principale du jeu

            elif game_result == "quit":  # Si le jeu a été quitté pendant la partie (par la croix)
                break  # Quitte la boucle principale du jeu

        elif action_menu == "crédits":
            credits_instance = CreditsScreen()
            action_apres_credits = credits_instance.run()
            if action_apres_credits == "menu":
                continue  # Retourne au début de la boucle principale (écran titre)
            elif action_apres_credits == "quit":
                break  # Quitte la boucle principale du jeu

        elif action_menu == "instructions":
            instructions_instance = InstructionsScreen()
            return_action = instructions_instance.run()
            if return_action == "menu":
                continue  # Retourne au menu principal après les instructions
            elif return_action == "quit":  # Si l'utilisateur quitte depuis les instructions
                break

        elif action_menu == "quit":
            break  # Quitte la boucle principale du jeu
        else:
            print(f"Action inattendue de l'écran titre: {action_menu}. Quitting.")
            break

    # Assure-toi que Pygame est bien quitté à la fin du programme
    pygame.quit()
    sys.exit()  # Quitte le programme proprement