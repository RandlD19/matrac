from collections import Counter

class SatSolver:
    def __init__(self):
        self.model = []

    def dpll(self, clauses, assignment):
        if not clauses:
            self.model = assignment
            return True
        if any([not clause for clause in clauses]):
            return False
        
        variable = self.select_unassigned_variable(clauses)
        
        new_clauses = self.simplify(clauses, variable)
        if self.dpll(new_clauses, assignment + [variable]):
            return True
        
        new_clauses = self.simplify(clauses, -variable)
        if self.dpll(new_clauses, assignment + [-variable]):
            return True
        
        return False
    
    def select_unassigned_variable_moms(self, clauses):
        literal_count = Counter()
        min_size = float('inf')
        
        for clause in clauses:
            if len(clause) < min_size:
                min_size = len(clause)
        
        for clause in clauses:
            if len(clause) == min_size:
                for literal in clause:
                    literal_count[literal] += 1
        
        most_common = literal_count.most_common(1)
        return abs(most_common[0][0]) if most_common else None
    
    def simplify(self, clauses, literal):
        new_clauses = []
        for clause in clauses:
            if literal in clause:
                continue
            new_clause = [x for x in clause if x != -literal]
            new_clauses.append(new_clause)
        return new_clauses
    
    def solve(self, clauses):
        self.model = []
        return self.dpll(clauses, [])
    
    def get_model(self):
        return self.model