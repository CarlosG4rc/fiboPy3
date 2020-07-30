vf = 0
vi = 1
fibo = 1
n = input("¿Cuántos términos Fibonacci quieres obtener?")
n = int(n)
for i in range (n):
    print(fibo)
    fibo = vf + vi
    vf = vi
    vi = fibo