import matplotlib.pyplot as plt

MAX = 100

r = float(input("Entre com a constante r: "))
x = float(input("Entre com o x0: "))

population = [x]

for i in range(1,MAX):
    x = r*x*(1-x)
    population.append(x)
    
print('população no longo ddo prazo: ',population[-1])

# Plota gráfico da população pelo tempo
eixox = list(range(MAX))
plt.figure(1)
plt.plot(eixox, population)
plt.show()


'''
a) r = 1 e x0 = 0.4 (extinção)
b) r = 2 e x0 = 0.4 (equilíbrio em 50%)
c) r = 2.4 e x0 = 0.6 (pequena oscilação, mas atinge equilíbrio em 58%)
d) r = 3 e x0 = 0.4 (não há equilíbrio, população oscila, mas em torno de uma média)
e) r = 4 e x0 = 0.4 (comportamento caótico, totalmente imprevisível)
'''