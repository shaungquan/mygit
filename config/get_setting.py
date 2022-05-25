import configparser
import os
def get_ini(lisename):
    conf = configparser.ConfigParser()
    curpath = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(curpath, 'setting.ini')
    conf.read(path, encoding="utf-8")
    value = dict(conf.items(lisename))
    return value