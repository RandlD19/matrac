from src.literal import Literal
class Clause:
    def __init__(self, literals, learned_clause=False, delete=True):
        self.literals = literals
        self.learned_clause = learned_clause
        self.delete = delete
        self.watch1 = literals[0] if len(literals) > 0 else None
        self.watch2 = literals[1] if len(literals) > 1 else self.watch1

    def __contains__(self, literal):
        return literal in self.literals

    def is_satisfied(self):
        return any([literal.is_satisfied() for literal in self.literals])
    
    def is_falsified(self):
        return all([literal.is_falsified() for literal in self.literals])

    def __str__(self):
        return " ∨ ".join(str(literal) for literal in self.literals)
    
    def __repr__(self):
        return " ∨ ".join(str(literal) for literal in self.literals)
