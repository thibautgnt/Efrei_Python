def fib(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1 or n == 2:
        return 1
    else:
        fib_prev = 1
        fib_curr = 1
        for _ in range(3, n + 1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr

for n in range(1, 10):
    print(n, "->", fib(n))