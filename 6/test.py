f = lambda x: x**2 + 9 * x + 5
for i in range(1, 1000):
    if f(i) % 2 == 0:
        print(i)