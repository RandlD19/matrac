import unittest

from src.variables import Variables

class TestVariables(unittest.TestCase):
    def setUp(self):
        self.vars = Variables(5)
        
    def test_initialization(self):
        for var in range(1, 6):
            self.assertIsNone(self.vars.get_value(var))
            self.assertIsNone(self.vars.get_decision_level(var))
            self.assertIsNone(self.vars.get_antecedent_clause(var))

    def test_assign_and_get(self):
        self.vars.assign(1, True, 1, [(2, False)])
        self.assertTrue(self.vars.is_assigned(1))
        self.assertEqual(self.vars.get_value(1), True)
        self.assertEqual(self.vars.get_decision_level(1), 1)
        self.assertEqual(self.vars.get_antecedent_clause(1), [(2, False)])

    def test_unassign(self):
        self.vars.assign(1, True, 1, [(2, False)])
        self.vars.unassign(1)
        self.assertFalse(self.vars.is_assigned(1))
        self.assertIsNone(self.vars.get_value(1))
        self.assertIsNone(self.vars.get_decision_level(1))
        self.assertIsNone(self.vars.get_antecedent_clause(1))

    def test_reassign(self):
        self.vars.assign(1, True, 1, [(2, False)])
        self.vars.assign(1, False, 2, [(3, True)])
        self.assertTrue(self.vars.is_assigned(1))
        self.assertEqual(self.vars.get_value(1), False)
        self.assertEqual(self.vars.get_decision_level(1), 2)
        self.assertEqual(self.vars.get_antecedent_clause(1), [(3, True)])

    def test_get_value(self):
        self.vars.assign(1, True, 1, [(2, False)])
        self.assertEqual(self.vars.get_value(1), True)
        self.assertIsNone(self.vars.get_value(2))

    def test_get_decision_level(self):
        self.vars.assign(1, True, 1, [(2, False)])
        self.assertEqual(self.vars.get_decision_level(1), 1)
        self.assertIsNone(self.vars.get_decision_level(2))

    def test_get_antecedent_clause(self):
        self.vars.assign(1, True, 1, [(2, False)])
        self.assertEqual(self.vars.get_antecedent_clause(1), [(2, False)])
        self.assertIsNone(self.vars.get_antecedent_clause(2))

    # Robni primeri
    def test_unassigned_variable(self):
        self.assertFalse(self.vars.is_assigned(4))
        self.assertIsNone(self.vars.get_value(4))
        self.assertIsNone(self.vars.get_decision_level(4))
        self.assertIsNone(self.vars.get_antecedent_clause(4))

    def test_assign_no_antecedent(self):
        self.vars.assign(3, True, 1)
        self.assertTrue(self.vars.is_assigned(3))
        self.assertEqual(self.vars.get_value(3), True)
        self.assertEqual(self.vars.get_decision_level(3), 1)
        self.assertIsNone(self.vars.get_antecedent_clause(3))

if __name__ == '__main__':
    unittest.main()
