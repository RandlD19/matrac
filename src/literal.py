class Literal:
    def __init__(self, var, is_positive, variables):
        self.var = var
        self.is_positive = is_positive
        self.variables = variables

    @property
    def is_assigned(self):
        return self.variables.is_assigned(self.var)

    @property
    def assignment(self):
        value = self.variables.get_value(self.var)
        if value is None:
            return None
        elif self.is_positive:
            return value
        else:
            return not value
        
    @assignment.setter
    def assignment(self, value):
        self.variables.assign(self.var, value, self.decision_level, self.antecedent_clause)

    @property
    def decision_level(self):
        return self.variables.get_decision_level(self.var)

    @decision_level.setter
    def decision_level(self, level):
        self.variables.set_decision_level(self.var, level)

    @property
    def antecedent_clause(self):
        return self.variables.get_antecedent_clause(self.var)

    @antecedent_clause.setter
    def antecedent_clause(self, clause):
        self.variables.set_antecedent_clause(self.var, clause)

    def unassign(self):
        self.variables.unassign(self.var)

    def is_satisfied(self):
        if self.assignment is None:
            return False
        return self.assignment

    def is_complementary(self, other):
        return self.var == other.var and self.is_positive != other.is_positive

    def get_complement(self):
        return Literal(self.var, not self.is_positive, self.variables)

    def __eq__(self, other):
        if isinstance(other, Literal):
            return self.var == other.var and self.is_positive == other.is_positive
        return False

    def __hash__(self):
        return hash((self.var, self.is_positive))

    def __str__(self):
        return f"{self.var}" if self.is_positive else f"-{self.var}"
