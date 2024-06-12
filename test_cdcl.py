from cdcl import * 
# literal1 = Literal(1)
# literal2 = Literal(-2)
# literal3 = Literal(3)
# literal4 = Literal(-4)
# literal5 = Literal(5)
# literal6 = Literal(-6)
# literal7 = Literal(-7)
# literal8 = Literal(8)
# literal9 = Literal(-9)
# literal10 = Literal(10)
# literal11 = Literal(11)
# literal12 = Literal(-12)

# literal1.decision_level = 1
# literal1.determined_by = 0
# literal1.successors = [literal2, literal3]

# literal2.decision_level = 1
# literal2.determined_by = 1
# literal2.successors = [literal5, literal8]

# literal3.decision_level = 1
# literal3.determined_by = 1
# literal3.successors = [literal4]

# literal4.decision_level = 1
# literal4.determined_by = 1
# literal4.successors = [literal5]

# literal5.decision_level = 1
# literal5.determined_by = 1
# literal5.successors = [literal7]

# literal6.decision_level = 2
# literal6.determined_by = 0
# literal6.successors = [literal7]

# literal7.decision_level = 2
# literal7.determined_by = 1
# literal7.successors = [literal8]

# literal8.decision_level = 2
# literal8.determined_by = 1
# literal8.successors = [literal9, literal10]

# literal9.decision_level = 2
# literal9.determined_by = 1
# literal9.successors = [literal11]

# literal10.decision_level = 2
# literal10.determined_by = 1
# literal10.successors = [literal11, literal12]

# literal11.decision_level = 2
# literal11.determined_by = 1
# literal11.successors = []

# literal12.decision_level = 2
# literal12.determined_by = 1
# literal12.successors = []

# trail = Trail()
# trail.add_literal(literal1)
# trail.add_literal(literal2)
# trail.add_literal(literal3)
# trail.add_literal(literal4)
# trail.add_literal(literal5)
# trail.add_literal(literal6)
# trail.add_literal(literal7)
# trail.add_literal(literal8)
# trail.add_literal(literal9)
# trail.add_literal(literal10)
# trail.add_literal(literal11)
# trail.add_literal(literal12)
# # uips = trail.find_uips()
# print(trail.get_learned_clause())

# TEST 2
# ========================
# literal_a = Literal(-1) 
# literal_b = Literal(-2) 
# literal_c = Literal(3) 
# literal_none = Literal(None)

# literal_a.decision_level = 1
# literal_a.determined_by = 0
# literal_a.successors = [literal_c, literal_none]

# literal_b.decision_level = 2
# literal_b.determined_by = 0
# literal_b.successors = [literal_c, literal_none]

# literal_c.decision_level = 2
# literal_c.determined_by = 1
# literal_c.successors = [literal_none]

# trail = Trail()
# trail.add_literal(literal_a)
# trail.add_literal(literal_b)
# trail.add_literal(literal_c)

# print(trail.get_learned_clause())

# TEST 3
# ========================
# literal_a = Literal(-1) 
# literal_b = Literal(2) 
# literal_c = Literal(3) 
# literal_none = Literal(None)

# literal_a.decision_level = 1
# literal_a.determined_by = 0
# literal_a.successors = [literal_b, literal_none]

# literal_b.decision_level = 1
# literal_b.determined_by = 1
# literal_b.successors = [literal_c, literal_none]

# literal_c.decision_level = 1
# literal_c.determined_by = 1
# literal_c.successors = [literal_none]

# trail = Trail()
# trail.add_literal(literal_a)
# trail.add_literal(literal_b)
# trail.add_literal(literal_c)

# print(trail.get_learned_clause())

# TEST 4
# ========================
# literal_a = Literal(1) 
# literal_b = Literal(-2) 
# literal_c = Literal(3) 
# literal_none = Literal(None)

# literal_a.decision_level = 0
# literal_a.determined_by = 1
# literal_a.successors = [literal_c, literal_none]

# literal_b.decision_level = 1
# literal_b.determined_by = 0
# literal_b.successors = [literal_c, literal_none]

# literal_c.decision_level = 1
# literal_c.determined_by = 1
# literal_c.successors = [literal_none]

# trail = Trail()
# trail.add_literal(literal_a)
# trail.add_literal(literal_b)
# trail.add_literal(literal_c)

# print(trail.get_learned_clause())

# TEST 4
# ========================
# literal_6 = Literal(-6) 
# literal_5 = Literal(-5) 
# literal_7 = Literal(-7) 
# literal_1 = Literal(1) 
# literal_2 = Literal(2) 
# literal_3 = Literal(3) 
# literal_4 = Literal(4) 
# literal_none = Literal(None)

# literal_6.decision_level = 1
# literal_6.determined_by = 0
# literal_6.successors = [literal_5]

# literal_5.decision_level = 1
# literal_5.determined_by = 1
# literal_5.successors = [literal_3]

# literal_7.decision_level = 2
# literal_7.determined_by = 0
# literal_7.successors = []

# literal_1.decision_level = 3
# literal_1.determined_by = 0
# literal_1.successors = [literal_2, literal_3]

# literal_2.decision_level = 3
# literal_2.determined_by = 1
# literal_2.successors = [literal_4]

# literal_3.decision_level = 3
# literal_3.determined_by = 1
# literal_3.successors = [literal_none]

# literal_4.decision_level = 3
# literal_4.determined_by = 1
# literal_4.successors = [literal_none]

# literal_none.decision_level = 1
# literal_none.determined_by = 1
# literal_none.successors = []

# trail = Trail()
# trail.add_literal(literal_6)
# trail.add_literal(literal_5)
# trail.add_literal(literal_7)
# trail.add_literal(literal_1)
# trail.add_literal(literal_2)
# trail.add_literal(literal_3)
# trail.add_literal(literal_4)
# trail.add_literal(literal_none)

# print(trail.get_learned_clause())


# TEST 6
# ========================
# literal_1 = Literal(1) 
# literal_2 = Literal(2) 
# literal_5 = Literal(5) 
# literal_6 = Literal(6) 
# literal_7 = Literal(7) 

# literal_none = Literal(None)

# literal_1.decision_level = 1
# literal_1.determined_by = 0
# literal_1.successors = [literal_5, literal_6, literal_none]

# literal_2.decision_level = 2
# literal_2.determined_by = 0
# literal_2.successors = [literal_5]

# literal_5.decision_level = 2
# literal_5.determined_by = 1
# literal_5.successors = [literal_6, literal_7]

# literal_6.decision_level = 2
# literal_6.determined_by = 0
# literal_6.successors = [literal_none]

# literal_7.decision_level = 2
# literal_7.determined_by = 0
# literal_7.successors = [literal_none]

# literal_none.decision_level = 2
# literal_none.determined_by = 1
# literal_none.successors = []

# trail = Trail()
# trail.add_literal(literal_1)
# trail.add_literal(literal_2)
# trail.add_literal(literal_5)
# trail.add_literal(literal_6)
# trail.add_literal(literal_7)

# trail.add_literal(literal_none)

# print(trail.get_learned_clause())

# TEST 7:
# ===================================
clauses = [
    [1, 2, 3],
    [1, 2, -3], 
    [-2, 4],
    [1, -2, -4], 
    [-1, 5, 6],
    [-1, 5, -6],
    [-5, -6], 
    [-1, -5, 6]
]

clauses = [Clause([Literal(literal, decision_level=0) for literal in c]) for c in clauses]
solver = Cdcl(clauses=clauses)
res = solver.solve()

