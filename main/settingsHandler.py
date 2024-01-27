from configparser import ConfigParser

class SettingsHandler:
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self.config = ConfigParser()
        self.load_settings()

    def load_settings(self):
        self.config.read(self.config_file)
        self.system_enabled = self.config.getboolean('Settings', 'system_enabled', fallback=False)
        self.notifications_enabled = self.config.getboolean('Settings', 'notifications_enabled', fallback=True)


    def save_settings(self):
        self.config.set('Settings', 'system_enabled', str(self.system_enabled))
        self.config.set('Settings', 'notifications_enabled', str(self.notifications_enabled))
        with open(self.config_file, 'w') as config_file:
            self.config.write(config_file)
