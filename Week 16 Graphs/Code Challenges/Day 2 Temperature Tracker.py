"""
Write a class TempTracker that tracks the max, min, mean, and mode of temperature values as they are inserted into the TempTracker. This class should have the following methods:

 insert() - records a new temperature.
 get_max() - returns the highest temperature we've seen so far.
 get_min() - returns the lowest temperature we've seen so far.
 get_mean() - returns the mean of all temperatures we've seen so far.
 get_mode() - returns a mode of all temperatures we've seen so far.

Favor speeding up the get methods over the insert method. Aim to get each of the get methods down to constant runtime. 

get_mean() should return a float. The rest of the methods can return integers. Temperatures should be recorded in Fahrenheit, so we can assume a range of 0 to 140.

If there is more than one mode, return any of the modes. 
"""

class TemperatureTracker:
    def __init__(self):
        self.max = -float('inf')
        self.min = float('inf')
        self.mean = 0
        self.mode = None
        
        self.mode_count = 0
        self.storage = {}
        self.size = 0
  
    def insert(self, temp):
        if temp not in self.storage:
            self.storage[temp] = 1
        else:
            self.storage[temp] += 1
            
        if temp > self.max:
            self.max = temp
        
        if temp < self.min:
            self.min = temp
            
        self.mean *= self.size
        self.mean += temp
        self.size += 1
        self.mean /= self.size
        
        count = self.storage[temp]
        if count > self.mode_count:
            self.mode = temp
            self.mode_count = count
  
    def get_max(self):
        return self.max
  
    def get_min(self):
        return self.min
  
    def get_mean(self):
        return self.mean
  
    def get_mode(self):
        return self.mode