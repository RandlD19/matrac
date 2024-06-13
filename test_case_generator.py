import random

def generate_random_clause(num_vars, clause_length=3):
    clause = set()
    while len(clause) < clause_length:
        var = random.randint(1, num_vars)
        if var not in clause and -var not in clause:
            if random.choice([True, False]):
                clause.add(var)
            else:
                clause.add(-var)
    return list(clause)

def generate_sat_problem(num_vars, num_clauses):
    clauses = [generate_random_clause(num_vars) for _ in range(num_clauses)]
    return clauses

def write_dimacs_file(filename, num_vars, clauses):
    with open(filename, 'w') as f:
        f.write(f"p cnf {num_vars} {len(clauses)}\n")
        for clause in clauses:
            clause_str = ' '.join(map(str, clause)) + ' 0\n'
            f.write(clause_str)

def main():
    num_vars = int(input("Enter the number of variables: "))
    num_clauses = int(input("Enter the number of clauses: "))
    
    clauses = generate_sat_problem(num_vars, num_clauses)   
    filename = f"random_problems/sat_problem_{num_vars}vars_{num_clauses}clauses.cnf"
    write_dimacs_file(filename, num_vars, clauses)
    
    print(f"Generated 10 SAT problem with {num_vars} variables and {num_clauses} clauses.")
    print(f"Problem saved in {filename}")

if __name__ == "__main__":
    main()
