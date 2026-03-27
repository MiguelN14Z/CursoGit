def fibonacci(n):
    """
    Calcula el n-ésimo número de Fibonacci de manera iterativa.

    Args:
        n (int): El índice del número de Fibonacci a calcular (n >= 0).

    Returns:
        int: El n-ésimo número de Fibonacci.
    """
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Ejemplo de uso
if __name__ == "__main__":
    for i in range(10):
        print(f"Fibonacci({i}) = {fibonacci(i)}")