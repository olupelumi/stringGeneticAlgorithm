import StringAgent
import random
import string
from fuzzywuzzy import fuzz

#This class will represent a population of candidate strings

class AgentPopulation:

    def __init__(self, num_pop, agent_length):
        self.num_pop = num_pop
        self.agent_len = agent_length
        self.agent_list = [StringAgent.StringAgent(self.agent_len) for _ in range(self.num_pop)]
    
    #setter
    def set_agent_list(self, agent_lst):
        self.agent_list = agent_lst
    
    #getter
    def get_agent_list(self):
        return self.agent_list

    def compute_fitness(self, true_string):
        """
        Requires:
        true_string is the string that we will compare each agent to

        Effect:
        Computes and sets the fitness of each of the agents in place by calculating
        Levenshtein Distance of the agent and true_string.

        Returns nothing
        """
        ag_list = self.get_agent_list()
        for agent in ag_list :
            #fitness is from 0 to 100, 100 being the agent matches the exact string
            agent.set_fitness(fuzz.ratio(agent.string, true_string))
        
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
        Returns a new population instance created from crossbreeding
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
        
        #creating a new population instance
        child_pop = AgentPopulation(self.num_pop, self.agent_len)

        #setting the new list of agents
        child_pop.set_agent_list(offspring_agents)

        return(child_pop)

    def mutate(self, agent):
        """
        Requires:
        agent is an instance of the StringAgent class

        Effect:
        mutates the inputted agent
        returns the mutated agent
        """
        #used because crossover doesn't always give enough diversity and one may start converging on a set of solutions
        #allows one to look at more candidates in the search space

        rand_idx = random.randint(0, self.agent_len)
        old_string = agent.get_string()
        new_string = old_string[:rand_idx] + random.choice(string.ascii_lowercase) + old_string[rand_idx + 1:self.agent_len]

        #setting the newly mutated string
        agent.set_string(new_string)
        return agent

    def make_child_population(self, mutation_rate):
        """
        Requires:
        mutation_rate is a float between 0 and 1 telling us how often we want to mutate the population

        Effect:
        returns a new population from the current population
        """
        elite_agent1, elite_agent2 = self.select_agents()
        new_pop = self.crossbreed(elite_agent1, elite_agent2)

        new_pop_lst = []
        for cand_agent in new_pop.get_agent_list():
            #checking if we need to mutate
            if (random.uniform(0,1.0) <= mutation_rate):
                #then we mutate
                newag = self.mutate(cand_agent)
                new_pop_lst.append(newag)
                print("new agent: {}".format(newag))
                continue
            #else add the agent as it is
            new_pop_lst.append(cand_agent)
        
        #setting a new population list
        new_pop.set_agent_list(new_pop_lst)

        return new_pop





