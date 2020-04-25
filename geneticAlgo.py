#Okay gonna try to make a genetic algorithm that will eventually match a name.
#magdah - 6 letters 26^6 = 308915776
import stringAgent
input_str = None
input_str_len = None
population_num = 20
generations = 1000


#eleents of a genetic algortithm

#1. deternine the fitness of each agent
#2. find the most fit ones
#3. crossbreed and mutate them to create a new population

def ga():
   agent_pop = init_agents(population_num, input_str_len)

    for generation in generations:
        print("generation " + str(generation))
        #doing the fitness on each agent
        agents = fitness(agent_pop)
        #picking the top agents I want
        agents = selection(agent_pop)
        agents = crossover(agent_pop)
        agents = mutation(agent_pop)

        if any(agent.fitness >= 90 for agent in agents):
            print ("Threshold met")
            exit(0)

def init_agents(pop_num, length):
    return [stringAgent(length) for _ in range(population_num)]

def fitness(agent_pop):
    """
    inputs a population of agents
    evaluates the fitness of each agent thats created
    """


