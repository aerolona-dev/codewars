def to_binary(n):
   return int(bin(n)[2:])

### Best Practice

def to_binary(n):
    return int(f'{n:b}')


