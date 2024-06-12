class Clause:
    def __init__(self, literals):
        self.literals = literals

    def is_satisfied(self):
        return any([literal.is_satisfied() for literal in self.literals])

    def __str__(self):
        return " ∨ ".join(str(literal) for literal in self.literals)
