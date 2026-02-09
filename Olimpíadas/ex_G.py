def main():
	# N: número total de cromos na coleção
	# M: número de cromos que o Pedro tem (com possíveis repetições)
	N, M = map(int, input().split())

	# Cromos do Pedro (podem repetir)
	cromos = list(map(int, input().split()))

	# Usamos um conjunto para ficar apenas com os cromos distintos que ele já tem
	distintos = set(cromos)

	# Cromos que faltam = total possíveis - distintos que ele já tem
	faltam = N - len(distintos)

	print(faltam)


if __name__ == "__main__":
	main()

