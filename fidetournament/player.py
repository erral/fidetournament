class Player(object):
    def __init__(self):
        self.startrank = 0
        self.sex = 'm'
        self.title = ''
        self.name = ''
        self.fide = 0
        self.fed = ''
        self.id = ''
        self.birthdate = ''
        self.points = ''
        self.rank = ''

    def __repr__(self):
        return '%s (%s) FIDE-ID: %s FIDE-Rat: %s' % (self.name,
            self.fed,
            self.id,
            self.fide
        )

    def create_trf_line(self):
        """
                  1         2         3         4         5         6         7
         1234567890123456789012345678901234567890123456789012345678901234567890
        """
        return ''

        # player.startrank = line[4:8].strip()
        # player.sex = line[9].strip()
        # player.title = line[10:13].strip()
        # player.name = line[14:47].strip()
        # player.fide = line[48:52].strip()
        # player.fed = line[53:56].strip()
        # player.id = line[57:68].strip()
        # player.birthdate = line[69:79].strip()
        # player.points = line[80:84].strip()
        # player.rank = line[85:89].strip()
        # opponent_data = line[91:].rstrip()
        # opponent_list = self.string_groupper(opponent_data, 10)
        # player.opponents = self.parse_opponent_list(opponent_list)
