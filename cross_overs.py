import random
from population import Individual


class CrossOverRandomSliceTwo:
    def __init__(self, prob):
        self.prob = prob

    def __call__(self, bests):
        indiv = random.sample(bests, k=2)
        rand = random.randint(0, 18)
        return Individual(indiv[0].genotype[:rand] + indiv[1].genotype[rand:])


class CrossOverScoreSliceTwo:
    def __init__(self, prob):
        self.prob = prob

    def __call__(self, bests):
        indiv = bests[:2]
        rand = random.randint(0, 1)
        score_ratio = int((indiv[0].score/indiv[1].score)*len(indiv[0].genotype))
        idx = (score_ratio, 1-score_ratio)
        return Individual(indiv[rand].genotype[:idx[rand]] + indiv[1-rand].genotype[idx[1-rand]:])
