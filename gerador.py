from numpy.random import default_rng

rng = default_rng()


def sorteios(num_jogos, dezenas, aposta):
    jogos = []
    for j in range(0, num_jogos):
        jogos.append(rng.choice(range(1, dezenas+1), size=aposta, replace=False))
    return jogos