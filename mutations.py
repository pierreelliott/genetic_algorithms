import random
from utils import available_characters


class NCharMutation:
    """
    Mutate n characters in the sequence
    """

    def __init__(self, n):
        self.n = n

    def __call__(self, individual):
        charidx_to_mutate = random.choices(range(len(individual.genotype)), k=self.n)

        for idx in charidx_to_mutate:
            individual.genotype[idx] = random.choice(available_characters)
