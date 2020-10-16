import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import random

from train import train_and_score


class Network:

    def __init__(self, nn_param_choice):
        self.nn_param_choices = nn_param_choice
        self.loss = 1
        self.network = {}
        self.name=""
        
    def create_random(self):
        """Create a random network."""
        for key in self.nn_param_choices:
            self.network[key] = random.choice(self.nn_param_choices[key])

    def create_set(self, network):
        """
        :param network dict: dictionary with network parameters
        :return:
        """
        self.network = network

    def train(self,path,output):
        self.loss = train_and_score(self.network,path,output)
        name=path[-11:-3]
        self.name=name
