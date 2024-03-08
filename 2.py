def fibonacci(n):
    seq = [0, 1]
    next_number=0
    while next_number< n:
        next_number = seq[-1] + seq[-2]
        seq.append(next_number)
    if seq[-1]== n:
        return ("Pertence a sequência") 
    else: 
        return ("Não pertence a sequência")
    

n = int(input("Digite um número para ver se ele pertence a sequência fibonacci: "))
test = fibonacci(n)
print(test)
