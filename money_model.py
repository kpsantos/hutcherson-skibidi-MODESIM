#importing stuff
import mesa

#Data visualization tools
import seaborn as sns

#math functions, multi-dimensional arrays and matrices
import numpy as np

#data manipulation and analysis
import pandas as pd

class MoneyAgent(mesa.Agent):
    #agent with fixed wealth rich as fuck
    
    def __init__(self, unique_id, model):
        #pass parameters to parent class
        super().__init__(unique_id, model)
        
        #agent variable inital
        self.wealth = 1
    
    #def step(self):
        #agent's step
        #demo only yung unique id print 
        #print(f"I am Josh Hutcherson's agent. My name is: {str(self.unique_id)}.")
    def step(self):
        # verify agent has some wealth
        if self.wealth > 0:
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent is not None:
                other_agent.wealth += 1 #parang makati empty and makati tong dalawa
                self.wealth -= 1
                
class MoneyModel(mesa.Model):
    #model with number of agents
    
    def __init__(self, N):
        self.num_agents = N
        #scheduler to assign to the model
        self.schedule = mesa.time.RandomActivation(self)
        
        #create agents 
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            #add agent to scheduler
            self.schedule.add(a)
    
    def step(self):
        #advance model by one step
        #The model's step will go here for now this will call the step method of each agent and print the agent's unique_id
        self.schedule.step()