from src.literal import Literal
from src.trail import Trail
from src.clause import Clause
from src.variables import Variables
from src.sat_solver import SATSolver

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

variables = Variables(6)

# Definicija klavzul
clauses = [
    Clause([Literal(1, True, variables), Literal(2, True, variables), Literal(3, True, variables)]),   # (𝑎 ∨ 𝑏 ∨ 𝑐)
    Clause([Literal(1, True, variables), Literal(2, True, variables), Literal(3, False, variables)]),  # (𝑎 ∨ 𝑏 ∨ ¬𝑐)
    Clause([Literal(2, False, variables), Literal(4, True, variables)]),  # (¬𝑏 ∨ 𝑑)
    Clause([Literal(1, True, variables), Literal(2, False, variables), Literal(4, False, variables)]),  # (𝑎 ∨ ¬𝑏 ∨ ¬𝑑)
    Clause([Literal(1, False, variables), Literal(5, True, variables), Literal(6, True, variables)]),  # (¬𝑎 ∨ 𝑒 ∨ 𝑓)
    Clause([Literal(1, False, variables), Literal(5, True, variables), Literal(6, False, variables)]),  # (¬𝑎 ∨ 𝑒 ∨ ¬𝑓)
    Clause([Literal(5, False, variables), Literal(6, False, variables)]),  # (¬𝑒 ∨ ¬𝑓)
    Clause([Literal(1, False, variables), Literal(5, False, variables), Literal(6, True, variables)])  # (¬𝑎 ∨ ¬𝑒 ∨ 𝑓)
]

# Inicializacija SAT Solverja
solver = SATSolver(clauses, variables)

# Reševanje SAT problema
result = solver.solve()

# Izpis rezultata
print("SAT Problem Solved:", result)

# literal2.assignment = False
# literal2.decision_level = 2
# print(variables.get_value(2))
# true = clause.is_satisfied()