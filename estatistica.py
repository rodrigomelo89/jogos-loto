import numpy as np


def stat(numeros, dezenas):
    stat = np.zeros(dezenas)
    for lin in range(0, np.size(numeros, 0)):
        for col in range(0, np.size(numeros, 1)):
            for i in range(1, dezenas+1):
                if numeros[lin][col] == i:
                    stat[i-1] += 1
                    break
    return stat


def jogos(stat, numeros, sorteio):
    mais_sorte = []
    menos_sorte = []
    copia = stat.copy()

    for i in range(sorteio):
        mais_sorte.append(np.argmax(copia) + 1)
        menos_sorte.append(np.argmin(copia) + 1)
        copia[np.argmax(copia)] = np.mean(copia)
        copia[np.argmin(copia)] = np.mean(copia)

    a = 0
    b = 0
    for i in range(len(numeros)):
        loop = 0
        while loop == 0:
            if not all(elem in numeros[i] for elem in mais_sorte) and all(elem in numeros[i] for elem in menos_sorte):
                menos_sorte[5] = np.argmin(copia) + 1
                copia[np.argmin(copia)] = np.mean(copia)
                a += 1
            elif all(elem in numeros[i] for elem in mais_sorte) and not all(elem in numeros[i] for elem in menos_sorte):
                mais_sorte[5] = (np.argmax(copia) + 1)
                copia[np.argmax(copia)] = np.mean(copia)
                b += 1
            elif not all(elem in numeros[i] for elem in mais_sorte) and not all(elem in numeros[i] for elem in menos_sorte):
                loop = 1
    print(a,b)
    return mais_sorte, menos_sorte