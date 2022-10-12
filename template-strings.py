def temple_strings(obj, feature): 
    return " are ".join([obj, feature])

### Best Practice

def temple_strings(obj, feature): 
    return f"{obj} are {feature}"