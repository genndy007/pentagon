from core.enum.color import PentaminoColor
from core.enum.collocation import PentaminoCollocation
from core.models.game.pentamino import Pentamino


class Pentaminoes:
    @staticmethod
    def init():
        T = Pentamino(450, 20, PentaminoColor.GREENERY, 'T', PentaminoCollocation.T)
        LADDER = Pentamino(600, 20, PentaminoColor.ROSE, 'LADDER', PentaminoCollocation.LADDER)
        SWAN = Pentamino(750, 20, PentaminoColor.SERENITY, 'SWAN', PentaminoCollocation.SWAN)
        L = Pentamino(900, 20, PentaminoColor.MARSALA, 'L', PentaminoCollocation.L)
        ARC = Pentamino(1050, 20, PentaminoColor.ORCHID, 'ARC', PentaminoCollocation.ARC)
        VERTZIG = Pentamino(1200, 20, PentaminoColor.EMERALD, 'VERTZIG', PentaminoCollocation.VERTZIG)
        RUG = Pentamino(450, 200, PentaminoColor.TANGO, 'RUG', PentaminoCollocation.RUG)
        STAIR = Pentamino(600, 200, PentaminoColor.HONEY, 'STAIR', PentaminoCollocation.STAIR)
        ONE = Pentamino(750, 200, PentaminoColor.TURQ, 'ONE', PentaminoCollocation.ONE)
        ZIGZAG = Pentamino(900, 20, PentaminoColor.MIMOSA, 'ZIGZAG', PentaminoCollocation.ZIGZAG)
        PLUS = Pentamino(1200, 200, PentaminoColor.LILY, 'PLUS', PentaminoCollocation.PLUS)

        return [T, LADDER, SWAN, L, ARC, VERTZIG, RUG, STAIR, ONE, ZIGZAG, PLUS]
