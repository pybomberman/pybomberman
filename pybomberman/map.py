BLOCK_OPEN = 0
BLOCK_DESTRUCTIBLE = 1
BLOCK_WALL = 2

MIN_X_SIZE = 3
MAX_X_SIZE = 90
MIN_Y_SIZE = 3
MAX_Y_SIZE = 42

class Map:

    def __init__(self, x, y):

        self.check_map_size(x, y)

    def check_map_size(self, x, y):

        if not x % 3 == 0:
            pass
            # raise exception

        elif not x >= MIN_X_SIZE:
            pass
            # raise exception

        elif not x <= MAX_X_SIZE:
            pass
            # raise exception

        elif not y % 3 == 0:
            pass
            # raise exception

        elif not y % 3 == 0:
            pass
            # raise exception

        elif not y >= MIN_Y_SIZE:
            pass
            # raise exception

        elif not y <= MAX_Y_SIZE:
            pass
            # raise exception

        else:
            return True

    def _generate_map_array(self, x, y):
        pass














