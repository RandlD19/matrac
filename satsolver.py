class SatSolver:
    def __init__(self, clauses):
        self.clauses = [clause[:] for clause in clauses]
        self.assignment = set()
        self.counter = self.count_occurrences()
        self.conflict_counter = self.init_conflict_counter()

    def init_conflict_counter(self):
        conflict_counter = {}
        for clause in self.clauses:
            for literal in clause:
                if literal not in conflict_counter:
                    conflict_counter[literal] = 0
        return conflict_counter

    def count_occurrences(self):
        counter = {}
        for clause in self.clauses:
            for literal in clause:
                var = abs(literal)
                if var not in counter:
                    counter[var] = [0, 0]
                if literal > 0:
                    counter[var][0] += 1
                else:
                    counter[var][1] += 1
        return counter

    def update_counter(self, clause):
        for literal in clause:
            if literal > 0:
                self.counter[literal][0] -= 1
            else:
                self.counter[-literal][1] -= 1

    def update_conflict_counter(self, clause):
        for literal in clause:
            if literal > 0:
                self.counter[literal][0] += 1
            else:
                self.counter[-literal][1] += 1

    def simplify_clause(self, clause):
        clause_copy = clause.copy()
        for literal in clause_copy:
            if literal > 0:
                if literal in self.assignment:
                    self.update_counter(clause)
                    return True
                elif -literal in self.assignment:
                    clause.remove(literal)
                    self.counter[literal][0] -= 1
            else:
                if literal in self.assignment:
                    self.update_counter(clause)
                    return True
                elif -literal in self.assignment:
                    clause.remove(literal)
                    self.counter[-literal][1] -= 1
        if clause == []:
            return False
        return clause

    def simplify(self):
        new_clauses = []
        for clause in self.clauses:
            new_clause = self.simplify_clause(clause)
            if new_clause == False:
                self.clauses = []
                self.update_conflict_counter(clause)
                return False
            if new_clause != True:
                new_clauses.append(new_clause)
        self.clauses = new_clauses
        if self.clauses == []:
            return True

    def unit_propagate(self):
        changed = True
        while changed:
            changed = False
            unit_clauses = [c for c in self.clauses if len(c) == 1]
            for unit in unit_clauses:
                literal = unit[0]
                if literal is False:
                    return False
                if -literal in self.assignment:
                    return False
                if literal not in self.assignment:
                    self.assignment.add(literal)
                    simplified = self.simplify()
                    if simplified == True:
                        return True
                    elif simplified == False:
                        return False
                    changed = True
        return True

    def choose_literal(self):
        for i in self.counter.keys():
            if i not in self.assignment and self.counter[i] != [0, 0]:
                return i
        return None
    
    def choose_literal_vsids(self):
        filtered_counter = {k: v for k, v in self.conflict_counter.items() if k not in self.assignment}
        if not filtered_counter:
            return None
        max_literal = max(filtered_counter.items(), key=lambda item: item[1])
        return max_literal[0]
    
    def find_pure_literal(self):
        for literal, counts in self.counter.items():
            if counts[0] > 0 and counts[1] == 0:
                return literal
            elif counts[1] > 0 and counts[0] == 0:
                return -literal

    def dpll_base(self):
        simplified = self.simplify()
        if simplified == True:
            return True
        elif simplified == False:
            self.assignment = set()
            return False
        if not self.clauses:
            return True
        
        literal = self.choose_literal()
        if literal is None:
            self.assignment = set()
            return False

        solver_with_literal = SatSolver([clause[:] for clause in self.clauses])
        solver_with_literal.assignment = self.assignment.copy()
        solver_with_literal.assignment.add(literal)
        if solver_with_literal.dpll_base():
            self.assignment = solver_with_literal.assignment
            return True

        solver_with_neg_literal = SatSolver([clause[:] for clause in self.clauses])
        solver_with_neg_literal.assignment = self.assignment.copy()
        solver_with_neg_literal.assignment.add(-literal)
        if solver_with_neg_literal.dpll_base():
            self.assignment = solver_with_neg_literal.assignment
            return True

        self.assignment = set()
        return False
    
    def dpll_up(self):
        simplified = self.simplify()
        if simplified == True:
            return True
        elif simplified == False:
            self.assignment = set()
            return False
        if not self.unit_propagate():
            self.assignment = set()
            return False
        if not self.clauses:
            return True
        
        literal = self.choose_literal()
        if literal is None:
            self.assignment = set()
            return False

        solver_with_literal = SatSolver([clause[:] for clause in self.clauses])
        solver_with_literal.assignment = self.assignment.copy()
        solver_with_literal.assignment.add(literal)
        if solver_with_literal.dpll_up():
            self.assignment = solver_with_literal.assignment
            return True

        solver_with_neg_literal = SatSolver([clause[:] for clause in self.clauses])
        solver_with_neg_literal.assignment = self.assignment.copy()
        solver_with_neg_literal.assignment.add(-literal)
        if solver_with_neg_literal.dpll_up():
            self.assignment = solver_with_neg_literal.assignment
            return True

        self.assignment = set()
        return False

    def dpll_up_pl(self):
        simplified = self.simplify()
        if simplified == True:
            return True
        elif simplified == False:
            self.assignment = set()
            return False
        if not self.unit_propagate():
            self.assignment = set()
            return False
        if not self.clauses:
            return True
        literal = self.find_pure_literal()
        if literal:
            self.assignment.add(literal)
            self.simplify()
            if simplified == True:
                return True
            elif simplified == False:
                self.assignment = set()
                return False
        if not self.clauses:
            return True
        
        literal = self.choose_literal()
        if literal is None:
            self.assignment = set()
            return False

        solver_with_literal = SatSolver([clause[:] for clause in self.clauses])
        solver_with_literal.assignment = self.assignment.copy()
        solver_with_literal.assignment.add(literal)
        if solver_with_literal.dpll_up_pl():
            self.assignment = solver_with_literal.assignment
            return True

        solver_with_neg_literal = SatSolver([clause[:] for clause in self.clauses])
        solver_with_neg_literal.assignment = self.assignment.copy()
        solver_with_neg_literal.assignment.add(-literal)
        if solver_with_neg_literal.dpll_up_pl():
            self.assignment = solver_with_neg_literal.assignment
            return True

        self.assignment = set()
        return False
    
    def dpll_vsids(self):
        simplified = self.simplify()
        if simplified == True:
            return True
        elif simplified == False:
            self.assignment = set()
            return False
        if not self.unit_propagate():
            self.assignment = set()
            return False
        if not self.clauses:
            return True
        literal = self.find_pure_literal()
        if literal:
            self.assignment.add(literal)
            self.simplify()
            if simplified == True:
                return True
            elif simplified == False:
                self.assignment = set()
                return False
        if not self.clauses:
            return True
        
        literal = self.choose_literal_vsids()
        if literal is None:
            self.assignment = set()
            return False

        solver_with_literal = SatSolver([clause[:] for clause in self.clauses])
        solver_with_literal.assignment = self.assignment.copy()
        solver_with_literal.assignment.add(literal)
        if solver_with_literal.dpll_vsids():
            self.assignment = solver_with_literal.assignment
            return True

        solver_with_neg_literal = SatSolver([clause[:] for clause in self.clauses])
        solver_with_neg_literal.assignment = self.assignment.copy()
        solver_with_neg_literal.assignment.add(-literal)
        if solver_with_neg_literal.dpll_vsids():
            self.assignment = solver_with_neg_literal.assignment
            return True

        self.assignment = set()
        return False

    def solve(self, method=2):
        if method == 0:
            return self.dpll_base()
        elif method == 1:
            return self.dpll_up()
        elif method == 2:
            return self.dpll_up_pl()
        elif method == 3:
            return self.dpll_vsids()

