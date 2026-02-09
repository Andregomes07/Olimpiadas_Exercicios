n, k = map(int, input().split())

floresta = []
for _ in range(n):
    floresta.append(input())

possivel = False

for linha in floresta:
    espacos_consecutivos = 0
    
    for celula in linha:
        if celula == '.':
            espacos_consecutivos += 1
            if espacos_consecutivos >= k:
                possivel = True
                break
        else:
            espacos_consecutivos = 0
    
    if possivel:
        break

if possivel:
    print(1)
else:
    print(0)
