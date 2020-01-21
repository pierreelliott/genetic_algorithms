from explorations import RandomExploration
from utils import generate_population, evaluate


class Population:
    def __init__(self, size, exploration=RandomExploration()):
        self.size = size
        self.population = generate_population(size)
        self.exploration = exploration

    def evaluate(self):
        self.population = sorted(map(evaluate, self.population), key=lambda x: x['score'], reverse=True)

    def evolve(self):
        self.exploration.evolve(self)

    def __str__(self):
        return ''.join(map(lambda x: ''.join(x['genotype']) + f" ({x['score']})\n", self.population)).strip()
    
    

class Individual:
    def __init__(self, genotype, score=None):
        """
        Genotype is always 18 characters long but phenotype can be under 12 characters because of blank character `''`
        """
        self.genotype = genotype
        self.score = score
    
    def phenotype(self):
        return ''.join(self.genotype)
    
    def clone(self):
        return Individual(self.genotype[:], self.score)