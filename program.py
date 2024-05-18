from satsolver import SatSolver
from pysat.solvers import Solver
from time import time
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

filename = 'benchmark_problems/uf150-032.cnf'
clauses = read_cnf_file(filename)
# write_dpll_file('dpll_problems/uf150-032.txt', clauses)
start = time()
# solver = SatSolver(clauses=clauses)
# solution = solver.solve(3)
solution = solve_sat(clauses)
stop = time()
if solution:
    # print(f"Satisfiable: {solver.assignment} \nTime: {stop - start}s")
    print(f"Satisfiable: {solution} \nTime: {stop - start}s")
else:
    print(f"Unsatisfiable \nTime: {stop - start}s")
