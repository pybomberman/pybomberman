from .exception import MapError

BLOCK_OPEN = 0
BLOCK_DESTRUCTIBLE = 1
BLOCK_WALL = 2

BLOCK_REPR = ('-', '*', 'x')

MIN_X_SIZE = 3
MAX_X_SIZE = 90
MIN_Y_SIZE = 3
MAX_Y_SIZE = 42

###########
#   ******
# x x*x x*x
#
# x x x x x

class Map:


    def __init__(self, x, y):

        self.check_map_size(x, y)
        self._generate_map_array(x, y)


    def check_map_size(self, x, y):

        if not x % 3 == 0:
            raise MapError('Map width should be an integer number multiple of'
                           '3')

        elif not x >= MIN_X_SIZE:
            raise MapError('Map width should be an integer number equal or'
                           'greater than {}'.format(MIN_X_SIZE))

        elif not x <= MAX_X_SIZE:
            raise MapError('Map width should be an integer number lesses or'
                           'equal to {}'.format(MAX_X_SIZE))

        elif not y % 3 == 0:
            raise MapError('Map height should be an integer number multiple of'
                           '3')

        elif not y >= MIN_Y_SIZE:
            raise MapError('Map height should be an integer number equal or'
                           'greater than {}'.format(MIN_X_SIZE))

        elif not y <= MAX_Y_SIZE:
            raise MapError('Map height should be an integer number lesser or'
                           'equal to {}'.format(MAX_Y_SIZE))

        else:
            return True


    def _generate_map_array(self, width, height):

        self.map_no_blocks = '\n'.join([
                             ''.join([self._return_block_type(x, y) for y in range(height)])
                              for x in range(width)])

        #self.meh = [''.join(line) for line in self.map_no_blocks]
        print(self.map_no_blocks)
        #print(self.map_no_blocks)


    def _return_block_type(self, x, y):

        if all((x%2==1, y%2==1)):
            return BLOCK_REPR[BLOCK_WALL]

        else:
            return BLOCK_REPR[BLOCK_OPEN]
