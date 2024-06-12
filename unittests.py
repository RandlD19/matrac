import unittest
from cdcl import *

class TestTrail(unittest.TestCase):

    def setUp(self):
        literal1 = Literal(1, decision_level=1, determined_by=0)
        literal2 = Literal(2, decision_level=2, determined_by=0)
        self.trail = Trail()

    def test_add_literal(self):
        literal1 = Literal(1, decision_level=1, determined_by=0)
        literal2 = Literal(2, decision_level=2, determined_by=0)
        trail = Trail()