import sys


MOD = 12345


def main():
	# Leitura robusta: N seguido dos N valores gi (podem estar em qualquer linha)
	data = list(map(int, sys.stdin.read().split()))
	if not data:
		return

	it = iter(data)
	try:
		N = next(it)
	except StopIteration:
		return

	prod = 1
	for _ in range(N):
		try:
			g = next(it)
		except StopIteration:
			return
		# Para cada grupo: escolher 0 ou 1 ingrediente entre g -> (g + 1) opções
		prod = (prod * ((g + 1) % MOD)) % MOD

	# Subtrair a opção em que não escolhe ingrediente nenhum
	ans = (prod - 1) % MOD
	print(ans)


if __name__ == "__main__":
	main()

