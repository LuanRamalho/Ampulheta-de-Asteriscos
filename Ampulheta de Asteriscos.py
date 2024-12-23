def desenhar_ampulheta(linhas):
    # Parte superior da ampulheta
    for i in range(linhas, 0, -1):
        espacos = ' ' * (linhas - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacos + asteriscos)

    # Parte inferior da ampulheta
    for i in range(2, linhas + 1):
        espacos = ' ' * (linhas - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacos + asteriscos)

# Define o tamanho da ampulheta
linhas = int(input("Digite o número de linhas para a ampulheta: "))
desenhar_ampulheta(linhas)
input()
