class Literal:
    def __init__(self, literal, decision_level=None, determined_by=None):
        self.literal = literal
        self.decision_level = decision_level
        self.determined_by = determined_by
        self.successors = []
        self.precessors = []

    def add_successor(self, successor):
        self.successors.append(successor)

    def __repr__(self):
        return f"Literal({self.literal}, level={self.decision_level}, by={self.determined_by})"

class Trail:
    def __init__(self):
        self.literals = []
        self.latest_decision_literal = None

    def add_literal(self, literal):
        self.literals.append(literal)
        if literal.determined_by == 0:
            if self.latest_decision_literal and self.latest_decision_literal.decision_level < literal.decision_level:
                self.latest_decision_literal = literal
            if not self.latest_decision_literal:
                self.latest_decision_literal = literal

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
        
    def get_conflict_clause(self):
        A, B = self.find_first_uip_cut()
        clause = []
        for literal in A:
            if literal.successors:
                for successor in literal.successors:
                    if successor in B:
                        clause.append(-literal.literal)
                        break
        return clause

    def __repr__(self):
        return f"Trail({self.literals})"