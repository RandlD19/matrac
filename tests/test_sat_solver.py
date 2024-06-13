import unittest
from src.clause import Clause
from src.literal import Literal
from src.trail import Trail
from src.variables import Variables
from src.sat_solver import SATSolver

class TestSATSolver(unittest.TestCase):
    def setUp(self):
        self.variables = Variables(6)
        self.clauses = [
            Clause([Literal(1, True, self.variables), Literal(2, True, self.variables), Literal(3, True, self.variables)]),   # (𝑎 ∨ 𝑏 ∨ 𝑐)
            Clause([Literal(1, True, self.variables), Literal(2, True, self.variables), Literal(3, False, self.variables)]),  # (𝑎 ∨ 𝑏 ∨ ¬𝑐)
            Clause([Literal(2, False, self.variables), Literal(4, True, self.variables)]),  # (¬𝑏 ∨ 𝑑)
            Clause([Literal(1, True, self.variables), Literal(2, False, self.variables), Literal(4, False, self.variables)]),  # (𝑎 ∨ ¬𝑏 ∨ ¬𝑑)
            Clause([Literal(1, False, self.variables), Literal(5, True, self.variables), Literal(6, True, self.variables)]),  # (¬𝑎 ∨ 𝑒 ∨ 𝑓)
            Clause([Literal(1, False, self.variables), Literal(5, True, self.variables), Literal(6, False, self.variables)]),  # (¬𝑎 ∨ 𝑒 ∨ ¬𝑓)
            Clause([Literal(5, False, self.variables), Literal(6, False, self.variables)]),  # (¬𝑒 ∨ ¬𝑓)
            Clause([Literal(1, False, self.variables), Literal(5, False, self.variables), Literal(6, True, self.variables)])  # (¬𝑎 ∨ ¬𝑒 ∨ 𝑓)
        ]
        self.solver = SATSolver(input_clauses=[])
        

    def test_solver_1(self):
        self.solver.clauses = self.clauses
        self.solver.variables = self.variables
        result, assignment = self.solver.solve()
        self.assertFalse(result)

    def test_solver_2(self):
        clauses = [
            [1, 6, 7, 8], 
            [2], 
            [3, 5], 
            [4], 
            [9]
        ]
        solver = SATSolver(clauses)
        result, assignment = solver.solve()
        self.assertTrue(result)

    def test_solver_3(self):
        clauses = [
            [1, 6, 7, 8],
            [2,],
            [3, 5],
            [4],
            [9],
            [-2, -3]
        ]
        solver = SATSolver(clauses)
        result, assignment = solver.solve()
        self.assertTrue(result)

    def test_process_input(self):
        clauses_as_lists = [
            [1, 2, 3],  # (𝑎 ∨ 𝑏 ∨ 𝑐)
            [1, 2, -3],  # (𝑎 ∨ 𝑏 ∨ ¬𝑐)
            [-2, 4],  # (¬𝑏 ∨ 𝑑)
            [1, -2, -4],  # (𝑎 ∨ ¬𝑏 ∨ ¬𝑑)
            [-1, 5, 6],  # (¬𝑎 ∨ 𝑒 ∨ 𝑓)
            [-1, 5, -6],  # (¬𝑎 ∨ 𝑒 ∨ ¬𝑓)
            [-5, -6],  # (¬𝑒 ∨ ¬𝑓)
            [-1, -5, 6]  # (¬𝑎 ∨ ¬𝑒 ∨ 𝑓)
        ]

        expected_literals = [
            [Literal(1, True, None), Literal(2, True, None), Literal(3, True, None)],
            [Literal(1, True, None), Literal(2, True, None), Literal(3, False, None)],
            [Literal(2, False, None), Literal(4, True, None)],
            [Literal(1, True, None), Literal(2, False, None), Literal(4, False, None)],
            [Literal(1, False, None), Literal(5, True, None), Literal(6, True, None)],
            [Literal(1, False, None), Literal(5, True, None), Literal(6, False, None)],
            [Literal(5, False, None), Literal(6, False, None)],
            [Literal(1, False, None), Literal(5, False, None), Literal(6, True, None)]
        ]

        clauses = self.solver.process_input(clauses_as_lists)

        self.assertEqual(self.solver.variables.num_vars, 6)

        for clause, expected_literal_list in zip(clauses, expected_literals):
            actual_literals = [Literal(lit.var, lit.is_positive, None) for lit in clause.literals]
            self.assertEqual(actual_literals, expected_literal_list)

    def test_solver_3(self):
        clauses = [
            [13, 15, -5],
            [5, -13, -9],
            [-2, -13, -9],
            [-16, 18, 19],
            [-6, 14, 5],
            [-7, 4, 11],
            [-15, 19, 14],
            [20, -3, -19],
            [-20, -9, -11],
            [2, -6, -10],
            [13, -6, 3],
            [9, 11, -8],
            [-9, -19, 7],
            [-17, -20, 12],
            [-17, 4, -16],
            [20, -5, -7],
            [-10, -4, 11],
            [5, 9, -1],
            [17, -1, 19],
            [-1, -2, -6],
            [15, 17, -19],
            [15, -14, 18],
            [-16, -15, 19],
            [-16, 6, -15],
            [-20, 5, -3],
            [-10, 20, 16],
            [-6, 17, -7],
            [7, 2, -16],
            [-18, 5, 13],
            [-17, 13, 12],
            [-14, -6, -12],
            [14, -2, -9],
            [3, -14, -17],
            [-1, 18, -6],
            [14, -18, -8],
            [7, -3, -19],
            [-18, -20, -5],
            [20, 12, 15],
            [5, 3, 15],
            [16, -6, -18],
            [8, 5, -18],
            [4, 6, -15],
            [6, 3, 4],
            [9, -11, -12],
            [12, 9, 5],
            [4, 18, -8],
            [16, -8, 1],
            [3, 1, -7],
            [15, -9, -4],
            [-5, -3, -10],
            [-16, -12, -19],
            [12, -3, -16],
            [4, -18, -6],
            [5, -7, -3],
            [15, -1, -5],
            [-16, 9, 10],
            [-9, 17, 5],
            [-2, 4, 10],
            [16, 9, -11],
            [1, -7, -15],
            [-20, -8, 3],
            [3, 9, 17],
            [-11, 9, 6],
            [8, 16, 19],
            [2, 8, -3],
            [-5, 15, 18],
            [1, 16, 2],
            [-18, -11, -9],
            [5, 7, -12],
            [-13, -10, 20],
            [11, -20, 1],
            [-13, 19, 2],
            [17, -3, 15],
            [-2, 4, 13],
            [5, -19, 12],
            [-12, -5, 7],
            [19, -4, 2],
            [-5, -14, 10],
            [-6, -1, -12],
            [20, -18, -11],
            [14, 16, 4],
            [5, 12, -10],
            [10, 3, -6],
            [-15, -3, 5],
            [12, -13, -1],
            [20, -9, -8],
            [-10, 18, -6],
            [16, 12, -18],
            [-14, 15, -2],
            [3, 19, 10],
            [15, 20, 13]
        ]
        solver = SATSolver(clauses)
        result, assignment = solver.solve()
        print(", ".join(map(str,sorted(assignment.literals, key=lambda x:abs(x.var)))))
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()