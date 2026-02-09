def main():
	# Leitura da entrada: número de velas e alturas
	N = int(input())
	alturas = list(map(int, input().split()))

	# Pilha de índices de velas com alturas em ordem crescente
	stack = []
	res = []

	for i in range(N):
		altura_atual = alturas[i]

		# Remover da pilha velas que não são estritamente mais baixas
		while stack and alturas[stack[-1]] >= altura_atual:
			stack.pop()

		# Se a pilha não estiver vazia, o topo é a vela mais próxima à esquerda e mais baixa
		if stack:
			res.append(str(stack[-1] + 1))  # converter para índice 1-based
		else:
			res.append("0")

		# Colocar vela atual na pilha
		stack.append(i)

	print(" ".join(res))


if __name__ == "__main__":
	main()

