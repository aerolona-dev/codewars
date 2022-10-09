from statistics import mean
find_average = mean

### Best Practice

def find_average(array):
    return sum(array) / len(array) if array else 0