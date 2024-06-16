import unittest
from src.clause import Clause
from src.literal import Literal
from src.two_watched_literals import TwoWatchedLiterals

class TestTwoWatchedLiterals(unittest.TestCase):
    def setUp(self):
        self.twl = TwoWatchedLiterals()

    def test_add_clause(self):
        clause = Clause([Literal(1, True, None), Literal(2, True, None)])
        self.twl.add_clause(clause)
        self.assertIn(clause, self.twl.get_clauses(Literal(1, True, None)))
        self.assertIn(clause, self.twl.get_clauses(Literal(2, True, None)))

    def test_update_watch(self):
        clause = Clause([Literal(1, True, None), Literal(2, True, None)])
        self.twl.add_clause(clause)
        self.twl.update_watch(clause, Literal(1, True, None), Literal(3, True, None))
        self.assertNotIn(clause, self.twl.get_clauses(Literal(1, True, None)))
        self.assertIn(clause, self.twl.get_clauses(Literal(3, True, None)))

    def test_remove_clause(self):
        clause = Clause([Literal(1, True, None), Literal(2, True, None)])
        self.twl.add_clause(clause)
        self.twl.remove_clause(clause)
        self.assertNotIn(clause, self.twl.get_clauses(Literal(1, True, None)))
        self.assertNotIn(clause, self.twl.get_clauses(Literal(2, True, None)))

if __name__ == '__main__':
    unittest.main()