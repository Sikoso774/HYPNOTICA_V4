# Fichier ecran_titre_logic.py
from ..config.settings import *
from ..config.support import *
from ..constants.mainmenu_const import *
from ..components.elements.mainmenu_button import Bouton
from ..components.sprites.hypnose_gif import Animation_GIF
from ..config.utils import display_text_center as center_text


class MainMenu:
    """ Main menu screen class.

    Args:
    screen (pygame.Surface): The main display surface.
    """
    _is_pygame_initialized_by_us = False

    def __init__(self, screen):# Prend maintenant l'écran en paramètre
        """ Initialize main menu screen elements.
        Args:
        screen (pygame.Surface): The main display surface."""
        
        # 1. Screen
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
    
        # 2. Assets (GIF)
        GIF_PATH = get_resource_path(join(IMAGES_DIR, "hypnose_frames"))
        self.gif_animator = Animation_GIF(GIF_PATH, self.screen)
        self.animation_frame = self.gif_animator.animation_frame

        # 3. Buttons
        self.buttons = []
        for bouton_data in BUTTONS_MENU: # Utilise la liste complète et fiable
            x = self.width // 2 - BUTTON_WITDH // 2
            y = bouton_data['y_offset'] 
            
            self.buttons.append(
                Bouton(x, y,BUTTON_WITDH, BUTTON_HEIGHT, bouton_data['text'], bouton_data['action'])
            )
        
        # 4 Music
        self.music_path = get_resource_path(join(AUDIO_DIR, "Max Brhon - AI [NCS Release].mp3"))

        return None
    
    def _manage_interactions(self, event):
        for button in self.buttons:
            action = button.manage_event(event)
            if action:
                return action

    def _draw(self):
        
        frame_index = self.gif_animator.animation_frame
        self.screen.blit(self.gif_animator.frames[frame_index], (0, 0))
        center_text(self.screen, "HYPNOTICA", COLORS['white'], self.height // 4,
                              font_path=get_resource_path(DEFAULT_FONT_NAME))
        center_text(self.screen, "Zoléni KOKOLO ZASSI - 2025", COLORS['white'], self.height// 4 + 50, font_size=28)
        for button in self.buttons:
            button.dessiner(self.screen, self.gif_animator.frames[self.animation_frame])


    # --- La méthode run est la boucle principale pour cet état ---
    def run(self) -> None:
        
        try:
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play(-1)
        except pygame.error as e:
            print(f"Erreur de lecture de la musique du titre: {e}")
        
        clock = pygame.time.Clock()
        running = True
        while running:
            
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                
                # Gestion des interactions des boutons
                action = self._manage_interactions(event)
                if action:
                    pygame.mixer.music.stop()
                    # Retourne l'action demandée par le bouton (ex: 'game', 'credits', 'quit')
                    return action 
            
            # Animation
            self.gif_animator.animate()
            
            # drawing
            self._draw()

            # update
            pygame.display.update()
            clock.tick(FPS)
            
        return None 
    

# Test rapide pour vérifier si l'écran titre fonctionne indépendamment
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    titre = MainMenu(screen)
    titre.run()
    pygame.quit()