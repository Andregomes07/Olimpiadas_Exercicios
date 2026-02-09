import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        print(0)
        return

    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
        k = int(next(it))
    except StopIteration:
        print(0)
        return

    planes = []
    for _ in range(n):
        try:
            x = int(next(it)); y = int(next(it))
        except StopIteration:
            print(0); return
        planes.append([x, y])

    clouds = set()
    for _ in range(m):
        try:
            cx = int(next(it)); cy = int(next(it))
        except StopIteration:
            print(0); return
        clouds.add((cx, cy))

    # Directions: 0=E,1=S,2=W,3=N (turn right => +1 mod 4)
    dirs = [(1,0),(0,-1),(-1,0),(0,1)]
    dir_idx = [0]*n

    pairs = set()

    def add_pairs(lst):
        L = len(lst)
        for a in range(L):
            for b in range(a+1, L):
                i = lst[a]; j = lst[b]
                if i < j:
                    pairs.add((i,j))
                else:
                    pairs.add((j,i))

    # simulate t = 1..k
    for _ in range(k):
        # store previous positions to detectar cruzamentos
        prev_pos = [tuple(p) for p in planes]

        # decide movement for each plane
        for i in range(n):
            x, y = planes[i]
            dx, dy = dirs[dir_idx[i]]
            nx, ny = x + dx, y + dy
            if (nx, ny) in clouds:
                # vira à direita, mas não se move nesta unidade de tempo
                dir_idx[i] = (dir_idx[i] + 1) % 4
            else:
                planes[i][0] = nx
                planes[i][1] = ny

        # colisões na mesma célula após o movimento
        pos_map = {}
        for i in range(n):
            p = tuple(planes[i])
            pos_map.setdefault(p, []).append(i)
        for lst in pos_map.values():
            if len(lst) > 1:
                add_pairs(lst)

        # colisões de frente: dois aviões trocam de posição no mesmo passo
        edge_map = {}
        for i in range(n):
            a = prev_pos[i]
            b = tuple(planes[i])
            if a == b:
                continue  # não se moveu
            if a < b:
                key = (a, b)
                dir_flag = 0  # low -> high
            else:
                key = (b, a)
                dir_flag = 1  # high -> low
            edge_map.setdefault(key, []).append((i, dir_flag))

        for entries in edge_map.values():
            # precisamos de pelo menos um em cada sentido
            low_to_high = [i for (i, d) in entries if d == 0]
            high_to_low = [i for (i, d) in entries if d == 1]
            if not low_to_high or not high_to_low:
                continue
            for i in low_to_high:
                for j in high_to_low:
                    if i < j:
                        pairs.add((i, j))
                    else:
                        pairs.add((j, i))

    print(len(pairs))

if __name__ == '__main__':
    main()