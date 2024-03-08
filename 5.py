def inverse(w):
    i = len(w)
    j = 1
    model = ""
    while j<=i:
        model +=(w[-j])
        j+=1
    return (model)

word = input("digite uma palavra para inverter:")
w = inverse(word)
print(f"a palavra {word} ao contrário é: {w}")
