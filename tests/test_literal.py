import unittest
from src.literal import Literal
from src.variables import Variables

class TestLiteral(unittest.TestCase):
    def setUp(self):
        self.variables = Variables(3)
        self.literal1 = Literal(1, True, self.variables)
        self.literal2 = Literal(2, False, self.variables)
        self.literal3 = Literal(3, True, self.variables)

    def test_assignment(self):
        self.literal1.assignment = True
        self.literal1.decision_level = 1
        self.assertTrue(self.variables.get_value(1))
        self.assertEqual(self.variables.get_decision_level(1), 1)

        self.literal2.assignment = False
        self.literal2.decision_level = 2
        self.assertFalse(self.variables.get_value(2))
        self.assertEqual(self.variables.get_decision_level(2), 2)

    def test_unassign(self):
        self.literal1.assignment = True
        self.literal1.decision_level = 1
        self.literal1.unassign()
        self.assertFalse(self.literal1.is_assigned)
        self.assertIsNone(self.variables.get_value(1))
        self.assertIsNone(self.variables.get_decision_level(1))

    def test_antecedent_clause(self):
        self.literal1.assignment = True
        self.literal1.decision_level = 1
        antecedent_clause = [(2, False), (3, True)]
        self.literal1.antecedent_clause = antecedent_clause
        self.assertEqual(self.variables.get_antecedent_clause(1), antecedent_clause)

    # Robni primeri
    def test_get_complement(self):
        complement = self.literal1.get_complement()
        self.assertEqual(complement.var, self.literal1.var)
        self.assertNotEqual(complement.is_positive, self.literal1.is_positive)

    def test_is_complementary(self):
        complement = self.literal1.get_complement()
        self.assertTrue(self.literal1.is_complementary(complement))
        self.assertFalse(self.literal1.is_complementary(self.literal2))

if __name__ == '__main__':
    unittest.main()
