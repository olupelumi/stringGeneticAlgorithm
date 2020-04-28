#A genetic algoritm for one word strings
import StringAgent
import Population

input_str = input("Enter one word with no spaces or dashes: ")
input_str_len = len(input_str)
population_num = int(input("How many agents do you want in a population? "))
generation_num = int(input("How many generations? "))
mutation_rate = float(input("mutation rate(a number between 0 and 1)? "))


#Initializing the first population of agents
curr_pop = Population.AgentPopulation(population_num, input_str_len)
for gen in range(generation_num):
    print("curr_generation " + str(gen))

    #Computes the fitness of all the agents
    curr_pop.compute_fitness(input_str)

    #creates a new population of agents
    new_pop = curr_pop.make_child_population(mutation_rate)

    #updating the population
    curr_pop = new_pop
 
