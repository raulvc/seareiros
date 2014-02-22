# -*- coding: UTF-8 -*-

import logging
import ConfigParser
import io

logger = logging.getLogger('settings')

class SettingsParser():
    """
        reads settings from .ini file
    """
    def __init__(self):
        self.log = logging.getLogger('SettingsParser')
        self._config = ConfigParser.RawConfigParser()
        if ( len(self._config.read('settings.ini')) == 0 ):
            defaults = """[Database]\nhostname = localhost
            """
            self._config.readfp(io.BytesIO(defaults))
            try:
                with open('settings.ini', 'wb') as configfile:
                    self._config.write(configfile)
            except IOError as e:
                self.log.error("I/O error({0}): {1}".format(e.errno, e.strerror))

    def get_value(self, section, option):
        return self._config.get(section, option)

