# imprime todos os contadores exceto o 13 = laço for
for i in range(1, 21):
    if (i == 13):
        continue
    else:
        print(i)
# imprime todos os contadores exceto o 13 = laço while
contador = 1
while (contador <= 20):
    if (contador == 13):
        contador = contador+1
        continue
    else:
        print(contador)
        contador = contador+1

# imprime todos os numeros em ordem decrescente exceto o numero 13
for p in range(20, 0, - 1):
    if (p == 13):
        continue
    else:
        print(p)
