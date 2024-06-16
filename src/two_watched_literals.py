from collections import defaultdict

class TwoWatchedLiterals:
    def __init__(self):
        self.watch_list = defaultdict(set)

    def add_clause(self, clause):
        self.watch_list[clause.watch1].add(clause)
        self.watch_list[clause.watch2].add(clause)

    def update_watch(self, clause, old_literal, new_literal):
        self.watch_list[old_literal].remove(clause)
        self.watch_list[new_literal].add(clause)
        if clause.watch1 == old_literal:
            clause.watch1 = new_literal
        else:
            clause.watch2 = new_literal
        if not self.watch_list[old_literal]:
            self.watch_list.pop(old_literal)

    def get_clauses(self, literal):
        return self.watch_list[literal]

    def remove_clause(self, clause):
        self.watch_list[clause.watch1].remove(clause)
        self.watch_list[clause.watch2].remove(clause)

    def __repr__(self) -> str:
        return str(self.watch_list)
    
    def __str__(self) -> str:
        return str(self.watch_list)
