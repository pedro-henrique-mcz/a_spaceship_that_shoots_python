'''Setting Class Module'''

class Settings():
    '''A class to storage all configs of 
    Alien Invasion Project'''
    def __init__(self):
        '''Starting game configs'''
        #Screen Config
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

        #Bullets config
        self.bullet_speed_factor = 3
        self.bullet_width = 300 
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        self.alien_speed_factor =1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        
        self.ship_limit = 3
