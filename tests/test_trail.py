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

    def test_analyze_conflict_1(self):
        variables = Variables(3)
        trail = Trail(variables)

        antecedent_clause = Clause([
            Literal(1, True, variables),
            Literal(2, True, variables),
            Literal(3, True, variables),
        ])

        trail.add_decision_literal(Literal(1, False, variables))  # 1 na decision_level=1
        trail.add_decision_literal(Literal(2, False, variables))  # ¬2 na decision_level=2
        trail.add_propagation_literal(Literal(3, True, variables), antecedent_clause)  # 3 na decision_level=2

        conflict_clause = Clause([
            Literal(1, True, variables),
            Literal(2, True, variables),
            Literal(3, False, variables)
        ])

        learned_clause, backtrack_level = trail.analyze_conflict(conflict_clause)

        # Preverimo rezultate
        expected_clause = Clause([
            Literal(1, True, self.variables),
            Literal(2, True, self.variables)
        ])
        expected_backtrack_level = 1

        self.assertCountEqual([str(lit) for lit in learned_clause.literals], [str(lit) for lit in expected_clause.literals])
        self.assertEqual(str(learned_clause), str(expected_clause))
        self.assertEqual(backtrack_level, expected_backtrack_level)

    def test_analyze_conflict_2(self):

        variables = Variables(12)

        clause1 = Clause([Literal(1, False, variables), Literal(2, False, variables)])  # (¬𝑥1 ∨ ¬𝑥2)
        clause2 = Clause([Literal(1, False, variables), Literal(3, True, variables)])   # (¬𝑥1 ∨ 𝑥3)
        clause3 = Clause([Literal(3, False, variables), Literal(4, False, variables)])  # (¬𝑥3 ∨ ¬𝑥4)
        clause4 = Clause([Literal(2, True, variables), Literal(4, True, variables), Literal(5, True, variables)])  # (𝑥2 ∨ 𝑥4 ∨ 𝑥5)
        clause5 = Clause([Literal(5, False, variables), Literal(6, True, variables), Literal(7, False, variables)])  # (¬𝑥5 ∨ 𝑥6 ∨ ¬𝑥7)
        clause6 = Clause([Literal(2, True, variables), Literal(7, True, variables), Literal(8, True, variables)])  # (𝑥2 ∨ 𝑥7 ∨ 𝑥8)
        clause7 = Clause([Literal(8, False, variables), Literal(9, False, variables)])  # (¬𝑥8 ∨ ¬𝑥9)
        clause8 = Clause([Literal(8, False, variables), Literal(10, True, variables)])  # (¬𝑥8 ∨ 𝑥10)
        clause9 = Clause([Literal(9, True, variables), Literal(10, False, variables), Literal(11, True, variables)])  # (𝑥9 ∨ ¬𝑥10 ∨ 𝑥11)
        clause10 = Clause([Literal(10, False, variables), Literal(12, False, variables)])  # (¬𝑥10 ∨ ¬𝑥12)
        clause11 = Clause([Literal(11, False, variables), Literal(12, True, variables)])  # (¬𝑥11 ∨ 𝑥12)

        trail = Trail(variables)

        trail.add_decision_literal(Literal(1, True, variables))  # Decision level 1
        trail.add_propagation_literal(Literal(2, False, variables), clause1)  # (¬𝑥1 ∨ ¬𝑥2)
        trail.add_propagation_literal(Literal(3, True, variables), clause2)  # (¬𝑥1 ∨ 𝑥3)
        trail.add_propagation_literal(Literal(4, False, variables), clause3)  # (¬𝑥3 ∨ ¬𝑥4)
        trail.add_propagation_literal(Literal(5, True, variables), clause4)  # (𝑥2 ∨ 𝑥4 ∨ 𝑥5)
        trail.add_decision_literal(Literal(6, False, variables))  # Decision level 2
        trail.add_propagation_literal(Literal(7, False, variables), clause5)  # (¬𝑥5 ∨ 𝑥6 ∨ ¬𝑥7)
        trail.add_propagation_literal(Literal(8, True, variables), clause6)  # (𝑥2 ∨ 𝑥7 ∨ 𝑥8)
        trail.add_propagation_literal(Literal(9, False, variables), clause7)  # (¬𝑥8 ∨ ¬𝑥9)
        trail.add_propagation_literal(Literal(10, True, variables), clause8)  # (¬𝑥8 ∨ 𝑥10)
        trail.add_propagation_literal(Literal(11, True, variables), clause9)  # (𝑥9 ∨ ¬𝑥10 ∨ 𝑥11)
        trail.add_propagation_literal(Literal(12, False, variables), clause10)  # (¬𝑥10 ∨ ¬𝑥12)

        conflict_clause = clause11
        learned_clause, backtrack_level = trail.analyze_conflict(conflict_clause)

        expected_clause = Clause([
            Literal(8, False, self.variables)
        ])
        expected_backtrack_level = 0
        self.assertCountEqual([str(lit) for lit in learned_clause.literals], [str(lit) for lit in expected_clause.literals])
        self.assertEqual(str(learned_clause), str(expected_clause))
        self.assertEqual(backtrack_level, expected_backtrack_level)

    def test_analyze_conflict_3(self):
        variables = Variables(4) 
        clause1 = Clause([Literal(1, True, variables), Literal(2, True, variables)])  # (𝑎 ∨ 𝑏)
        clause2 = Clause([Literal(2, False, variables), Literal(4, True, variables)])  # (¬𝑏 ∨ 𝑑)
        trail = Trail(variables)

        trail.add_decision_literal(Literal(1, False, variables))  # ¬𝑎, Decision level 1
        trail.add_propagation_literal(Literal(2, True, variables), clause1)  # 𝑏, (𝑎 ∨ 𝑏)
        trail.add_propagation_literal(Literal(4, True, variables), clause2)  # 𝑑, (¬𝑏 ∨ 𝑑)

        conflict_clause = Clause([Literal(1, True, variables), Literal(2, False, variables), Literal(4, False, variables)])  # (𝑎 ∨ ¬𝑏 ∨ ¬𝑑)

        learned_clause, backtrack_level = trail.analyze_conflict(conflict_clause)

        # Preverimo rezultate
        expected_clause = Clause([
            Literal(1, True, self.variables)
        ])
        expected_backtrack_level = 0

        self.assertCountEqual([str(lit) for lit in learned_clause.literals], [str(lit) for lit in expected_clause.literals])
        self.assertEqual(str(learned_clause), str(expected_clause))
        self.assertEqual(backtrack_level, expected_backtrack_level)

    def test_analyze_conflict_4(self):
        variables = Variables(6)  
        clause1 = Clause([Literal(1, False, variables), Literal(5, True, variables), Literal(6, True, variables)])  # (¬𝑎 ∨ 𝑒 ∨ 𝑓)
        clause2 = Clause([Literal(1, False, variables), Literal(5, True, variables), Literal(6, False, variables)])  # (¬𝑎 ∨ 𝑒 ∨ ¬𝑓)

        trail = Trail(variables)

        trail.add_propagation_literal(Literal(1, True, variables), Clause([Literal(1, True, variables)]))  # 𝑎, (𝑎)
        trail.add_decision_literal(Literal(5, False, variables))  # ¬𝑒, Decision level 1
        trail.add_propagation_literal(Literal(6, True, variables), clause1)  # 𝑓, (¬𝑎 ∨ 𝑒 ∨ 𝑓)

        conflict_clause = Clause([Literal(1, False, variables), Literal(5, True, variables), Literal(6, False, variables)])  # (¬𝑎 ∨ 𝑒 ∨ ¬𝑓)
        learned_clause, backtrack_level = trail.analyze_conflict(conflict_clause)
        # Preverimo rezultate
        expected_clause = Clause([
            Literal(5, True, self.variables)
        ])
        expected_backtrack_level = 0

        self.assertCountEqual([str(lit) for lit in learned_clause.literals], [str(lit) for lit in expected_clause.literals])
        self.assertEqual(str(learned_clause), str(expected_clause))
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
