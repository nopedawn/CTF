from sympy import symbols, Eq, solve

a1, a2, a3, a4 = symbols('a1 a2 a3 a4')

eq1 = Eq(3*a4 + a3 + 4*a2 - 10*a1, 28)
eq2 = Eq(9*a2 - 8*a1 + 6*a3 - 2*a4, 72)
eq3 = Eq(a4 - 3*a2 - 2*a1 - 8*a3, 29)
eq4 = Eq(a3 + 5*a1 + 7*a2 - 6*a4, 88)

solution = solve((eq1, eq2, eq3, eq4), (a1, a2, a3, a4))

print(solution)
