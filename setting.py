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
