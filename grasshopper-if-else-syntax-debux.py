def check_alive(health): return 1 if health > 0 else 0

### Best Practice

def check_alive(health: int) -> bool:
    """ Return `true` if the player's health is greater than 0 or `false` if it is 0 or below. """
    return health > 0