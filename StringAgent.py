import random
import string

def score(string_cand, trueString):
    score_val = 0
    for letterpair in zip(trueString, string_cand):
        if letterpair[0] == letterpair[1]:
            score_val += 1
    return (score_val)
        

#will represent each string candidate
class stringAgent:
    def __init__(self, length):

        #ccreate a random string of lowercase letters
        self.string = "".join(random.choice(string.lowercase) for _ in range(length))
        # The fitness of string. Initialized as -1 so we know the fitness hasn't been evaluated yet
        self.fitness = -1
    def __str__(self):
        #overruns
        #A "special method of the class" to use (its what prints when we print the agent)
        return "String " + str(self.string) + " Fitness: " + str(self.fitness)
