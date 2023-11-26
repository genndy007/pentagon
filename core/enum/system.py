class StaticPath:
    _BASE_DIR = 'static'
    FONT = _BASE_DIR + '/fonts/menu.ttf'
    ICON = _BASE_DIR + '/icons/icon.png'
    HELP = _BASE_DIR + '/text/help.txt'


class SavePath:
    _BASE_DIR = 'bin/saves'
    FILE = _BASE_DIR + '/save.dat'


class WindowParams:
    WIDTH = 1350
    HEIGHT = 768
    FPS = 60
    MIN_BORDER_CORNER = 20
    MAX_BORDER_CORNER = 361
