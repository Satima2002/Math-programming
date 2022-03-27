from pulp import *
import time
start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
problem = pulp.LpProblem('0',LpMaximize)

problem += (10**2)*x1+10*x2+x3, "Функция цели"

problem += 90*x1+ 5*x2 <= 10000, "1"
problem +=x2 ==3*x1, "2"
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Прибыль:")
print (value(problem.objective))
stop = time.time()
print ("Время :")
print(stop - start)