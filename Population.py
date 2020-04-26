import StringAgent
import random
from fuzzywuzzy import fuzz

#This class will represent a population of candidate strings

class AgentPopulation:
    def __init__(self, num_pop, agent_length):
        self.num_pop = num_pop
        self.agent_len = agent_length
        self.agent_list = [StringAgent.StringAgent(self.agent_len) for _ in range(self.num_pop)]
    
    def set_agent_list(self, agent_lst):
        self.agent_list = agent_lst
    
    def compute_fitness(self, true_string):
        """
        Requires:
        true_string is the string that we will compare each agent to

        Effect:
        Computes and sets the fitness of each of the agents in place by calculating
        Levenshtein Distance of the agent and true_string.

        Returns nothing
        """
        for agent in self.agent_list:
            #fitness is from 0 to 100, 100 being the agent matches the exact string
            agent.fitness = fuzz.ratio(agent.string, true_string)

    def select_agents(self):
        """
        selects a mating pool of agents to use to mutate and crossbreed
        returns an aray of selected agents
        """
        #Chooses the top two most fit agents

        #sorting agents by their fitness
        sorted_agents = sorted(self.agent_list, key = lambda agent: agent.fitness, reverse = True)
        parent1 = sorted_agents[0]
        parent2 = sorted_agents[1]

        print("parent 1: {}, parent 2: {}".format(parent1.string, parent2.string))
        return (parent1, parent2)

    def crossbreed(self, parent1, parent2):
        """
        Requires:
        two agent strings, agent 1 and agent 2

        Effect:
        Computes a new population from crossbreeding these two agents
        Returns a new population object
        """
        offspring_agents =[]
        for _ in range(self.num_pop//2):
            split_idx = random.randint(0, self.agent_len)
            #One way I can crossbreed is to combine the first portions of the first parent and the end portions of the second parent. 
            #The new strings beginning will be the beginning of the first parent and add the end of the string will be the end of the second parent and vice versa
            child1_string = parent1[:split_idx] + parent2[split_idx:self.agent_len]
            child2_string = parent2[:split_idx] + parent1[split_idx:self.agent_len]

            #creating the agent offspring
            child1_agent = StringAgent.StringAgent(self.agent_len)
            child2_agent = StringAgent.StringAgent(self.agent_len)

            #Setting the strings
            child1_agent.set_string(child1_string)
            child2_agent.set_string(child2_string)

            #append the agents
            offspring_agents.extend([child1_agent, child2_agent])



       

        pass
    
    def mutate(self, agent):
        """
        Requires:
        agent is an instance of the StringAgent class

        Effect:
        mutates the inputted agent
        """
        pass



