#def distinct(seq):
    #nseq = [*set(seq)]  #First Solution
    #return nseq

distinct = lambda seq : list(set(seq))

print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))