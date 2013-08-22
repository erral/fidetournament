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

    def parse(self, filename=''):
        """ create a Tournament object based on a TRF file """
        fp = open(filename, 'r')
        for line in fp.readlines():
            # check for tournament data
            data = line[:4].strip()
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



        fp.close()

    def serialize(self):
        """ serialize Tournament information to a TRF file """
        raise NotImplementedError
