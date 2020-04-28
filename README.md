# stringGeneticAlgorithm
Made a simple genetic algorithm using strings too match a certain input string

### Basic Idea
For those who don't know, a gentic algorithm is a randomized algorithm that uses ideas from evolutionary biology to come to either an exact solution or an approximate one.

The basic idea is that we start with a population of random candidate solutions(or agents) that have a notion of fitness, or how good of a solution the agent is. Like in evoutionary biology, the most fit live to survive and they breed to make new children(a new population) who have their genetic traits. There is also an element of random mutation that could occur in the offspring to bring novel genetic information to reduce the chances of agents converging to one solution space. The system continues to produce new children with greater and greater improved fitness until a good enough approximate solution is found or the exact solution is found.

### What I did:
Selecting candidates to breed:\
I pick a random two of the top ten most fit agents

Crossbreeding:/
I get a random integer n from 0 up to the lenghth of the agent's string minus 1.The first strings beginning will be the beginning of the first parent up to index n and the end of the string will be the end of the second parent and vice versa for the second string. I repeat that for the number of generations/2 times.

Mutate: 
I get a random integer n from 0 up to the lenghth of the agent's string minus 1. I replace the n'th index of the agent's string with a random letter.

### What I practiced:
Utilized some of the object oriented and functional programming concepts I learned in my classes.\
Things like:\
using getters and setters\
abstraction and encapsulation\
Using functions as inputs in other functions\

### Requirements:
Python 3.7\
Python Fuzzywuzzy module\
Python random module

### Please feel free to try it out on your own
