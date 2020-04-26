import random
import string

# def score(string_cand, trueString):
#     score_val = 0
#     for letterpair in zip(trueString, string_cand):
#         if letterpair[0] == letterpair[1]:
#             score_val += 1
#     return (score_val)
        

# represent each string candidate
class StringAgent:
    def __init__(self, length):

        #ccreate a random string of lowercase letters
        self.string = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
        # The fitness of string. Initialized as -1 so we know the fitness hasn't been evaluated yet
        self.fitness = -1
    def __str__(self):
        #overruns
        #A "special method of the class" to use (its what prints when we print the agent)
        return "String " + str(self.string) + " Fitness: " + str(self.fitness)

    #some setters 
    def set_string(self, new_string):
        self.string = new_string

    def set_fitness(self, new_fitness):
        self.fitness = new_fitness
    
    #getters
    def get_string(self):
        return self.string
