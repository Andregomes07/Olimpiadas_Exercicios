n = int(input())
alturas = list(map(int, input().split()))

count = 0
max_altura = 0

for altura in alturas:
    if altura > max_altura:
        count += 1
        max_altura = altura

print(count)
