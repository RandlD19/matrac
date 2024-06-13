from src.clause import Clause
from src.literal import Literal
from src.trail import Trail
from src.variables import Variables
import random

class SATSolver:
    def __init__(self, input_clauses):
        self.input_clauses = input_clauses
        self.variables = None
        self.clauses = self.process_input(input_clauses)
        self.trail = Trail(self.variables)

    def process_input(self, clauses_as_lists):
        max_var = 0
        clauses = []
        for clause in clauses_as_lists:
            for literal in clause:
                max_var = max(max_var, abs(literal))
        self.variables = Variables(max_var)

        for clause in clauses_as_lists:
            literals = []
            for literal in clause:
                if literal > 0:
                    literals.append(Literal(literal, True, self.variables))
                else:
                    literals.append(Literal(-literal, False, self.variables))
            clauses.append(Clause(literals))
        return clauses

    def unit_propagation(self):
        while True:
            unit_clause = None
            for clause in self.clauses:
                if not clause.is_satisfied():
                    unassigned_literals = [lit for lit in clause.literals if not self.variables.is_assigned(lit.var)]
                    if len(unassigned_literals) == 1:
                        unit_clause = clause
                        break
            
            if unit_clause is None:
                return (True, None)

            unit_literal = unassigned_literals[0]

            self.trail.add_propagation_literal(unit_literal, unit_clause)

            is_consistent, conflict_clause = self.is_consistent()
            if not is_consistent:
                return (False, conflict_clause)

    def is_consistent(self):
        for clause in self.clauses:
            if clause.is_falsified():
                return (False, clause)
        return (True, None)

    def solve(self):
        decision_level = 0
        while True:
            unit_propagation, conflict_clause = self.unit_propagation()
            if not unit_propagation:
                if decision_level == 0:
                    return (False, None)
                learned_clause, backtrack_level = self.trail.analyze_conflict(conflict_clause)
                if backtrack_level < 0:
                    return  (False, None)
                self.trail.backtrack(backtrack_level)
                self.clauses.append(learned_clause)
                decision_level = backtrack_level
                continue
            unassigned_literal = self.select_unassigned_variable()
            decision_level += 1
            if unassigned_literal is None:
                return (True, self.trail)
            self.trail.add_decision_literal(unassigned_literal)
            # print(self.trail)

    def select_unassigned_variable(self):
        # literal_var = input("Vnesi literal: ")
        # if literal_var == "None":
        #     return None
        # literal_var = int(literal_var)
        # literal =  Literal(abs(literal_var), True if literal_var > 0 else False, self.variables)
        # return literal
        num_vars_list = list(range(1, self.variables.num_vars + 1 ))
        random.shuffle(num_vars_list)
        for var in num_vars_list:
            if not self.variables.is_assigned(var):
                return Literal(var, True, self.variables)
        return None
