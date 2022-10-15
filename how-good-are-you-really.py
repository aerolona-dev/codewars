def better_than_average(class_points, your_points):
    return 1 if your_points > sum(class_points)/len(class_points) else 0
    
### Best Practice

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)