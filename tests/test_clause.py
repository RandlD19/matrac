import unittest

from src.literal import Literal
from src.clause import Clause
from src.variables import Variables

class TestClause(unittest.TestCase):
    def setUp(self):
        self.variables = Variables(3)
        self.literal1 = Literal(1, True, self.variables)
        self.literal2 = Literal(2, False, self.variables)
        self.literal3 = Literal(3, True, self.variables)
        self.clause = Clause([self.literal1, self.literal2, self.literal3])

    def test_is_satisfied(self):
        self.assertFalse(self.clause.is_satisfied())
        
        self.literal1.assignment = True
        self.assertTrue(self.clause.is_satisfied())

        self.literal1.unassign()
        self.literal2.assignment = False
        self.assertTrue(self.clause.is_satisfied())

        self.literal2.unassign()
        self.literal3.assignment = True
        self.assertTrue(self.clause.is_satisfied())

    def test_str(self):
        self.assertEqual(str(self.clause), "1 ∨ -2 ∨ 3")

    # Robni primeri
    def test_empty_clause(self):
        empty_clause = Clause([])
        self.assertFalse(empty_clause.is_satisfied())

    def test_single_literal_clause(self):
        single_literal_clause = Clause([self.literal1])
        self.assertFalse(single_literal_clause.is_satisfied())
        self.literal1.assignment = True
        self.assertTrue(single_literal_clause.is_satisfied())

if __name__ == '__main__':
    unittest.main()
