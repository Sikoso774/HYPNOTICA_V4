import pygame
import sys
from os.path import join
from ..config.settings import *
from ..config.support import get_resource_path
from ..constants.instruction_const import INSTRUCTIONS_CONTENT

class Instructions:
    _is_pygame_initialized_by_us = False

    def __init__(self):
        if not pygame.get_init():
            pygame.init()
            Instructions._is_pygame_initialized_by_us = True
            
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        
        self.instruction_data = INSTRUCTIONS_CONTENT
        
        # Gestion Musique
        self.music_path = get_resource_path(join("assets", "musics", "Max Brhon - AI [NCS Release].mp3"))
        
        # --- LOGIQUE FLUIDITÉ MUSIQUE ---
        # On ne charge la musique que si rien ne joue.
        # Si "Max Brhon" joue déjà (venant du menu), ça continue sans coupure.
        try:
            if pygame.mixer.get_init() and not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(self.music_path)
                pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Erreur musique instructions: {e}")

        # Variables animation
        self.current_char_index = 0
        self.last_char_time = 0
        self.typing_speed = 30 
        
        self.prepared_items = []
        self.total_chars = 0
        self._prepare_content()

    def _prepare_content(self):
        current_y = WINDOW_HEIGHT // 6 
        self.total_chars = 0
        font_path = get_resource_path(join("assets", "fonts", "MINDCONTROL.ttf"))

        for item in self.instruction_data:
            if item['type'] == 'text':
                try:
                    font = pygame.font.Font(font_path, item.get('font-size', 30))
                except FileNotFoundError:
                    font = pygame.font.Font(None, item.get('font-size', 30))
                
                self.prepared_items.append({
                    'type': 'text',
                    'full_text': item['value'],
                    'font': font,
                    'color': item.get('color', COLORS['white']),
                    'y': current_y,
                    'start_index': self.total_chars,
                    'length': len(item['value'])
                })
                
                self.total_chars += len(item['value'])
                current_y += font.get_height() + 10 
            elif item['type'] == 'spacer':
                current_y += item.get('height', 20)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if Instructions._is_pygame_initialized_by_us:
                    pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.current_char_index < self.total_chars:
                        self.current_char_index = self.total_chars
                    else:
                        return "menu"
                elif event.key == pygame.K_ESCAPE:
                    return "menu"
        return None

    def draw(self):
        self.screen.fill(COLORS['black'])
        for item in self.prepared_items:
            if item['type'] == 'text':
                if self.current_char_index > item['start_index']:
                    char_limit = min(self.current_char_index - item['start_index'], item['length'])
                    text_to_render = item['full_text'][:char_limit]
                    surf = item['font'].render(text_to_render, True, item['color'])
                    rect = surf.get_rect(center=(WINDOW_WIDTH // 2, item['y']))
                    self.screen.blit(surf, rect)

    def run(self):
        self.current_char_index = 0
        self.last_char_time = pygame.time.get_ticks()
        running = True
        while running:
            action = self._handle_events()
            if action == "menu":
                return "menu"

            current_time = pygame.time.get_ticks()
            if self.current_char_index < self.total_chars:
                if current_time - self.last_char_time > self.typing_speed:
                    self.current_char_index += 1
                    self.last_char_time = current_time
            
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    inst = Instructions()
    inst.run()