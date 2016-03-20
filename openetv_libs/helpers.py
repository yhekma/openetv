from ConfigParser import ConfigParser
import sys


class OpenError(Exception):
    def __init__(self, msg):
        print msg
        sys.exit(2)


def get_config(config_file):
    config_obj = ConfigParser()
    config_obj.read(config_file)
    config = {}

    for section in config_obj.sections():
        for item in config_obj.items(section):
            val = item[1]
            try:
                config[section][item[0]] = val
            except KeyError:
                config[section] = {item[0]: val}

    return config


def open_file(path, mode, errormsg):
    try:
        return open(path, mode)
    except IOError:
        raise OpenError(errormsg)
