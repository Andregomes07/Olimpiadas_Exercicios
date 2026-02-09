def main():
    # Tamanho e valores do primeiro baralho
    n1 = int(input())
    baralho1 = list(map(int, input().split()))

    # Tamanho e valores do segundo baralho
    n2 = int(input())
    baralho2 = list(map(int, input().split()))

    # Contar quantas cartas pares e ímpares há em cada baralho
    a_par = sum(1 for x in baralho1 if x % 2 == 0)
    a_impar = len(baralho1) - a_par

    b_par = sum(1 for x in baralho2 if x % 2 == 0)
    b_impar = len(baralho2) - b_par

    # Pares com soma par: par+par ou ímpar+ímpar
    soma_par = a_par * b_par + a_impar * b_impar

    # Pares com soma ímpar: par+ímpar ou ímpar+par
    soma_impar = a_par * b_impar + a_impar * b_par

    # Saída: número de pares com soma par e número de pares com soma ímpar
    print(soma_par, soma_impar)


if __name__ == "__main__":
    main()