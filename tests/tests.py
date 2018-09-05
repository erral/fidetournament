from fidetournament.tournament import Tournament

import os
import unittest

class TestTournament(unittest.TestCase):

    def build_path_to_file(self, filepath):
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), filepath)

    def test_parse(self):
        t = Tournament()
        t.parse(self.build_path_to_file('test_demo.trf'))
        self.assertNotEqual(len(t.players), 0)
