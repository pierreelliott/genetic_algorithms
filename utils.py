import string
from blackbox37 import check
import random


available_characters = list(string.ascii_uppercase) + [str(i) for i in range(10)]
available_characters.append("")
GROUP_ID = 2


def copy_individual(individual):
    return {'genotype': individual['genotype'][:], 'score': individual['score']}


def evaluate(x):
    x.score = check(GROUP_ID, x.phenotype())
    return x





