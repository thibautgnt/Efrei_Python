# Définition de la fonction factorial_function
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    # Calcul du factoriel
    factorial = 1
    for i in range(2, n+1):
        factorial *= i

    return factorial

# Test de la fonction factorial_function
for n in range(1, 6):
    print(n, factorial_function(n))
