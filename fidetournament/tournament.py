# -*- coding: utf-8 -*-

from .player import Player
from six import StringIO


class Tournament(object):
    """ Base class for saving tournament data
    """

    def __init__(self):
        self.name = u''
        self.city = u''
        self.federation = u''
        self.startdate = u''
        self.enddate = u''
        self.numplayers = 0
        self.numratedplayers = 0
        self.numteams = 0  # unsupported yet
        self.type = 0
        self.chiefarbiter = u''
        self.deputyarbiters = u''
        self.rateofplay = u''
        self.rounddates = []
        self.players = []
        self.teams = []

    def parse(self, filename=''):
        """ create a Tournament object based on a TRF file """
        fp = open(filename, 'r')
        for line in fp.readlines():
            # check for tournament data
            data = line[4:].strip()
            if line.startswith('012 '):
                self.name = data
            elif line.startswith('022 '):
                self.city = data
            elif line.startswith('032 '):
                self.federation = data
            elif line.startswith('042 '):
                self.startdate = data
            elif line.startswith('052 '):
                self.enddate = data
            elif line.startswith('062 '):
                self.numplayers = int(data)
            elif line.startswith('072 '):
                self.numratedplayers = int(data)
            elif line.startswith('082 '):
                self.numteams = int(data)
            elif line.startswith('092 '):
                self.type = data
            elif line.startswith('102 '):
                self.chiefarbiter = data
            elif line.startswith('112 '):
                self.deputyarbiters = data
            elif line.startswith('122 '):
                self.rateofplay = data
            elif line.startswith('132 '):
                self.rounddates = self.string_groupper(data, 10)
            elif line.startswith('001 '):
                player = self.parse_player(line)
                self.players.append(player)

            elif line.startswith('013 '):
                team = self.parse_team(data)
                self.teams.append(team)

        fp.close()

    def parse_player(self, line):
        player = Player()
        player.startrank = line[4:8].strip()
        player.sex = line[9].strip()
        player.title = line[10:13].strip()
        player.name = line[14:47].strip()
        player.fide = line[48:52].strip()
        player.fed = line[53:56].strip()
        player.id = line[57:68].strip()
        player.birthdate = line[69:79].strip()
        player.points = line[80:84].strip()
        player.rank = line[85:89].strip()
        opponent_data = line[91:].rstrip()
        opponent_list = self.string_groupper(opponent_data, 10)
        player.opponents = self.parse_opponent_list(opponent_list)
        return player

    def parse_opponent_list(self, opponent_list):
        opponents = []
        roundnumber = 1
        for opponent in opponent_list:
            data = {}
            data['id'] = opponent and opponent[:4] or None
            data['color'] = opponent and opponent[5] or None
            data['result'] = opponent and opponent[7] or None
            data['round'] = roundnumber
            roundnumber = roundnumber + 1
            opponents.append(data)
        return opponents

    def parse_team(self, data):
        pass

    def serialize(self):
        """ serialize Tournament information to a TRF file """
        raise NotImplementedError

    def string_groupper(self, lst, n):
        """ group string in n sized substrings """
        def group(lst, n):
            return zip(*[lst[i::n] for i in range(n)])

        items = group(lst, n)
        ret = []
        for item in items:
            ret.append(''.join(item).rstrip())

        return ret

    def __repr__(self):
        return '%s (%s) from %s to %s' % (self.name,
          self.federation,
          self.startdate,
          self.enddate)

    def create_trf_file(self, extra_XX_fields=[]):
        """ output TRF file, with extra XX fields if
            asked
        """
        out = StringIO()
        out.write('012 %s' % self.name)
        out.write('\n')
        out.write('022 %s' % self.city)
        out.write('\n')
        out.write('032 %s' % self.federation)
        out.write('\n')
        out.write('042 %s' % self.startdate)
        out.write('\n')
        out.write('052 %s' % self.enddate)
        out.write('\n')
        out.write('062 %s' % self.numplayers)
        out.write('\n')
        out.write('072 %s' % self.numratedplayers)
        out.write('\n')
        out.write('082 %s' % self.numteams)
        out.write('\n')
        out.write('092 %s' % self.type)
        out.write('\n')
        out.write('102 %s' % self.chiefarbiter)
        out.write('\n')
        out.write('112 %s' % self.deputyarbiters)
        out.write('\n')
        out.write('122 %s' % self.rateofplay)
        out.write('\n')
        for player in self.players:
            out.write(player.create_trf_line())
            out.write('\n')

        for field, value in extra_XX_fields.items():
            out.write('%s %s' % (field, value))
            out.write('\n')

        return out.getvalue()
