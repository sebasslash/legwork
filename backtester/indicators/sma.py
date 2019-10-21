import numpy as np
import pandas as pd
import math

class SMA:
    transformed_data = np.ndarray([])
    counter = 0;
    def __init__(self, market_data, timeframe, option="close"):
        self.data = market_data[option].values
        self.time_set = timeframe
        self.calculate_sma()
    def calculate_sma(self):
        for day in range(self.time_set, len(self.data)):
            avg = 0;
            for x in range(0, self.time_set):
                    avg += self.data[day - x]
            self.transformed_data = np.append(self.transformed_data, avg/self.time_set)
            self.counter = self.counter + 1

    def get_sma(self, day):
        if day == -1:
            return self.transformed_data
        if not isinstance(day, int):
            raise Exception("error: day specified for sma is not an integer");
        return self.transformed_data[math.floor(day / self.time_set)]
        
        
        
