""""""
"""                                                                                              
Template for implementing QLearner  (c) 2015 Tucker Balch                                                                                              

Copyright 2018, Georgia Institute of Technology (Georgia Tech)                                                                                              
Atlanta, Georgia 30332                                                                                              
All Rights Reserved                                                                                              

Template code for CS 4646/7646                                                                                              

Georgia Tech asserts copyright ownership of this template and all derivative                                                                                              
works, including solutions to the projects assigned in this course. Students                                                                                              
and other users of this template code are advised not to share it with others                                                                                              
or to make it available on publicly viewable websites including repositories                                                                                              
such as github and gitlab.  This copyright statement should not be removed                                                                                              
or edited.                                                                                              

We do grant permission to share solutions privately with non-students such                                                                                              
as potential employers. However, sharing with other current or future                                                                                              
students of CS 7646 is prohibited and subject to being investigated as a                                                                                              
GT honor code violation.                                                                                              

-----do not edit anything above this line---                                                                                              

Student Name: Tucker Balch (replace with your name)                                                                                              
GT User ID: tb34 (replace with your User ID)                                                                                              
GT ID: 900897987 (replace with your GT ID)                                                                                              
"""

import random as rand
import numpy as np


class QLearner(object):
    """
    This is a Q learner object.

    :param num_states: The number of states to consider.
    :type num_states: int
    :param num_actions: The number of actions available..
    :type num_actions: int
    :param alpha: The learning rate used in the update rule. Should range between 0.0 and 1.0 with 0.2 as a typical value.
    :type alpha: float
    :param gamma: The discount rate used in the update rule. Should range between 0.0 and 1.0 with 0.9 as a typical value.
    :type gamma: float
    :param rar: Random action rate: the probability of selecting a random action at each step. Should range between 0.0 (no random actions) to 1.0 (always random action) with 0.5 as a typical value.
    :type rar: float
    :param radr: Random action decay rate, after each update, rar = rar * radr. Ranges between 0.0 (immediate decay to 0) and 1.0 (no decay). Typically 0.99.
    :type radr: float
    :param dyna: The number of dyna updates for each regular update. When Dyna is used, 200 is a typical value.
    :type dyna: int
    :param verbose: If â€œverboseâ€� is True, your code can print out information for debugging.
    :type verbose: bool
    """

    def __init__(
            self,
            num_states=100,
            num_actions=4,
            alpha=0.2,
            gamma=0.9,
            rar=0.5,
            radr=0.99,
            dyna=0,
            verbose=False,
    ):
        """
        Constructor method
        """
        self.verbose = verbose
        self.num_actions = num_actions
        self.s = 0
        self.a = 0
        self.num_states = num_states
        self.alpha = alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna
        self.Q_table = np.zeros((num_states, num_actions))
        self.pastExperiences = {} #this dictionary will store all robo experiences as a tuple
        self.key = 0

    def querysetstate(self, s):
        """
        Update the state without updating the Q-table

        :param s: The new state
        :type s: int
        :return: The selected action
        :rtype: int
        """
        self.s = s
        if rand.random() < self.rar:
            action = rand.randint(0, self.num_actions - 1)
        else:
            action = np.argmax(self.Q_table[s, :])

        self.a = action

        if self.verbose:
            print(f"s = {s}, a = {action}")
        
        return action

    def query(self, s_prime, r):
        """
        Update the Q table and return an action

        :param s_prime: The new state
        :type s_prime: int
        :param r: The immediate reward
        :type r: float
        :return: The selected action
        :rtype: int
        """
        # Update Q table formula -> (1- alpha)Q[s,a] + alpha*improved estimate
        prevQ_Val = (1 - self.alpha) * self.Q_table[self.s, self.a]
        improved_futureEstimate = (r + (self.gamma * self.Q_table[s_prime, np.argmax(self.Q_table[s_prime, :])]))
        self.Q_table[self.s, self.a] = prevQ_Val + self.alpha * improved_futureEstimate
        
        #determine action
        if rand.random() < self.rar:
            action = rand.randint(0, self.num_actions - 1)
        else:
            action = np.argmax(self.Q_table[s_prime, :])
            
        experience_tuple = (self.s, self.a, s_prime, r)
        self.pastExperiences[self.key] = experience_tuple
        
        # implement dyna algorithm
        if self.dyna > 0:
            self.implementDyna(self.pastExperiences)

        self.rar = self.rar * self.radr
        self.s = s_prime
        self.a = action
        self.key = self.key+1

        if self.verbose:
            print(f"s = {s_prime}, a = {action}, r={r}")

        return action

    def implementDyna(self, Robo_experiences):
        for i in range(0, self.dyna):
            #Fetch past experiences randomly from the dictionary
            experience_vals = Robo_experiences[rand.randint(0, len(Robo_experiences)-1)]
            rand_state = experience_vals[0]
            rand_action = experience_vals[1]
            rand_sPrime = experience_vals[2]
            reward = experience_vals[3]
    
            # Update the q value with the random values
            prevQ_Val = (1 - self.alpha) * self.Q_table[rand_state, rand_action]
            improved_futureEstimate = (reward + (self.gamma * self.Q_table[rand_sPrime, np.argmax(self.Q_table[rand_sPrime])]))
    
            self.Q_table[rand_state, rand_action] = prevQ_Val + self.alpha * improved_futureEstimate
        
        return
    
    def author(self):
        return "mkurale3"


if __name__ == "__main__":
    print("Remember Q from Star Trek? Well, this isn't him")
