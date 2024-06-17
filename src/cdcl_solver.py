from src.clause import Clause
from src.literal import Literal
from src.trail import Trail
from src.variables import Variables
from src.two_watched_literals import TwoWatchedLiterals
from collections import defaultdict
import random
import time

class CDCLSolver:
    def __init__(self, input_clauses, stop_flag=None):
        self.input_clauses = input_clauses
        self.variables = None
        self.twl = TwoWatchedLiterals()
        self.clauses = self.process_input(input_clauses)
        self.trail = Trail(self.variables)
        self.cleanup_interval = 200
        self.conflict_count = 0
        self.stop_flag = stop_flag
        self.propagation_time = 0

        self.scores = defaultdict(int)
        self.decay_factor = 0.95
        self.conflicts_since_last_decay = 0

    def vsids_update(self, clause):
        for literal in clause.literals:
            self.scores[literal.var] += 1

    def vsids_decay(self):
        for var in self.scores:
            self.scores[var] *= self.decay_factor

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
            new_clause = Clause(literals)
            clauses.append(new_clause)
            self.twl.add_clause(new_clause)
        return clauses

    def unit_propagation(self):
        # while True:
        #     if self.stop_flag and self.stop_flag.is_set():
        #         return (None, None)

        #     unit_clause = None

        #     for literal in self.trail.literals:
        #         if unit_clause:
        #             break
        #         complement = literal.get_complement()
        #         if complement in self.twl.watch_list:
        #             clauses_to_check = list(self.twl.get_clauses(complement).copy())
                    
        #             for clause in clauses_to_check:
        #                 if unit_clause:
        #                     break
        #                 if clause.is_satisfied():
        #                     continue
        #                 if clause.watch1 == complement:
        #                     other_watch = clause.watch2
        #                 else:
        #                     other_watch = clause.watch1

        #                 found_new_watch = False
                        
        #                 for lit in clause.literals:
        #                     if lit != complement and lit != other_watch and not self.variables.is_assigned(lit.var):
        #                         self.twl.update_watch(clause, complement, lit)
        #                         found_new_watch = True
        #                         break
        #                 if not found_new_watch:
        #                     if not self.variables.is_assigned(other_watch.var):
        #                         unit_clause = clause
        #                     elif self.variables.get_value(other_watch.var) == (not other_watch.is_positive):
        #                         return (False, clause)

        #     if unit_clause is None:
        #         return (True, None)

        #     self.trail.add_propagation_literal(other_watch, unit_clause)

            # is_consistent, conflict_clause = self.is_consistent()
            # if not is_consistent:
            #     return False, conflict_clause


        while True:
            unit_clause = None
            # start = time.time()
            for clause in self.clauses:
                if not clause.is_satisfied():
                    unassigned_literals = [lit for lit in clause.literals if not self.variables.is_assigned(lit.var)]
                    if len(unassigned_literals) == 1:
                        unit_clause = clause
                        break
            end = time.time()
            # print(f"Time: {end-start}s")
            # self.propagation_time += end-start
            if unit_clause is None:
                return (True, None)

            unit_literal = unassigned_literals[0]

            self.trail.add_propagation_literal(unit_literal, unit_clause)

            start = time.time()
            is_consistent, conflict_clause = self.is_consistent()
            if not is_consistent:
                self.conflict_count += 1
                return (False, conflict_clause)
            # end = time.time()
            # self.propagation_time += end-start

    def is_consistent(self):
        for clause in self.clauses:
            if clause.is_falsified():
                return (False, clause)
        return (True, None)

    def solve(self):
        decision_level = 0
        while True:
            if self.stop_flag and self.stop_flag.is_set():
                return (None, None)
            if self.conflict_count > self.cleanup_interval:
                self.remove_learned_clauses()
                self.conflict_count = 0
            unit_propagation, conflict_clause = self.unit_propagation()
            if unit_propagation is None:
                return (None, None)
            if not unit_propagation:
                if decision_level == 0:
                    return (False, None)
                self.vsids_update(conflict_clause) 
                self.conflict_count += 1
                self.conflicts_since_last_decay += 1
                if self.conflicts_since_last_decay >= 50:
                    self.vsids_decay()
                    self.conflicts_since_last_decay = 0
                learned_clause, backtrack_level = self.trail.analyze_conflict(conflict_clause)
                if backtrack_level < 0:
                    return  (False, None)
                self.trail.backtrack(backtrack_level)
                self.clauses.append(learned_clause)
                self.twl.add_clause(learned_clause)
                decision_level = backtrack_level
                continue
            unassigned_literal = self.select_unassigned_variable()
            decision_level += 1
            if unassigned_literal is None:
                return (True, sorted([str(literal) for literal in self.trail.literals], key=lambda x: abs(int(x))))
            self.trail.add_decision_literal(unassigned_literal)

    def remove_learned_clauses(self):
        delete_clauses = set([clause for clause in self.clauses if (clause.learned_clause and clause.delete)])
        new_clauses = []
        for clause in self.clauses:
            if clause not in delete_clauses:
                clause.delete = True
                new_clauses.append(clause)
        self.clauses = new_clauses

    def select_unassigned_variable(self):
        unassigned_vars = [var for var in range(1, self.variables.num_vars + 1) if not self.variables.is_assigned(var)]
        if not unassigned_vars:
            return None
        best_var = max(unassigned_vars, key=lambda var: self.scores[var])
        return Literal(best_var, True, self.variables)

