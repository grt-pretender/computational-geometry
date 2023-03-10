# Design a time-based key-value data structure 
# that can store multiple values for the same key at different time stamps 
# and retrieve the key's value at a certain timestamp.

class TimeMap:

# Creating an object of this class
# Using a hashmap (the key + the list of value-timestamp)
    
    def __init__(self):
        self.store = {}


# Storing the key with the value at the given time timestamp
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])


# Returning a value such that set was called previously, with timestamp_prev <= timestamp. 
# If there are multiple such values, it returns the value associated with the largest timestamp_prev. 
# If there are no values, it returns "" (result).

# The list is already sorted because of the timestamp nature (linear time) 
# Using binary search

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        given_values = self.store.get(key, [])

        left = 0
        right = len(given_values) - 1
        
        while left <= right:
            m = (right - left)/ 2
            if given_values[m][1] <= timestamp:
                result = given_values[m][0]
                left = m + 1
            else:
                right = m - 1
        
        return result


