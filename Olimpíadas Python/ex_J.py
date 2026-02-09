import sys


def main():
	# Lê todos os inteiros da entrada (formato geral):
	# M N A1 A2 ... AM
	data = list(map(int, sys.stdin.read().split()))
	if len(data) < 2:
		return

	it = iter(data)
	M = next(it)
	N = next(it)

	alturas = []
	for _ in range(M):
		try:
			alturas.append(next(it))
		except StopIteration:
			break

	# Se não houver alturas suficientes, não há como atribuir (caso inválido de entrada)
	if len(alturas) < M:
		print(0)
		return

	# Se há mais amigos do que canecas/prateleiras, é impossível
	if M > N:
		print(0)
		return

	alturas.sort()

	# j‑ésimo amigo mais baixo precisa chegar pelo menos à prateleira j
	for j, h in enumerate(alturas, start=1):
		if h < j:
			print(0)
			return

	# Se todas as condições passaram, é possível
	print(1)


if __name__ == "__main__":
	main()

