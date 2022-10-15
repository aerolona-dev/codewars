def bonus_time(salary, bonus):
    return f"${salary * 10 if bonus == True else salary}"

### Best Practice

def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))