import random
from population import Individual


class CrossOverRandomSliceTwo:
    def __init__(self, prob):
        self.prob = prob

    def __call__(self, bests):
        indiv = random.sample(bests, k=2)
        rand = random.randint(0, 18)
        return Individual(indiv[0].genotype[:rand] + indiv[1].genotype[rand:])


class CrossOverRandomTwo:
    def __init__(self, prob):
        self.prob = prob

    def __call__(self, bests):
        indiv = random.sample(bests, k=2)
        gen = []
        for i in range(len(indiv[0].genotype)):
            gen.append(indiv[random.randint(0, 1)].genotype[i])
        return Individual(gen)
