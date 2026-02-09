import sys
from bisect import bisect_right


def main():


	data = list(map(int, sys.stdin.read().split()))
	if not data:
		return

	it = iter(data)

	try:
		N = next(it)
		M = next(it)
	except StopIteration:
		return

	precos = []
	for _ in range(N):
		try:
			precos.append(next(it))
		except StopIteration:
			return

	orcamentos = []
	for _ in range(M):
		try:
			orcamentos.append(next(it))
		except StopIteration:
			return

	precos.sort()
	prefixo = [0]
	for p in precos:
		prefixo.append(prefixo[-1] + p)

	for dinheiro in orcamentos:
		k = bisect_right(prefixo, dinheiro) - 1
		print(k)


if __name__ == "__main__":
	main()

