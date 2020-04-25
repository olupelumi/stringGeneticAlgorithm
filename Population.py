import StringAgent
from fuzzywuzzy import fuzz

#This class will represent a population of candidate strings

class AgentPopulation:
    def __init__(self, num_pop, length):
        self.num_pop = num_pop
        self.length = length
        self.agent_list = [stringAgent(self.length) for _ in range(self.num_pop)]
    
    def compute_fitness(self):
        """
        Computes the fitness of each of the agents
        """
        pass

    def select_agents(self):
        """
        selects a mating pool of agents to use to mutate and crossbreed
        returns an aray of selected agents
        """
        pass

    def crossbreed(self, agent1, agent2):
        """
        Requires:
        two agent strings, agent 1 and agent 2

        Effect:
        Computes a new population from crossbreeding these two agents
        Returns a new population object
        """
        pass
    
    def mutate(self, agent):
        """
        Requires:
        agent is an instance of the StringAgent class

        Effect:
        mutates the inputted agent
        """
        pass



