#Okay gonna try to make a genetic algorithm that will eventually match a name.
#magdah - 6 letters 26^6 = 308915776
import StringAgent
import Population
input_str = "Pelumi"
input_str_len = len(input_str)
population_num = 20
generation_num = 10
mutation_rate = 0.1


#eleents of a genetic algortithm

#1. deternine the fitness of each agent
#2. find the most fit ones
#3. crossbreed and mutate them to create a new population

#Initializing the first population of agents
curr_pop = Population.AgentPopulation(population_num, input_str_len)
for gen in range(generation_num):
    print("generation " + str(generation_num))

    #Computes the fitness of all the agents
    curr_pop.compute_fitness(input_str)

    #creates a new population of agents
    new_pop = curr_pop.make_child_population(mutation_rate)

    #updating the population
    curr_pop = new_pop
 





# def ga():
#    agent_pop = init_agents(population_num, input_str_len)

#     for generation in generations:
#         print("generation " + str(generation))
#         #doing the fitness on each agent
#         agents = fitness(agent_pop)
#         #picking the top agents I want
#         agents = selection(agent_pop)
#         agents = crossover(agent_pop)
#         agents = mutation(agent_pop)

#         if any(agent.fitness >= 90 for agent in agents):
#             print ("Threshold met")
#             exit(0)

# def init_agents(pop_num, length):
#     return [stringAgent(length) for _ in range(population_num)]

# def fitness(agent_pop):
#     """
#     inputs a population of agents
#     evaluates the fitness of each agent thats created
#     """


