class GameStats():
    '''Storage statistc data from Alien Invasion'''

    def __init__(self, ai_settings):
        '''Start the statistc data'''
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_activate = True

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit