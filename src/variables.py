class Variables:
    def __init__(self, num_vars):
        self.num_vars = num_vars
        self.assignments = [None] * (num_vars + 1)
        self.decision_levels = [None] * (num_vars + 1)
        self.antecedent_clauses = [None] * (num_vars + 1)

    def assign(self, var, value, decision_level, antecedent_clause=None):
        self.assignments[var] = value
        self.decision_levels[var] = decision_level
        self.antecedent_clauses[var] = antecedent_clause

    def unassign(self, var):
        self.assignments[var] = None
        self.decision_levels[var] = None
        self.antecedent_clauses[var] = None

    def is_assigned(self, var):
        return self.assignments[var] is not None

    def get_value(self, var):
        return self.assignments[var]

    def get_decision_level(self, var):
        return self.decision_levels[var]

    def get_antecedent_clause(self, var):
        return self.antecedent_clauses[var]

    def set_decision_level(self, var, decision_level):
        self.decision_levels[var] = decision_level

    def set_antecedent_clause(self, var, antecedent_clause):
        self.antecedent_clauses[var] = antecedent_clause

    def reset_assignments(self):
        self.assignments = [None] * (self.num_vars + 1)
        self.decision_levels = [None] * (self.num_vars + 1)
        self.antecedent_clauses = [None] * (self.num_vars + 1)
