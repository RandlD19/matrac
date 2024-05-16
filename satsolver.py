class SatSolver:
    def __init__(self, clauses):
        self.clauses = [clause[:] for clause in clauses]
        self.assignment = set()

    def unit_propagate(self):
        changed = True
        while changed:
            changed = False
            unit_clauses = [c for c in self.clauses if len(c) == 1]
            for unit in unit_clauses:
                literal = unit[0]
                if -literal in self.assignment:
                    return False
                if literal not in self.assignment:
                    self.assignment.add(literal)
                    self.clauses = [c for c in self.clauses if literal not in c]
                    for c in self.clauses:
                        if -literal in c:
                            c.remove(-literal)
                    changed = True
        return True

    def choose_literal(self):
        for clause in self.clauses:
            for literal in clause:
                return literal
        return None

    def dpll(self):
        if not self.unit_propagate():
            return False

        if not self.clauses:
            return True

        literal = self.choose_literal()
        if literal is None:
            return False

        solver_with_literal = SatSolver([clause[:] for clause in self.clauses])
        solver_with_literal.assignment = self.assignment.copy()
        solver_with_literal.assignment.add(literal)
        if solver_with_literal.dpll():
            self.assignment = solver_with_literal.assignment
            return True

        solver_with_neg_literal = SatSolver([clause[:] for clause in self.clauses])
        solver_with_neg_literal.assignment = self.assignment.copy()
        solver_with_neg_literal.assignment.add(-literal)
        if solver_with_neg_literal.dpll():
            self.assignment = solver_with_neg_literal.assignment
            return True

        return False

    def solve(self):
        return self.dpll()

# Testni primeri

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

solver1 = SatSolver(clauses1)
# solver2 = SatSolver(clauses2)
# solver3 = SatSolver(clauses3)

print("Testni primer 1:", "Zadovoljiv" if solver1.solve() else "Nezadovoljiv")
# print("Testni primer 2:", "Zadovoljiv" if solver2.solve() else "Nezadovoljiv")
# print("Testni primer 3:", "Zadovoljiv" if solver3.solve() else "Nezadovoljiv")
