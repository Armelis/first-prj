import sys, pygame
from setting import Settings
from ship import Ship
import game_funstons as gf
from pygame.sprite import Group
from stats import GameStats
from buttom import Button

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen)
    stats = GameStats(ai_settings)
    aliens = Group()
    bullets = Group()
    gf.create_fleet(ai_settings, screen,ship, aliens)
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.update()

    while True:
        gf.check_events(ai_settings, screen,stats, play_button, ship, aliens, bullets)
        if stats.game_active:
          ship.update()
          gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
          gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
          for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullet.remove(bullets)
                print(len(bullets))
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)



run_game()
