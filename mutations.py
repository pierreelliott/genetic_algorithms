import random
from utils import available_characters


class NCharRandomMutation:
    """
    Mutate n characters randomly in the sequence
    """

    def __init__(self, n):
        self.n = n

    def __call__(self, individual):
        charidx_to_mutate = random.choices(range(len(individual.genotype)), k=self.n)

        for idx in charidx_to_mutate:
            individual.genotype[idx] = random.choice(available_characters)


class NCharNextPrevMutation:
    """
    Mutate n random characters in the sequence, by changing it with the next or previous char
    """

    def __init__(self, n):
        self.n = n

    def __call__(self, individual):
        charidx_to_mutate = random.choices(range(len(individual.genotype)), k=self.n)

        for idx in charidx_to_mutate:
            char_idx = available_characters.index(individual.genotype[idx])

            if random.randint(0, 1) == 0:
                char_idx = char_idx+1 if char_idx < len(available_characters)-1 else 0
            else:
                char_idx = char_idx-1

            individual.genotype[idx] = available_characters[char_idx]


class NCharSeqMutation:
    """
    Mutate randomly a sequence of N characters in the sequence
    """

    def __init__(self, n):
        self.n = n

    def __call__(self, individual):
        charidx_to_mutate = random.randint(0, len(individual.genotype)-1)

        for i in range(self.n):
            char_idx = charidx_to_mutate - i

            individual.genotype[char_idx] = random.choice(available_characters)


class NCharSeqNextPrevMutation:
    """
    Mutate a random sequence of N characters, by changing each one with the next or previous char
    """

    def __init__(self, n):
        self.n = n

    def __call__(self, individual):
        charidx_to_mutate = random.randint(0, len(individual.genotype)-1)

        for i in range(self.n):
            char_idx = charidx_to_mutate - i

            idx = available_characters.index(individual.genotype[char_idx])

            if random.randint(0, 1) == 0:
                idx = idx+1 if idx < len(available_characters)-1 else 0
            else:
                idx = idx-1

            individual.genotype[char_idx] = available_characters[idx]
