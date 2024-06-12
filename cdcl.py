class Cdcl:
    def __init__(self, clauses):
        self.clauses = [clause for clause in clauses]
        self.assignment = set()
        self.decision_level = 0 
        self.trail = Trail()
        self.counter = self.count_occurrences()
        # self.conflict_counter = self.init_conflict_counter()

    # def init_conflict_counter(self):
    #     conflict_counter = {}
    #     for clause in self.clauses:
    #         for literal in clause:
    #             if literal not in conflict_counter:
    #                 conflict_counter[literal] = 0
    #     return conflict_counter

    def count_occurrences(self):
        counter = {}
        for clause in self.clauses:
            for literal in clause.literals:
                var = abs(literal.literal)
                if var not in counter:
                    counter[var] = [0, 0]
                if literal.literal > 0:
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

    def is_conflict_occured(assignment):
        for literal in assignment:
            if -literal in assignment:
                return True
        return False

    def unit_propagate(self):
        changed = True
        while changed:
            changed = False
            unit_clauses = [c for c in self.clauses if c.is_unit(self.assignment)]
            current_assignment = self.assignment.copy() 
            for unit in unit_clauses:
                literal = unit.get_unit(current_assignment)
                literal.decision_level = self.decision_level
                literal.determined_by = 1
                if -literal.literal in self.assignment:
                    self.trail.add_literal(literal, clause=unit, none=True)
                    return False
                if literal.literal not in self.assignment:
                    self.assignment.add(literal.literal)
                    self.trail.add_literal(literal, clause=unit)
                    changed = True
        return True

    def second_largest_dec_level(clause):
        sec_largest = 0
        sorted_literals = sorted(clause.literals, key=lambda x:x.decision_level, reverse=True)
        largest = sorted_literals[0].decision_level
        for literal in sorted_literals:
            if literal.decision_level < largest:
                return literal.decision_level
        return sec_largest
    
    def choose_literal(self, i):
        zap = [Literal(-1, decision_level=self.decision_level), Literal(-2,decision_level=self.decision_level), Literal(-5,decision_level=self.decision_level)]
        return zap[i]
    
    def solve(self):
        i = 0
        while True:
            valid_assignment = self.unit_propagate()
            if not valid_assignment:
                if self.decision_level == 0:
                    return (False, [])
                learned_clause = self.trail.get_learned_clause()
                self.clauses = [learned_clause] + self.clauses
                # backjump
                m = Cdcl.second_largest_dec_level(learned_clause)
                new_trail = Trail([literal for literal in self.trail.literals if literal.decision_level <= m])
                new_solver = Cdcl(self.clauses)
                new_solver.assignment = set([literal.literal for literal in new_trail.literals])
                new_solver.trail = new_trail
                new_solver.solve()
            else:
                if len(self.counter.keys()) == len(self.assignment): 
                    return (True, self.assignment)
                self.decision_level += 1
                literal = self.choose_literal(i)
                literal.determined_by = 0
                self.assignment.add(literal.literal)
                self.trail.add_literal(literal)
                i += 1

class Clause:
    def __init__(self, literals):
        self.literals = literals

    def is_false(self, assignment):
        for literal in self.literals:
            if -literal.literal not in assignment:
                return False
        return True
    
    def is_true(self, assignment):
        for literal in self.literals:
            if literal.literal in assignment:
                return True
        return False
    
    def is_unit(self, assignment):
        count = len(self.literals)
        for literal in self.literals:
            if literal.literal in assignment or -literal.literal in assignment:
                count -= 1
        if count == 1:
            return True
        return False
    
    def get_unit(self, assignment):
        count = len(self.literals)
        literals_copy = set([literal for literal in self.literals])
        assigned_literals = set()
        for literal in self.literals:
            if literal.literal in assignment or -literal.literal in assignment:
                assigned_literals.add(literal)
                count -= 1
        if count == 1:
            literal =  literals_copy.difference(assigned_literals).pop()
            return literal
        else:
            raise Exception("Can not get a unit because this clause is not unit. Call method is_unit first!")

class Literal:
    def __init__(self, literal, decision_level=None, determined_by=None):
        self.literal = literal
        self.decision_level = decision_level
        self.determined_by = determined_by
        self.successors = []

    def add_successor(self, successor):
        self.successors.append(successor)

    def __eq__(self, other):
        return self.literal == other.literal
    
    def __neq__(self, other):
        return self.literal != other.literal
    
    def __hash__(self):
        return hash(self.literal)
    
    def negative(self):
        if self.literal is None:
            return self
        return Literal(-self.literal, self.decision_level, self.determined_by)

    def __repr__(self):
        return f"Literal({self.literal}, level={self.decision_level}, by={self.determined_by})"

class Trail:
    def __init__(self, literals=[]):
        self.literals = literals
        self.latest_decision_literal = None

    def add_literal(self, literal, clause=None, none=False):
        if none:
            self.literals.append(Literal(None, literal.decision_level, determined_by=1))
        else:
            self.literals.append(literal)
        if literal.determined_by == 0:
            if self.latest_decision_literal and self.latest_decision_literal.decision_level < literal.decision_level:
                self.latest_decision_literal = literal
            if not self.latest_decision_literal:
                self.latest_decision_literal = literal
        if clause:
            for trail_literal in self.literals:
                if trail_literal != literal and (trail_literal in clause.literals or trail_literal.negative() in clause.literals):
                    if none:
                       trail_literal.add_successor(Literal(None, literal.decision_level, determined_by=1)) 
                    else:
                        trail_literal.add_successor(literal)

    def is_uip(self, literal):
        if self.latest_decision_literal:
            if literal == self.latest_decision_literal:
                return True
            current_literal = self.latest_decision_literal
            while True:
                if len(current_literal.successors) != 1:
                    return False
                else:
                    if current_literal.successors[0] == literal:
                        return True
                    else:
                        current_literal = current_literal.successors[0]
        else:
            return False
        
    def uip_cut(self, uip_literal):
        B = set(uip_literal.successors)
        A = set()
        trenutni_literali = uip_literal.successors[:]
        while trenutni_literali:
            literal = trenutni_literali.pop(0)
            set_successors = set(literal.successors)
            B = B.union(set_successors)
            trenutni_literali.extend(literal.successors)
        A = set(self.literals).difference(B)
        return A, B

    def find_uips(self):
        uips = []
        for literal in self.literals:
            if self.is_uip(literal):
                uips.append(literal)
        return uips
    
    def find_first_uip_cut(self):
        uips = self.find_uips()
        if uips:
            first = uips[0]
            first_cut = self.uip_cut(first)
            first_A_len = len(first_cut[0])
            for uip in uips:
                uip_cut = self.uip_cut(uip)
                uip_A_len = len(uip_cut[0])
                if uip_A_len > first_A_len:
                    first = uip
                    first_cut = uip_cut
                    first_A_len = uip_A_len
            return uip_cut
        else:
            return None
        
    def get_learned_clause(self):
        A, B = self.find_first_uip_cut()
        literals = []
        for literal in A:
            if literal.decision_level > 0 and literal.successors:
                for successor in literal.successors:
                    if successor in B:
                        literals.append(literal.negative())
                        break
        clause = Clause(literals)
        return clause

    def __repr__(self):
        return f"Trail({self.literals})"