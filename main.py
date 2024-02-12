import numpy as np

import gerador, estatistica

# test_list = [[9, 4, 5, 8, 10], [1, 2, 3, 6, 7]]
# sub_list = [[4, 5, 8, 9, 10]]
#
# # printing original lists
# print("Original list : " + str(test_list))
# print("Original sub list : " + str(sub_list))
#
# # using all() to
# # check subset of list
# flag = 0
# if (any(x in sub_list for x in test_list)):
#     flag = 1
#
# # printing result
# if (flag):
#     print("Yes, list is subset of other.")
# else:
#     print("No, list is not subset of other.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sorteios = gerador.sorteios(5000, 60, 6)
    dados = estatistica.stat(sorteios, 60)
    jogo_1, jogo_2 = estatistica.jogos(dados, sorteios, 6)
    print('mais_sorteado: ', jogo_1)
    print('menos_sorteado: ', jogo_2)
