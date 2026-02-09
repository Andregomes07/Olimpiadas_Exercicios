A, L, C = map(int, input().split())

volume = A * L * C

if volume >= 50 and A >= 3:
    print(1)
else:
    print(0)
