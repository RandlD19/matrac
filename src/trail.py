from src.clause import Clause

class Trail:
    def __init__(self, variables):
        self.variables = variables
        self.literals = []
        self.decision_levels = [0]

    def add_decision_literal(self, literal):
        self.literals.append(literal)
        decision_level = self.current_decision_level() + 1
        self.decision_levels.append(decision_level)
        literal.assignment = literal.is_positive
        literal.decision_level = decision_level

    def add_propagation_literal(self, literal, antecedent_clause=None):
        self.literals.append(literal)
        decision_level = self.current_decision_level()
        literal.assignment = literal.is_positive
        literal.decision_level = decision_level
        literal.antecedent_clause = antecedent_clause
        if antecedent_clause:
            antecedent_clause.delete = False

    def backtrack(self, level):
        if level < 0 or level >= len(self.decision_levels):
            raise ValueError("Invalid decision level")

        backtrack_point = self.decision_levels[level]
        for literal in self.literals[backtrack_point:]:
            literal.unassign()

        self.literals = self.literals[:backtrack_point]
        self.decision_levels = self.decision_levels[:level + 1]

    def analyze_conflict(self, conflict_clause):
        learned_clause = []
        seen = set()
        backtrack_level = 0

        current_level = self.current_decision_level()
        num_literals_at_current_level = 0

        for literal in conflict_clause.literals:
            if literal.decision_level == current_level:
                num_literals_at_current_level += 1
            if literal not in seen and literal.get_complement() not in seen:
                seen.add(literal)

        index = 1
        for literal in reversed(self.literals):
            if num_literals_at_current_level <= 1:
                break
            if literal in seen or literal.get_complement() in seen:
                antecedent_clause = literal.antecedent_clause
                if antecedent_clause is not None:
                    for antecedent_literal in antecedent_clause.literals:
                        if antecedent_literal not in seen and antecedent_literal.get_complement() not in seen:
                            seen.add(antecedent_literal)
                            if antecedent_literal.decision_level == current_level:
                                num_literals_at_current_level += 1
                num_literals_at_current_level -= 1
            index += 1

        uip_index = len(self.literals) - index + 1
        A_literals = set(self.literals[:uip_index])
        B_literals = set(self.literals[uip_index:])
        learned_clause_set = set()
        for b_literal in B_literals:
            if b_literal.antecedent_clause is not None:
                for antecedent_literal in b_literal.antecedent_clause.literals:
                    if antecedent_literal != b_literal and antecedent_literal != b_literal.get_complement() and antecedent_literal in A_literals or antecedent_literal.get_complement() in A_literals:
                        if antecedent_literal.decision_level != 0:
                            learned_clause_set.add(antecedent_literal)
        for literal in conflict_clause.literals:
            if literal in A_literals or literal.get_complement() in A_literals:
                if literal.decision_level != 0:
                    learned_clause_set.add(literal)

        learned_clause = list(learned_clause_set)

        for literal in learned_clause:
            if literal.decision_level != current_level:
                backtrack_level = max(backtrack_level, literal.decision_level)

        return Clause(learned_clause, learned_clause=True, delete=False), backtrack_level

    def current_decision_level(self):
        return self.decision_levels[-1]

    def __str__(self):
        return " -> ".join(str(literal) for literal in self.literals)
    
    def __repr__(self):
        return " -> ".join(str(literal) for literal in self.literals)
