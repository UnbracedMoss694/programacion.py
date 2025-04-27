with open('traffic.in') as archivo:
    N = int(archivo.readline())
    segmentos = []

    for _ in range(N):
        partes = archivo.readline().split()
        tipo = partes[0]
        a = int(partes[1])
        b = int(partes[2])
        segmentos.append((tipo, a, b))


min_flow = 0
max_flow = 1000

for i in range(N-1, -1, -1):
    tipo, a, b = segmentos[i]
    if tipo == 'none':
        min_flow = max(min_flow, a)
        max_flow = min(max_flow, b)
    elif tipo == 'off': 
        min_flow += a
        max_flow += b
    elif tipo == 'on':  
        min_flow = max(0, min_flow - b)
        max_flow = max(0, max_flow - a)

inicio_min = min_flow
inicio_max = max_flow


min_flow = inicio_min
max_flow = inicio_max

for i in range(N):
    tipo, a, b = segmentos[i]
    if tipo == 'none':
        min_flow = max(min_flow, a)
        max_flow = min(max_flow, b)
    elif tipo == 'on':  
        min_flow += a
        max_flow += b
    elif tipo == 'off': 
        min_flow = max(0, min_flow - b)
        max_flow = max(0, max_flow - a)


with open('traffic.out', 'w') as archivo:
    archivo.write(f"{inicio_min} {inicio_max}\n")
    archivo.write(f"{min_flow} {max_flow}\n")
