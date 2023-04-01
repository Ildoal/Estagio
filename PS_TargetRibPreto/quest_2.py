def fibonacci_sequence(n):
    
    sequence = [0, 1]
    
    
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    
   
    if n in sequence:
        print(f"{n} pertence à sequência de Fibonacci.")
    else:
        print(f"{n} não pertence à sequência de Fibonacci.")

    return sequence
# Exemplo de uso:
fibonacci_sequence(21)
