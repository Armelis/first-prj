import sys, pygame
from setting import Settings
from ship import Ship
import game_funstons as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.update()

    while True:
        gf.check_events(ship, ai_settings, bullets, screen)
        ship.update()
        gf.bullet_update(bullets)
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullet.remove(bullets)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)
run_game()
