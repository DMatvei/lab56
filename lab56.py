import math
from sympy import *
 
def get_index(xx, arr_x):
    idx = 0
    for i in range(n):
        if (arr_x[i] <= xx < arr_x[i + 1]):
            idx = i
            break
    return idx
 
def build_spline(x, arr_x, M, xx, h):
    idx = get_index(xx, arr_x)
    S = M[idx] + (M[idx+1] - M[idx]) / h * (x - arr_x[idx])
    print(f'Вторая производная от сплайна:\n{S}')
    print('Значение второй производной функции y = x^2 - sin(x), полученное с помощью сплайна: ', S.subs(x, xx))
    print('Значение, полученное непосредственно при подстановке', diff(func, x, 2).subs(x, xx))
    return 0
 
left = 0.5
right = 1.0
n = 10
h = (right - left) / n
arr_x = [left + i * h for i in range(n+1)]
arr_y = [x**2 - math.sin(x) for x in arr_x]
 
x = Symbol('x')
func = x**2 - sin(x)
 
f = [6 / h * ((arr_y[1] - arr_y[0]) / h - diff(func, x).subs(x, left))]
for i in range(1, n):
    f.append(6 / (h + h) * ((arr_y[i+1] - arr_y[i]) / h - (arr_y[i] - arr_y[i-1]) / h)) 
f.append(6 / h * (diff(func, x).subs(x, right) - (arr_y[n] - arr_y[n-1]) / h))
 
a = [0]
b = [2]
c = [1]
mu = h / (h + h)
for i in range(1, n):
    a.append(mu)
    b.append(2)
    c.append(mu)
a.append(1)
b.append(2)
c.append(0)
 
alpha = [-c[0]/b[0]]
beta = [f[0]/b[0]]
 
for i in range(1, n+1):
    alpha.append(-c[i-1]/(alpha[i-1] * a[i-1] + b[i-1]))
    beta.append((f[i-1] - beta[i-1] * a[i-1]) / (alpha[i-1] * a[i-1] + b[i-1]))
 
M = []
for i in range(n+1):
    M.append(0)
 
M[n] = (f[n] - beta[n] * a[n]) / (b[n] + alpha[n] * a[n])
 
for i in range(n-1, -1, -1):
    M[i] = alpha[i+1] * M[i+1] + beta[i+1]
 
print(M)
 
xx = float(input(f'Введите значение точки на отрезке [{left}, {right}], в которой нужно вычислить вторую производную: '))
 
build_spline(x, arr_x, M, xx, h)