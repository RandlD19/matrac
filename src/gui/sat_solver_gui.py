import tkinter as tk
import threading
from tkinter import filedialog, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
from src.cdcl_solver import CDCLSolver
from src.dpll_solver import DPLLSolver
from pysat.solvers import Solver
import random
import os
import time

class SATSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SAT Solver")

        self.algorithm_var = tk.StringVar(value="CDCL")
        self.stop_flag = threading.Event()
        self.start_time = None

        # CNF Input Frame
        self.cnf_frame = tk.LabelFrame(root, text="CNF Input")
        self.cnf_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.cnf_text = ScrolledText(self.cnf_frame, height=10)
        self.cnf_text.pack(fill="both", expand="yes", padx=10, pady=10)

        self.load_button = tk.Button(self.cnf_frame, text="Load from File", command=self.load_file)
        self.load_button.pack(side="left", padx=10, pady=10)

        self.generate_button = tk.Button(self.cnf_frame, text="Generate Test Case", command=self.generate_test_case)
        self.generate_button.pack(side="left", padx=10, pady=10)

        # Algorithm Selection Frame
        self.algorithm_frame = tk.LabelFrame(root, text="Select Algorithm")
        self.algorithm_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.cdcl_radio = tk.Radiobutton(self.algorithm_frame, text="CDCL", variable=self.algorithm_var, value="CDCL")
        self.cdcl_radio.pack(side="left", padx=10, pady=10)

        self.dpll_radio = tk.Radiobutton(self.algorithm_frame, text="DPLL", variable=self.algorithm_var, value="DPLL")
        self.dpll_radio.pack(side="left", padx=10, pady=10)

        self.dpll_radio = tk.Radiobutton(self.algorithm_frame, text="Glucose3", variable=self.algorithm_var, value="PySAT")
        self.dpll_radio.pack(side="left", padx=10, pady=10)

        # Solve Button
        self.solve_button = tk.Button(root, text="Solve", command=self.start_solving)
        self.solve_button.pack(pady=10)

        # Stop Button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_solving)
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED) 

        # Output Frame
        self.output_frame = tk.LabelFrame(root, text="Output")
        self.output_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.output_text = ScrolledText(self.output_frame, height=10)
        self.output_text.pack(fill="both", expand="yes", padx=10, pady=10)

        # Time Frame
        self.time_frame = tk.LabelFrame(root, text="Computation Time")
        self.time_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.time_label = tk.Label(self.time_frame, text="Time: 0.00 seconds")
        self.time_label.pack(pady=10)

    def load_file(self):
        initial_dir = 'test_cases' if os.path.exists('test_cases') else '/'
        file_path = filedialog.askopenfilename(initialdir=initial_dir, filetypes=[("CNF files", "*.cnf"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                cnf_data = file.read()
                self.cnf_text.delete(1.0, tk.END)
                self.cnf_text.insert(tk.END, cnf_data)

    def generate_test_case(self):
        num_vars = simpledialog.askinteger("Input", "Number of variables:", minvalue=1)
        num_clauses = simpledialog.askinteger("Input", "Number of clauses:", minvalue=1)

        if num_vars and num_clauses:
            cnf = self.create_random_cnf(num_vars, num_clauses)
            self.cnf_text.delete(1.0, tk.END)
            self.cnf_text.insert(tk.END, cnf)
            
    def generate_random_clause(self, num_vars, clause_length=3):
        clause = set()
        while len(clause) < clause_length:
            var = random.randint(1, num_vars)
            if var not in clause and -var not in clause:
                if random.choice([True, False]):
                    clause.add(var)
                else:
                    clause.add(-var)
        return list(clause)

    def create_random_cnf(self, num_vars, num_clauses):
        clauses = [self.generate_random_clause(num_vars) for _ in range(num_clauses)]
        cnf = f"p cnf {num_vars} {num_clauses}\n"
        for clause in clauses:
            cnf += ' '.join(map(str, clause)) + ' 0\n'
        return cnf

    def parse_cnf(self, cnf_text):
        try:
            lines = cnf_text.strip().split("\n")
            clauses = []
            for line in lines:
                if line.startswith('p') or line.startswith('c') or line.startswith('%') or line.startswith('0'):
                    continue
                literals = list(map(int, line.split()))
                literals.pop()  # Remove the trailing 0
                clauses.append(literals)
            return clauses
        except:
            messagebox.showerror("Invalid Format", "Invalid input format. Input type must be in CNF or DIMACS format!")
            return None
        
    def glucose3_solve(self, clauses):
        solver = Solver(name='glucose3')
        for clause in clauses:
            solver.add_clause(clause)
        if solver.solve():
            return solver.get_model()
        else:
            return None
        
    def start_solving(self):
        cnf_text = self.cnf_text.get(1.0, tk.END)
        clauses = self.parse_cnf(cnf_text)
        if clauses is None:
            return
        self.stop_flag.clear()
        self.start_time = time.time()
        self.update_time()
        algorithm = self.algorithm_var.get()
        if algorithm == "CDCL":
            solver = CDCLSolver(clauses, self.stop_flag)
        elif algorithm == "DPLL":
            solver = DPLLSolver(clauses, self.stop_flag)
        else:
            solver = Solver(name='glucose3')
            for clause in clauses:
                solver.add_clause(clause)

        self.stop_button.config(state=tk.NORMAL) 
        self.solve_button.config(state=tk.DISABLED)
        self.solving_thread = threading.Thread(target=self.solve, args=(solver,))
        self.solving_thread.start()

    def stop_solving(self):
        self.stop_flag.set()

    def update_time(self):
        if self.start_time is not None and not self.stop_flag.is_set():
            elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f"Time: {elapsed_time:.2f} seconds")
            self.root.after(10, self.update_time) 

    def solve(self, solver):
        result = solver.solve()
        end_time = time.time()
        if isinstance(result, tuple):  
            result = result[-1]
        else:
            result = solver.get_model()
        computation_time = end_time - self.start_time
        self.start_time = None
        self.time_label.config(text=f"Time: {computation_time:.2f} seconds")

        self.output_text.delete(1.0, tk.END)
        if result:
            self.output_text.insert(tk.END, "SATISFIABLE\n")
            self.output_text.insert(tk.END, ", ".join(list(map(str,result))))
        else:
            if (solver.stop_flag.is_set()):
                self.output_text.insert(tk.END, "FINISHED\n")
            else:
                self.output_text.insert(tk.END, "UNSATISFIABLE\n")
        self.stop_button.config(state=tk.DISABLED) 
        self.solve_button.config(state=tk.NORMAL)
