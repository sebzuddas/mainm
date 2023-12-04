"""
This is a set of classes for functions that help with creation of manim animaitons. 
"""

import math


class CalculateMean:
    def __init__(self):
        self.data = []
        self.mean = 0

    def add_data(self, new_data):
        self.data.append(new_data)
        self.mean = sum(self.data) / len(self.data)
        return self.mean

class CalculateStandardDeviation:
    def __init__(self):
        self.data = []
        self.mean = 0

    def add_data(self, new_data):
        self.data.append(new_data)
        self.mean = sum(self.data) / len(self.data)
        variance = sum((x - self.mean) ** 2 for x in self.data) / len(self.data)
        return variance ** 0.5
    
class CalculateGaussianDistribution:
    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev

    def calculate_pdf(self, x):
        if self.mean or self.std_dev == 0:
            return 0
        else:
            return (1 / (math.sqrt(2 * math.pi) * self.std_dev)) * math.exp(-0.5 * ((x - self.mean) / self.std_dev) ** 2)
        

class CalculatePercentageChange:
    def __init__(self) -> list:
        self.percentage_change_list = []

    def calculate(self, list_a, list_b):
        self.percentage_change_list = []
        for a, b in zip(list_a, list_b):
            if a == 0:
                change = float('inf') if b != 0 else 0
            else:
                change = ((b - a)/a)*100
            self.percentage_change_list.append(change)
        return self.percentage_change_list
