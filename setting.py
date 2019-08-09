class Settings():

    def __init__(self):
        self.screen_width = 1850
        self.screen_height = 1010
        self.bg_color = (27,26,57)
        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255,255,255)
        self.bullets_allowed = 15
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.5
        self.initialize_dynamic_settings()
        self.fleet_direction = 1
        self.ship_limit = 3



    def initialize_dynamic_settings(self):
      self.ship_speed_factor = 2
      self.bullet_speed_factor = 3
      self.alien_speed_factor = 2

    def increase_speed(self):
      self.ship_speed_factor *= self.speedup_scale
      self.bullet_speed_factor *= self.speedup_scale
      self.alien_speed_factor *= self.speedup_scale