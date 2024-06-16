import tkinter as tk
from src.gui.sat_solver_gui import SATSolverGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = SATSolverGUI(root)
    root.mainloop()
