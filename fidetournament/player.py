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
        sr = '{: 3}'.format(self.startrank)
        sex = self.sex
        title = '{: 2}'.format(self.title)
        name = '{: 32}'.format(self.name)
        fide = '{: 4}'.format(self.fide)
        fed = '{: 3}'.format(self.fed)
        id = '{: 10}'.format(self.id)
        birthdate = '{: 10}'.format(self.birthdate)
        points = '{: 3}'.format(self.points)
        rank = '{: 3}'.format(self.rank)
        opponents = []
        for opponent in sorted(self.opponents, lambda x,y:cmp(x.get('round'), y.get('round'))):
            opponent_str = ''
            id = '{: 4}'.format(opponent.get('id'))
            color = opponent.get('color')
            result = opponent.get('result')

            opponent_str = ' '.join([id, color, result])
            opponents.append(opponent_str)

        return ' '.join([
            '001',
            sr,
            sex,
            title,
            name,
            fide,
            fed,
            id,
            birthdate,
            points,
            rank,
            opponent_str
        ])
