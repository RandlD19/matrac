from satsolver import SatSolver
from pysat.solvers import Solver
from time import time
from src.sat_solver import SATSolver

def read_cnf_file(filename):
    clauses = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('p') or line.startswith('c') or line.startswith('%') or line.startswith('0'):
                continue 
            clause = [int(x) for x in line.strip().split() if int(x) != 0]
            if clause:
                clauses.append(clause)
    return clauses

def solve_sat(clauses):
    solver = Solver(name='glucose3')
    for clause in clauses:
        solver.add_clause(clause)
    if solver.solve():
        return solver.get_model()
    else:
        return None


def write_dpll_file(filename, clauses):
    with open(filename, 'w') as file:
        for clause in clauses:
            line = " ".join(list(map(str, clause))) + '\n'
            file.write(line)


filename = f'random_problems/sat_problem_150vars_1000clauses.cnf'
clauses = read_cnf_file(filename)
# write_dpll_file('dpll_problems/uf150-032.txt', clauses)
start = time()
solver = SATSolver(input_clauses=clauses)
solution1, assignment = solver.solve()
# solver = SatSolver(clauses=clauses)
# solution1 = solver.solve(2)
# solution2 = solve_sat(clauses)
# if solution:
#     assignment = list(map(str,sorted(assignment.literals, key=lambda x:abs(x.var))))
stop = time()
# if not solution2:
#     print(filename)
# if solution1 and not solution2 or solution2 and not solution1:
#     print(f"Ni istoo!!: {filename}")
# if solution1:
#     print(f"Satisfiable: {solver.assignment} \nTime: {stop - start}s")
#     print(f"Satisfiable: {solution}")
# else:
#     print(f"Unsatisfiable")
if solution1:
    # print(f"Satisfiable: {solver.assignment} \nTime: {stop - start}s")
    print(f"Satisfiable: {solution1} \nTime: {stop - start}s")
else:
    print(f"Unsatisfiable \nTime: {stop - start}s")
