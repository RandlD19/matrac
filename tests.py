# Testni primeri
from satsolver import SatSolver
# Testni primer 1: Zadovoljiv problem
clauses1 = [
    [1, -3, 4],
    [-1, 2, 3],
    [-1, -2, -4],
    [1, -2, 3]
]

# Testni primer 2: Nezadovoljiv problem
clauses2 = [
    [1, 2, 3],
    [-1, -2, -3],
    [1, -2, 3],
    [-1, 2, -3]
]

# Testni primer 3: Zadovoljiv problem
clauses3 = [
    [1, 2, 3],
    [-1, -2, 3],
    [-1, 2, -3],
    [1, -2, -3]
]

clauses4 = [
    [1, 2],
    [-1, -2, 3]
]

clauses5 = [
    [-1, 2],
    [-1, 3]
]

clauses6 = [
    [1, 2, 3],
    [-2, -3]
]

clauses7 = [
    [-1, 3, 4],   # ¬x1 ∨ x3 ∨ x4
    [-2, 6, 4],   # ¬x2 ∨ x6 ∨ x4
    [-2, -6, -3], # ¬x2 ∨ ¬x6 ∨ ¬x3
    [-4, -2],     # ¬x4 ∨ ¬x2
    [2, -3, -1],  # x2 ∨ ¬x3 ∨ ¬x1
    [2, 6, 3],    # x2 ∨ x6 ∨ x3
    [2, -6, -4],  # x2 ∨ ¬x6 ∨ ¬x4
    [1, 5],       # x1 ∨ x5
    [1, 6],       # x1 ∨ x6
    [-6, 3, -5],  # ¬x6 ∨ x3 ∨ ¬x5
    [1, -3, -5]
]

clauses8 = [
    [-1, -2],   # ¬x1 ∨ ¬x2
    [1, -2],    # x1 ∨ ¬x2
    [-1, -3]    # ¬x1 ∨ ¬x3
]

clauses9 = [
    [-1, -2],   # ¬x1 ∨ ¬x2
    [-1, 2],    # ¬x1 ∨ x2
    [1, -2],    # x1 ∨ ¬x2
    [2, -3],    # x2 ∨ ¬x3
    [1, 3]      # x1 ∨ x3
]

clauses10 = [
    [2, 1],     # x2 ∨ x1
    [-1],       # ¬x1
    [-2, -3],   # ¬x2 ∨ ¬x3
    [3, 1]      # x3 ∨ x1
]

clauses11 = [
    [1, -2, 3],      # (x1 ∨ ¬x2 ∨ x3)
    [-1, 2, -3],     # (¬x1 ∨ x2 ∨ ¬x3)
    [2, 4],          # (x2 ∨ x4)
    [-2, -4],        # (¬x2 ∨ ¬x4)
    [1, -3],         # (x1 ∨ ¬x3)
    [3, -5],         # (x3 ∨ ¬x5)
    [1, 4, 5],       # (x1 ∨ x4 ∨ x5)
    [-4, 5],         # (¬x4 ∨ x5)
    [2, 3, -5],      # (x2 ∨ x3 ∨ ¬x5)
    [-1, -2, 3, 5]   # (¬x1 ∨ ¬x2 ∨ x3 ∨ x5)
]

clauses12 = [
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


# assignment4 = set([1, -3])
# assignment5 = set([1, -3])
# assignment6 = set([1, -3])
assignment7 = set()

# solver4 = SatSolver(clauses4)
# solver5 = SatSolver(clauses5)
# solver6 = SatSolver(clauses6)
solver7 = SatSolver(clauses12)
# solver4.assignment = assignment4
# solver5.assignment = assignment5
# solver6.assignment = assignment6
solver7.assignment = assignment7
# simp4 = solver4.simplify()
# simp5 = solver5.simplify()
# simp6 = solver6.simplify()
simp7 = solver7.solve(3)

# print(solver4.clauses)
# print(solver5.clauses)
# print(solver6.clauses)
print(simp7)
print(solver7.assignment)
# print(solver4.clauses)
# solver2 = SatSolver(clauses2)
# solver3 = SatSolver(clauses3)

# print("Testni primer 1:", "Zadovoljiv" if solver1.solve() else "Nezadovoljiv")
# print("Testni primer 2:", "Zadovoljiv" if solver2.solve() else "Nezadovoljiv")
# print("Testni primer 3:", "Zadovoljiv" if solver3.solve() else "Nezadovoljiv")
