#Okay gonna try to make a genetic algorithm that will eventually match a name.
#magdah - 6 letters 26^6 = 308915776
import StringAgent
import Population
input_str = "pelumi"
input_str_len = len(input_str)
population_num = 40
generation_num = 500
mutation_rate = 0.4


#eleents of a genetic algortithm

#1. deternine the fitness of each agent
#2. find the most fit ones
#3. crossbreed and mutate them to create a new population

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
 

# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()