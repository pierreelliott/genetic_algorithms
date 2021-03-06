from utils import evaluate, available_characters
import random


class Population:
    def __init__(self, size, exploration):
        self.size = size
        self.population = generate_population(size)
        self.exploration = exploration

    def evaluate(self):
        self.population = sorted(map(evaluate, self.population), key=lambda x: x.score, reverse=True)

    def evolve(self):
        self.exploration.evolve(self)

    def get_max(self):
        return max(self.population, key=lambda x: x.score)

    def get_n_max(self, n):
        res = []
        pop = self.population[:]
        for i in range(n):
            max_individual = max(pop, key=lambda x: x.score)
            res.append(max_individual)
            pop.remove(max_individual)
        return res

    def get_average_score(self):
        s = 0
        for ind in self.population:
            s += ind.score
        return s/len(self.population)

    def __str__(self):
        return ''.join(map(lambda x: x.phenotype + f" ({x.score})\n", self.population)).strip()
    

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
    

def generate(size=18):
    individual = random.choices(available_characters, k=size)
    while len(''.join(individual)) < 12:
        individual = random.choices(available_characters, k=size)
    return individual


def generate_population(size):
    """
    Generate `size` Individuals with random genotype
    """
    return [Individual(generate()) for i in range(size)]