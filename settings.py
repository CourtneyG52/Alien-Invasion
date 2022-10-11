class Settings:
    
    def __init__(self):
        #Games settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        self.ship_speed = 5
        self.ship_limit = 3
        
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        #Alien speed
        self.alien_speed = 5
        self.fleet_drop_speed = 50
        
        #How quickly the game speeds up
        self.speedup_scale = 2.0
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
        #fleet directions of 1 represents right (-1 is left)
        self.fleet_direction = 1
        
    def initialize_dynamic_settings(self):
        #Settings that change throughout the game
        self.ship_speed = 3.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.5
        
        #fleet directions (1 is right, -1 is left)
        self.fleet_direction = 1
        
        #Scoring
        self.alien_points = 50
        
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien.points * self.score_scale)
        print(self.alien_points)