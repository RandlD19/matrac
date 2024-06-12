from literal import Literal
from trail import Trail
from clause import Clause
from variables import Variables

# trail = Trail()

# # Dodamo literale v trail kot je podano v primeru
# lit1 = Literal(1, is_positive=False)  # Literal(1, False, decision_level=1)
# lit2 = Literal(2, is_positive=False)  # Literal(2, False, decision_level=2)
# lit3 = Literal(3, is_positive=True)   # Literal(3, True, decision_level=2)

# lit1.assign(False, 1)
# lit2.assign(False, 2)
# lit3.assign(True, 2)

# trail.add_decision_literal(lit1)
# trail.add_decision_literal(lit2)
# trail.add_propagation_literal(lit3)

# print(lit1.decision_level)
# print(lit2.decision_level)
# print(lit3.decision_level)

# lit1_conflict = Literal(1, is_positive=True)
# lit2_conflict = Literal(2, is_positive=True)
# lit3_conflict = Literal(3, is_positive=False)

# conflict_clause = Clause([lit1_conflict, lit2_conflict, lit3_conflict])

# # Kličemo analyze_conflict
# learned_clause, backtrack_level = trail.analyze_conflict(conflict_clause)
# print(learned_clause)
# # Preverimo rezultate
# expected_clause = Clause([lit1, lit2])
# expected_backtrack_level = 1

variables = Variables(3)
literal1 = Literal(1, True, variables)
literal2 = Literal(2, False, variables)
literal3 = Literal(3, True, variables)
clause = Clause([literal1, literal2, literal3])

literal2.assignment = False
literal2.decision_level = 2
print(variables.get_value(2))
# true = clause.is_satisfied()