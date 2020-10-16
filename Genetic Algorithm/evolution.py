import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from tqdm import tqdm
import pandas as pd
# from logger import logger

from optimizer import Optimizer


class NeuroEvolution:
    def __init__(self, generations, population, params):
        """
        :param generations int: number of generation
        :param population int: number of population inside each generation
        :param params dict: dictionary with parameters
        """
        self._generations = generations
        self._population = population
        self._params = params
        self.networks = None
        self.best_params = None
        self.dataframe= pd.DataFrame()

    def evolve(self,model_path,output):
        """
        Takes data for traning and data for test and iterate thought generations to find parameters with lowest error
        :param x_train array: array with features for traning
        :param y_train array: array with real values for traning
        :param x_test array: array with features for test
        :param y_test array: array with real values for test
        :return: None

        """
        optimizer = Optimizer(self._params)
        self._networks = list(optimizer.create_population(self._population))

        for i in range(self._generations - 1):
            self._train_networks(model_path,output)
            self._networks= optimizer.evolve(self._networks)

        self._networks = sorted(self._networks, key=lambda x: x.loss, reverse=False)
        self.best_params = self._networks[0]

        self.dataframe=self.dataframe.append({'name':self.best_params.name,'output_fixed':output,'loss':self.best_params.loss,'params':self.best_params.network}, ignore_index=True) 


        return self._networks[0],self.dataframe

    

    def _train_networks(self,path,output):
        """
        Method for networks training
        :param x_train array: array with features for traning
        :param y_train array: array with real values for traning
        :param x_test array: array with features for test
        :param y_test array: array with real values for test
        :return: None
        """
        pbar = tqdm(total=len(self._networks))
        for network in self._networks:
            network.train(path,output)
            pbar.update(1)
        pbar.close()

    def _get_average_accuracy(self, networks):
        """
        :param networks list: list of dictionaries
        :return float: mean loss per population
        """
        return sum([network.loss for network in networks]) / len(networks)
