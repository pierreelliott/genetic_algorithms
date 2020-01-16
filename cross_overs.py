import random


class CrossOverRandomTwo:
    def __init__(self, prob):
        self.prob = prob

    def __call__(self, bests):
        indiv = random.sample(bests, k=2)
        rand = random.randint(0, 18)
        return {'genotype': indiv[0]['genotype'][:rand] + indiv[1]['genotype'][rand:], 'score': None}