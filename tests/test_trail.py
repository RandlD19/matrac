import unittest

from src.literal import Literal
from src.clause import Clause
from src.trail import Trail
from src.variables import Variables

class TestTrail(unittest.TestCase):
    def setUp(self):
        self.variables = Variables(3)
        self.trail = Trail(self.variables)
        
        # Dodamo literale v trail kot je podano v primeru
        self.literal1 = Literal(1, True, self.variables)
        self.literal2 = Literal(2, False, self.variables)
        self.literal3 = Literal(3, True, self.variables)

        self.trail.add_decision_literal(self.literal1)  # 1 na decision_level=1
        self.trail.add_decision_literal(self.literal2)  # ¬2 na decision_level=2
        self.trail.add_propagation_literal(self.literal3)  # 3 na decision_level=2

    def test_add_decision_literal(self):
        self.assertEqual(len(self.trail.literals), 3)
        self.assertEqual(self.trail.current_decision_level(), 2)
        self.assertTrue(self.variables.is_assigned(1))
        self.assertEqual(self.variables.get_decision_level(1), 1)

    def test_add_propagation_literal(self):
        self.assertTrue(self.variables.is_assigned(2))
        self.assertEqual(self.variables.get_decision_level(2), 2)

    def test_backtrack(self):
        self.trail.backtrack(1)
        self.assertEqual(len(self.trail.literals), 1)
        self.assertEqual(self.trail.current_decision_level(), 1)
        self.assertFalse(self.variables.is_assigned(2))
        self.assertFalse(self.variables.is_assigned(3))

    def test_analyze_conflict(self):
        # Konfliktna klavzula [1, 2, -3]
        conflict_clause = Clause([
            Literal(1, True, self.variables),
            Literal(2, True, self.variables),
            Literal(3, False, self.variables)
        ])

        # Kličemo analyze_conflict
        learned_clause, backtrack_level = self.trail.analyze_conflict(conflict_clause)

        # Preverimo rezultate
        expected_clause = Clause([
            Literal(1, True, self.variables),
            Literal(2, True, self.variables)
        ])
        expected_backtrack_level = 1

        # Primerjamo literale v naučeni klavzuli in pričakovano naučeno klavzulo
        self.assertCountEqual([str(lit) for lit in learned_clause.literals], [str(lit) for lit in expected_clause.literals])
        self.assertEqual(backtrack_level, expected_backtrack_level)

    # Robni primeri
    def test_backtrack_to_level_zero(self):
        self.trail.backtrack(0)
        self.assertEqual(len(self.trail.literals), 0)
        self.assertEqual(self.trail.current_decision_level(), 0)
        self.assertFalse(self.variables.is_assigned(1))
        self.assertFalse(self.variables.is_assigned(2))
        self.assertFalse(self.variables.is_assigned(3))

    def test_analyze_conflict_empty_clause(self):
        conflict_clause = Clause([])
        learned_clause, backtrack_level = self.trail.analyze_conflict(conflict_clause)
        self.assertEqual(len(learned_clause.literals), 0)
        self.assertEqual(backtrack_level, 0)

if __name__ == '__main__':
    unittest.main()
