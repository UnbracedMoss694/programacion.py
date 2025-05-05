def censurar(S, T):
    pila = []
    len_T = len(T)

    for c in S:
        pila.append(c)
        
        if len(pila) >= len_T and ''.join(pila[-len_T:]) == T:
            
            for _ in range(len_T):
                pila.pop()

    return ''.join(pila)



with open('censor.in', 'r') as fin:
    S = fin.readline().strip()
    T = fin.readline().strip()

resultado = censurar(S, T)

with open('censor.out', 'w') as fout:
    fout.write(resultado + '\n')
