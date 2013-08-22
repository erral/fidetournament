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
