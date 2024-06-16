
from pysat.solvers import Solver
from time import time
from src.cdcl_solver import CDCLSolver
from src.dpll_solver import DPLLSolver


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


filename = f'test_cases/benchmark_problems/uf75-099.cnf'
clauses = read_cnf_file(filename)
# write_dpll_file('dpll_problems/uf150-032.txt', clauses)
start = time()
# solver = CDCLSolver(input_clauses=clauses)
# solution1, assignment = solver.solve()
solver = DPLLSolver(clauses=clauses)
solution1, assignment = solver.solve(1)
# solution2 = solve_sat(clauses)
# if solution:
#     assignment = list(map(str,sorted(assignment.literals, key=lambda x:abs(x.var))))
stop = time()

if solution1:
    print(f"Satisfiable: {assignment} \nTime: {stop - start}s")
else:
    print(f"Unsatisfiable \nTime: {stop - start}s")

clauses2 = clauses[:]
for clause in clauses:
    for literal in clause:
        if literal in assignment:
            clauses2.remove(clause)
            break
print(clauses2)